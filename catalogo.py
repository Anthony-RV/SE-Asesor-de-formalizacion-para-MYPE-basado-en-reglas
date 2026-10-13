# -*- coding: utf-8 -*-
"""
Catálogo del dominio: trámites, rubros, distritos y parámetros.

IMPORTANTE: todo dato legal (montos, normas, requisitos, nombres de oficinas)
debe ser validado con el experto y contrastado con la fuente oficial vigente
(SUNAT, SUNARP, TUPA de cada municipalidad, INDECOPI, DIGESA, etc.).
Los campos FUENTES son el punto de partida para la sección 2.3 y las
referencias del informe.
"""

UIT = 5500  # S/ -- VERIFICAR el valor vigente de la UIT


def s(n):
    return f"S/ {n:,.0f}"


# ----------------------------------------------------------------- parámetros
# (id, tope anual en S/, etiqueta que ve el usuario)
INGRESOS = [
    ("B1", 96_000, f"Hasta {s(96_000)} al año (≈ S/ 8,000 al mes)"),
    ("B2", 240_000, f"De {s(96_001)} a {s(240_000)} al año (≈ hasta S/ 20,000 al mes)"),
    ("B3", 525_000, f"De {s(240_001)} a {s(525_000)} al año"),
    ("B4", 150 * UIT, f"De {s(525_001)} a {s(150 * UIT)} al año (hasta 150 UIT)"),
    ("B5", 1700 * UIT, f"De {s(150 * UIT + 1)} a {s(1700 * UIT)} al año (hasta 1,700 UIT)"),
    ("B6", None, f"Más de {s(1700 * UIT)} al año"),
]
TAMANO = {"B1": "micro", "B2": "micro", "B3": "micro", "B4": "micro",
          "B5": "pequena", "B6": "fuera_mype"}

PERSONAS = {"natural": "Persona natural (el negocio va a mi nombre)",
            "juridica": "Persona jurídica (SAC, EIRL, SRL, etc.)"}

LOCALES = {"propio": "Local propio",
           "alquilado": "Local alquilado",
           "domicilio": "En mi domicilio / vivienda",
           "mercado": "Puesto en mercado o galería",
           "ambulante": "Ambulante (sin local fijo)",
           "ninguno_aun": "Aún no tengo local"}
ESTABLECIDOS = ("propio", "alquilado", "domicilio", "mercado", "ninguno_aun")

AREAS = {"a1": "Hasta 100 m²", "a2": "De 101 a 500 m²", "a3": "Más de 500 m²"}
NIVELES = ("bajo", "medio", "alto", "muy_alto")
NIVEL_AREA = {"a1": "bajo", "a2": "medio", "a3": "alto"}  # simplificación

TRABAJADORES = {"t0": "Solo yo (o familiares sin planilla)",
                "t1": "De 1 a 10 trabajadores",
                "t2": "Más de 10 trabajadores"}


def _mun(n, prov=False):
    return f"Municipalidad {'Provincial' if prov else 'Distrital'} de {n}"


DISTRITOS = {
    "Chiclayo": _mun("Chiclayo", True),
    "José Leonardo Ortiz": _mun("José Leonardo Ortiz"),
    "La Victoria": _mun("La Victoria"),
    "Pimentel": _mun("Pimentel"),
    "Monsefú": _mun("Monsefú"),
    "Reque": _mun("Reque"),
    "Pomalca": _mun("Pomalca"),
    "Tumán": _mun("Tumán"),
    "Santa Rosa": _mun("Santa Rosa"),
    "Eten": _mun("Eten"),
    "Lambayeque": _mun("Lambayeque", True),
    "Mochumí": _mun("Mochumí"),
    "Túcume": _mun("Túcume"),
    "Ferreñafe": _mun("Ferreñafe", True),
    "Pueblo Nuevo": _mun("Pueblo Nuevo"),
}

# -------------------------------------------------------------------- trámites
# nombre, entidad, orden (secuencia sugerida), dependencias, tipo (oblig/rec)
def _t(n, ent, orden, deps="", tipo="oblig"):
    return dict(n=n, ent=ent, orden=orden, deps=deps.split(), tipo=tipo)


