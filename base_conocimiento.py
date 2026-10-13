# -*- coding: utf-8 -*-
"""
Base de conocimiento del Asesor de formalización para MYPE (Lambayeque).

Las reglas se generan desde las tablas de catalogo.py, de modo que cada regla
tiene ID, grupo, justificación y fuente. Para el informe (Anexo B) use
`python main.py --exportar`.
"""
from motor import Regla, Cond as C, Pregunta
import catalogo as K

SI_NO = [("si", "Sí"), ("no", "No")]


def _nivel_max(a, b):
    return K.NIVELES[max(K.NIVELES.index(a), K.NIVELES.index(b))]


def consejo_local(local, rb):
    """Texto específico según la combinación rubro × local."""
    if local == "domicilio":
        if rb["dom"]:
            return ("verifique que la zonificación residencial admita el giro; si vive en edificio o "
                    "condominio puede necesitar autorización de la junta de propietarios.")
        return ("ALERTA: es poco probable que este giro sea compatible con una vivienda; "
                "evalúe un local comercial o industrial y pida antes el certificado de zonificación.")
    if local == "mercado":
        if rb["mer"]:
            return "pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado."
        return "ALERTA: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad."
    if local == "ambulante":
        if rb["amb"]:
            return ("necesita autorización municipal de comercio ambulatorio, solo en zonas y horarios permitidos; "
                    "no se tramita licencia de funcionamiento.")
        return "ALERTA: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento."
    if local == "alquilado":
        return ("verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización "
                "del propietario con firma legalizada para la licencia.")
    if local == "propio":
        return "tenga a mano el título o partida registral y revise cargas y zonificación del predio."
    return ("antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso "
            "para el giro; no pague adelantos sin ese documento.")


