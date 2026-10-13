# -*- coding: utf-8 -*-
"""
Asesor de formalización para MYPE (Lambayeque) -- sistema experto basado en reglas.

Uso:
    python main.py              consulta interactiva
    python main.py --demo       3 casos de ejemplo sin preguntas
    python main.py --verificar  verifica la base de conocimiento
    python main.py --exportar   genera reglas.csv (Anexo B del informe)
"""
import csv
import sys

import catalogo as K
from base_conocimiento import construir_reglas, construir_preguntas
from motor import Motor
from verificador import verificar, imprimir

AVISO = ("AVISO: este sistema orienta, no reemplaza a un contador, abogado o a la municipalidad. "
         "Verifique requisitos, tasas y plazos en el TUPA vigente de su municipalidad.")


def preguntar_consola(var, p):
    print(f"\n{p.texto}")
    for i, (_, etiqueta) in enumerate(p.opciones, 1):
        print(f"  {i}. {etiqueta}")
    while True:
        s = input("> ").strip()
        if s.isdigit() and 1 <= int(s) <= len(p.opciones):
            return p.opciones[int(s) - 1][0]
        print("Opción no válida, ingrese el número.")


def mostrar(motor, res):
    print("\n" + "=" * 70)
    perfil = motor.hechos
    print(f"Rubro: {K.RUBROS[perfil['rubro']]['n']} | Régimen sugerido: {perfil.get('regimen')} | "
          f"Riesgo ITSE: {perfil.get('nivel_riesgo')} | Tamaño: {perfil.get('tamano')}")
    print("=" * 70)
    if res["formalizado"]:
        print("✔ Su negocio cumple todos los trámites obligatorios evaluados.")
    else:
        print(f"✘ Negocio NO formalizado: faltan {len(res['pendientes'])} trámites obligatorios.")
        print("\nTRÁMITES PENDIENTES (en el orden recomendado):")
    for n, t in enumerate(res["pendientes"], 1):
        info = K.TRAMITES[t]
        donde = motor.hechos.get(f"donde.{t}") or info["ent"]
        print(f"\n{n}. {info['n']}")
        print(f"   Dónde: {donde}")
        for rid, por, fuente, _ in motor.por_que(f"req.{t}")[:2]:
            print(f"   Por qué ({rid}): {por}  [Fuente: {fuente}]")
        docs = motor.hechos.get(f"docs.{t}") or []
        if docs:
            print("   Documentos habituales:")
            for d in docs:
                print(f"     - {d}")
    if res["cumplidos"]:
        print("\nYA CUMPLIDOS: " + "; ".join(K.TRAMITES[t]["n"] for t in res["cumplidos"]))
    if res["recomendados"]:
        print("\nRECOMENDADOS (no obligatorios): " + "; ".join(K.TRAMITES[t]["n"] for t in res["recomendados"]))
    if res["avisos"]:
        print("\nAVISOS Y ALERTAS:")
        for a in res["avisos"]:
            print(f"  • {a}")
    print("\n" + AVISO)


def construir_motor(ask_fn=None, hechos=None):
    return Motor(construir_reglas(), construir_preguntas(), ask_fn, hechos)


def consulta_interactiva():
    motor = construir_motor(preguntar_consola)
    res = motor.consultar(K.TRAMITES)
    mostrar(motor, res)
    while True:
        s = input("\n¿Cómo? Ingrese el número de un trámite pendiente para ver todas las reglas "
                  "que lo concluyeron (Enter para salir): ").strip()
        if not s:
            break
        if s.isdigit() and 1 <= int(s) <= len(res["pendientes"]):
            t = res["pendientes"][int(s) - 1]
            for rid, por, fuente, texto in motor.por_que(f"req.{t}"):
                print(f"  {rid}: {texto}\n      {por}  [{fuente}]")


DEMOS = {
    "Caso demo 1: restaurante en Chiclayo (persona natural, local alquilado)": dict(
        rubro="restaurante", persona="natural", distrito="Chiclayo", local="alquilado", area="a1",
        ingresos="B2", trabajadores="t1", vende_a_empresas="no", tiene_letrero="si", vende_alcohol="no",
        **{"hecho.RUC": True, "hecho.CLAVE_SOL": True, "hecho.ELEGIR_REGIMEN": True}),
    "Caso demo 2: botica SAC en La Victoria": dict(
        rubro="botica", persona="juridica", distrito="La Victoria", local="alquilado", area="a2",
        ingresos="B4", trabajadores="t1", tiene_letrero="no",
        **{"hecho.BUSQUEDA_RESERVA": True, "hecho.MINUTA_ESCRITURA": True, "hecho.INSCRIPCION_SUNARP": True,
           "hecho.RUC": True}),
    "Caso demo 3: venta ambulante de juguería en Lambayeque": dict(
        rubro="cafeteria", persona="natural", distrito="Lambayeque", local="ambulante", ingresos="B1",
        trabajadores="t0", vende_a_empresas="no"),
}


def demo():
    for titulo, hechos in DEMOS.items():
        print("\n\n##### " + titulo)
        motor = construir_motor(hechos=hechos)
        mostrar(motor, motor.consultar(K.TRAMITES))


def exportar(ruta="reglas.csv"):
    with open(ruta, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Grupo", "SI", "ENTONCES", "Justificación", "Fuente"])
        for r in construir_reglas():
            si = " Y ".join(c.texto() for c in r.conds) or "SIEMPRE"
            w.writerow([r.id, r.grupo, si, f"{r.var} = {r.val}", r.por_que, r.fuente])
    print(f"Base exportada en {ruta}")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--demo":
        demo()
    elif arg == "--verificar":
        imprimir(verificar(construir_reglas(), construir_preguntas()), len(construir_reglas()))
    elif arg == "--exportar":
        exportar()
    else:
        print(AVISO)
        consulta_interactiva()