TRAMITES = {
    "BUSQUEDA_RESERVA": _t("Búsqueda y reserva de nombre de la empresa", "SUNARP", 10),
    "MINUTA_ESCRITURA": _t("Minuta y escritura pública de constitución", "Notaría", 11, "BUSQUEDA_RESERVA"),
    "INSCRIPCION_SUNARP": _t("Inscripción de la empresa en Registros Públicos", "SUNARP", 12, "MINUTA_ESCRITURA"),
    "RUC": _t("Inscripción en el RUC", "SUNAT", 20),
    "CLAVE_SOL": _t("Obtener la Clave SOL", "SUNAT", 21, "RUC"),
    "ELEGIR_REGIMEN": _t("Elegir/declarar el régimen tributario", "SUNAT", 22, "RUC"),
    "COMPROBANTES": _t("Habilitar la emisión de comprobantes de pago electrónicos", "SUNAT", 23, "RUC CLAVE_SOL ELEGIR_REGIMEN"),
    "ACREDITAR_PROPIEDAD": _t("Acreditar la propiedad del local", "Registros Públicos / título", 30),
    "CONTRATO_ALQUILER": _t("Contrato de alquiler y autorización del propietario", "Propietario / Notaría", 31),
    "ACREDITAR_LOCAL": _t("Definir y acreditar el local (propiedad o contrato)", "Propietario / Registros Públicos", 32),
    "CERT_ZONIFICACION": _t("Certificado de zonificación y compatibilidad de uso", "Municipalidad", 35),
    "AUTORIZ_PUESTO_MERCADO": _t("Constancia/autorización de conducción de puesto en mercado", "Municipalidad / administración del mercado", 36),
    "AUTORIZ_AMBULANTE": _t("Autorización municipal de comercio ambulatorio", "Municipalidad", 37),
    "ITSE_BASICA": _t("ITSE básica (inspección técnica de seguridad en edificaciones)", "Municipalidad", 40),
    "ITSE_DETALLE": _t("ITSE de detalle", "Municipalidad", 41),
    "ITSE_MULTI": _t("ITSE multidisciplinaria", "Municipalidad / entes técnicos", 42),
    "CARNE_SANIDAD": _t("Carné de sanidad de manipuladores de alimentos", "Municipalidad / establecimiento de salud", 45),
    "INSPECCION_SANITARIA": _t("Inspección/autorización sanitaria del establecimiento", "Municipalidad", 46),
    "REGISTRO_SANITARIO_DIGESA": _t("Registro sanitario de alimentos y bebidas envasados", "DIGESA", 47),
    "AUTORIZ_BOTICA": _t("Autorización sanitaria de botica/farmacia y director técnico", "DIRESA Lambayeque (Autoridad Regional de Medicamentos)", 48),
    "REG_PLAGUICIDAS": _t("Registro de establecimiento de venta de plaguicidas", "SENASA", 49),
    "REG_HOSPEDAJE": _t("Registro/clasificación del establecimiento de hospedaje", "DIRCETUR Lambayeque", 50),
    "REG_AGENCIA_VIAJES": _t("Registro de agencia de viajes y turismo", "DIRCETUR Lambayeque", 51),
    "LICENCIA_FUNCIONAMIENTO": _t("Licencia de funcionamiento", "Municipalidad", 55, "RUC"),
    "AUTORIZ_ALCOHOL": _t("Autorización municipal para venta de bebidas alcohólicas", "Municipalidad", 56, "LICENCIA_FUNCIONAMIENTO"),
    "AUTORIZ_ANUNCIO": _t("Autorización de anuncio/letrero publicitario", "Municipalidad", 57, "LICENCIA_FUNCIONAMIENTO"),
    "LIBRO_RECLAMACIONES": _t("Libro de Reclamaciones (físico o virtual)", "INDECOPI", 60),
    "REMYPE": _t("Inscripción en el REMYPE", "MTPE / SUNAT", 63, "RUC CLAVE_SOL"),
    "CONTRATOS_LABORALES": _t("Contratos de trabajo y boletas de pago", "Empleador / MTPE", 64),
    "T_REGISTRO": _t("Registro de trabajadores en T-Registro/PLAME y EsSalud", "SUNAT / EsSalud", 65, "RUC CLAVE_SOL"),
    "SST_BASICO": _t("Sistema básico de seguridad y salud en el trabajo", "Empleador (fiscaliza SUNAFIL)", 69),
    "SCTR": _t("Seguro complementario de trabajo de riesgo (SCTR)", "EsSalud / aseguradora", 68, "T_REGISTRO"),
    "LIBROS_CONTABLES": _t("Llevar libros y registros contables según el régimen", "SUNAT", 70, "RUC"),
    "DECLARACION_MENSUAL": _t("Declarar y pagar impuestos mensualmente", "SUNAT", 71, "RUC CLAVE_SOL ELEGIR_REGIMEN"),
    "REG_MARCA": _t("Registro de marca (recomendado)", "INDECOPI", 80, tipo="rec"),
    "REG_ARTESANO": _t("Registro Nacional del Artesano (recomendado)", "DIRCETUR / MINCETUR", 81, tipo="rec"),
}