def construir_reglas():
    R = []

    def r(grupo, conds, var, val, por_que, fuente, prio=0):
        R.append(Regla(f"R{len(R) + 1:04d}", tuple(conds), var, val, por_que, fuente, grupo, prio))

    # ---------------------------------------------------- 1. constitución
    for t in ("BUSQUEDA_RESERVA", "MINUTA_ESCRITURA", "INSCRIPCION_SUNARP"):
        r("constitucion", [C("persona", "=", "juridica")], f"req.{t}", True,
          f"Una persona jurídica existe legalmente al inscribirse en Registros Públicos: {K.TRAMITES[t]['n']}.",
          K.FUENTES[t])

    # ---------------------------------------------------- 2. tributario común
    for t in ("RUC", "CLAVE_SOL", "ELEGIR_REGIMEN", "COMPROBANTES", "DECLARACION_MENSUAL", "LIBRO_RECLAMACIONES"):
        por = {"RUC": "Todo negocio necesita RUC para operar formalmente.",
               "CLAVE_SOL": "La Clave SOL permite realizar los trámites tributarios en línea.",
               "ELEGIR_REGIMEN": "Debe estar acogido a un régimen tributario.",
               "COMPROBANTES": "Debe emitir comprobantes de pago por sus ventas.",
               "DECLARACION_MENSUAL": "Todo régimen exige declarar o pagar periódicamente.",
               "LIBRO_RECLAMACIONES": "Todo proveedor que atiende consumidores debe contar con Libro de Reclamaciones."}[t]
        r("tributario", [], f"req.{t}", True, por, K.FUENTES[t])

    r("tributario", [C("rubro", "=", "prof")], "profesional", True,
      "Los servicios profesionales con título no pueden acogerse al NRUS.", K.FUENTES["ELEGIR_REGIMEN"])

    for reg in ("RER", "RMT", "RG"):
        r("tributario", [C("regimen", "=", reg)], "req.LIBROS_CONTABLES", True,
          f"En el régimen {reg} se deben llevar libros o registros contables (el NRUS no).",
          K.FUENTES["LIBROS_CONTABLES"])

    # tamaño de empresa
    for b, _, _ in K.INGRESOS:
        r("regimen", [C("ingresos", "=", b)], "tamano", K.TAMANO[b],
          "El tamaño de la empresa se determina por el nivel de ventas anuales (UIT).",
          "TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar límites vigentes")

    # régimen tributario sugerido (solo se pregunta lo necesario)
    f_reg = K.FUENTES["ELEGIR_REGIMEN"] + " -- verificar topes vigentes"
    r("regimen", [C("ingresos", "=", "B6")], "regimen", "RG", "Con ventas sobre 1,700 UIT corresponde el Régimen General.", f_reg)
    for b in ("B4", "B5"):
        r("regimen", [C("ingresos", "=", b)], "regimen", "RMT",
          "Con ventas hasta 1,700 UIT y más de 525 mil al año corresponde el Régimen MYPE Tributario.", f_reg)
    r("regimen", [C("persona", "=", "juridica"), C("ingresos", "in", ("B1", "B2", "B3"))], "regimen", "RMT",
      "Una persona jurídica no puede acogerse al NRUS; con ventas bajas, el RMT es la opción habitual.", f_reg)
    r("regimen", [C("persona", "=", "natural"), C("ingresos", "=", "B3")], "regimen", "RER",
      "Persona natural con ventas sobre el tope del NRUS y hasta 525 mil al año: RER.", f_reg)
    for b in ("B1", "B2"):
        r("regimen", [C("persona", "=", "natural"), C("ingresos", "=", b), C("profesional", "=", True)],
          "regimen", "RER", "El NRUS excluye servicios profesionales; con ventas bajas corresponde el RER.", f_reg)
        r("regimen", [C("persona", "=", "natural"), C("ingresos", "=", b), C("profesional", "=", False),
                      C("vende_a_empresas", "=", "si")],
          "regimen", "RER", "Si vende a empresas necesita emitir facturas, lo que el NRUS no permite: RER.", f_reg)
        r("regimen", [C("persona", "=", "natural"), C("ingresos", "=", b), C("profesional", "=", False),
                      C("vende_a_empresas", "=", "no")],
          "regimen", "NRUS", "Persona natural con ventas bajas que solo emite boletas: NRUS.", f_reg)

    # ---------------------------------------------------- 3. local
    for l in K.ESTABLECIDOS:
        r("local", [C("local", "=", l)], "req.LICENCIA_FUNCIONAMIENTO", True,
          "Todo establecimiento donde se atiende al público necesita licencia de funcionamiento.",
          K.FUENTES["LICENCIA_FUNCIONAMIENTO"])
    for l in ("propio", "alquilado", "domicilio", "ninguno_aun"):
        r("local", [C("local", "=", l)], "req.CERT_ZONIFICACION", True,
          "Debe comprobar que el giro sea compatible con la zonificación del predio.",
          K.FUENTES["CERT_ZONIFICACION"])
    for l, t in (("propio", "ACREDITAR_PROPIEDAD"), ("alquilado", "CONTRATO_ALQUILER"),
                 ("domicilio", "ACREDITAR_LOCAL"), ("ninguno_aun", "ACREDITAR_LOCAL"),
                 ("mercado", "AUTORIZ_PUESTO_MERCADO"), ("ambulante", "AUTORIZ_AMBULANTE")):
        r("local", [C("local", "=", l)], f"req.{t}", True,
          f"Según el tipo de local ({K.LOCALES[l]}) se requiere: {K.TRAMITES[t]['n']}.", K.FUENTES[t])
    for l in K.ESTABLECIDOS:
        r("local", [C("local", "=", l), C("tiene_letrero", "=", "si")], "req.AUTORIZ_ANUNCIO", True,
          "Los letreros y anuncios publicitarios requieren autorización municipal.", K.FUENTES["AUTORIZ_ANUNCIO"])

    # ---------------------------------------------------- 4. seguridad (riesgo e ITSE)
    f_riesgo = K.F_ITSE + " -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente"
    for k, rb in K.RUBROS.items():
        for a, nv_area in K.NIVEL_AREA.items():
            nv = _nivel_max(rb["riesgo"], nv_area)
            r("riesgo", [C("rubro", "=", k), C("area", "=", a)], "nivel_riesgo", nv,
              f"{rb['n']} (riesgo base {rb['riesgo']}) con {K.AREAS[a].lower()} -> riesgo {nv}.", f_riesgo)
    itse = {"bajo": "ITSE_BASICA", "medio": "ITSE_BASICA", "alto": "ITSE_DETALLE", "muy_alto": "ITSE_MULTI"}
    for l in K.ESTABLECIDOS:
        for nv, t in itse.items():
            r("seguridad", [C("local", "=", l), C("nivel_riesgo", "=", nv)], f"req.{t}", True,
              f"Riesgo {nv} en un establecimiento ({K.LOCALES[l].lower()}) exige {K.TRAMITES[t]['n']}.", K.F_ITSE)

    # ---------------------------------------------------- 5. requisitos por rubro
    for k, rb in K.RUBROS.items():
        for t in rb["tr"]:
            r("rubro", [C("rubro", "=", k)], f"req.{t}", True,
              f"El giro «{rb['n']}» requiere: {K.TRAMITES[t]['n']}.", K.FUENTES[t])
        if rb["alc"]:
            r("rubro", [C("rubro", "=", k), C("vende_alcohol", "=", "si")], "req.AUTORIZ_ALCOHOL", True,
              "Vender bebidas alcohólicas requiere autorización municipal adicional.", K.FUENTES["AUTORIZ_ALCOHOL"])

    # ---------------------------------------------------- 6. laboral
    for t_ in ("t1", "t2"):
        for t in ("T_REGISTRO", "CONTRATOS_LABORALES", "SST_BASICO"):
            r("laboral", [C("trabajadores", "=", t_)], f"req.{t}", True,
              f"Con trabajadores a cargo, el empleador debe cumplir: {K.TRAMITES[t]['n']}.", K.FUENTES[t])
        for tam in ("micro", "pequena"):
            r("laboral", [C("trabajadores", "=", t_), C("tamano", "=", tam)], "req.REMYPE", True,
              "La MYPE con trabajadores debe acreditarse en el REMYPE para acceder al régimen laboral especial.",
              K.FUENTES["REMYPE"])
        for k, rb in K.RUBROS.items():
            if rb["sctr"]:
                r("laboral", [C("rubro", "=", k), C("trabajadores", "=", t_)], "req.SCTR", True,
                  f"«{rb['n']}» implica actividad de riesgo: el personal debe contar con SCTR "
                  f"(verificar el anexo de actividades de riesgo).", K.FUENTES["SCTR"])

    # ---------------------------------------------------- 7. dependencias entre trámites
    for t, info in K.TRAMITES.items():
        for d in info["deps"]:
            r("dependencia", [C(f"req.{t}", "=", True)], f"req.{d}", True,
              f"«{K.TRAMITES[t]['n']}» exige haber realizado antes «{K.TRAMITES[d]['n']}».", K.FUENTES[t])

    # ---------------------------------------------------- 8. dónde se tramita (por distrito)
    for dist, ent in K.DISTRITOS.items():
        for t, ofi in K.MUN_OFICINA.items():
            r("distrito", [C("distrito", "=", dist), C(f"req.{t}", "=", True)], f"donde.{t}",
              f"{ent} -- {ofi}",
              f"En {dist} este trámite lo atiende la municipalidad correspondiente.",
              "TUPA de la municipalidad (la denominación de la oficina puede variar)")

    # ---------------------------------------------------- 9. documentos
    for t, docs in K.DOCS.items():
        for d in docs:
            r("documentos", [C(f"req.{t}", "=", True)], f"docs.{t}", d,
              f"Documento habitual para «{K.TRAMITES[t]['n']}».", K.FUENTES[t] + " -- contrastar con TUPA")

    # ---------------------------------------------------- 10. avisos y alertas
    for k, rb in K.RUBROS.items():
        for f in rb["flags"]:
            r("avisos", [C("rubro", "=", k)], "avisos", f"[{rb['n']}] {K.FLAGS[f]}",
              f"Obligación o buena práctica propia del giro ({f}).", "Normativa sectorial -- validar con el experto")
        if rb["nota"]:
            r("avisos", [C("rubro", "=", k)], "avisos", f"[{rb['n']}] {rb['nota']}",
              "Nota específica del giro.", "Normativa sectorial -- validar con el experto")
        for t_ in ("t1", "t2"):
            extra = ("con 20 o más trabajadores corresponde un comité de seguridad y salud."
                     if t_ == "t2" else "designe un supervisor de seguridad y salud en el trabajo.")
            r("avisos", [C("rubro", "=", k), C("trabajadores", "=", t_)], "avisos",
              f"[{rb['n']}] Peligros típicos: {rb['peligro']}. Elabore la matriz IPERC y {extra}",
              "Ley 29783 obliga a identificar peligros y evaluar riesgos.", K.FUENTES["SST_BASICO"])
        for a in ("a2", "a3"):
            r("avisos", [C("local", "in", K.ESTABLECIDOS), C("rubro", "=", k), C("area", "=", a)], "avisos",
              f"[{rb['n']}] Con {K.AREAS[a].lower()} prepare plan de seguridad, extintores, señalización "
              f"y luces de emergencia; la ITSE será más exigente.",
              "A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.", K.F_ITSE)
        lista = {"bajo": "extintor vigente, señalización de salida y botiquín",
                 "medio": "extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas",
                 "alto": "planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos",
                 "muy_alto": "expediente técnico completo, informes de especialistas y plan de contingencia"}
        for nv, chk in lista.items():
            r("avisos", [C("local", "in", K.ESTABLECIDOS), C("rubro", "=", k), C("nivel_riesgo", "=", nv)], "avisos",
              f"[{rb['n']} / riesgo {nv}] Prepare para la ITSE: {chk}. Peligros del giro: {rb['peligro']}.",
              "La ITSE verifica las condiciones de seguridad según el nivel de riesgo.", K.F_ITSE)
        for l in K.LOCALES:
            r("avisos", [C("rubro", "=", k), C("local", "=", l)], "avisos",
              f"[{rb['n']} / {K.LOCALES[l].lower()}] {consejo_local(l, rb).capitalize()}",
              "Condición propia de la combinación giro-local.", K.FUENTES["LICENCIA_FUNCIONAMIENTO"])
        r("avisos", [C("rubro", "=", k), C("persona", "=", "natural")], "avisos",
          f"[{rb['n']}] Como persona natural responde con su patrimonio personal; si el negocio crece "
          f"o hay riesgo, evalúe constituir una EIRL o SAC.", "Responsabilidad según Ley General de Sociedades / EIRL",
          "Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar")
        r("avisos", [C("rubro", "=", k), C("persona", "=", "juridica")], "avisos",
          f"[{rb['n']}] Mantenga vigente la vigencia de poder del representante y el libro de actas; "
          f"se las pedirán en licencias y trámites.", "Los trámites de una persona jurídica los realiza su representante.",
          K.FUENTES["INSCRIPCION_SUNARP"])

    av_reg = {"NRUS": "El NRUS solo permite emitir boletas y tiene tope de compras y ventas; si lo supera debe cambiar de régimen.",
              "RER": "En el RER debe llevar registros de compras y ventas y vigilar el tope de ingresos anuales.",
              "RMT": "En el RMT las obligaciones varían según el nivel de ingresos; pida orientación a un contador.",
              "RG": "En el Régimen General debe llevar contabilidad completa; contrate un contador."}
    for reg, txt in av_reg.items():
        r("avisos", [C("regimen", "=", reg)], "avisos", f"[Régimen {reg}] {txt}",
          "Cada régimen tiene obligaciones distintas.", K.FUENTES["ELEGIR_REGIMEN"])
    r("avisos", [C("tamano", "=", "fuera_mype")], "avisos",
      "Sus ventas superan el límite de la pequeña empresa: no califica como MYPE para beneficios MYPE.",
      "El tamaño se define por ventas anuales.", "TUO Ley MYPE (D.S. 013-2013-PRODUCE)")
    _ampliacion(r)
    return R


