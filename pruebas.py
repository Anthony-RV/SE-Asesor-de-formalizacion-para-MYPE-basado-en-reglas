# -*- coding: utf-8 -*-
"""
Script para ejecutar 50 casos de prueba automatizados en el sistema experto.
Guarda los resultados en memoria y los imprime por consola.
Uso: python pruebas_automatizadas.py
"""
import random
import catalogo as K
from base_conocimiento import construir_reglas, construir_preguntas
from motor import Motor

def dummy_ask(var, pregunta):
    """Simula la respuesta del usuario para no bloquear la ejecución interactiva."""
    if var.startswith("hecho."):
        # Asumimos que la MYPE no ha realizado ningún trámite previo
        return False
    return None

def generar_casos(n=50):
    """Genera n casos de prueba aleatorios pero válidos y representativos."""
    random.seed(42)  # Semilla fija para que los resultados sean siempre reproducibles
    casos = []
    
    # Listas de opciones desde el catálogo
    rubros = list(K.RUBROS.keys())
    personas = list(K.PERSONAS.keys())
    distritos = list(K.DISTRITOS.keys())
    locales = list(K.LOCALES.keys())
    areas = list(K.AREAS.keys())
    ingresos = [b for b, _, _ in K.INGRESOS]
    trabajadores = list(K.TRABAJADORES.keys())
    sino = ["si", "no"]

    for i in range(n):
        caso = {
            "id_caso": f"Caso-{i+1:03d}",
            "rubro": random.choice(rubros),
            "persona": random.choice(personas),
            "distrito": random.choice(distritos),
            "local": random.choice(locales),
            "area": random.choice(areas),
            "ingresos": random.choice(ingresos),
            "trabajadores": random.choice(trabajadores),
            "vende_a_empresas": random.choice(sino),
            "tiene_letrero": random.choice(sino),
            "vende_alcohol": random.choice(sino)
        }
        
        # Pre-rellenar los hechos de trámites para evitar preguntas interactivas (ask_fn)
        for t in K.TRAMITES:
            caso[f"hecho.{t}"] = False
            
        casos.append(caso)
    return casos

def ejecutar_pruebas():
    # 1. Cargar la base de conocimiento (Motor)
    reglas = construir_reglas()
    preguntas = construir_preguntas()
    
    # 2. Generar los 50 casos en memoria
    casos = generar_casos(50)
    resultados_en_memoria = []

    print("============================================================")
    print(f" INICIANDO EJECUCIÓN AUTOMATIZADA DE {len(casos)} CASOS DE PRUEBA")
    print("============================================================\n")

    # 3. Procesar caso por caso de manera desatendida
    for caso in casos:
        id_caso = caso.pop("id_caso")
        
        # Instanciar el motor inyectando los datos del caso directamente en "hechos"
        motor = Motor(reglas, preguntas, ask_fn=dummy_ask, hechos=caso)
        res = motor.consultar(K.TRAMITES)
        
        # Extraer métricas y determinaciones clave del motor
        pendientes = res["pendientes"]
        regimen = motor.hechos.get("regimen", "No determinado")
        riesgo = motor.hechos.get("nivel_riesgo", "No aplica")
        tamano = motor.hechos.get("tamano", "No aplica")
        
        # Guardar resultados en memoria (como diccionarios)
        resultados_en_memoria.append({
            "id_caso": id_caso,
            "entradas": caso,
            "pendientes": pendientes,
            "total_pendientes": len(pendientes),
            "regimen_sugerido": regimen,
            "riesgo_itse": riesgo,
            "tamano": tamano
        })
        
        # Imprimir salida resumida de la iteración
        print(f"[{id_caso}] Rubro: {caso['rubro'].upper()} | Local: {caso['local']} | Régimen: {regimen} | ITSE: {riesgo}")
        print(f"  -> Trámites obligatorios a realizar: {len(pendientes)}")
        if pendientes:
            # Mostrar solo los 3 primeros trámites en la consola para limpieza visual
            print(f"  -> Primeros pasos: {', '.join(pendientes[:3])}...")
        print("-" * 60)

    # 4. Resultados globales
    print("\n============================================================")
    print(" RESUMEN FINAL DE LAS PRUEBAS")
    print("============================================================")
    print(f"Total de pruebas procesadas y guardadas en memoria: {len(resultados_en_memoria)}")
    
    # Calcular algunas estadísticas básicas sobre los casos en memoria
    promedio_tramites = sum(r['total_pendientes'] for r in resultados_en_memoria) / len(resultados_en_memoria)
    print(f"Promedio de trámites pendientes por MYPE: {promedio_tramites:.1f}")
    
    regimenes_asignados = {}
    for r in resultados_en_memoria:
        reg = r["regimen_sugerido"]
        regimenes_asignados[reg] = regimenes_asignados.get(reg, 0) + 1
    
    print(f"Distribución de regímenes tributarios sugeridos:")
    for reg, count in regimenes_asignados.items():
        print(f"  - {reg}: {count} casos")
        
    print("============================================================")
    
    # Se retorna la lista para que pueda ser utilizada/exportada si se requiere más adelante
    return resultados_en_memoria

if __name__ == "__main__":
    # Al ejecutar este script se procesan las 50 iteraciones
    mis_resultados = ejecutar_pruebas()