# Oficina que atiende cada trámite municipal (el nombre puede variar según el ROF/TUPA)
MUN_OFICINA = {
    "LICENCIA_FUNCIONAMIENTO": "Subgerencia de Licencias / Desarrollo Económico",
    "CERT_ZONIFICACION": "Gerencia de Desarrollo Urbano",
    "ITSE_BASICA": "Subgerencia de Defensa Civil / Gestión del Riesgo",
    "ITSE_DETALLE": "Subgerencia de Defensa Civil / Gestión del Riesgo",
    "ITSE_MULTI": "Subgerencia de Defensa Civil / Gestión del Riesgo",
    "CARNE_SANIDAD": "Área de Salud / Sanidad municipal",
    "INSPECCION_SANITARIA": "Área de Salud / Sanidad municipal",
    "AUTORIZ_ALCOHOL": "Subgerencia de Licencias",
    "AUTORIZ_ANUNCIO": "Gerencia de Desarrollo Urbano / Licencias",
    "AUTORIZ_PUESTO_MERCADO": "Administración de Mercados",
    "AUTORIZ_AMBULANTE": "Subgerencia de Comercio / Fiscalización",
}

# ---------------------------------------------------------------------- fuentes
F_LIC = "Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal"
F_ITSE = "D.S. 002-2018-PCM (Reglamento de ITSE)"
F_SUNAT = "Normativa SUNAT (RUC, comprobantes, regímenes)"
F_SAN = "D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas)"
FUENTES = {
    "BUSQUEDA_RESERVA": "SUNARP – Reglamento del Registro de Sociedades",
    "MINUTA_ESCRITURA": "Ley General de Sociedades (Ley 26887); D.Leg. 1049 (Notariado)",
    "INSCRIPCION_SUNARP": "Ley General de Sociedades (Ley 26887); SUNARP",
    "RUC": F_SUNAT,
    "CLAVE_SOL": F_SUNAT,
    "ELEGIR_REGIMEN": "D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta",
    "COMPROBANTES": "Reglamento de Comprobantes de Pago (R.S. 007-99/SUNAT)",
    "ACREDITAR_PROPIEDAD": F_LIC,
    "CONTRATO_ALQUILER": F_LIC,
    "ACREDITAR_LOCAL": F_LIC,
    "CERT_ZONIFICACION": F_LIC,
    "AUTORIZ_PUESTO_MERCADO": "Ordenanza municipal de mercados (TUPA)",
    "AUTORIZ_AMBULANTE": "Ordenanza municipal de comercio ambulatorio (TUPA)",
    "ITSE_BASICA": F_ITSE, "ITSE_DETALLE": F_ITSE, "ITSE_MULTI": F_ITSE,
    "CARNE_SANIDAD": F_SAN,
    "INSPECCION_SANITARIA": F_SAN,
    "REGISTRO_SANITARIO_DIGESA": F_SAN,
    "AUTORIZ_BOTICA": "Ley 29459 (Productos Farmacéuticos) y D.S. 014-2011-SA",
    "REG_PLAGUICIDAS": "Reglamento del Sistema Nacional de Plaguicidas Agrícolas (SENASA)",
    "REG_HOSPEDAJE": "D.S. 001-2015-MINCETUR (Reglamento de establecimientos de hospedaje)",
    "REG_AGENCIA_VIAJES": "Reglamento de agencias de viajes y turismo (MINCETUR)",
    "LICENCIA_FUNCIONAMIENTO": F_LIC,
    "AUTORIZ_ALCOHOL": "Ley 28681 (bebidas alcohólicas) y ordenanza municipal",
    "AUTORIZ_ANUNCIO": "Ordenanza municipal de anuncios y avisos publicitarios",
    "LIBRO_RECLAMACIONES": "Ley 29571 (Código de Protección y Defensa del Consumidor)",
    "REMYPE": "TUO Ley MYPE (D.S. 013-2013-PRODUCE)",
    "CONTRATOS_LABORALES": "D.S. 003-97-TR (TUO de la Ley de Productividad y Competitividad Laboral)",
    "T_REGISTRO": "D.S. 018-2007-TR (T-Registro y PLAME)",
    "SST_BASICO": "Ley 29783 (Seguridad y Salud en el Trabajo)",
    "SCTR": "Ley 26790 y D.S. 003-98-SA (SCTR)",
    "LIBROS_CONTABLES": "R.S. 234-2006/SUNAT (libros y registros vinculados a asuntos tributarios)",
    "DECLARACION_MENSUAL": F_SUNAT,
    "REG_MARCA": "D.Leg. 1075 y Decisión Andina 486 (propiedad industrial)",
    "REG_ARTESANO": "Ley 29073 (Ley del Artesano)",
}