# ======================================================================
# AMPLIACIÓN: documentos específicos, obligaciones por régimen, beneficios
# por tamaño y orientación por distrito. (Validar cada texto con el experto.)
# ======================================================================
TIPO_RUBRO = {}
for _k in ("restaurante", "polleria", "cafeteria", "panaderia", "bodega", "minimarket", "pescaderia", "carniceria"):
    TIPO_RUBRO[_k] = "alimentos"
for _k in ("prod_alimentos", "molino_arroz", "metalmecanica", "confecciones", "artesania"):
    TIPO_RUBRO[_k] = "produccion"
for _k in ("ropa", "ferreteria", "tecnologia", "libreria", "agroinsumos", "botica", "online", "licores", "autopartes"):
    TIPO_RUBRO[_k] = "comercio"
for _k in ("peluqueria", "taller", "hospedaje", "prof", "lavanderia", "gimnasio", "agencia", "veterinaria"):
    TIPO_RUBRO[_k] = "servicio"

REG_TXT = {
    ("comercio", "NRUS"): "emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.",
    ("comercio", "RER"): "registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",
    ("comercio", "RMT"): "lleve los registros exigidos según su nivel de ingresos y sustente sus compras con comprobantes para deducir gastos.",
    ("comercio", "RG"): "lleve contabilidad completa con control de inventarios y pagos a cuenta mensuales.",
    ("alimentos", "NRUS"): "emita boleta o ticket por cada venta y guarde los comprobantes de sus insumos; vigile el tope mensual.",
    ("alimentos", "RER"): "registre compras de insumos y ventas diarias; vigile el tope anual de ingresos del RER.",
    ("alimentos", "RMT"): "sustente con comprobantes la compra de insumos y mantenga registros de ventas y compras al día.",
    ("alimentos", "RG"): "lleve contabilidad completa y costeo de insumos; contrate un contador.",
    ("produccion", "NRUS"): "el NRUS limita compras y ventas mensuales; si produce y compra insumos en volumen, probablemente deba cambiar de régimen.",
    ("produccion", "RER"): "registre compras de materia prima y ventas; valore sus activos fijos frente al tope del régimen.",
    ("produccion", "RMT"): "lleve registros de compras y ventas y sustente la materia prima con comprobantes para deducir costos.",
    ("produccion", "RG"): "lleve contabilidad completa con costos de producción e inventarios.",
    ("servicio", "NRUS"): "emita boleta por cada servicio; si presta servicios a empresas que piden factura deberá cambiar de régimen.",
    ("servicio", "RER"): "emita comprobantes por cada servicio y registre ingresos y compras; vigile el tope del régimen.",
    ("servicio", "RMT"): "registre ingresos y gastos con comprobantes; los pagos de honorarios y servicios deben sustentarse.",
    ("servicio", "RG"): "lleve contabilidad completa; los servicios facturados generan pagos a cuenta mensuales.",
}
TAM_TXT = {
    "micro": "Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.",
    "pequena": "Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",
}
LOCAL_HINT = {
    "propio": "tenga a mano el título o partida del local.",
    "alquilado": "lleve el contrato de alquiler y la autorización del propietario legalizada.",
    "domicilio": "pregunte si su zona permite actividad comercial en vivienda.",
    "mercado": "coordine primero con la administración del mercado.",
    "ambulante": "pregunte por las zonas y horarios habilitados para comercio ambulatorio.",
    "ninguno_aun": "consulte el certificado de zonificación antes de elegir el local.",
}
FLAG_DOC = {
    "BPM": ("INSPECCION_SANITARIA", "Programa de higiene y saneamiento (BPM) del establecimiento"),
    "cadena_frio": ("INSPECCION_SANITARIA", "Descripción de equipos de refrigeración y formato de registro de temperaturas"),
    "pesca": ("INSPECCION_SANITARIA", "Comprobantes de compra a proveedores con habilitación sanitaria SANIPES"),
    "carne": ("INSPECCION_SANITARIA", "Comprobantes de compra a camales autorizados"),
    "residuos": ("LICENCIA_FUNCIONAMIENTO", "Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita)"),
    "ruido": ("LICENCIA_FUNCIONAMIENTO", "Declaración de medidas de control de ruido (según ordenanza)"),
    "etiquetado": ("LICENCIA_FUNCIONAMIENTO", "Muestra de etiqueta o ficha de productos (si se solicita)"),
    "marca": ("LICENCIA_FUNCIONAMIENTO", "Denominación comercial/marca que se usará en el letrero"),
    "quimicos": ("ITSE_BASICA", "Hojas de seguridad (SDS) y relación de productos químicos almacenados"),
    "residuos_pel": ("LICENCIA_FUNCIONAMIENTO", "Contrato o compromiso con EO-RS para residuos peligrosos"),
    "raee": ("LICENCIA_FUNCIONAMIENTO", "Compromiso de entrega de residuos electrónicos a operador autorizado"),
    "polvo": ("ITSE_BASICA", "Descripción de control de polvo y mantenimiento de maquinaria"),
    "datos": ("LICENCIA_FUNCIONAMIENTO", "Política de privacidad o aviso de tratamiento de datos (si almacena datos de clientes)"),
    "comercio_electronico": ("LICENCIA_FUNCIONAMIENTO", "Dirección web o redes de venta del negocio"),
    "seg_estructural": ("ITSE_DETALLE", "Plano de evacuación con rutas y salidas de emergencia"),
    "seguridad_publica": ("ITSE_BASICA", "Aforo máximo declarado y botiquín"),
    "alcohol_menores": ("AUTORIZ_ALCOHOL", "Compromiso de no vender a menores y respetar horarios"),
    "residuos_bio": ("LICENCIA_FUNCIONAMIENTO", "Contrato o compromiso con EO-RS para residuos biocontaminados"),
}
DOCS_PERSONA = {
    "natural": "Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",
    "juridica": "Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.",
}
DOCS_LOCAL = {
    "propio": "Título de propiedad o partida registral del local.",
    "alquilado": "Contrato de alquiler y autorización del propietario con firma legalizada.",
    "domicilio": "Constancia de propiedad o posesión de la vivienda (y autorización de la junta de propietarios si es multifamiliar).",
    "mercado": "Constancia de conducción del puesto emitida por la administración del mercado.",
    "ninguno_aun": "Documento que acredite el local, exigible al presentar la solicitud.",
}
AV_ING = {
    "B1": "Está en el nivel más bajo de ventas: vigile mes a mes sus ventas y compras para saber cuándo debe cambiar de régimen.",
    "B2": "Está cerca del tope del NRUS: si lo supera deberá pasar al RER o RMT.",
    "B3": "Con ventas sobre el tope del NRUS corresponde RER o RMT; compare cuotas y obligaciones con un contador.",
    "B4": "Con estas ventas el RMT es el régimen habitual y exige más registros.",
    "B5": "Con estas ventas se aplica el RMT con tasas por tramos; se recomienda contador.",
    "B6": "Con estas ventas se aplica el Régimen General y se sale de las definiciones MYPE.",
}


