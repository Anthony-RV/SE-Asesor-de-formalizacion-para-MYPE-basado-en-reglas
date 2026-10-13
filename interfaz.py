# -*- coding: utf-8 -*-
"""
Interfaz gráfica (Tkinter) del Asesor de formalización para MYPE.

Cada pregunta ocupa toda la pantalla: título grande arriba y opciones como
botones con borde (A, B, C...) que se reacomodan solos al cambiar el tamaño
de la ventana, sea que la pregunta tenga 2 opciones o 30. Se responde con un
clic o con el teclado (A, B, C... o 1-9). Retroceder: botón "Atrás" o Esc.

Uso:  python interfaz.py
(colocar junto a main.py, motor.py, catalogo.py y base_conocimiento.py)
"""
import math
import os
import tkinter as tk
from tkinter import font as tkfont

import catalogo as K
from main import construir_motor, DEMOS, AVISO

BG = "#ffffff"
TEXTO = "#111827"
GRIS = "#6b7280"
# Estilo formal de los botones de opciones (azul institucional + gris)
AZUL, AZUL_CLARO, AZUL_SUAVE = "#1e3a8a", "#2f4fa8", "#dbe5fb"
CARA, SOMBRA = "#f8fafc", "#cbd5e1"
PALETA = ["#2196f3", "#e53950", "#f2a900", "#27a844", "#8e44e0", "#00a3a3", "#f26b21", "#d6409f"]
VERDE, ROJO = "#27a844", "#e53950"


class Atras(Exception):
    """Aborta la consulta en curso para retroceder una respuesta."""


class Inicio(Exception):
    """Aborta la consulta en curso y vuelve a la pantalla de inicio."""