# -------------------------------------------------------- documentos por trámite
DOCS = {
    "BUSQUEDA_RESERVA": ["Consulta de homonimia en el índice de personas jurídicas de SUNARP",
                         "Reserva del nombre (vigencia limitada)", "Pago de la tasa registral"],
    "MINUTA_ESCRITURA": ["Minuta firmada por abogado con estatuto y aportes de capital",
                         "DNI de los socios", "Constancia del aporte (dinero o bienes)",
                         "Elevación a escritura pública en notaría"],
    "INSCRIPCION_SUNARP": ["Testimonio de la escritura pública", "Solicitud de inscripción (título)",
                           "Pago de derechos registrales"],
    "RUC": ["DNI vigente del titular o representante legal",
            "Documento que acredite el domicilio fiscal (recibo de servicio o contrato)",
            "Ficha o partida registral (solo persona jurídica)",
            "Actividad económica (CIIU) y régimen tributario elegido"],
    "CLAVE_SOL": ["RUC activo", "DNI del titular o representante", "Generar la clave en SUNAT o en el portal"],
    "ELEGIR_REGIMEN": ["Declarar el régimen al inscribirse o actualizar el RUC",
                       "Proyección de ingresos y compras anuales"],
    "COMPROBANTES": ["Clave SOL", "Afiliación al sistema de emisión electrónica autorizado",
                     "Series de boleta/factura según el régimen"],
    "ACREDITAR_PROPIEDAD": ["Título de propiedad o partida registral",
                            "Copia literal actualizada del predio"],
    "CONTRATO_ALQUILER": ["Contrato de alquiler que autorice el uso comercial",
                          "DNI del propietario",
                          "Autorización del propietario para tramitar la licencia (firma legalizada)"],
    "ACREDITAR_LOCAL": ["Ubicación definida del local",
                        "Certificado de zonificación antes de pagar adelantos",
                        "Título de propiedad o contrato de alquiler"],
    "CERT_ZONIFICACION": ["Solicitud con dirección exacta del predio", "Giro o actividad a desarrollar",
                          "Pago de la tasa municipal"],
    "AUTORIZ_PUESTO_MERCADO": ["Solicitud a la administración del mercado",
                               "Constancia de conducción del puesto", "DNI y RUC"],
    "AUTORIZ_AMBULANTE": ["Solicitud municipal", "DNI", "Carné de sanidad (si vende alimentos)",
                          "Croquis de ubicación y horario propuesto"],
    "ITSE_BASICA": ["Solicitud/declaración jurada de ITSE", "Croquis de ubicación y distribución",
                    "Extintores vigentes y señalización", "Constancias de instalaciones eléctricas/gas si aplica"],
    "ITSE_DETALLE": ["Solicitud de ITSE de detalle", "Planos de ubicación, arquitectura y evacuación",
                     "Memoria descriptiva", "Plan de seguridad y certificados de operatividad de sistemas"],
    "ITSE_MULTI": ["Solicitud de ITSE multidisciplinaria", "Expediente técnico con planos y memoria",
                   "Informes de especialistas", "Plan de contingencia (según TUPA)"],
    "CARNE_SANIDAD": ["DNI", "Exámenes médicos exigidos", "Fotografías", "Pago de la tasa"],
    "INSPECCION_SANITARIA": ["Solicitud al área de salud municipal", "Croquis del establecimiento",
                             "Certificados de fumigación y de limpieza de tanque", "Pago de la tasa"],
    "REGISTRO_SANITARIO_DIGESA": ["Solicitud", "Ficha técnica y proceso de elaboración",
                                  "Informe de ensayo de laboratorio acreditado",
                                  "Proyecto de rotulado", "Pago de la tasa"],
    "AUTORIZ_BOTICA": ["Solicitud a la autoridad regional de medicamentos",
                       "Director técnico químico-farmacéutico (colegiatura y habilidad)",
                       "Planos y descripción del establecimiento",
                       "Cumplimiento de Buenas Prácticas de Oficina Farmacéutica"],
    "REG_PLAGUICIDAS": ["Solicitud a SENASA", "Responsable técnico", "Descripción del local y almacenamiento seguro"],
    "REG_HOSPEDAJE": ["Declaración jurada de clasificación/categoría", "Licencia de funcionamiento",
                      "Planos y número de habitaciones", "Libro/registro de huéspedes"],
    "REG_AGENCIA_VIAJES": ["Solicitud a DIRCETUR", "Licencia de funcionamiento",
                           "Requisitos del reglamento de agencias de viajes"],
    "LICENCIA_FUNCIONAMIENTO": ["Solicitud con carácter de declaración jurada", "Copia del RUC",
                                "DNI o vigencia de poder del representante (persona jurídica)",
                                "Declaración jurada de condiciones de seguridad o certificado ITSE según riesgo",
                                "Pago de la tasa"],
    "AUTORIZ_ALCOHOL": ["Solicitud municipal", "Licencia de funcionamiento con el giro autorizado",
                        "Cumplir horarios y distancias de la ordenanza"],
    "AUTORIZ_ANUNCIO": ["Solicitud", "Diseño y medidas del anuncio", "Autorización del propietario del inmueble"],
    "LIBRO_RECLAMACIONES": ["Libro físico o virtual", "Aviso visible sobre la existencia del libro",
                            "Hoja de reclamación conforme al reglamento"],
    "REMYPE": ["RUC y Clave SOL", "Declaración jurada de ser MYPE",
               "Al menos un trabajador registrado en T-Registro"],
    "CONTRATOS_LABORALES": ["Contrato escrito según la modalidad", "Boletas de pago mensuales",
                            "Registro del contrato en el MTPE si es modal"],
    "T_REGISTRO": ["Clave SOL", "Datos de cada trabajador (DNI, fecha de ingreso, remuneración)",
                   "Alta en PLAME / planilla electrónica"],
    "SST_BASICO": ["Política de seguridad y salud", "Matriz IPERC", "Registro de inducción y capacitaciones"],
    "SCTR": ["Contratar con EsSalud o aseguradora privada", "Lista de trabajadores en actividad de riesgo"],
    "LIBROS_CONTABLES": ["Registro de ventas e ingresos", "Registro de compras",
                         "Libro diario/mayor si el régimen lo exige"],
    "DECLARACION_MENSUAL": ["Calendario de vencimientos SUNAT", "Declaración y pago con Clave SOL"],
    "REG_MARCA": ["Búsqueda de antecedentes fonéticos y figurativos", "Solicitud de registro en INDECOPI",
                  "Pago de la tasa"],
    "REG_ARTESANO": ["Solicitud ante la autoridad competente", "Declaración de actividad artesanal",
                     "Fotografías o muestras de la producción"],
}