def _ampliacion(r):
    T = K.TRAMITES
    # A. documentos según tipo de persona
    for t in ("RUC", "CLAVE_SOL", "COMPROBANTES", "REMYPE", "LICENCIA_FUNCIONAMIENTO", "CERT_ZONIFICACION",
              "ITSE_BASICA", "ITSE_DETALLE", "ITSE_MULTI", "INSPECCION_SANITARIA", "AUTORIZ_ALCOHOL", "AUTORIZ_ANUNCIO"):
        for pe, txt in DOCS_PERSONA.items():
            r("documentos", [C("persona", "=", pe), C(f"req.{t}", "=", True)], f"docs.{t}", txt,
              f"Documento de identidad/representación según el tipo de persona para «{T[t]['n']}».",
              K.FUENTES[t] + " -- contrastar con TUPA")
    # B. documentos según local
    for t in ("LICENCIA_FUNCIONAMIENTO", "CERT_ZONIFICACION", "ITSE_BASICA"):
        for l, txt in DOCS_LOCAL.items():
            r("documentos", [C("local", "=", l), C(f"req.{t}", "=", True)], f"docs.{t}", txt,
              f"Prueba del local exigible según el tipo de local ({K.LOCALES[l].lower()}).", K.FUENTES[t])
    for k, rb in K.RUBROS.items():
        # C. documentos propios del giro
        for f in rb["flags"]:
            if f in FLAG_DOC:
                t, txt = FLAG_DOC[f]
                r("documentos", [C("rubro", "=", k), C(f"req.{t}", "=", True)], f"docs.{t}", txt,
                  f"Documento propio del giro «{rb['n']}» ({f}).", K.FUENTES[t] + " -- puede variar según el TUPA")
        # E. obligaciones tributarias según régimen
        for reg in ("NRUS", "RER", "RMT", "RG"):
            r("avisos", [C("rubro", "=", k), C("regimen", "=", reg)], "avisos",
              f"[{rb['n']} / {reg}] {REG_TXT[(TIPO_RUBRO[k], reg)].capitalize()}",
              f"Obligaciones tributarias típicas de un negocio de tipo {TIPO_RUBRO[k]} en el régimen {reg}.",
              K.FUENTES["ELEGIR_REGIMEN"] + " -- validar con el contador experto")
        # F. beneficios según tamaño
        for tam, txt in TAM_TXT.items():
            r("avisos", [C("rubro", "=", k), C("tamano", "=", tam)], "avisos", f"[{rb['n']}] {txt}",
              "El tamaño de la empresa define el régimen laboral especial aplicable.",
              "TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia")
        # I. letrero
        r("avisos", [C("local", "in", K.ESTABLECIDOS), C("rubro", "=", k), C("tiene_letrero", "=", "si")], "avisos",
          f"[{rb['n']}] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.",
          "El anuncio se autoriza según el giro y las dimensiones permitidas.", K.FUENTES["AUTORIZ_ANUNCIO"])
        # J. área pequeña
        r("avisos", [C("local", "in", K.ESTABLECIDOS), C("rubro", "=", k), C("area", "=", "a1")], "avisos",
          f"[{rb['n']}] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener "
          f"extintor, señalización y salida despejada.", "Menor área reduce el nivel de riesgo, no elimina las exigencias.", K.F_ITSE)
        # L. trabaja solo
        r("avisos", [C("rubro", "=", k), C("trabajadores", "=", "t0")], "avisos",
          f"[{rb['n']}] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; "
          f"si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",
          "Toda relación laboral remunerada genera obligaciones.", K.FUENTES["T_REGISTRO"])
    # G. orientación por distrito × local
    for dist, ent in K.DISTRITOS.items():
        for l, hint in LOCAL_HINT.items():
            r("distrito", [C("distrito", "=", dist), C("local", "=", l)], "avisos",
              f"[{dist} / {K.LOCALES[l].lower()}] Presente los trámites municipales en la {ent}; {hint} "
              f"Revise el TUPA vigente en su portal institucional.",
              "Cada municipalidad tiene su propio TUPA y ordenanzas.", "TUPA de la municipalidad")
    # Q. régimen × trabajadores
    TXT_RT = {"t0": "sin planilla: sus ingresos y compras siguen sujetos a los topes del régimen.",
              "t1": "con personal: declare planilla electrónica (PLAME) y pague aportes mensuales además del impuesto del régimen.",
              "t2": "con más de 10 trabajadores: revise obligaciones laborales y tributarias reforzadas; se recomienda contador y asesoría laboral."}
    for reg in ("NRUS", "RER", "RMT", "RG"):
        for tr_, txt in TXT_RT.items():
            r("avisos", [C("regimen", "=", reg), C("trabajadores", "=", tr_)], "avisos",
              f"[Régimen {reg} / {K.TRABAJADORES[tr_].lower()}] Como está {txt}",
              "El régimen tributario y la planilla se declaran por separado.", K.FUENTES["T_REGISTRO"])
    # R. ventas × trabajadores
    for b, _, etq in K.INGRESOS:
        for tr_ in K.TRABAJADORES:
            r("avisos", [C("ingresos", "=", b), C("trabajadores", "=", tr_)], "avisos",
              f"[Ventas {b} / {K.TRABAJADORES[tr_].lower()}] Compare el costo de planilla con sus ventas anuales "
              f"al planificar contrataciones y su régimen.", "La carga laboral incide en la viabilidad del negocio.",
              "TUO Ley MYPE (D.S. 013-2013-PRODUCE)")
    # P. ingresos × persona
    for b, _, etq in K.INGRESOS:
        for pe in ("natural", "juridica"):
            r("avisos", [C("ingresos", "=", b), C("persona", "=", pe)], "avisos",
              f"[Ventas: {etq.lower()}] {AV_ING[b]}", "El régimen depende del nivel de ventas.",
              K.FUENTES["ELEGIR_REGIMEN"] + " -- verificar topes")


