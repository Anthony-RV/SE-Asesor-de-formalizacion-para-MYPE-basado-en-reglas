# -*- coding: utf-8 -*-
"""Verificación de la base: redundancias, conflictos, circularidad, reglas sin salida."""
from collections import defaultdict
import catalogo as K
from motor import es_acumulativa


def verificar(reglas, preguntas):
    informe = {}
    por_var = defaultdict(list)
    for r in reglas:
        por_var[r.var].append(r)
    derivadas = set(por_var)
    preguntables = set(preguntas)

    # 1) IDs únicos y fuente informada
    ids = [r.id for r in reglas]
    informe["ids_repetidos"] = sorted({i for i in ids if ids.count(i) > 1})
    informe["sin_fuente"] = [r.id for r in reglas if not r.fuente.strip()]

    # 2) variables sin definición (reglas "sin salida") y valores fuera de dominio
    indef, fuera = [], []
    for r in reglas:
        for c in r.conds:
            if c.var not in derivadas and c.var not in preguntables:
                indef.append((r.id, c.var))
            elif c.var in preguntables and c.op in ("=", "in") and c.var in preguntas:
                dom = {v for v, _ in preguntas[c.var].opciones}
                vals = c.val if c.op == "in" else (c.val,)
                if any(v not in dom for v in vals):
                    fuera.append((r.id, c.var, c.val))
    informe["variables_sin_definicion"] = indef
    informe["valores_fuera_de_dominio"] = fuera

    # 3) redundancias (misma condición y misma conclusión) y conflictos (misma condición, otro valor)
    vistos, redundantes, conflictos = {}, [], []
    for r in reglas:
        clave = (frozenset(r.conds), r.var)
        if es_acumulativa(r.var):
            clave = (frozenset(r.conds), r.var, r.val)
        if clave in vistos:
            previo = vistos[clave]
            if previo.val == r.val:
                redundantes.append((previo.id, r.id))
            else:
                conflictos.append((previo.id, r.id))
        else:
            vistos[clave] = r
    informe["redundantes"] = redundantes
    informe["conflictos"] = conflictos

    # 4) circularidad entre variables derivadas
    grafo = {v: {c.var for r in rs for c in r.conds if c.var in derivadas} for v, rs in por_var.items()}
    ciclos, estado = [], {}

    def dfs(v, ruta):
        estado[v] = 1
        for w in grafo.get(v, ()):
            if estado.get(w) == 1:
                ciclos.append(" -> ".join(ruta + [v, w]))
            elif w not in estado:
                dfs(w, ruta + [v])
        estado[v] = 2

    for v in grafo:
        if v not in estado:
            dfs(v, [])
    informe["ciclos"] = ciclos

    # 5) conclusiones que nadie usa (ni son salida del sistema)
    usadas = {c.var for r in reglas for c in r.conds}
    salidas = ("req.", "donde.", "docs.", "avisos")
    informe["conclusiones_sin_uso"] = sorted(
        v for v in derivadas if v not in usadas and not v.startswith(salidas))

    # 6) orden de trámites coherente con dependencias
    mal = [(t, d) for t, i in K.TRAMITES.items() for d in i["deps"]
           if K.TRAMITES[d]["orden"] >= i["orden"]]
    informe["orden_incoherente"] = mal

    # 7) toda variable `req.X` usada existe en el catálogo
    informe["tramites_inexistentes"] = sorted(
        {v[4:] for v in derivadas | usadas if v.startswith("req.") and v[4:] not in K.TRAMITES})
    return informe


def imprimir(informe, n_reglas):
    print(f"Reglas totales: {n_reglas}")
    ok = True
    for k, v in informe.items():
        estado = "OK " if not v else "ERR"
        if v:
            ok = False
        print(f"  [{estado}] {k}: {len(v)}")
        for x in list(v)[:5]:
            print("        ", x)
    print("Resultado:", "base consistente" if ok else "revisar los puntos marcados")