# --------------------------------------------------------------------- avisos
FLAGS = {
    "BPM": "Aplique Buenas Prácticas de Manipulación, higiene del personal y un programa de limpieza y desinfección; conserve certificados de fumigación y limpieza de tanque.",
    "residuos": "Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).",
    "cadena_frio": "Mantenga la cadena de frío y lleve un registro de temperaturas de refrigeración/congelación.",
    "ruido": "Controle ruido y emisiones según la ordenanza municipal; puede restringirse el horario o la zona.",
    "pesca": "Compre productos hidrobiológicos solo a proveedores con habilitación sanitaria de SANIPES y conserve comprobantes de compra (trazabilidad).",
    "carne": "Compre carne solo de camales autorizados (SENASA/municipal) y conserve la guía de transporte y comprobante.",
    "etiquetado": "Cumpla las normas de etiquetado aplicables (alimentos envasados: Ley 30021; textiles y calzado: norma técnica de etiquetado vigente).",
    "marca": "Considere registrar su marca en INDECOPI antes de invertir en publicidad o empaques.",
    "quimicos": "Almacene productos químicos con hojas de seguridad (SDS), envases rotulados y ventilación adecuada.",
    "residuos_pel": "Aceites usados, baterías y trapos con hidrocarburos son residuos peligrosos: entréguelos a una empresa operadora de residuos sólidos (EO-RS) registrada.",
    "raee": "Los residuos de aparatos eléctricos y electrónicos deben entregarse a operadores autorizados (D.S. 009-2019-MINAM).",
    "polvo": "Controle el polvo y mantenga limpias las máquinas: el polvo orgánico/de madera es inflamable.",
    "datos": "Si guarda datos personales de clientes, cumpla la Ley 29733 (Protección de Datos Personales): consentimiento y medidas de seguridad.",
    "comercio_electronico": "En su tienda virtual publique razón social, RUC, precios con IGV, plazos de entrega y política de cambios (Código del Consumidor).",
    "seg_estructural": "Mantenga rutas de evacuación libres, luces de emergencia, extintores y detectores; la ITSE verifica estos puntos.",
    "seguridad_publica": "Controle el aforo y mantenga botiquín y personal con primeros auxilios.",
    "alcohol_menores": "Está prohibido vender bebidas alcohólicas a menores de edad y fuera del horario autorizado.",
    "residuos_bio": "Los residuos biocontaminados (jeringas, restos orgánicos) deben segregarse y entregarse a una EO-RS.",
}


