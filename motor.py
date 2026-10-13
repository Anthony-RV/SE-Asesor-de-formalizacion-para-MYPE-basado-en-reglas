# -*- coding: utf-8 -*-
"""
Motor de inferencia con ENCADENAMIENTO HACIA ATRÁS.

Meta principal : negocio_formalizado
Submetas       : req.<TRAMITE>  (¿se requiere?)  y  hecho.<TRAMITE> (¿ya se hizo?)
                 negocio_formalizado = no queda ningún trámite obligatorio pendiente.

Para demostrar una variable el motor busca las reglas que la concluyen y
trata sus condiciones como submetas. Si una variable no se puede derivar y es
"preguntable", se la pide al usuario (solo cuando hace falta).

Resolución de conflictos (variables con un solo valor):
    1) mayor prioridad  2) mayor especificidad (más condiciones)  3) orden de definición.
Variables booleanas (req.*): se evalúan TODAS las reglas para poder explicar.
Variables acumulativas (avisos, docs.*): se juntan los valores de todas las reglas.
Cierre del mundo: una variable booleana sin regla disparada vale False.
"""
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Cond:
    var: str
    op: str      # "=", "!=", "in", "not_in"
    val: object

    def evalua(self, x):
        if self.op == "=":
            return x == self.val
        if self.op == "!=":
            return x != self.val
        if self.op == "in":
            return x in self.val
        if self.op == "not_in":
            return x not in self.val
        raise ValueError(f"Operador desconocido: {self.op}")

    def texto(self):
        simb = {"=": "=", "!=": "≠", "in": "∈", "not_in": "∉"}[self.op]
        return f"{self.var} {simb} {self.val}"


@dataclass
class Regla:
    id: str
    conds: tuple
    var: str
    val: object
    por_que: str
    fuente: str
    grupo: str = ""
    prioridad: int = 0

    def texto(self):
        si = " Y ".join(c.texto() for c in self.conds) or "SIEMPRE"
        return f"SI {si} ENTONCES {self.var} = {self.val}"


@dataclass
class Pregunta:
    texto: str
    opciones: list   # [(valor, etiqueta)]


def es_acumulativa(var):
    return var == "avisos" or var.startswith("docs.")


class Motor:
    def __init__(self, reglas, preguntas, ask_fn=None, hechos=None):
        self.reglas = reglas
        self.preguntas = preguntas
        self.ask_fn = ask_fn
        self.por_var = defaultdict(list)
        for r in reglas:
            self.por_var[r.var].append(r)
        for rs in self.por_var.values():
            rs.sort(key=lambda r: (-r.prioridad, -len(r.conds)))  # sort estable
        self.booleanas = {v for v, rs in self.por_var.items()
                          if all(isinstance(r.val, bool) for r in rs)}
        self.hechos = dict(hechos or {})
        self.como = {}          # variable -> reglas que se dispararon
        self.preguntadas = []
        self.ciclos = []
        self._pila = []

    # ------------------------------------------------------------ inferencia
    def _cumple(self, regla):
        return all(c.evalua(self.valor(c.var)) for c in regla.conds)

    def valor(self, var):
        if var in self.hechos:
            return self.hechos[var]
        if var in self._pila:                       # circularidad
            self.ciclos.append(" -> ".join(self._pila + [var]))
            return None
        if var in self.por_var:
            self._pila.append(var)
            disp = [r for r in self.por_var[var] if self._cumple(r)]
            self._pila.pop()
            if disp:
                self.como[var] = disp
                if es_acumulativa(var):
                    val = [r.val for r in disp]
                elif var in self.booleanas:
                    val = True
                else:
                    val = disp[0].val               # resolución de conflictos
            else:
                val = [] if es_acumulativa(var) else (False if var in self.booleanas else None)
            self.hechos[var] = val
            return val
        if var in self.preguntas:
            val = self.ask_fn(var, self.preguntas[var]) if self.ask_fn else None
            self.preguntadas.append(var)
            self.hechos[var] = val
            return val
        self.hechos[var] = None
        return None

    # ------------------------------------------------------------- consulta
    def consultar(self, tramites):
        """Demuestra la meta negocio_formalizado y arma la lista ordenada."""
        res = {"pendientes": [], "cumplidos": [], "recomendados": [], "formalizado": None}
        for t in sorted(tramites, key=lambda k: tramites[k]["orden"]):
            if self.valor(f"req.{t}"):
                hecho = bool(self.valor(f"hecho.{t}"))
                if tramites[t]["tipo"] == "oblig":
                    (res["cumplidos"] if hecho else res["pendientes"]).append(t)
                elif not hecho:
                    res["recomendados"].append(t)
        res["formalizado"] = not res["pendientes"]
        for t in res["pendientes"] + res["recomendados"]:
            self.valor(f"donde.{t}")
            self.valor(f"docs.{t}")
        res["avisos"] = self.valor("avisos")
        return res

    # ----------------------------------------------------------- explicación
    def por_que(self, var):
        """¿Por qué se concluyó esto? -> reglas disparadas con su justificación y fuente."""
        return [(r.id, r.por_que, r.fuente, r.texto()) for r in self.como.get(var, [])]