def construir_preguntas():
    P = {
        "rubro": Pregunta("¿A qué rubro pertenece su negocio?", [(k, v["n"]) for k, v in K.RUBROS.items()]),
        "persona": Pregunta("¿Qué tipo de persona es el titular del negocio?", list(K.PERSONAS.items())),
        "distrito": Pregunta("¿En qué distrito funcionará el negocio?", [(d, d) for d in K.DISTRITOS]),
        "local": Pregunta("¿Qué tipo de local tiene o tendrá?", list(K.LOCALES.items())),
        "area": Pregunta("¿Qué área aproximada tendrá el local?", list(K.AREAS.items())),
        "ingresos": Pregunta("¿Cuáles serán sus ventas anuales aproximadas?", [(b, e) for b, _, e in K.INGRESOS]),
        "trabajadores": Pregunta("¿Cuántos trabajadores tendrá?", list(K.TRABAJADORES.items())),
        "vende_a_empresas": Pregunta("¿Venderá a empresas que le pidan factura?", SI_NO),
        "tiene_letrero": Pregunta("¿Colocará letrero o anuncio publicitario?", SI_NO),
        "vende_alcohol": Pregunta("¿Venderá bebidas alcohólicas?", SI_NO),
    }
    for t, info in K.TRAMITES.items():
        P[f"hecho.{t}"] = Pregunta(f"¿Ya realizó este trámite?  {info['n']}  [{info['ent']}]",
                                   [(True, "Sí, ya lo hice"), (False, "No todavía")])
    return P