# ------------------------------------------------------------------ utilidades
def mezcla(color, f):
    """f < 1 oscurece el color; f > 1 lo aclara."""
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    if f < 1:
        r, g, b = (int(c * f) for c in (r, g, b))
    else:
        r, g, b = (int(c + (255 - c) * (f - 1)) for c in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


def rect_red(c, x1, y1, x2, y2, r, **kw):
    r = max(1, min(r, (x2 - x1) / 2, (y2 - y1) / 2))
    pts = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y2 - r, x2, y2,
           x2 - r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
    return c.create_polygon(pts, smooth=True, **kw)


class Tipos:
    """Fuentes en píxeles (tamaño negativo) con caché."""

    def __init__(self, root):
        disp = set(tkfont.families(root))
        self.fam = next((f for f in ("Segoe UI", "SF Pro Display", "Helvetica Neue", "Ubuntu",
                                     "Noto Sans", "DejaVu Sans", "Arial") if f in disp), "Helvetica")
        self._c = {}

    def get(self, px, bold=True, italic=False):
        k = (px, bold, italic)
        if k not in self._c:
            self._c[k] = tkfont.Font(family=self.fam, size=-px, weight="bold" if bold else "normal",
                                     slant="italic" if italic else "roman")
        return self._c[k]


def envolver(texto, fuente, ancho):
    lineas = []
    for parrafo in texto.split("\n"):
        actual = ""
        for pal in parrafo.split():
            prueba = (actual + " " + pal).strip()
            if fuente.measure(prueba) <= ancho or not actual:
                actual = prueba
            else:
                lineas.append(actual)
                actual = pal
        lineas.append(actual)
    return lineas


def ajustar(tipos, textos, ancho, alto, maximo, minimo, bold=True):
    """Mayor tamaño de fuente (px) con el que TODOS los textos caben en ancho x alto."""
    for px in range(int(maximo), int(minimo) - 1, -2):
        f = tipos.get(px, bold)
        lh = f.metrics("linespace") * 1.1
        ok = True
        for t in textos:
            ls = envolver(t, f, ancho)
            if len(ls) * lh > alto or any(f.measure(x) > ancho for x in ls):
                ok = False
                break
        if ok:
            return px
    return int(minimo)


def etiqueta_letra(i, n):
    return chr(65 + i) if n <= 26 else str(i + 1)


# ---------------------------------------------------------------- mosaico
class Mosaico(tk.Canvas):
    """Botones grandes con borde que llenan el espacio y se reacomodan al redimensionar."""
    MIN_H, MIN_W = 62, 130

    def __init__(self, master, tipos, etiquetas, alclic, primarios=None, marcada=None, letras=True):
        super().__init__(master, bg=BG, highlightthickness=0)
        self.t, self.et, self.alclic = tipos, etiquetas, alclic
        self.primarios = set(primarios or ())
        self.marcada, self.letras = marcada, letras
        self.caras = {}
        self.bind("<Configure>", lambda e: self.dibujar())

    def _nec(self, w, h):
        """Altura mínima de un botón de ancho w para que su texto más largo quepa (letra de 11 px)."""
        pad = max(8, int(w * 0.04))
        d = int(min(max(h * 0.30, 24), 56)) if self.letras else 0
        f = self.t.get(11)
        lineas = max(len(envolver(t, f, w - 2 * pad - (d + pad if d else 0))) for t in self.et)
        return lineas * f.metrics("linespace") + 16

    def _disposicion(self, W, H, n, gap):
        """Elige cuántas columnas usar: la que da botones más grandes y legibles sin necesitar scroll."""
        mejor = None
        for cols in range(1, n + 1):
            rows = math.ceil(n / cols)
            w = (W - gap * (cols + 1)) / cols
            if w < self.MIN_W and cols > 1:
                break
            h_av = (H - gap * (rows + 1)) / rows
            h0 = min(h_av, w * 0.9) if h_av >= self.MIN_H else self.MIN_H
            h = max(h0, self._nec(w, h0), self.MIN_H)
            total = rows * h + (rows + 1) * gap
            pen = 1.0 if total <= H + 1 else 0.35 * H / total
            area = w * h * pen * min(1, 3.2 / (w / h))
            if mejor is None or area > mejor[0]:
                mejor = (area, cols, w, h)
        return mejor[1], mejor[2], mejor[3]

    def dibujar(self):
        self.delete("all")
        self.caras = {}
        W, H, n = self.winfo_width(), self.winfo_height(), len(self.et)
        if W < 60 or H < 60 or n == 0:
            return
        gap = max(10, int(min(W, H) * 0.025))
        cols, w, h = self._disposicion(W, H, n, gap)
        rows = math.ceil(n / cols)
        pad = max(8, int(w * 0.04))
        d = int(min(max(h * 0.30, 24), 56)) if self.letras else 0
        ancho_txt = w - 2 * pad - (d + pad if d else 0)
        sombra = max(4, int(h * 0.04))
        # si el texto más largo no cabe ni con letra pequeña, los botones crecen y aparece el scroll
        need = self._nec(w, h)
        if need > h:
            h = need
            sombra = max(4, int(h * 0.04))
        total = rows * h + (rows + 1) * gap
        y0 = max(0, (H - total) / 2)
        self.configure(scrollregion=(0, 0, W, max(H, total)))
        if total <= H:
            self.yview_moveto(0)
        alto_txt = h - sombra - pad * 1.2
        # tamaño común para el 80 % de textos más cortos; los más largos se achican solos
        cortos = sorted(self.et, key=len)[:max(1, int(n * 0.8))]
        px_u = ajustar(self.t, cortos, ancho_txt, alto_txt, maximo=min(h * 0.5, 66), minimo=13)
        for i, texto in enumerate(self.et):
            r, c = divmod(i, cols)
            en_fila = min(cols, n - r * cols)
            off = (cols - en_fila) * (w + gap) / 2
            x1, y1 = gap + off + c * (w + gap), y0 + gap + r * (h + gap)
            x2, y2 = x1 + w, y1 + h
            prim, sel = i in self.primarios, self.marcada == i
            tag = f"t{i}"
            rad = max(8, int(h * 0.12))
            fondo = AZUL if prim else (AZUL_SUAVE if sel else CARA)
            tinta = "white" if prim else AZUL
            rect_red(self, x1, y1 + sombra, x2, y2, rad, fill=SOMBRA if not prim else mezcla(AZUL, 0.7),
                     outline="", tags=(tag,))
            cara = rect_red(self, x1, y1, x2, y2 - sombra, rad, fill=fondo, outline=AZUL,
                            width=4 if sel else 2, tags=(tag,))
            cy = y1 + (h - sombra) / 2
            tx1 = x1 + pad
            ovalo = letra = None
            if d:
                ovalo = self.create_oval(tx1, cy - d / 2, tx1 + d, cy + d / 2, fill=AZUL if not prim else "white",
                                         outline="", tags=(tag,))
                letra = self.create_text(tx1 + d / 2, cy, text=etiqueta_letra(i, n),
                                         fill="white" if not prim else AZUL,
                                         font=self.t.get(int(d * 0.55)), tags=(tag,))
                tx1 += d + pad
            f = self.t.get(ajustar(self.t, [texto], ancho_txt, alto_txt, maximo=px_u, minimo=11))
            lineas = envolver(texto, f, ancho_txt)
            txt = self.create_text(tx1 + ancho_txt / 2, cy, text="\n".join(lineas), fill=tinta, font=f,
                                   justify="center", width=ancho_txt + 4, tags=(tag,))
            self.caras[i] = dict(cara=cara, txt=txt, ovalo=ovalo, letra=letra, fondo=fondo, tinta=tinta, prim=prim)
            self.tag_bind(tag, "<Enter>", lambda e, i=i: self._sobre(i, True))
            self.tag_bind(tag, "<Leave>", lambda e, i=i: self._sobre(i, False))
            self.tag_bind(tag, "<ButtonRelease-1>", lambda e, i=i: self.alclic(i))

    def _sobre(self, i, dentro):
        c = self.caras.get(i)
        if not c:
            return
        if c["prim"]:
            self.itemconfig(c["cara"], fill=AZUL_CLARO if dentro else c["fondo"])
        else:  # al pasar el mouse el botón se invierte: fondo azul y letra blanca
            self.itemconfig(c["cara"], fill=AZUL if dentro else c["fondo"])
            self.itemconfig(c["txt"], fill="white" if dentro else c["tinta"])
            if c["ovalo"]:
                self.itemconfig(c["ovalo"], fill="white" if dentro else AZUL)
                self.itemconfig(c["letra"], fill=AZUL if dentro else "white")
        self.configure(cursor="hand2" if dentro else "")


# ----------------------------------------------------- lista con scroll (resultado)
class Lista(tk.Frame):
    def __init__(self, master, registrar_scroll, alelegir):
        super().__init__(master, bg="#f3f4f6")
        self.cv = tk.Canvas(self, bg="#f3f4f6", highlightthickness=0)
        sb = tk.Scrollbar(self, command=self.cv.yview)
        self.cv.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self.cv.pack(side="left", fill="both", expand=True)
        self.inner = tk.Frame(self.cv, bg="#f3f4f6")
        self.win = self.cv.create_window(0, 0, window=self.inner, anchor="nw")
        self.inner.bind("<Configure>", lambda e: self.cv.configure(scrollregion=self.cv.bbox("all")))
        self.cv.bind("<Configure>", self._ancho)
        self.items, self.alelegir, self.sel = [], alelegir, None
        registrar_scroll(self.cv)

    def _ancho(self, e):
        self.cv.itemconfig(self.win, width=e.width)
        for lb, _ in self.items:
            lb.configure(wraplength=max(120, e.width - 36))

    def agregar(self, texto, fuente, color=TEXTO):
        i = len(self.items)
        lb = tk.Label(self.inner, text=texto, font=fuente, bg="white", fg=color, anchor="w", justify="left",
                      padx=12, pady=10, wraplength=240, cursor="hand2")
        lb.pack(fill="x", padx=8, pady=(6 if i == 0 else 3, 3))
        lb.bind("<Button-1>", lambda e, i=i: self.elegir(i))
        self.items.append((lb, color))

    def elegir(self, i):
        for k, (lb, _) in enumerate(self.items):
            lb.configure(bg="#dbeafe" if k == i else "white")
        self.sel = i
        self.alelegir(i)


# ------------------------------------------------------------------- aplicación
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Asesor de formalización MYPE - Lambayeque")
        self.geometry("1150x740")
        self.minsize(560, 460)
        self.configure(bg=BG)
        self.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
        self.tipos = Tipos(self)
        self.listo = tk.IntVar()
        self.resp, self.previa = {}, None
        self.esperando, self.accion, self.opcion, self.teclas = False, None, None, {}
        self._scrolls = []

        pie = tk.Label(self, text=AVISO, bg="#f3f4f6", fg=GRIS, font=self.tipos.get(12, False),
                       padx=12, pady=5, anchor="w", justify="left")
        pie.pack(side="bottom", fill="x")
        pie.bind("<Configure>", lambda e: pie.configure(wraplength=e.width - 24))
        self.cuerpo = tk.Frame(self, bg=BG)
        self.cuerpo.pack(fill="both", expand=True)

        self.bind_all("<Key>", self._tecla)
        self.bind_all("<MouseWheel>", self._rueda)
        self.bind_all("<Button-4>", self._rueda)
        self.bind_all("<Button-5>", self._rueda)
        self.inicio()

    # --------------------------------------------------------------- base
    def limpiar(self):
        self._scrolls = []
        for w in self.cuerpo.winfo_children():
            w.destroy()

    def registrar_scroll(self, cv):
        self._scrolls.append(cv)

    def _rueda(self, e):
        w = self.winfo_containing(e.x_root, e.y_root)
        if w is None:
            return
        ruta = str(w)
        for cv in reversed(self._scrolls):
            if cv.winfo_exists() and ruta.startswith(str(cv)):
                d = -1 if (getattr(e, "num", 0) == 4 or getattr(e, "delta", 0) > 0) else 1
                cv.yview_scroll(d * 2, "units")
                return

    def _tecla(self, e):
        if e.keysym in ("Escape", "BackSpace"):
            self.atras()
        elif self.esperando and e.char and e.char.lower() in self.teclas:
            self.teclas[e.char.lower()]()

    def boton(self, padre, texto, cmd, color="#eef1f5", fg=TEXTO, lado="left"):
        b = tk.Button(padre, text=texto, command=cmd, bg=color, fg=fg, activebackground=mezcla(color, 0.92),
                      relief="flat", bd=0, padx=14, pady=6, cursor="hand2", font=self.tipos.get(14))
        b.pack(side=lado, padx=4, pady=6)
        return b

    def barra(self, centro, atras_texto="←  Atrás", habilitar_atras=True):
        bar = tk.Frame(self.cuerpo, bg="#f3f4f6")
        bar.pack(fill="x")
        if habilitar_atras:
            self.boton(bar, atras_texto, self.atras)
        tk.Label(bar, text=centro, bg="#f3f4f6", fg=GRIS, font=self.tipos.get(15)).pack(side="left", padx=10)
        if habilitar_atras or centro:
            self.boton(bar, "⌂  Inicio", self.ir_inicio, lado="right")
        return bar

    def encabezado(self, padre, titulo, sub="", color=TEXTO, pesos=1):
        cv = tk.Canvas(padre, bg=BG, highlightthickness=0)

        def dibujar(_=None):
            cv.delete("all")
            W, H = cv.winfo_width(), cv.winfo_height()
            if W < 50 or H < 30:
                return
            ancho = W - 2 * max(16, int(W * 0.05))
            hs = int(H * 0.26) if sub else 0
            px = ajustar(self.tipos, [titulo], ancho, H - hs - 14, maximo=76, minimo=18)
            f = self.tipos.get(px)
            ls = envolver(titulo, f, ancho)
            lh = f.metrics("linespace")
            bloque = len(ls) * lh
            fs = None
            if sub:
                pxs = ajustar(self.tipos, [sub], ancho, hs, maximo=max(14, int(px * 0.6)), minimo=11, bold=False)
                fs = self.tipos.get(pxs, False)
                bloque += fs.metrics("linespace") + 8
            y = max(6, (H - bloque) / 2)
            cv.create_text(W / 2, y, text="\n".join(ls), font=f, fill=color, anchor="n", justify="center")
            if sub:
                cv.create_text(W / 2, y + len(ls) * lh + 8, text="\n".join(envolver(sub, fs, ancho)), font=fs,
                               fill=GRIS, anchor="n", justify="center")

        cv.bind("<Configure>", dibujar)
        return cv

    def pantalla_mosaico(self, titulo, sub, etiquetas, alclic, primarios=None, marcada=None, centro="", atras=True,
                         letras=True):
        """Título arriba + mosaico de opciones debajo, ocupando todo el espacio."""
        self.limpiar()
        self.barra(centro, habilitar_atras=atras)
        n = len(etiquetas)
        marco = tk.Frame(self.cuerpo, bg=BG)
        marco.pack(fill="both", expand=True)
        marco.grid_columnconfigure(0, weight=1)
        a, b = (4, 6) if n <= 4 else (3, 7) if n <= 8 else (2, 8) if n <= 16 else (3, 17)
        marco.grid_rowconfigure(0, weight=a, uniform="x")
        marco.grid_rowconfigure(1, weight=b, uniform="x")
        self.encabezado(marco, titulo, sub).grid(row=0, column=0, sticky="nsew")
        m = Mosaico(marco, self.tipos, etiquetas, alclic, primarios, marcada, letras)
        m.grid(row=1, column=0, sticky="nsew")
        self.registrar_scroll(m)

    # -------------------------------------------------------------- inicio
    def inicio(self):
        self.resp, self.previa = {}, None
        nombres = list(DEMOS)
        etiquetas = ["▶  Iniciar mi consulta"] + nombres
        def clic(i):
            self.after(10, self.nueva if i == 0 else (lambda: self.ver_demo(nombres[i - 1])))

        self.pantalla_mosaico("Asesor de formalización para MYPE",
                              "Lambayeque · sistema experto basado en reglas — elija cómo empezar",
                              etiquetas, clic, {0}, centro="", atras=False, letras=False)

    def ir_inicio(self):
        if self.esperando:
            self.accion, self.esperando = "inicio", False
            self.listo.set(self.listo.get() + 1)
        else:
            self.inicio()

    # ----------------------------------------------------- consulta (preguntas)
    def nueva(self):
        self.resp, self.previa = {}, None
        self.consultar()

    def consultar(self):
        """Corre la consulta; si el usuario retrocede, quita su última respuesta y la repite."""
        while True:
            self.motor = construir_motor(self.preguntar)
            try:
                res = self.motor.consultar(K.TRAMITES)
                break
            except Atras:
                self.previa = self.resp.popitem()
            except Inicio:
                self.inicio()
                return
        self.resultado(self.motor, res)

    def atras(self):
        if self.esperando:
            self.accion = "atras" if self.resp else "inicio"
            self.esperando = False
            self.listo.set(self.listo.get() + 1)
        elif self.resp:  # pantalla de resultado: deshacer la última respuesta
            self.previa = self.resp.popitem()
            self.consultar()
        else:
            self.inicio()

    def ver_demo(self, nombre):
        self.resp, self.previa = {}, None
        self.motor = construir_motor(hechos=DEMOS[nombre])
        self.resultado(self.motor, self.motor.consultar(K.TRAMITES), demo=nombre)

    def preguntar(self, var, p):
        """ask_fn del motor: muestra la pregunta a pantalla completa y espera la respuesta."""
        if var.startswith("hecho.") and any(self.motor.hechos.get("hecho." + d) is False
                                            for d in K.TRAMITES[var[6:]]["deps"]):
            return False  # si falta un trámite previo, este tampoco está hecho: no se pregunta
        if var in self.resp:
            return self.resp[var]  # ya contestada (se repite la consulta tras retroceder)
        valores = [v for v, _ in p.opciones]
        etiquetas = [e for _, e in p.opciones]
        marcada = valores.index(self.previa[1]) if self.previa and self.previa[0] == var else None
        partes = [x.strip() for x in p.texto.split("  ") if x.strip()]
        titulo, sub = partes[0], " ".join(partes[1:])

        def elegir(i):
            if not self.esperando:
                return
            self.opcion, self.accion, self.esperando = i, "ok", False
            self.listo.set(self.listo.get() + 1)

        n = len(etiquetas)
        self.teclas = {}
        if n <= 26:
            self.teclas.update({chr(97 + i): (lambda i=i: elegir(i)) for i in range(n)})
        if n <= 9:
            self.teclas.update({str(i + 1): (lambda i=i: elegir(i)) for i in range(n)})
        self.esperando = True
        self.pantalla_mosaico(titulo, sub, etiquetas, elegir, None, marcada, centro=f"Pregunta {len(self.resp) + 1}")
        self.wait_variable(self.listo)
        self.esperando, self.teclas = False, {}
        if self.accion == "atras":
            raise Atras
        if self.accion == "inicio":
            raise Inicio
        self.resp[var] = p.opciones[self.opcion][0]  # valor original (True/False, texto...)
        return self.resp[var]

    # ------------------------------------------------------------- resultado
    def resultado(self, motor, res, demo=None):
        self.limpiar()
        self.previa = None
        h, ok = motor.hechos, res["formalizado"]
        color = "#1b9e4b" if ok else "#d93a2f"
        self.barra("Resultado" if not demo else "Resultado (caso de demostración)",
                   "←  Corregir última respuesta", habilitar_atras=bool(self.resp))
        ban = tk.Frame(self.cuerpo, bg=color)
        ban.pack(fill="x")
        msg = ("✔  Su negocio cumple todos los trámites obligatorios evaluados." if ok else
               f"✘  Negocio NO formalizado: faltan {len(res['pendientes'])} trámites obligatorios.")
        lb = tk.Label(ban, text=msg, bg=color, fg="white", font=self.tipos.get(26), anchor="w", justify="left",
                      padx=20, pady=14)
        lb.pack(fill="x")
        ban.bind("<Configure>", lambda e: lb.configure(wraplength=e.width - 40))

        chips = tk.Frame(self.cuerpo, bg=BG)
        chips.pack(fill="x", padx=8, pady=8)
        datos = (("Rubro", K.RUBROS[h["rubro"]]["n"]), ("Régimen", h.get("regimen")),
                 ("Riesgo ITSE", h.get("nivel_riesgo") or "no aplica"), ("Tamaño", h.get("tamano")))
        for j, (a, b) in enumerate(datos):
            chips.grid_columnconfigure(j, weight=3 if j == 0 else 1, uniform="chip")
            c = tk.Frame(chips, bg="#eef2f7")
            c.grid(row=0, column=j, sticky="nsew", padx=4)
            tk.Label(c, text=a, bg="#eef2f7", fg=GRIS, font=self.tipos.get(12, False), anchor="w").pack(fill="x", padx=10, pady=(6, 0))
            l2 = tk.Label(c, text=str(b), bg="#eef2f7", fg=TEXTO, font=self.tipos.get(15), anchor="w", justify="left")
            l2.pack(fill="x", padx=10, pady=(0, 6))
            c.bind("<Configure>", lambda e, l2=l2: l2.configure(wraplength=e.width - 20))

        self.boton(self.cuerpo, "↺  Nueva consulta", self.nueva if not demo else self.inicio,
                   color=VERDE, fg="white", lado="bottom")
        panel = tk.Frame(self.cuerpo, bg=BG)
        panel.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        panel.grid_columnconfigure(0, weight=2, minsize=230, uniform="p")
        panel.grid_columnconfigure(1, weight=3, uniform="p")
        panel.grid_rowconfigure(0, weight=1)

        derecha = tk.Frame(panel, bg=BG)
        derecha.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        sb = tk.Scrollbar(derecha)
        sb.pack(side="right", fill="y")
        txt = tk.Text(derecha, wrap="word", padx=18, pady=14, bd=0, bg="#fbfbfd", yscrollcommand=sb.set,
                      font=self.tipos.get(15, False), spacing3=4, cursor="arrow")
        txt.pack(side="left", fill="both", expand=True)
        sb.configure(command=txt.yview)
        t = self.tipos
        txt.tag_configure("h1", font=t.get(24), foreground=TEXTO, spacing3=10)
        txt.tag_configure("h2", font=t.get(16), foreground="#1d4ed8", spacing1=12, spacing3=4)
        txt.tag_configure("fuente", font=t.get(13, False, True), foreground=GRIS, lmargin1=22, lmargin2=22)
        txt.tag_configure("li", lmargin1=12, lmargin2=28)
        txt.tag_configure("ok", foreground="#1b7f3b")
        txt.tag_configure("rec", foreground="#b45309")

        def pintar(partes):
            txt.configure(state="normal")
            txt.delete("1.0", "end")
            for tag, s in partes:
                txt.insert("end", s + "\n", tag)
            txt.configure(state="disabled")

        items = [("Resumen", self.resumen(res), "#1d4ed8")]
        for i, tr in enumerate(res["pendientes"], 1):
            items.append((f"{i}. {K.TRAMITES[tr]['n']}", self.detalle(motor, tr), "#b3261e"))
        for tr in res["recomendados"]:
            items.append((f"★ {K.TRAMITES[tr]['n']}", self.detalle(motor, tr), "#b45309"))

        lista = Lista(panel, self.registrar_scroll, lambda i: pintar(items[i][1]))
        lista.grid(row=0, column=0, sticky="nsew")
        for titulo, _, col in items:
            lista.agregar(titulo, t.get(15), col)
        lista.elegir(1 if len(items) > 1 else 0)

    def resumen(self, res):
        p = [("h1", "Resumen")]
        p.append(("h2", f"Trámites obligatorios pendientes: {len(res['pendientes'])}"))
        p += [("li", f"•  {K.TRAMITES[tr]['n']}") for tr in res["pendientes"]] or [("li", "Ninguno.")]
        p.append(("h2", "Ya cumplidos"))
        p += [("ok li", f"✔  {K.TRAMITES[tr]['n']}") for tr in res["cumplidos"]] or [("li", "Ninguno todavía.")]
        if res["recomendados"]:
            p.append(("h2", "Recomendados (no obligatorios)"))
            p += [("rec li", f"★  {K.TRAMITES[tr]['n']}") for tr in res["recomendados"]]
        p.append(("h2", "Avisos y alertas"))
        p += [("li", f"•  {a}") for a in res["avisos"]] or [("li", "Sin avisos.")]
        return p

    def detalle(self, motor, tr):
        info = K.TRAMITES[tr]
        p = [("h1", info["n"]), ("h2", "Dónde se tramita"), ("li", motor.hechos.get("donde." + tr) or info["ent"]),
             ("h2", "Por qué se requiere")]
        for rid, por, fuente, regla in motor.por_que(f"req.{tr}"):
            p.append(("li", f"•  {por}"))
            p.append(("fuente", f"Fuente: {fuente}  ({rid})"))
        docs = motor.hechos.get(f"docs.{tr}") or []
        if docs:
            p.append(("h2", "Documentos habituales"))
            p += [("li", f"✓  {d}") for d in docs]
        return p


if __name__ == "__main__":
    App().mainloop()