def _r(n, riesgo, flags, tr, peligro, dom, mer, amb, alc=False, sctr=False, nota=""):
    return dict(n=n, riesgo=riesgo, flags=flags.split(), tr=tr.split(), peligro=peligro,
                dom=dom, mer=mer, amb=amb, alc=alc, sctr=sctr, nota=nota)


# dom/mer/amb: ¿el giro suele ser compatible con vivienda / puesto de mercado / venta ambulatoria?
RUBROS = {
    "restaurante": _r("Restaurante / cevichería / menú", "medio", "BPM residuos cadena_frio ruido",
                      "INSPECCION_SANITARIA CARNE_SANIDAD", "quemaduras, cortes e incendio por gas",
                      False, True, False, alc=True),
    "polleria": _r("Pollería / parrilla", "medio", "BPM residuos cadena_frio ruido",
                   "INSPECCION_SANITARIA CARNE_SANIDAD", "incendio por gas y grasas, quemaduras",
                   False, True, False, alc=True),
    "cafeteria": _r("Cafetería / juguería / snack", "bajo", "BPM residuos",
                    "INSPECCION_SANITARIA CARNE_SANIDAD", "quemaduras y resbalones",
                    True, True, True),
    "panaderia": _r("Panadería / pastelería", "medio", "BPM residuos ruido",
                    "INSPECCION_SANITARIA CARNE_SANIDAD", "hornos: quemaduras, incendio, polvo de harina",
                    True, True, False),
    "bodega": _r("Bodega / tienda de abarrotes", "bajo", "residuos cadena_frio",
                 "INSPECCION_SANITARIA", "caídas y manipulación manual de cargas",
                 True, True, False, alc=True),
    "minimarket": _r("Minimarket / autoservicio", "medio", "residuos cadena_frio",
                     "INSPECCION_SANITARIA", "caídas, cargas e incendio",
                     False, False, False, alc=True),
    "pescaderia": _r("Pescadería / venta de mariscos", "bajo", "BPM cadena_frio pesca residuos",
                     "INSPECCION_SANITARIA CARNE_SANIDAD", "cortes, resbalones y frío",
                     False, True, False),
    "carniceria": _r("Carnicería / venta de aves", "bajo", "BPM cadena_frio carne residuos",
                     "INSPECCION_SANITARIA CARNE_SANIDAD", "cortes y resbalones",
                     False, True, False),
    "prod_alimentos": _r("Producción de alimentos envasados (dulces, conservas, snacks)", "medio",
                         "BPM etiquetado marca residuos",
                         "REGISTRO_SANITARIO_DIGESA CARNE_SANIDAD REG_MARCA",
                         "quemaduras, cortes y maquinaria", False, False, False),
    "molino_arroz": _r("Molino / pilado de arroz y granos", "alto", "ruido residuos polvo",
                       "REGISTRO_SANITARIO_DIGESA", "maquinaria, polvo y ruido",
                       False, False, False, sctr=True),
    "ropa": _r("Venta de ropa y calzado", "bajo", "etiquetado", "",
               "caídas y manipulación de cargas", True, True, True),
    "ferreteria": _r("Ferretería / materiales de construcción", "medio", "residuos quimicos", "",
                     "cargas pesadas e incendio por inflamables", False, False, False),
    "tecnologia": _r("Venta o reparación de celulares y tecnología", "bajo", "datos raee", "",
                     "descargas eléctricas", True, True, False),
    "libreria": _r("Librería / bazar / útiles", "bajo", "residuos", "",
                   "caídas e incendio por papel", True, True, True),
    "agroinsumos": _r("Venta de agroinsumos y plaguicidas", "alto", "quimicos residuos",
                      "REG_PLAGUICIDAS", "intoxicación, incendio y derrames",
                      False, False, False),
    "botica": _r("Botica / farmacia", "medio", "datos residuos", "AUTORIZ_BOTICA",
                 "pinchazos, caídas y manejo de productos controlados", False, False, False,
                 nota="Debe contar con director técnico (químico-farmacéutico) presente en el horario de atención y cumplir las Buenas Prácticas de Oficina Farmacéutica."),
    "online": _r("Venta por internet / redes sociales", "bajo", "comercio_electronico datos", "",
                 "ergonomía y manipulación de cargas", True, True, True,
                 nota="Aunque venda solo por internet necesita RUC, comprobantes de pago y Libro de Reclamaciones virtual."),
    "peluqueria": _r("Peluquería / salón de belleza / barbería", "bajo", "quimicos residuos", "",
                     "químicos, cortes y ergonomía", True, True, False),
    "taller": _r("Taller mecánico / mecánica automotriz", "alto", "residuos_pel ruido quimicos", "",
                 "aceites usados, incendio, atrapamiento y ruido", False, False, False, sctr=True),
    "hospedaje": _r("Hospedaje (hostal, alojamiento)", "alto", "datos seg_estructural", "REG_HOSPEDAJE",
                    "incendio, evacuación y resbalones", False, False, False,
                    nota="Lleve el registro de huéspedes y cumpla las exigencias de seguridad para evacuación."),
    "prof": _r("Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)", "bajo", "datos", "",
               "ergonomía y estrés", True, False, False,
               nota="Si su profesión lo exige, mantenga colegiatura y habilidad vigentes."),
    "lavanderia": _r("Lavandería", "medio", "quimicos residuos", "",
                     "vapor, químicos y maquinaria", False, False, False),
    "gimnasio": _r("Gimnasio / centro deportivo", "medio", "datos seguridad_publica", "",
                   "lesiones y sobreaforo", False, False, False),
    "agencia": _r("Agencia de viajes y turismo", "bajo", "datos", "REG_AGENCIA_VIAJES",
                  "ergonomía", True, False, False),
    "metalmecanica": _r("Carpintería metálica / de madera", "alto", "ruido quimicos polvo residuos", "",
                        "cortes, atrapamiento, ruido y soldadura", False, False, False, sctr=True),
    "artesania": _r("Artesanía (textil, paja, cerámica)", "bajo", "marca", "REG_MARCA REG_ARTESANO",
                    "posturas forzadas y herramientas cortantes", True, True, True),
    "confecciones": _r("Confección de prendas y calzado", "medio", "etiquetado marca ruido", "REG_MARCA",
                       "maquinaria, cortes, pinchazos e incendio", True, True, False, sctr=True),
    "licores": _r("Distribuidora / venta de licores", "medio", "alcohol_menores residuos",
                  "AUTORIZ_ALCOHOL", "caídas, cargas y rotura de envases", False, False, False),
    "autopartes": _r("Venta de repuestos y autopartes", "medio", "residuos quimicos", "",
                     "cargas pesadas y químicos", False, False, False),
    "veterinaria": _r("Veterinaria / pet shop", "medio", "residuos_bio", "",
                      "mordeduras y zoonosis", False, False, False),
}