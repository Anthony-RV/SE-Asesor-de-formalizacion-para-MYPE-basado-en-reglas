ID,Grupo,SI,ENTONCES,Justificación,Fuente 

R0001,constitucion,persona = juridica,req.BUSQUEDA_RESERVA = True,Una persona jurídica existe legalmente al inscribirse en Registros Públicos: Búsqueda y reserva de nombre de la empresa.,SUNARP – Reglamento del Registro de Sociedades 

R0002,constitucion,persona = juridica,req.MINUTA_ESCRITURA = True,Una persona jurídica existe legalmente al inscribirse en Registros Públicos: Minuta y escritura pública de constitución.,Ley General de Sociedades (Ley 26887); D.Leg. 1049 (Notariado) 

R0003,constitucion,persona = juridica,req.INSCRIPCION_SUNARP = True,Una persona jurídica existe legalmente al inscribirse en Registros Públicos: Inscripción de la empresa en Registros Públicos.,Ley General de Sociedades (Ley 26887); SUNARP 

R0004,tributario,SIEMPRE,req.RUC = True,Todo negocio necesita RUC para operar formalmente.,"Normativa SUNAT (RUC, comprobantes, regímenes)" 

R0005,tributario,SIEMPRE,req.CLAVE_SOL = True,La Clave SOL permite realizar los trámites tributarios en línea.,"Normativa SUNAT (RUC, comprobantes, regímenes)" 

R0006,tributario,SIEMPRE,req.ELEGIR_REGIMEN = True,Debe estar acogido a un régimen tributario.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta 

R0007,tributario,SIEMPRE,req.COMPROBANTES = True,Debe emitir comprobantes de pago por sus ventas.,Reglamento de Comprobantes de Pago (R.S. 00799/SUNAT) 

R0008,tributario,SIEMPRE,req.DECLARACION_MENSUAL = True,Todo régimen exige declarar o pagar periódicamente.,"Normativa SUNAT (RUC, comprobantes, regímenes)" 

R0009,tributario,SIEMPRE,req.LIBRO_RECLAMACIONES = True,Todo proveedor que atiende consumidores debe contar con Libro de Reclamaciones.,Ley 29571 (Código de Protección y Defensa del Consumidor) 

R0010,tributario,rubro = prof,profesional = True,Los servicios profesionales con título no pueden acogerse al NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta 

R0011,tributario,regimen = RER,req.LIBROS_CONTABLES = True,En el régimen RER se deben llevar libros o registros contables (el NRUS no).,R.S. 234-2006/SUNAT (libros y registros vinculados a asuntos tributarios) 

R0012,tributario,regimen = RMT,req.LIBROS_CONTABLES = True,En el régimen RMT se deben llevar libros o registros contables (el NRUS no).,R.S. 2342006/SUNAT (libros y registros vinculados a asuntos tributarios) 

R0013,tributario,regimen = RG,req.LIBROS_CONTABLES = True,En el régimen RG se deben llevar libros o registros contables (el NRUS no).,R.S. 234-2006/SUNAT (libros y registros vinculados a asuntos tributarios) 

R0014,regimen,ingresos = B1,tamano = micro,El tamaño de la empresa se determina por el nivel de ventas anuales (UIT).,TUO Ley MYPE (D.S. 013-2013PRODUCE) -- verificar límites vigentes 

R0015,regimen,ingresos = B2,tamano = micro,El tamaño de la empresa se determina por el nivel de ventas anuales (UIT).,TUO Ley MYPE (D.S. 013-2013PRODUCE) -- verificar límites vigentes 

R0016,regimen,ingresos = B3,tamano = micro,El tamaño de la empresa se determina por el nivel de ventas anuales (UIT).,TUO Ley MYPE (D.S. 013-2013PRODUCE) -- verificar límites vigentes 

R0017,regimen,ingresos = B4,tamano = micro,El tamaño de la empresa se determina por el nivel de ventas anuales (UIT).,TUO Ley MYPE (D.S. 013-2013PRODUCE) -- verificar límites vigentes 

R0018,regimen,ingresos = B5,tamano = pequena,El tamaño de la empresa se determina por el nivel de ventas anuales (UIT).,TUO Ley MYPE (D.S. 013-2013PRODUCE) -- verificar límites vigentes 

R0019,regimen,ingresos = B6,tamano = fuera_mype,El tamaño de la empresa se determina por el nivel de ventas anuales (UIT).,TUO Ley MYPE (D.S. 013-2013PRODUCE) -- verificar límites vigentes 

R0020,regimen,ingresos = B6,regimen = RG,"Con ventas sobre 1,700 UIT corresponde el Régimen General.",D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0021,regimen,ingresos = B4,regimen = RMT,"Con ventas hasta 1,700 UIT y más de 525 mil al año corresponde el Régimen MYPE Tributario.",D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0022,regimen,ingresos = B5,regimen = RMT,"Con ventas hasta 1,700 UIT y más de 525 mil al año corresponde el Régimen MYPE Tributario.",D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0023,regimen,"persona = juridica Y ingresos ∈ ('B1', 'B2', 'B3')",regimen = RMT,"Una persona jurídica no puede acogerse al NRUS; con ventas bajas, el RMT es la 

opción habitual.",D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0024,regimen,persona = natural Y ingresos = B3,regimen = RER,Persona natural con ventas sobre el tope del NRUS y hasta 525 mil al año: RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0025,regimen,persona = natural Y ingresos = B1 Y profesional = True,regimen = RER,El NRUS excluye servicios profesionales; con ventas bajas corresponde el RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0026,regimen,persona = natural Y ingresos = B1 Y profesional = False Y vende_a_empresas = si,regimen = RER,"Si vende a empresas necesita emitir facturas, lo que el NRUS no permite: RER.",D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0027,regimen,persona = natural Y ingresos = B1 Y profesional = False Y vende_a_empresas = no,regimen = NRUS,Persona natural con ventas bajas que solo emite boletas: NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0028,regimen,persona = natural Y ingresos = B2 Y profesional = True,regimen = RER,El NRUS excluye servicios profesionales; con ventas bajas corresponde el RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0029,regimen,persona = natural Y ingresos = B2 Y profesional = False Y vende_a_empresas = si,regimen = RER,"Si vende a empresas necesita emitir facturas, lo que el NRUS no permite: RER.",D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0030,regimen,persona = natural Y ingresos = B2 Y profesional = False Y vende_a_empresas = no,regimen = NRUS,Persona natural con ventas bajas que solo emite boletas: NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes vigentes 

R0031,local,local = propio,req.LICENCIA_FUNCIONAMIENTO = True,Todo establecimiento donde se atiende al público necesita licencia de funcionamiento.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0032,local,local = alquilado,req.LICENCIA_FUNCIONAMIENTO = True,Todo establecimiento donde se atiende al público necesita licencia de 

funcionamiento.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0033,local,local = domicilio,req.LICENCIA_FUNCIONAMIENTO = True,Todo establecimiento donde se atiende al público necesita licencia de funcionamiento.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0034,local,local = mercado,req.LICENCIA_FUNCIONAMIENTO = True,Todo establecimiento donde se atiende al público necesita licencia de funcionamiento.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0035,local,local = ninguno_aun,req.LICENCIA_FUNCIONAMIENTO = True,Todo establecimiento donde se atiende al público necesita licencia de funcionamiento.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0036,local,local = propio,req.CERT_ZONIFICACION = True,Debe comprobar que el giro sea compatible con la zonificación del predio.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0037,local,local = alquilado,req.CERT_ZONIFICACION = True,Debe comprobar que el giro sea compatible con la zonificación del predio.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0038,local,local = domicilio,req.CERT_ZONIFICACION = True,Debe comprobar que el giro sea compatible con la zonificación del predio.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0039,local,local = ninguno_aun,req.CERT_ZONIFICACION = True,Debe comprobar que el giro sea compatible con la zonificación del predio.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0040,local,local = propio,req.ACREDITAR_PROPIEDAD = True,Según el tipo de local (Local propio) se requiere: Acreditar la propiedad del local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0041,local,local = alquilado,req.CONTRATO_ALQUILER = True,Según el tipo de local (Local alquilado) se requiere: Contrato de alquiler y autorización del propietario.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0042,local,local = domicilio,req.ACREDITAR_LOCAL = True,Según el tipo de local (En mi domicilio / vivienda) se requiere: Definir y acreditar el local (propiedad o contrato).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0043,local,local = ninguno_aun,req.ACREDITAR_LOCAL = True,Según el tipo de local (Aún no tengo local) se requiere: Definir y acreditar el local (propiedad o contrato).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0044,local,local = mercado,req.AUTORIZ_PUESTO_MERCADO = True,Según el tipo de local (Puesto en mercado o galería) se requiere: Constancia/autorización de conducción de puesto en mercado.,Ordenanza municipal de mercados (TUPA) 

R0045,local,local = ambulante,req.AUTORIZ_AMBULANTE = True,Según el tipo de local (Ambulante (sin local fijo)) se requiere: Autorización municipal de comercio ambulatorio.,Ordenanza municipal de comercio ambulatorio (TUPA) 

R0046,local,local = propio Y tiene_letrero = si,req.AUTORIZ_ANUNCIO = True,Los letreros y anuncios publicitarios requieren autorización municipal.,Ordenanza municipal de anuncios y avisos publicitarios 

R0047,local,local = alquilado Y tiene_letrero = si,req.AUTORIZ_ANUNCIO = True,Los letreros y anuncios publicitarios requieren autorización municipal.,Ordenanza municipal de anuncios y avisos publicitarios 

R0048,local,local = domicilio Y tiene_letrero = si,req.AUTORIZ_ANUNCIO = True,Los letreros y anuncios publicitarios requieren autorización municipal.,Ordenanza municipal de anuncios y avisos publicitarios 

R0049,local,local = mercado Y tiene_letrero = si,req.AUTORIZ_ANUNCIO = True,Los letreros y anuncios publicitarios requieren autorización municipal.,Ordenanza municipal de anuncios y avisos publicitarios 

R0050,local,local = ninguno_aun Y tiene_letrero = si,req.AUTORIZ_ANUNCIO = True,Los letreros y anuncios publicitarios requieren autorización municipal.,Ordenanza municipal de anuncios y avisos publicitarios 

R0051,riesgo,rubro = restaurante Y area = a1,nivel_riesgo = medio,Restaurante / cevichería / menú (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0052,riesgo,rubro = restaurante Y area = a2,nivel_riesgo = medio,Restaurante / cevichería / menú (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0053,riesgo,rubro = restaurante Y area = a3,nivel_riesgo = alto,Restaurante / cevichería / menú (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0054,riesgo,rubro = polleria Y area = a1,nivel_riesgo = medio,Pollería / parrilla (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0055,riesgo,rubro = polleria Y area = a2,nivel_riesgo = medio,Pollería / parrilla (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0056,riesgo,rubro = polleria Y area = a3,nivel_riesgo = alto,Pollería / parrilla (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0057,riesgo,rubro = cafeteria Y area = a1,nivel_riesgo = bajo,Cafetería / juguería / snack (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0058,riesgo,rubro = cafeteria Y area = a2,nivel_riesgo = medio,Cafetería / juguería / snack (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0059,riesgo,rubro = cafeteria Y area = a3,nivel_riesgo = alto,Cafetería / juguería / snack (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0060,riesgo,rubro = panaderia Y area = a1,nivel_riesgo = medio,Panadería / pastelería (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0061,riesgo,rubro = panaderia Y area = a2,nivel_riesgo = medio,Panadería / pastelería (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0062,riesgo,rubro = panaderia Y area = a3,nivel_riesgo = alto,Panadería / pastelería (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0063,riesgo,rubro = bodega Y area = a1,nivel_riesgo = bajo,Bodega / tienda de abarrotes (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0064,riesgo,rubro = bodega Y area = a2,nivel_riesgo = medio,Bodega / tienda de abarrotes (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0065,riesgo,rubro = bodega Y area = a3,nivel_riesgo = alto,Bodega / tienda de abarrotes (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0066,riesgo,rubro = minimarket Y area = a1,nivel_riesgo = medio,Minimarket / autoservicio (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0067,riesgo,rubro = minimarket Y area = a2,nivel_riesgo = medio,Minimarket / autoservicio (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0068,riesgo,rubro = minimarket Y area = a3,nivel_riesgo = alto,Minimarket / autoservicio (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0069,riesgo,rubro = pescaderia Y area = a1,nivel_riesgo = bajo,Pescadería / venta de mariscos (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0070,riesgo,rubro = pescaderia Y area = a2,nivel_riesgo = medio,Pescadería / venta de mariscos (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0071,riesgo,rubro = pescaderia Y area = a3,nivel_riesgo = alto,Pescadería / venta de mariscos (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0072,riesgo,rubro = carniceria Y area = a1,nivel_riesgo = bajo,Carnicería / venta de aves (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0073,riesgo,rubro = carniceria Y area = a2,nivel_riesgo = medio,Carnicería / venta de aves (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0074,riesgo,rubro = carniceria Y area = a3,nivel_riesgo = alto,Carnicería / venta de aves (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0075,riesgo,rubro = prod_alimentos Y area = a1,nivel_riesgo = medio,"Producción de alimentos envasados (dulces, conservas, snacks) (riesgo base medio) con hasta 100 m² -> riesgo medio.",D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0076,riesgo,rubro = prod_alimentos Y area = a2,nivel_riesgo = medio,"Producción de alimentos envasados (dulces, conservas, snacks) (riesgo base medio) con de 101 a 500 m² -> riesgo medio.",D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0077,riesgo,rubro = prod_alimentos Y area = a3,nivel_riesgo = alto,"Producción de alimentos envasados (dulces, conservas, snacks) (riesgo base medio) con más de 500 m² -> riesgo alto.",D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0078,riesgo,rubro = molino_arroz Y area = a1,nivel_riesgo = alto,Molino / pilado de arroz y granos (riesgo base alto) con hasta 100 m² -> riesgo alto.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0079,riesgo,rubro = molino_arroz Y area = a2,nivel_riesgo = alto,Molino / pilado de arroz y granos (riesgo base alto) con de 101 a 500 m² -> riesgo alto.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0080,riesgo,rubro = molino_arroz Y area = a3,nivel_riesgo = alto,Molino / pilado de arroz y granos (riesgo base alto) con más de 500 m² -> riesgo alto.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0081,riesgo,rubro = ropa Y area = a1,nivel_riesgo = bajo,Venta de ropa y calzado (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0082,riesgo,rubro = ropa Y area = a2,nivel_riesgo = medio,Venta de ropa y calzado (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0083,riesgo,rubro = ropa Y area = a3,nivel_riesgo = alto,Venta de ropa y calzado (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0084,riesgo,rubro = ferreteria Y area = a1,nivel_riesgo = medio,Ferretería / materiales de construcción (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0085,riesgo,rubro = ferreteria Y area = a2,nivel_riesgo = medio,Ferretería / materiales de construcción (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0086,riesgo,rubro = ferreteria Y area = a3,nivel_riesgo = alto,Ferretería / materiales de construcción (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0087,riesgo,rubro = tecnologia Y area = a1,nivel_riesgo = bajo,Venta o reparación de celulares y tecnología (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0088,riesgo,rubro = tecnologia Y area = a2,nivel_riesgo = medio,Venta o reparación de celulares y tecnología (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0089,riesgo,rubro = tecnologia Y area = a3,nivel_riesgo = alto,Venta o reparación de celulares y tecnología (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0090,riesgo,rubro = libreria Y area = a1,nivel_riesgo = bajo,Librería / bazar / útiles (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0091,riesgo,rubro = libreria Y area = a2,nivel_riesgo = medio,Librería / bazar / útiles (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0092,riesgo,rubro = libreria Y area = a3,nivel_riesgo = alto,Librería / bazar / útiles (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0093,riesgo,rubro = agroinsumos Y area = a1,nivel_riesgo = alto,Venta de agroinsumos y plaguicidas (riesgo base alto) con hasta 100 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0094,riesgo,rubro = agroinsumos Y area = a2,nivel_riesgo = alto,Venta de agroinsumos y plaguicidas (riesgo base alto) con de 101 a 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0095,riesgo,rubro = agroinsumos Y area = a3,nivel_riesgo = alto,Venta de agroinsumos y plaguicidas (riesgo base alto) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0096,riesgo,rubro = botica Y area = a1,nivel_riesgo = medio,Botica / farmacia (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0097,riesgo,rubro = botica Y area = a2,nivel_riesgo = medio,Botica / farmacia (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0098,riesgo,rubro = botica Y area = a3,nivel_riesgo = alto,Botica / farmacia (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0099,riesgo,rubro = online Y area = a1,nivel_riesgo = bajo,Venta por internet / redes sociales (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 002-2018- 

PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0100,riesgo,rubro = online Y area = a2,nivel_riesgo = medio,Venta por internet / redes sociales (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0101,riesgo,rubro = online Y area = a3,nivel_riesgo = alto,Venta por internet / redes sociales (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0102,riesgo,rubro = peluqueria Y area = a1,nivel_riesgo = bajo,Peluquería / salón de belleza / barbería (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0103,riesgo,rubro = peluqueria Y area = a2,nivel_riesgo = medio,Peluquería / salón de belleza / barbería (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0104,riesgo,rubro = peluqueria Y area = a3,nivel_riesgo = alto,Peluquería / salón de belleza / barbería (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0105,riesgo,rubro = taller Y area = a1,nivel_riesgo = alto,Taller mecánico / mecánica automotriz (riesgo base alto) con hasta 100 m² -> riesgo alto.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0106,riesgo,rubro = taller Y area = a2,nivel_riesgo = alto,Taller mecánico / mecánica automotriz (riesgo base alto) con de 101 a 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0107,riesgo,rubro = taller Y area = a3,nivel_riesgo = alto,Taller mecánico / mecánica automotriz (riesgo base alto) con más de 500 m² -> riesgo alto.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0108,riesgo,rubro = hospedaje Y area = a1,nivel_riesgo = alto,"Hospedaje (hostal, alojamiento) (riesgo base alto) con hasta 100 m² -> riesgo alto.",D.S. 002-2018- 

PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0109,riesgo,rubro = hospedaje Y area = a2,nivel_riesgo = alto,"Hospedaje (hostal, alojamiento) (riesgo base alto) con de 101 a 500 m² -> riesgo alto.",D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0110,riesgo,rubro = hospedaje Y area = a3,nivel_riesgo = alto,"Hospedaje (hostal, alojamiento) (riesgo base alto) con más de 500 m² -> riesgo alto.",D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0111,riesgo,rubro = prof Y area = a1,nivel_riesgo = bajo,"Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) (riesgo base bajo) con hasta 100 m² -> riesgo bajo.",D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0112,riesgo,rubro = prof Y area = a2,nivel_riesgo = medio,"Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.",D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0113,riesgo,rubro = prof Y area = a3,nivel_riesgo = alto,"Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) (riesgo base bajo) con más de 500 m² -> riesgo alto.",D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0114,riesgo,rubro = lavanderia Y area = a1,nivel_riesgo = medio,Lavandería (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0115,riesgo,rubro = lavanderia Y area = a2,nivel_riesgo = medio,Lavandería (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0116,riesgo,rubro = lavanderia Y area = a3,nivel_riesgo = alto,Lavandería (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0117,riesgo,rubro = gimnasio Y area = a1,nivel_riesgo = medio,Gimnasio / centro deportivo (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0118,riesgo,rubro = gimnasio Y area = a2,nivel_riesgo = medio,Gimnasio / centro deportivo (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0119,riesgo,rubro = gimnasio Y area = a3,nivel_riesgo = alto,Gimnasio / centro deportivo (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0120,riesgo,rubro = agencia Y area = a1,nivel_riesgo = bajo,Agencia de viajes y turismo (riesgo base bajo) con hasta 100 m² -> riesgo bajo.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0121,riesgo,rubro = agencia Y area = a2,nivel_riesgo = medio,Agencia de viajes y turismo (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0122,riesgo,rubro = agencia Y area = a3,nivel_riesgo = alto,Agencia de viajes y turismo (riesgo base bajo) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0123,riesgo,rubro = metalmecanica Y area = a1,nivel_riesgo = alto,Carpintería metálica / de madera (riesgo base alto) con hasta 100 m² -> riesgo alto.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0124,riesgo,rubro = metalmecanica Y area = a2,nivel_riesgo = alto,Carpintería metálica / de madera (riesgo base alto) con de 101 a 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0125,riesgo,rubro = metalmecanica Y area = a3,nivel_riesgo = alto,Carpintería metálica / de madera (riesgo base alto) con más de 500 m² -> riesgo alto.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0126,riesgo,rubro = artesania Y area = a1,nivel_riesgo = bajo,"Artesanía (textil, paja, cerámica) (riesgo base bajo) con hasta 100 m² -> riesgo bajo.",D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0127,riesgo,rubro = artesania Y area = a2,nivel_riesgo = medio,"Artesanía (textil, paja, cerámica) (riesgo base bajo) con de 101 a 500 m² -> riesgo medio.",D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0128,riesgo,rubro = artesania Y area = a3,nivel_riesgo = alto,"Artesanía (textil, paja, cerámica) (riesgo base bajo) con más de 500 m² -> riesgo alto.",D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0129,riesgo,rubro = confecciones Y area = a1,nivel_riesgo = medio,Confección de prendas y calzado (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0130,riesgo,rubro = confecciones Y area = a2,nivel_riesgo = medio,Confección de prendas y calzado (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0131,riesgo,rubro = confecciones Y area = a3,nivel_riesgo = alto,Confección de prendas y calzado (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 0022018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0132,riesgo,rubro = licores Y area = a1,nivel_riesgo = medio,Distribuidora / venta de licores (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0133,riesgo,rubro = licores Y area = a2,nivel_riesgo = medio,Distribuidora / venta de licores (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0134,riesgo,rubro = licores Y area = a3,nivel_riesgo = alto,Distribuidora / venta de licores (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0135,riesgo,rubro = autopartes Y area = a1,nivel_riesgo = medio,Venta de repuestos y autopartes (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0136,riesgo,rubro = autopartes Y area = a2,nivel_riesgo = medio,Venta de repuestos y autopartes (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0137,riesgo,rubro = autopartes Y area = a3,nivel_riesgo = alto,Venta de repuestos y autopartes (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0138,riesgo,rubro = veterinaria Y area = a1,nivel_riesgo = medio,Veterinaria / pet shop (riesgo base medio) con hasta 100 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0139,riesgo,rubro = veterinaria Y area = a2,nivel_riesgo = medio,Veterinaria / pet shop (riesgo base medio) con de 101 a 500 m² -> riesgo medio.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0140,riesgo,rubro = veterinaria Y area = a3,nivel_riesgo = alto,Veterinaria / pet shop (riesgo base medio) con más de 500 m² -> riesgo alto.,D.S. 002-2018-PCM (Reglamento de ITSE) -- SIMPLIFICACIÓN: contrastar con la matriz de riesgos vigente 

R0141,seguridad,local = propio Y nivel_riesgo = bajo,req.ITSE_BASICA = True,Riesgo bajo en un establecimiento (local propio) exige ITSE básica (inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0142,seguridad,local = propio Y nivel_riesgo = medio,req.ITSE_BASICA = True,Riesgo medio en un establecimiento (local propio) exige ITSE básica (inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0143,seguridad,local = propio Y nivel_riesgo = alto,req.ITSE_DETALLE = True,Riesgo alto en un establecimiento (local propio) exige ITSE de detalle.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0144,seguridad,local = propio Y nivel_riesgo = muy_alto,req.ITSE_MULTI = True,Riesgo muy_alto en un establecimiento (local propio) exige ITSE multidisciplinaria.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0145,seguridad,local = alquilado Y nivel_riesgo = bajo,req.ITSE_BASICA = True,Riesgo bajo en un establecimiento (local alquilado) exige ITSE básica 

(inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0146,seguridad,local = alquilado Y nivel_riesgo = medio,req.ITSE_BASICA = True,Riesgo medio en un establecimiento (local alquilado) exige ITSE básica (inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0147,seguridad,local = alquilado Y nivel_riesgo = alto,req.ITSE_DETALLE = True,Riesgo alto en un establecimiento (local alquilado) exige ITSE de detalle.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0148,seguridad,local = alquilado Y nivel_riesgo = muy_alto,req.ITSE_MULTI = True,Riesgo muy_alto en un establecimiento (local alquilado) exige ITSE multidisciplinaria.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0149,seguridad,local = domicilio Y nivel_riesgo = bajo,req.ITSE_BASICA = True,Riesgo bajo en un establecimiento (en mi domicilio / vivienda) exige ITSE básica (inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0150,seguridad,local = domicilio Y nivel_riesgo = medio,req.ITSE_BASICA = True,Riesgo medio en un establecimiento (en mi domicilio / vivienda) exige ITSE básica (inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0151,seguridad,local = domicilio Y nivel_riesgo = alto,req.ITSE_DETALLE = True,Riesgo alto en un establecimiento (en mi domicilio / vivienda) exige ITSE de detalle.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0152,seguridad,local = domicilio Y nivel_riesgo = muy_alto,req.ITSE_MULTI = True,Riesgo muy_alto en un establecimiento (en mi domicilio / vivienda) exige ITSE multidisciplinaria.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0153,seguridad,local = mercado Y nivel_riesgo = bajo,req.ITSE_BASICA = True,Riesgo bajo en un establecimiento (puesto en mercado o galería) exige ITSE básica (inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0154,seguridad,local = mercado Y nivel_riesgo = medio,req.ITSE_BASICA = True,Riesgo medio en un establecimiento (puesto en mercado o galería) exige ITSE básica (inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0155,seguridad,local = mercado Y nivel_riesgo = alto,req.ITSE_DETALLE = True,Riesgo alto en un establecimiento (puesto en mercado o galería) exige ITSE de detalle.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0156,seguridad,local = mercado Y nivel_riesgo = muy_alto,req.ITSE_MULTI = True,Riesgo muy_alto en un establecimiento (puesto en mercado o galería) exige ITSE multidisciplinaria.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0157,seguridad,local = ninguno_aun Y nivel_riesgo = bajo,req.ITSE_BASICA = True,Riesgo bajo en un establecimiento (aún no tengo local) exige ITSE básica (inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0158,seguridad,local = ninguno_aun Y nivel_riesgo = medio,req.ITSE_BASICA = True,Riesgo medio en un establecimiento (aún no tengo local) exige ITSE básica (inspección técnica de seguridad en edificaciones).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0159,seguridad,local = ninguno_aun Y nivel_riesgo = alto,req.ITSE_DETALLE = True,Riesgo alto en un establecimiento (aún no tengo local) exige ITSE de detalle.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0160,seguridad,local = ninguno_aun Y nivel_riesgo = muy_alto,req.ITSE_MULTI = True,Riesgo muy_alto en un establecimiento (aún no tengo local) exige ITSE multidisciplinaria.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0161,rubro,rubro = restaurante,req.INSPECCION_SANITARIA = True,El giro «Restaurante / cevichería / menú» requiere: Inspección/autorización sanitaria del establecimiento.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0162,rubro,rubro = restaurante,req.CARNE_SANIDAD = True,El giro «Restaurante / cevichería / menú» requiere: Carné de sanidad de manipuladores de alimentos.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0163,rubro,rubro = restaurante Y vende_alcohol = si,req.AUTORIZ_ALCOHOL = True,Vender bebidas alcohólicas requiere autorización municipal adicional.,Ley 28681 (bebidas alcohólicas) y ordenanza municipal 

R0164,rubro,rubro = polleria,req.INSPECCION_SANITARIA = True,El giro «Pollería / parrilla» requiere: Inspección/autorización sanitaria del establecimiento.,D.S. 00798-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0165,rubro,rubro = polleria,req.CARNE_SANIDAD = True,El giro «Pollería / parrilla» requiere: Carné de sanidad de manipuladores de alimentos.,D.S. 007-98SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0166,rubro,rubro = polleria Y vende_alcohol = si,req.AUTORIZ_ALCOHOL = True,Vender bebidas alcohólicas requiere autorización municipal adicional.,Ley 28681 (bebidas alcohólicas) y ordenanza municipal 

R0167,rubro,rubro = cafeteria,req.INSPECCION_SANITARIA = True,El giro «Cafetería / juguería / snack» requiere: Inspección/autorización sanitaria del establecimiento.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0168,rubro,rubro = cafeteria,req.CARNE_SANIDAD = True,El giro «Cafetería / juguería / snack» requiere: Carné de sanidad de manipuladores de alimentos.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0169,rubro,rubro = panaderia,req.INSPECCION_SANITARIA = True,El giro «Panadería / pastelería» requiere: Inspección/autorización sanitaria del establecimiento.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0170,rubro,rubro = panaderia,req.CARNE_SANIDAD = True,El giro «Panadería / pastelería» requiere: Carné de sanidad de manipuladores de alimentos.,D.S. 00798-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0171,rubro,rubro = bodega,req.INSPECCION_SANITARIA = True,El giro «Bodega / tienda de abarrotes» requiere: Inspección/autorización sanitaria del establecimiento.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0172,rubro,rubro = bodega Y vende_alcohol = si,req.AUTORIZ_ALCOHOL = True,Vender bebidas alcohólicas requiere autorización municipal adicional.,Ley 28681 (bebidas alcohólicas) y ordenanza municipal 

R0173,rubro,rubro = minimarket,req.INSPECCION_SANITARIA = True,El giro «Minimarket / autoservicio» requiere: Inspección/autorización sanitaria del establecimiento.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0174,rubro,rubro = minimarket Y vende_alcohol = si,req.AUTORIZ_ALCOHOL = True,Vender bebidas alcohólicas requiere autorización municipal adicional.,Ley 28681 (bebidas alcohólicas) y ordenanza municipal 

R0175,rubro,rubro = pescaderia,req.INSPECCION_SANITARIA = True,El giro «Pescadería / venta de mariscos» requiere: Inspección/autorización sanitaria del establecimiento.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0176,rubro,rubro = pescaderia,req.CARNE_SANIDAD = True,El giro «Pescadería / venta de mariscos» requiere: Carné de sanidad de manipuladores de alimentos.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0177,rubro,rubro = carniceria,req.INSPECCION_SANITARIA = True,El giro «Carnicería / venta de aves» requiere: Inspección/autorización sanitaria del establecimiento.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0178,rubro,rubro = carniceria,req.CARNE_SANIDAD = True,El giro «Carnicería / venta de aves» requiere: Carné de sanidad de manipuladores de alimentos.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0179,rubro,rubro = prod_alimentos,req.REGISTRO_SANITARIO_DIGESA = True,"El giro «Producción de alimentos envasados (dulces, conservas, snacks)» requiere: Registro sanitario de alimentos y bebidas envasados.",D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0180,rubro,rubro = prod_alimentos,req.CARNE_SANIDAD = True,"El giro «Producción de alimentos envasados (dulces, conservas, snacks)» requiere: Carné de sanidad de manipuladores de alimentos.",D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0181,rubro,rubro = prod_alimentos,req.REG_MARCA = True,"El giro «Producción de alimentos envasados (dulces, conservas, snacks)» requiere: Registro de marca (recomendado).",D.Leg. 1075 y Decisión Andina 486 (propiedad industrial) 

R0182,rubro,rubro = molino_arroz,req.REGISTRO_SANITARIO_DIGESA = True,El giro «Molino / pilado de arroz y granos» requiere: Registro sanitario de alimentos y bebidas envasados.,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) 

R0183,rubro,rubro = agroinsumos,req.REG_PLAGUICIDAS = True,El giro «Venta de agroinsumos y plaguicidas» requiere: Registro de establecimiento de venta de plaguicidas.,Reglamento del Sistema Nacional de Plaguicidas Agrícolas (SENASA) 

R0184,rubro,rubro = botica,req.AUTORIZ_BOTICA = True,El giro «Botica / farmacia» requiere: Autorización sanitaria de botica/farmacia y director técnico.,Ley 29459 (Productos Farmacéuticos) y D.S. 014-2011-SA 

R0185,rubro,rubro = hospedaje,req.REG_HOSPEDAJE = True,"El giro «Hospedaje (hostal, alojamiento)» requiere: Registro/clasificación del establecimiento de hospedaje.",D.S. 001-2015-MINCETUR (Reglamento de establecimientos de hospedaje) 

R0186,rubro,rubro = agencia,req.REG_AGENCIA_VIAJES = True,El giro «Agencia de viajes y turismo» requiere: Registro de agencia de viajes y turismo.,Reglamento de agencias de viajes y turismo (MINCETUR) 

R0187,rubro,rubro = artesania,req.REG_MARCA = True,"El giro «Artesanía (textil, paja, cerámica)» requiere: Registro de marca (recomendado).",D.Leg. 1075 y Decisión Andina 486 (propiedad industrial) 

R0188,rubro,rubro = artesania,req.REG_ARTESANO = True,"El giro «Artesanía (textil, paja, cerámica)» requiere: Registro Nacional del Artesano (recomendado).",Ley 29073 (Ley del Artesano) 

R0189,rubro,rubro = confecciones,req.REG_MARCA = True,El giro «Confección de prendas y calzado» requiere: Registro de marca (recomendado).,D.Leg. 1075 y Decisión Andina 486 (propiedad industrial) 

R0190,rubro,rubro = licores,req.AUTORIZ_ALCOHOL = True,El giro «Distribuidora / venta de licores» requiere: Autorización municipal para venta de bebidas alcohólicas.,Ley 28681 (bebidas alcohólicas) y ordenanza municipal 

R0191,laboral,trabajadores = t1,req.T_REGISTRO = True,"Con trabajadores a cargo, el empleador debe cumplir: Registro de trabajadores en T-Registro/PLAME y EsSalud.",D.S. 018-2007-TR (T-Registro y PLAME) 

R0192,laboral,trabajadores = t1,req.CONTRATOS_LABORALES = True,"Con trabajadores a cargo, el empleador debe cumplir: Contratos de trabajo y boletas de pago.",D.S. 003-97-TR (TUO de la Ley de Productividad y Competitividad Laboral) 

R0193,laboral,trabajadores = t1,req.SST_BASICO = True,"Con trabajadores a cargo, el empleador debe cumplir: Sistema básico de seguridad y salud en el trabajo.",Ley 29783 (Seguridad y Salud en el Trabajo) 

R0194,laboral,trabajadores = t1 Y tamano = micro,req.REMYPE = True,La MYPE con trabajadores debe acreditarse en el REMYPE para acceder al régimen laboral especial.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R0195,laboral,trabajadores = t1 Y tamano = pequena,req.REMYPE = True,La MYPE con trabajadores debe acreditarse en el REMYPE para acceder al régimen laboral especial.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R0196,laboral,rubro = molino_arroz Y trabajadores = t1,req.SCTR = True,«Molino / pilado de arroz y granos» implica actividad de riesgo: el personal debe contar con SCTR (verificar el anexo de actividades de riesgo).,Ley 26790 y D.S. 003-98-SA (SCTR) 

R0197,laboral,rubro = taller Y trabajadores = t1,req.SCTR = True,«Taller mecánico / mecánica automotriz» implica actividad de riesgo: el personal debe contar con SCTR (verificar el anexo de actividades de riesgo).,Ley 26790 y D.S. 003-98-SA (SCTR) 

R0198,laboral,rubro = metalmecanica Y trabajadores = t1,req.SCTR = True,«Carpintería metálica / de madera» implica actividad de riesgo: el personal debe contar con SCTR (verificar el anexo de actividades de riesgo).,Ley 26790 y D.S. 003-98-SA (SCTR) 

R0199,laboral,rubro = confecciones Y trabajadores = t1,req.SCTR = True,«Confección de prendas y calzado» implica actividad de riesgo: el personal debe contar con SCTR (verificar el anexo de actividades de riesgo).,Ley 26790 y D.S. 003-98-SA (SCTR) 

R0200,laboral,trabajadores = t2,req.T_REGISTRO = True,"Con trabajadores a cargo, el empleador debe cumplir: Registro de trabajadores en T-Registro/PLAME y EsSalud.",D.S. 018-2007-TR (T-Registro y PLAME) 

R0201,laboral,trabajadores = t2,req.CONTRATOS_LABORALES = True,"Con trabajadores a cargo, el empleador debe cumplir: Contratos de trabajo y boletas de pago.",D.S. 003-97-TR (TUO de la Ley de Productividad y Competitividad Laboral) 

R0202,laboral,trabajadores = t2,req.SST_BASICO = True,"Con trabajadores a cargo, el empleador debe cumplir: Sistema básico de seguridad y salud en el trabajo.",Ley 29783 (Seguridad y Salud en el Trabajo) 

R0203,laboral,trabajadores = t2 Y tamano = micro,req.REMYPE = True,La MYPE con trabajadores debe acreditarse en el REMYPE para acceder al régimen laboral especial.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R0204,laboral,trabajadores = t2 Y tamano = pequena,req.REMYPE = True,La MYPE con trabajadores debe acreditarse en el REMYPE para acceder al régimen laboral especial.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R0205,laboral,rubro = molino_arroz Y trabajadores = t2,req.SCTR = True,«Molino / pilado de arroz y granos» implica actividad de riesgo: el personal debe contar con SCTR (verificar el anexo de actividades de riesgo).,Ley 26790 y D.S. 003-98-SA (SCTR) 

R0206,laboral,rubro = taller Y trabajadores = t2,req.SCTR = True,«Taller mecánico / mecánica automotriz» implica actividad de riesgo: el personal debe contar con SCTR (verificar el anexo de actividades de riesgo).,Ley 26790 y D.S. 003-98-SA (SCTR) 

R0207,laboral,rubro = metalmecanica Y trabajadores = t2,req.SCTR = True,«Carpintería metálica / de madera» implica actividad de riesgo: el personal debe contar con SCTR (verificar el anexo de actividades de riesgo).,Ley 26790 y D.S. 003-98-SA (SCTR) 

R0208,laboral,rubro = confecciones Y trabajadores = t2,req.SCTR = True,«Confección de prendas y calzado» implica actividad de riesgo: el personal debe contar con SCTR (verificar el anexo de actividades de riesgo).,Ley 26790 y D.S. 003-98-SA (SCTR) 

R0209,dependencia,req.MINUTA_ESCRITURA = True,req.BUSQUEDA_RESERVA = True,«Minuta y escritura pública de constitución» exige haber realizado antes «Búsqueda y reserva de nombre de la empresa».,Ley General de Sociedades (Ley 26887); D.Leg. 1049 (Notariado) 

R0210,dependencia,req.INSCRIPCION_SUNARP = True,req.MINUTA_ESCRITURA = True,«Inscripción de la empresa en Registros Públicos» exige haber realizado antes «Minuta y escritura pública de constitución».,Ley General de Sociedades (Ley 26887); SUNARP 

R0211,dependencia,req.CLAVE_SOL = True,req.RUC = True,«Obtener la Clave SOL» exige haber realizado antes «Inscripción en el RUC».,"Normativa SUNAT (RUC, comprobantes, regímenes)" 

R0212,dependencia,req.ELEGIR_REGIMEN = True,req.RUC = True,«Elegir/declarar el régimen tributario» exige haber realizado antes «Inscripción en el RUC».,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta 

R0213,dependencia,req.COMPROBANTES = True,req.RUC = True,«Habilitar la emisión de comprobantes de pago electrónicos» exige haber realizado antes «Inscripción en el RUC».,Reglamento de Comprobantes de Pago (R.S. 00799/SUNAT) 

R0214,dependencia,req.COMPROBANTES = True,req.CLAVE_SOL = True,«Habilitar la emisión de comprobantes de pago electrónicos» exige haber realizado antes «Obtener la Clave SOL».,Reglamento de Comprobantes de Pago (R.S. 00799/SUNAT) 

R0215,dependencia,req.COMPROBANTES = True,req.ELEGIR_REGIMEN = True,«Habilitar la emisión de comprobantes de pago electrónicos» exige haber 

realizado antes «Elegir/declarar el régimen tributario».,Reglamento de Comprobantes de Pago (R.S. 007-99/SUNAT) 

R0216,dependencia,req.LICENCIA_FUNCIONAMIENTO = True,req.RUC = True,«Licencia de funcionamiento» exige haber realizado antes «Inscripción en el RUC».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0217,dependencia,req.AUTORIZ_ALCOHOL = True,req.LICENCIA_FUNCIONAMIENTO = True,«Autorización municipal para venta de bebidas alcohólicas» exige haber realizado antes «Licencia de funcionamiento».,Ley 28681 (bebidas alcohólicas) y ordenanza municipal 

R0218,dependencia,req.AUTORIZ_ANUNCIO = 

True,req.LICENCIA_FUNCIONAMIENTO = True,«Autorización de anuncio/letrero publicitario» exige haber realizado antes «Licencia de 

funcionamiento».,Ordenanza municipal de anuncios y avisos publicitarios 

R0219,dependencia,req.REMYPE = True,req.RUC = True,«Inscripción en el REMYPE» exige haber realizado antes «Inscripción en el RUC».,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R0220,dependencia,req.REMYPE = True,req.CLAVE_SOL = True,«Inscripción en el REMYPE» exige haber realizado antes «Obtener la Clave SOL».,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R0221,dependencia,req.T_REGISTRO = True,req.RUC = True,«Registro de trabajadores en T-Registro/PLAME y EsSalud» exige haber realizado antes «Inscripción en el RUC».,D.S. 018-2007-TR (T-Registro y PLAME) 

R0222,dependencia,req.T_REGISTRO = True,req.CLAVE_SOL = True,«Registro de trabajadores en T-Registro/PLAME y EsSalud» exige haber realizado antes «Obtener la Clave SOL».,D.S. 018-2007-TR (T-Registro y PLAME) 

R0223,dependencia,req.SCTR = True,req.T_REGISTRO = True,«Seguro complementario de trabajo de riesgo (SCTR)» exige haber realizado antes «Registro de trabajadores en T-Registro/PLAME y EsSalud».,Ley 26790 y D.S. 003-98-SA (SCTR) 

R0224,dependencia,req.LIBROS_CONTABLES = True,req.RUC = True,«Llevar libros y registros contables según el régimen» exige haber realizado antes «Inscripción en el RUC».,R.S. 234-2006/SUNAT (libros y registros vinculados a asuntos tributarios) 

R0225,dependencia,req.DECLARACION_MENSUAL = True,req.RUC = True,«Declarar y pagar impuestos mensualmente» exige haber realizado antes «Inscripción en el RUC».,"Normativa SUNAT (RUC, comprobantes, regímenes)" 

R0226,dependencia,req.DECLARACION_MENSUAL = True,req.CLAVE_SOL = True,«Declarar y pagar impuestos mensualmente» exige haber realizado antes «Obtener la Clave SOL».,"Normativa SUNAT (RUC, comprobantes, regímenes)" 

R0227,dependencia,req.DECLARACION_MENSUAL = True,req.ELEGIR_REGIMEN = True,«Declarar y pagar impuestos mensualmente» exige haber realizado antes «Elegir/declarar el régimen tributario».,"Normativa SUNAT (RUC, comprobantes, regímenes)" 

R0228,distrito,distrito = Chiclayo Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Provincial de Chiclayo -- Subgerencia de Licencias / Desarrollo Económico,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0229,distrito,distrito = Chiclayo Y req.CERT_ZONIFICACION = 

True,donde.CERT_ZONIFICACION = Municipalidad Provincial de Chiclayo -- Gerencia de Desarrollo Urbano,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0230,distrito,distrito = Chiclayo Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Provincial de Chiclayo -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0231,distrito,distrito = Chiclayo Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Provincial de Chiclayo -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0232,distrito,distrito = Chiclayo Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Provincial de Chiclayo -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0233,distrito,distrito = Chiclayo Y req.CARNE_SANIDAD = 

True,donde.CARNE_SANIDAD = Municipalidad Provincial de Chiclayo -- Área de Salud / Sanidad municipal,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0234,distrito,distrito = Chiclayo Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Provincial de Chiclayo -- Área de Salud / Sanidad municipal,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0235,distrito,distrito = Chiclayo Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Provincial de Chiclayo -- Subgerencia de Licencias,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0236,distrito,distrito = Chiclayo Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Provincial de Chiclayo -- Gerencia de Desarrollo Urbano / Licencias,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0237,distrito,distrito = Chiclayo Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Provincial de Chiclayo - - Administración de Mercados,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0238,distrito,distrito = Chiclayo Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Provincial de Chiclayo -- Subgerencia de Comercio / Fiscalización,En Chiclayo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0239,distrito,distrito = José Leonardo Ortiz Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de José Leonardo Ortiz -- Subgerencia de Licencias / Desarrollo Económico,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0240,distrito,distrito = José Leonardo Ortiz Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Distrital de José Leonardo Ortiz -- Gerencia de Desarrollo Urbano,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0241,distrito,distrito = José Leonardo Ortiz Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de José Leonardo Ortiz -- Subgerencia de Defensa Civil / Gestión del Riesgo,En José Leonardo Ortiz este 

trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0242,distrito,distrito = José Leonardo Ortiz Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de José Leonardo Ortiz -- Subgerencia de Defensa Civil / Gestión del Riesgo,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0243,distrito,distrito = José Leonardo Ortiz Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de José Leonardo Ortiz -- Subgerencia de Defensa Civil / Gestión del Riesgo,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0244,distrito,distrito = José Leonardo Ortiz Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Distrital de José Leonardo Ortiz -- Área de Salud / Sanidad municipal,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0245,distrito,distrito = José Leonardo Ortiz Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de José Leonardo Ortiz -- Área de Salud / Sanidad municipal,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0246,distrito,distrito = José Leonardo Ortiz Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de José Leonardo Ortiz -- Subgerencia de Licencias,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0247,distrito,distrito = José Leonardo Ortiz Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de José Leonardo Ortiz -- Gerencia de Desarrollo Urbano / Licencias,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0248,distrito,distrito = José Leonardo Ortiz Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de José Leonardo Ortiz -- Administración de Mercados,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0249,distrito,distrito = José Leonardo Ortiz Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de José Leonardo Ortiz -- Subgerencia de Comercio / Fiscalización,En José Leonardo Ortiz este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0250,distrito,distrito = La Victoria Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de La Victoria -- Subgerencia de Licencias / Desarrollo Económico,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0251,distrito,distrito = La Victoria Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Distrital de La Victoria -- Gerencia de Desarrollo Urbano,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0252,distrito,distrito = La Victoria Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de La Victoria -- Subgerencia de Defensa Civil / Gestión del Riesgo,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0253,distrito,distrito = La Victoria Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de La Victoria -- Subgerencia de Defensa Civil / Gestión del Riesgo,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0254,distrito,distrito = La Victoria Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de La Victoria -- Subgerencia de Defensa Civil / Gestión del Riesgo,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0255,distrito,distrito = La Victoria Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Distrital de La Victoria -- Área de Salud / Sanidad municipal,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0256,distrito,distrito = La Victoria Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de La Victoria -- Área de Salud / Sanidad municipal,En La Victoria este trámite lo atiende la 

municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0257,distrito,distrito = La Victoria Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de La Victoria -- Subgerencia de Licencias,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0258,distrito,distrito = La Victoria Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de La Victoria -- Gerencia de Desarrollo Urbano / Licencias,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0259,distrito,distrito = La Victoria Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de La Victoria - - Administración de Mercados,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0260,distrito,distrito = La Victoria Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de La Victoria -- Subgerencia de Comercio / Fiscalización,En La Victoria este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0261,distrito,distrito = Pimentel Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Pimentel -- Subgerencia de Licencias / Desarrollo Económico,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0262,distrito,distrito = Pimentel Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Pimentel -- Gerencia de Desarrollo Urbano,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0263,distrito,distrito = Pimentel Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Pimentel -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0264,distrito,distrito = Pimentel Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de Pimentel -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0265,distrito,distrito = Pimentel Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Pimentel -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0266,distrito,distrito = Pimentel Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Distrital de Pimentel -- Área de Salud / Sanidad municipal,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0267,distrito,distrito = Pimentel Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Pimentel -- Área de Salud / Sanidad municipal,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0268,distrito,distrito = Pimentel Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Pimentel -- Subgerencia de Licencias,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0269,distrito,distrito = Pimentel Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Pimentel -- Gerencia de Desarrollo Urbano / Licencias,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0270,distrito,distrito = Pimentel Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Pimentel -- Administración de Mercados,En Pimentel este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0271,distrito,distrito = Pimentel Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Pimentel -- Subgerencia de Comercio / Fiscalización,En Pimentel este trámite lo atiende la 

municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0272,distrito,distrito = Monsefú Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Monsefú -- Subgerencia de Licencias / Desarrollo Económico,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0273,distrito,distrito = Monsefú Y req.CERT_ZONIFICACION = 

True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Monsefú -- Gerencia de Desarrollo Urbano,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0274,distrito,distrito = Monsefú Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Monsefú -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0275,distrito,distrito = Monsefú Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de Monsefú -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0276,distrito,distrito = Monsefú Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Monsefú -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0277,distrito,distrito = Monsefú Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Distrital de Monsefú -- Área de Salud / Sanidad municipal,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0278,distrito,distrito = Monsefú Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Monsefú -- Área de Salud / Sanidad municipal,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0279,distrito,distrito = Monsefú Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Monsefú -- Subgerencia de Licencias,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0280,distrito,distrito = Monsefú Y req.AUTORIZ_ANUNCIO = 

True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Monsefú -- Gerencia de Desarrollo Urbano / Licencias,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0281,distrito,distrito = Monsefú Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Monsefú -- Administración de Mercados,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0282,distrito,distrito = Monsefú Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Monsefú -- Subgerencia de Comercio / Fiscalización,En Monsefú este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0283,distrito,distrito = Reque Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Reque -- Subgerencia de Licencias / Desarrollo Económico,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0284,distrito,distrito = Reque Y req.CERT_ZONIFICACION = 

True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Reque -- Gerencia de Desarrollo Urbano,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0285,distrito,distrito = Reque Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Reque -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0286,distrito,distrito = Reque Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de Reque -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0287,distrito,distrito = Reque Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Reque -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0288,distrito,distrito = Reque Y req.CARNE_SANIDAD = 

True,donde.CARNE_SANIDAD = Municipalidad Distrital de Reque -- Área de Salud / Sanidad municipal,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0289,distrito,distrito = Reque Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Reque -- Área de Salud / Sanidad municipal,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0290,distrito,distrito = Reque Y req.AUTORIZ_ALCOHOL = 

True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Reque -- Subgerencia de Licencias,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0291,distrito,distrito = Reque Y req.AUTORIZ_ANUNCIO = 

True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Reque -- Gerencia de Desarrollo Urbano / Licencias,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0292,distrito,distrito = Reque Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Reque -- Administración de Mercados,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0293,distrito,distrito = Reque Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Reque -- Subgerencia de Comercio / Fiscalización,En Reque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0294,distrito,distrito = Pomalca Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Pomalca -- Subgerencia de Licencias / Desarrollo Económico,En Pomalca este trámite lo 

atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0295,distrito,distrito = Pomalca Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Pomalca -- Gerencia de Desarrollo Urbano,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0296,distrito,distrito = Pomalca Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Pomalca -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0297,distrito,distrito = Pomalca Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de Pomalca -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0298,distrito,distrito = Pomalca Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Pomalca -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0299,distrito,distrito = Pomalca Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Distrital de Pomalca -- Área de Salud / Sanidad municipal,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0300,distrito,distrito = Pomalca Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Pomalca -- Área de Salud / Sanidad municipal,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0301,distrito,distrito = Pomalca Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Pomalca -- Subgerencia de Licencias,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0302,distrito,distrito = Pomalca Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Pomalca -- Gerencia de Desarrollo Urbano / Licencias,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0303,distrito,distrito = Pomalca Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Pomalca -- Administración de Mercados,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0304,distrito,distrito = Pomalca Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Pomalca -- Subgerencia de Comercio / Fiscalización,En Pomalca este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0305,distrito,distrito = Tumán Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Tumán -- Subgerencia de Licencias / Desarrollo Económico,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0306,distrito,distrito = Tumán Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Tumán -- Gerencia de Desarrollo Urbano,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0307,distrito,distrito = Tumán Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Tumán -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0308,distrito,distrito = Tumán Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de Tumán -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0309,distrito,distrito = Tumán Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Tumán -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0310,distrito,distrito = Tumán Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Distrital de Tumán -- Área de Salud / Sanidad municipal,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0311,distrito,distrito = Tumán Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Tumán -- Área de Salud / Sanidad municipal,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0312,distrito,distrito = Tumán Y req.AUTORIZ_ALCOHOL = 

True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Tumán -- Subgerencia de Licencias,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0313,distrito,distrito = Tumán Y req.AUTORIZ_ANUNCIO = 

True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Tumán -- Gerencia de Desarrollo Urbano / Licencias,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0314,distrito,distrito = Tumán Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Tumán -- Administración de Mercados,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0315,distrito,distrito = Tumán Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Tumán -- Subgerencia de Comercio / Fiscalización,En Tumán este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0316,distrito,distrito = Santa Rosa Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Santa Rosa -- Subgerencia de Licencias / Desarrollo Económico,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0317,distrito,distrito = Santa Rosa Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Santa Rosa -- Gerencia de Desarrollo Urbano,En Santa Rosa este trámite lo atiende la 

municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0318,distrito,distrito = Santa Rosa Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Santa Rosa -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0319,distrito,distrito = Santa Rosa Y req.ITSE_DETALLE = 

True,donde.ITSE_DETALLE = Municipalidad Distrital de Santa Rosa -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0320,distrito,distrito = Santa Rosa Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Santa Rosa -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0321,distrito,distrito = Santa Rosa Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Distrital de Santa Rosa -- Área de Salud / Sanidad municipal,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0322,distrito,distrito = Santa Rosa Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Santa Rosa -- Área de Salud / Sanidad municipal,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0323,distrito,distrito = Santa Rosa Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Santa Rosa -- Subgerencia de Licencias,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0324,distrito,distrito = Santa Rosa Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Santa Rosa -- Gerencia de Desarrollo Urbano / Licencias,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0325,distrito,distrito = Santa Rosa Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Santa Rosa -- Administración de Mercados,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0326,distrito,distrito = Santa Rosa Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Santa Rosa -- Subgerencia de Comercio / Fiscalización,En Santa Rosa este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0327,distrito,distrito = Eten Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Eten -- Subgerencia de Licencias / Desarrollo Económico,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0328,distrito,distrito = Eten Y req.CERT_ZONIFICACION = 

True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Eten -- Gerencia de Desarrollo Urbano,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0329,distrito,distrito = Eten Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Eten -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0330,distrito,distrito = Eten Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de Eten -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0331,distrito,distrito = Eten Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Eten -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0332,distrito,distrito = Eten Y req.CARNE_SANIDAD = 

True,donde.CARNE_SANIDAD = Municipalidad Distrital de Eten -- Área de Salud / Sanidad municipal,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0333,distrito,distrito = Eten Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Eten -- Área de Salud / Sanidad municipal,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0334,distrito,distrito = Eten Y req.AUTORIZ_ALCOHOL = 

True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Eten -- Subgerencia de Licencias,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0335,distrito,distrito = Eten Y req.AUTORIZ_ANUNCIO = 

True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Eten -- Gerencia de Desarrollo Urbano / Licencias,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0336,distrito,distrito = Eten Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Eten -- Administración de Mercados,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0337,distrito,distrito = Eten Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Eten -- Subgerencia de Comercio / Fiscalización,En Eten este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0338,distrito,distrito = Lambayeque Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Provincial de Lambayeque -- Subgerencia de Licencias / Desarrollo Económico,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0339,distrito,distrito = Lambayeque Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Provincial de Lambayeque -- Gerencia de Desarrollo Urbano,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0340,distrito,distrito = Lambayeque Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Provincial de Lambayeque -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Lambayeque este trámite lo 

atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0341,distrito,distrito = Lambayeque Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Provincial de Lambayeque -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0342,distrito,distrito = Lambayeque Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Provincial de Lambayeque -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0343,distrito,distrito = Lambayeque Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Provincial de Lambayeque -- Área de Salud / Sanidad municipal,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0344,distrito,distrito = Lambayeque Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Provincial de Lambayeque -- Área de Salud / Sanidad municipal,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0345,distrito,distrito = Lambayeque Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Provincial de Lambayeque -- Subgerencia de Licencias,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0346,distrito,distrito = Lambayeque Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Provincial de Lambayeque -- Gerencia de Desarrollo Urbano / Licencias,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0347,distrito,distrito = Lambayeque Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Provincial de Lambayeque -- Administración de Mercados,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0348,distrito,distrito = Lambayeque Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Provincial de Lambayeque -- Subgerencia de Comercio / Fiscalización,En Lambayeque este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0349,distrito,distrito = Mochumí Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Mochumí -- Subgerencia de Licencias / Desarrollo Económico,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0350,distrito,distrito = Mochumí Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Mochumí -- Gerencia de Desarrollo Urbano,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0351,distrito,distrito = Mochumí Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Mochumí -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0352,distrito,distrito = Mochumí Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de Mochumí -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0353,distrito,distrito = Mochumí Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Mochumí -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0354,distrito,distrito = Mochumí Y req.CARNE_SANIDAD = 

True,donde.CARNE_SANIDAD = Municipalidad Distrital de Mochumí -- Área de Salud / Sanidad municipal,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0355,distrito,distrito = Mochumí Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Mochumí -- Área de Salud / Sanidad municipal,En Mochumí este trámite lo atiende la 

municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0356,distrito,distrito = Mochumí Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Mochumí -- Subgerencia de Licencias,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0357,distrito,distrito = Mochumí Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Mochumí -- Gerencia de Desarrollo Urbano / Licencias,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0358,distrito,distrito = Mochumí Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Mochumí -- Administración de Mercados,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0359,distrito,distrito = Mochumí Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Mochumí -- Subgerencia de Comercio / Fiscalización,En Mochumí este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0360,distrito,distrito = Túcume Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Túcume -- Subgerencia de Licencias / Desarrollo Económico,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0361,distrito,distrito = Túcume Y req.CERT_ZONIFICACION = 

True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Túcume -- Gerencia de Desarrollo Urbano,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0362,distrito,distrito = Túcume Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Túcume -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0363,distrito,distrito = Túcume Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de Túcume -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0364,distrito,distrito = Túcume Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Túcume -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0365,distrito,distrito = Túcume Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Distrital de Túcume -- Área de Salud / Sanidad municipal,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0366,distrito,distrito = Túcume Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Túcume -- Área de Salud / Sanidad municipal,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0367,distrito,distrito = Túcume Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Túcume -- Subgerencia de Licencias,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0368,distrito,distrito = Túcume Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Túcume -- Gerencia de Desarrollo Urbano / Licencias,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0369,distrito,distrito = Túcume Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Túcume -- Administración de Mercados,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0370,distrito,distrito = Túcume Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Túcume -- Subgerencia de Comercio / Fiscalización,En Túcume este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0371,distrito,distrito = Ferreñafe Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Provincial de Ferreñafe -- Subgerencia de Licencias / Desarrollo Económico,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0372,distrito,distrito = Ferreñafe Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Provincial de Ferreñafe -- Gerencia de Desarrollo Urbano,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0373,distrito,distrito = Ferreñafe Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Provincial de Ferreñafe -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0374,distrito,distrito = Ferreñafe Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Provincial de Ferreñafe -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0375,distrito,distrito = Ferreñafe Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Provincial de Ferreñafe -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0376,distrito,distrito = Ferreñafe Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Provincial de Ferreñafe -- Área de Salud / Sanidad municipal,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0377,distrito,distrito = Ferreñafe Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Provincial de Ferreñafe -- Área de Salud / Sanidad municipal,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0378,distrito,distrito = Ferreñafe Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Provincial de Ferreñafe -- Subgerencia de Licencias,En Ferreñafe este trámite lo atiende la municipalidad 

correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0379,distrito,distrito = Ferreñafe Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Provincial de Ferreñafe -- Gerencia de Desarrollo Urbano / Licencias,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0380,distrito,distrito = Ferreñafe Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Provincial de Ferreñafe -- Administración de Mercados,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0381,distrito,distrito = Ferreñafe Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Provincial de Ferreñafe -- Subgerencia de Comercio / Fiscalización,En Ferreñafe este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0382,distrito,distrito = Pueblo Nuevo Y req.LICENCIA_FUNCIONAMIENTO = True,donde.LICENCIA_FUNCIONAMIENTO = Municipalidad Distrital de Pueblo Nuevo -- Subgerencia de Licencias / Desarrollo Económico,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0383,distrito,distrito = Pueblo Nuevo Y req.CERT_ZONIFICACION = True,donde.CERT_ZONIFICACION = Municipalidad Distrital de Pueblo Nuevo -- Gerencia de Desarrollo Urbano,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0384,distrito,distrito = Pueblo Nuevo Y req.ITSE_BASICA = True,donde.ITSE_BASICA = Municipalidad Distrital de Pueblo Nuevo -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0385,distrito,distrito = Pueblo Nuevo Y req.ITSE_DETALLE = True,donde.ITSE_DETALLE = Municipalidad Distrital de Pueblo Nuevo -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0386,distrito,distrito = Pueblo Nuevo Y req.ITSE_MULTI = True,donde.ITSE_MULTI = Municipalidad Distrital de Pueblo Nuevo -- Subgerencia de Defensa Civil / Gestión del Riesgo,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0387,distrito,distrito = Pueblo Nuevo Y req.CARNE_SANIDAD = True,donde.CARNE_SANIDAD = Municipalidad Distrital de Pueblo Nuevo -- Área de Salud / Sanidad municipal,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0388,distrito,distrito = Pueblo Nuevo Y req.INSPECCION_SANITARIA = True,donde.INSPECCION_SANITARIA = Municipalidad Distrital de Pueblo Nuevo -- Área de Salud / Sanidad municipal,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0389,distrito,distrito = Pueblo Nuevo Y req.AUTORIZ_ALCOHOL = True,donde.AUTORIZ_ALCOHOL = Municipalidad Distrital de Pueblo Nuevo -- Subgerencia de Licencias,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0390,distrito,distrito = Pueblo Nuevo Y req.AUTORIZ_ANUNCIO = True,donde.AUTORIZ_ANUNCIO = Municipalidad Distrital de Pueblo Nuevo -- Gerencia de Desarrollo Urbano / Licencias,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0391,distrito,distrito = Pueblo Nuevo Y req.AUTORIZ_PUESTO_MERCADO = True,donde.AUTORIZ_PUESTO_MERCADO = Municipalidad Distrital de Pueblo Nuevo -- Administración de Mercados,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0392,distrito,distrito = Pueblo Nuevo Y req.AUTORIZ_AMBULANTE = True,donde.AUTORIZ_AMBULANTE = Municipalidad Distrital de Pueblo Nuevo -- Subgerencia de Comercio / Fiscalización,En Pueblo Nuevo este trámite lo atiende la municipalidad correspondiente.,TUPA de la municipalidad (la denominación de la oficina puede variar) 

R0393,documentos,req.BUSQUEDA_RESERVA = True,docs.BUSQUEDA_RESERVA = Consulta de homonimia en el índice de personas jurídicas de SUNARP,Documento habitual para «Búsqueda y reserva de nombre de la 

empresa».,SUNARP – Reglamento del Registro de Sociedades -- contrastar con TUPA 

R0394,documentos,req.BUSQUEDA_RESERVA = True,docs.BUSQUEDA_RESERVA = Reserva del nombre (vigencia limitada),Documento habitual para «Búsqueda y reserva de nombre de la empresa».,SUNARP – Reglamento del Registro de Sociedades -- contrastar con TUPA 

R0395,documentos,req.BUSQUEDA_RESERVA = True,docs.BUSQUEDA_RESERVA = Pago de la tasa registral,Documento habitual para «Búsqueda y reserva de nombre de la empresa».,SUNARP – Reglamento del Registro de Sociedades -- contrastar con TUPA 

R0396,documentos,req.MINUTA_ESCRITURA = True,docs.MINUTA_ESCRITURA = Minuta firmada por abogado con estatuto y aportes de capital,Documento habitual para «Minuta y escritura pública de constitución».,Ley General de Sociedades (Ley 26887); D.Leg. 1049 (Notariado) -- contrastar con TUPA 

R0397,documentos,req.MINUTA_ESCRITURA = True,docs.MINUTA_ESCRITURA = DNI de los socios,Documento habitual para «Minuta y escritura pública de constitución».,Ley General de Sociedades (Ley 26887); D.Leg. 1049 (Notariado) -- contrastar con TUPA 

R0398,documentos,req.MINUTA_ESCRITURA = True,docs.MINUTA_ESCRITURA = Constancia del aporte (dinero o bienes),Documento habitual para «Minuta y escritura pública de constitución».,Ley General de Sociedades (Ley 26887); D.Leg. 1049 (Notariado) -- contrastar con TUPA 

R0399,documentos,req.MINUTA_ESCRITURA = True,docs.MINUTA_ESCRITURA = Elevación a escritura pública en notaría,Documento habitual para «Minuta y escritura pública de constitución».,Ley General de Sociedades (Ley 26887); D.Leg. 1049 (Notariado) -- contrastar con TUPA 

R0400,documentos,req.INSCRIPCION_SUNARP = 

True,docs.INSCRIPCION_SUNARP = Testimonio de la escritura 

pública,Documento habitual para «Inscripción de la empresa en Registros Públicos».,Ley General de Sociedades (Ley 26887); SUNARP -- contrastar con TUPA 

R0401,documentos,req.INSCRIPCION_SUNARP = 

True,docs.INSCRIPCION_SUNARP = Solicitud de inscripción (título),Documento habitual para «Inscripción de la empresa en Registros Públicos».,Ley General de Sociedades (Ley 26887); SUNARP -- contrastar con TUPA 

R0402,documentos,req.INSCRIPCION_SUNARP = 

True,docs.INSCRIPCION_SUNARP = Pago de derechos registrales,Documento 

habitual para «Inscripción de la empresa en Registros Públicos».,Ley General de Sociedades (Ley 26887); SUNARP -- contrastar con TUPA 

R0403,documentos,req.RUC = True,docs.RUC = DNI vigente del titular o representante legal,Documento habitual para «Inscripción en el RUC».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R0404,documentos,req.RUC = True,docs.RUC = Documento que acredite el domicilio fiscal (recibo de servicio o contrato),Documento habitual para «Inscripción en el RUC».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R0405,documentos,req.RUC = True,docs.RUC = Ficha o partida registral (solo persona jurídica),Documento habitual para «Inscripción en el RUC».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R0406,documentos,req.RUC = True,docs.RUC = Actividad económica (CIIU) y régimen tributario elegido,Documento habitual para «Inscripción en el RUC».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R0407,documentos,req.CLAVE_SOL = True,docs.CLAVE_SOL = RUC activo,Documento habitual para «Obtener la Clave SOL».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R0408,documentos,req.CLAVE_SOL = True,docs.CLAVE_SOL = DNI del titular o representante,Documento habitual para «Obtener la Clave SOL».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R0409,documentos,req.CLAVE_SOL = True,docs.CLAVE_SOL = Generar la clave en SUNAT o en el portal,Documento habitual para «Obtener la Clave 

SOL».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R0410,documentos,req.ELEGIR_REGIMEN = True,docs.ELEGIR_REGIMEN = Declarar el régimen al inscribirse o actualizar el RUC,Documento habitual para «Elegir/declarar el régimen tributario».,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- contrastar con TUPA 

R0411,documentos,req.ELEGIR_REGIMEN = True,docs.ELEGIR_REGIMEN = Proyección de ingresos y compras anuales,Documento habitual para «Elegir/declarar el régimen tributario».,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- contrastar con TUPA 

R0412,documentos,req.COMPROBANTES = True,docs.COMPROBANTES = Clave SOL,Documento habitual para «Habilitar la emisión de comprobantes de pago 

electrónicos».,Reglamento de Comprobantes de Pago (R.S. 007-99/SUNAT) -- contrastar con TUPA 

R0413,documentos,req.COMPROBANTES = True,docs.COMPROBANTES = Afiliación al sistema de emisión electrónica autorizado,Documento habitual para «Habilitar la emisión de comprobantes de pago electrónicos».,Reglamento de Comprobantes de Pago (R.S. 007-99/SUNAT) -- contrastar con TUPA 

R0414,documentos,req.COMPROBANTES = True,docs.COMPROBANTES = Series de boleta/factura según el régimen,Documento habitual para «Habilitar la emisión de comprobantes de pago electrónicos».,Reglamento de Comprobantes de Pago (R.S. 007-99/SUNAT) -- contrastar con TUPA 

R0415,documentos,req.ACREDITAR_PROPIEDAD = 

True,docs.ACREDITAR_PROPIEDAD = Título de propiedad o partida registral,Documento habitual para «Acreditar la propiedad del local».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0416,documentos,req.ACREDITAR_PROPIEDAD = True,docs.ACREDITAR_PROPIEDAD = Copia literal actualizada del predio,Documento habitual para «Acreditar la propiedad del local».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0417,documentos,req.CONTRATO_ALQUILER = True,docs.CONTRATO_ALQUILER = Contrato de alquiler que autorice el uso comercial,Documento habitual para «Contrato de alquiler y autorización del propietario».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0418,documentos,req.CONTRATO_ALQUILER = True,docs.CONTRATO_ALQUILER = DNI del propietario,Documento habitual para «Contrato de alquiler y autorización del propietario».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0419,documentos,req.CONTRATO_ALQUILER = True,docs.CONTRATO_ALQUILER = Autorización del propietario para tramitar la licencia (firma legalizada),Documento habitual para «Contrato de alquiler y autorización del propietario».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0420,documentos,req.ACREDITAR_LOCAL = True,docs.ACREDITAR_LOCAL = Ubicación definida del local,Documento habitual para «Definir y acreditar el local (propiedad o contrato)».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0421,documentos,req.ACREDITAR_LOCAL = True,docs.ACREDITAR_LOCAL = Certificado de zonificación antes de pagar adelantos,Documento habitual para «Definir y acreditar el local (propiedad o contrato)».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0422,documentos,req.ACREDITAR_LOCAL = True,docs.ACREDITAR_LOCAL = Título de propiedad o contrato de alquiler,Documento habitual para «Definir y acreditar el local (propiedad o contrato)».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0423,documentos,req.CERT_ZONIFICACION = True,docs.CERT_ZONIFICACION = Solicitud con dirección exacta del predio,Documento habitual para «Certificado de zonificación y compatibilidad de uso».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0424,documentos,req.CERT_ZONIFICACION = True,docs.CERT_ZONIFICACION = Giro o actividad a desarrollar,Documento habitual para «Certificado de zonificación y compatibilidad de uso».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0425,documentos,req.CERT_ZONIFICACION = True,docs.CERT_ZONIFICACION = Pago de la tasa municipal,Documento habitual para «Certificado de zonificación y compatibilidad de uso».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0426,documentos,req.AUTORIZ_PUESTO_MERCADO = 

True,docs.AUTORIZ_PUESTO_MERCADO = Solicitud a la administración del mercado,Documento habitual para «Constancia/autorización de conducción de puesto en mercado».,Ordenanza municipal de mercados (TUPA) -- contrastar con TUPA 

R0427,documentos,req.AUTORIZ_PUESTO_MERCADO = True,docs.AUTORIZ_PUESTO_MERCADO = Constancia de conducción del puesto,Documento habitual para «Constancia/autorización de conducción de puesto en mercado».,Ordenanza municipal de mercados (TUPA) -- contrastar con TUPA 

R0428,documentos,req.AUTORIZ_PUESTO_MERCADO = 

True,docs.AUTORIZ_PUESTO_MERCADO = DNI y RUC,Documento habitual para «Constancia/autorización de conducción de puesto en mercado».,Ordenanza municipal de mercados (TUPA) -- contrastar con TUPA 

R0429,documentos,req.AUTORIZ_AMBULANTE = True,docs.AUTORIZ_AMBULANTE = Solicitud municipal,Documento habitual para «Autorización municipal de 

comercio ambulatorio».,Ordenanza municipal de comercio ambulatorio (TUPA) -- contrastar con TUPA 

R0430,documentos,req.AUTORIZ_AMBULANTE = True,docs.AUTORIZ_AMBULANTE = DNI,Documento habitual para «Autorización municipal de comercio ambulatorio».,Ordenanza municipal de comercio ambulatorio (TUPA) -- contrastar con TUPA 

R0431,documentos,req.AUTORIZ_AMBULANTE = True,docs.AUTORIZ_AMBULANTE = Carné de sanidad (si vende alimentos),Documento habitual para «Autorización municipal de comercio ambulatorio».,Ordenanza municipal de comercio ambulatorio (TUPA) -- contrastar con TUPA 

R0432,documentos,req.AUTORIZ_AMBULANTE = True,docs.AUTORIZ_AMBULANTE = Croquis de ubicación y horario propuesto,Documento habitual para «Autorización municipal de comercio ambulatorio».,Ordenanza municipal de comercio ambulatorio (TUPA) -- contrastar con TUPA 

R0433,documentos,req.ITSE_BASICA = True,docs.ITSE_BASICA = Solicitud/declaración jurada de ITSE,Documento habitual para «ITSE básica (inspección técnica de seguridad en edificaciones)».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0434,documentos,req.ITSE_BASICA = True,docs.ITSE_BASICA = Croquis de ubicación y distribución,Documento habitual para «ITSE básica (inspección técnica de seguridad en edificaciones)».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0435,documentos,req.ITSE_BASICA = True,docs.ITSE_BASICA = Extintores vigentes y señalización,Documento habitual para «ITSE básica (inspección técnica de seguridad en edificaciones)».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0436,documentos,req.ITSE_BASICA = True,docs.ITSE_BASICA = Constancias de instalaciones eléctricas/gas si aplica,Documento habitual para «ITSE básica (inspección técnica de seguridad en edificaciones)».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0437,documentos,req.ITSE_DETALLE = True,docs.ITSE_DETALLE = Solicitud de ITSE de detalle,Documento habitual para «ITSE de detalle».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0438,documentos,req.ITSE_DETALLE = True,"docs.ITSE_DETALLE = Planos de ubicación, arquitectura y evacuación",Documento habitual para «ITSE de detalle».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0439,documentos,req.ITSE_DETALLE = True,docs.ITSE_DETALLE = Memoria descriptiva,Documento habitual para «ITSE de detalle».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0440,documentos,req.ITSE_DETALLE = True,docs.ITSE_DETALLE = Plan de seguridad y certificados de operatividad de sistemas,Documento habitual para «ITSE de detalle».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0441,documentos,req.ITSE_MULTI = True,docs.ITSE_MULTI = Solicitud de ITSE multidisciplinaria,Documento habitual para «ITSE multidisciplinaria».,D.S. 0022018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0442,documentos,req.ITSE_MULTI = True,docs.ITSE_MULTI = Expediente técnico con planos y memoria,Documento habitual para «ITSE multidisciplinaria».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0443,documentos,req.ITSE_MULTI = True,docs.ITSE_MULTI = Informes de especialistas,Documento habitual para «ITSE multidisciplinaria».,D.S. 002-2018PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0444,documentos,req.ITSE_MULTI = True,docs.ITSE_MULTI = Plan de contingencia (según TUPA),Documento habitual para «ITSE multidisciplinaria».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R0445,documentos,req.CARNE_SANIDAD = True,docs.CARNE_SANIDAD = DNI,Documento habitual para «Carné de sanidad de manipuladores de alimentos».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0446,documentos,req.CARNE_SANIDAD = True,docs.CARNE_SANIDAD = Exámenes médicos exigidos,Documento habitual para «Carné de sanidad de manipuladores de alimentos».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0447,documentos,req.CARNE_SANIDAD = True,docs.CARNE_SANIDAD = Fotografías,Documento habitual para «Carné de sanidad de manipuladores de alimentos».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0448,documentos,req.CARNE_SANIDAD = True,docs.CARNE_SANIDAD = Pago de la tasa,Documento habitual para «Carné de sanidad de manipuladores de alimentos».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0449,documentos,req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Solicitud al área de salud municipal,Documento habitual para «Inspección/autorización sanitaria del establecimiento».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0450,documentos,req.INSPECCION_SANITARIA = 

True,docs.INSPECCION_SANITARIA = Croquis del establecimiento,Documento habitual para «Inspección/autorización sanitaria del establecimiento».,D.S. 00798-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0451,documentos,req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Certificados de fumigación y de limpieza de tanque,Documento habitual para «Inspección/autorización sanitaria del establecimiento».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0452,documentos,req.INSPECCION_SANITARIA = 

True,docs.INSPECCION_SANITARIA = Pago de la tasa,Documento habitual para «Inspección/autorización sanitaria del establecimiento».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0453,documentos,req.REGISTRO_SANITARIO_DIGESA = True,docs.REGISTRO_SANITARIO_DIGESA = Solicitud,Documento habitual para «Registro sanitario de alimentos y bebidas envasados».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0454,documentos,req.REGISTRO_SANITARIO_DIGESA = 

True,docs.REGISTRO_SANITARIO_DIGESA = Ficha técnica y proceso de elaboración,Documento habitual para «Registro sanitario de alimentos y bebidas envasados».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0455,documentos,req.REGISTRO_SANITARIO_DIGESA = 

True,docs.REGISTRO_SANITARIO_DIGESA = Informe de ensayo de laboratorio acreditado,Documento habitual para «Registro sanitario de alimentos y bebidas envasados».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0456,documentos,req.REGISTRO_SANITARIO_DIGESA = 

True,docs.REGISTRO_SANITARIO_DIGESA = Proyecto de rotulado,Documento habitual para «Registro sanitario de alimentos y bebidas envasados».,D.S. 007-98- 

SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0457,documentos,req.REGISTRO_SANITARIO_DIGESA = True,docs.REGISTRO_SANITARIO_DIGESA = Pago de la tasa,Documento habitual para «Registro sanitario de alimentos y bebidas envasados».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R0458,documentos,req.AUTORIZ_BOTICA = True,docs.AUTORIZ_BOTICA = Solicitud a la autoridad regional de medicamentos,Documento habitual para «Autorización sanitaria de botica/farmacia y director técnico».,Ley 29459 (Productos Farmacéuticos) y D.S. 014-2011-SA -- contrastar con TUPA 

R0459,documentos,req.AUTORIZ_BOTICA = True,docs.AUTORIZ_BOTICA = Director técnico químico-farmacéutico (colegiatura y habilidad),Documento habitual para «Autorización sanitaria de botica/farmacia y director técnico».,Ley 29459 (Productos Farmacéuticos) y D.S. 014-2011-SA -- contrastar con TUPA 

R0460,documentos,req.AUTORIZ_BOTICA = True,docs.AUTORIZ_BOTICA = Planos y descripción del establecimiento,Documento habitual para «Autorización sanitaria de botica/farmacia y director técnico».,Ley 29459 (Productos Farmacéuticos) y D.S. 014-2011-SA -- contrastar con TUPA 

R0461,documentos,req.AUTORIZ_BOTICA = True,docs.AUTORIZ_BOTICA = Cumplimiento de Buenas Prácticas de Oficina Farmacéutica,Documento habitual para «Autorización sanitaria de botica/farmacia y director técnico».,Ley 29459 (Productos Farmacéuticos) y D.S. 014-2011-SA -- contrastar con TUPA 

R0462,documentos,req.REG_PLAGUICIDAS = True,docs.REG_PLAGUICIDAS = Solicitud a SENASA,Documento habitual para «Registro de establecimiento de venta de plaguicidas».,Reglamento del Sistema Nacional de Plaguicidas Agrícolas (SENASA) -- contrastar con TUPA 

R0463,documentos,req.REG_PLAGUICIDAS = True,docs.REG_PLAGUICIDAS = Responsable técnico,Documento habitual para «Registro de establecimiento de venta de plaguicidas».,Reglamento del Sistema Nacional de Plaguicidas Agrícolas (SENASA) -- contrastar con TUPA 

R0464,documentos,req.REG_PLAGUICIDAS = True,docs.REG_PLAGUICIDAS = Descripción del local y almacenamiento seguro,Documento habitual para «Registro de establecimiento de venta de plaguicidas».,Reglamento del Sistema Nacional de Plaguicidas Agrícolas (SENASA) -- contrastar con TUPA 

R0465,documentos,req.REG_HOSPEDAJE = True,docs.REG_HOSPEDAJE = Declaración jurada de clasificación/categoría,Documento habitual para 

«Registro/clasificación del establecimiento de hospedaje».,D.S. 001-2015MINCETUR (Reglamento de establecimientos de hospedaje) -- contrastar con TUPA 

R0466,documentos,req.REG_HOSPEDAJE = True,docs.REG_HOSPEDAJE = Licencia de funcionamiento,Documento habitual para «Registro/clasificación del establecimiento de hospedaje».,D.S. 001-2015-MINCETUR (Reglamento de establecimientos de hospedaje) -- contrastar con TUPA 

R0467,documentos,req.REG_HOSPEDAJE = True,docs.REG_HOSPEDAJE = Planos y número de habitaciones,Documento habitual para «Registro/clasificación del establecimiento de hospedaje».,D.S. 001-2015-MINCETUR (Reglamento de establecimientos de hospedaje) -- contrastar con TUPA 

R0468,documentos,req.REG_HOSPEDAJE = True,docs.REG_HOSPEDAJE = Libro/registro de huéspedes,Documento habitual para «Registro/clasificación del establecimiento de hospedaje».,D.S. 001-2015-MINCETUR (Reglamento de establecimientos de hospedaje) -- contrastar con TUPA 

R0469,documentos,req.REG_AGENCIA_VIAJES = True,docs.REG_AGENCIA_VIAJES = Solicitud a DIRCETUR,Documento habitual para «Registro de agencia de viajes y turismo».,Reglamento de agencias de viajes y turismo (MINCETUR) -- contrastar con TUPA 

R0470,documentos,req.REG_AGENCIA_VIAJES = True,docs.REG_AGENCIA_VIAJES = Licencia de funcionamiento,Documento habitual para «Registro de agencia de viajes y turismo».,Reglamento de agencias de viajes y turismo (MINCETUR) -- contrastar con TUPA 

R0471,documentos,req.REG_AGENCIA_VIAJES = True,docs.REG_AGENCIA_VIAJES = Requisitos del reglamento de agencias de viajes,Documento habitual para «Registro de agencia de viajes y turismo».,Reglamento de agencias de viajes y turismo (MINCETUR) -- contrastar con TUPA 

R0472,documentos,req.LICENCIA_FUNCIONAMIENTO = 

True,docs.LICENCIA_FUNCIONAMIENTO = Solicitud con carácter de declaración jurada,Documento habitual para «Licencia de funcionamiento».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0473,documentos,req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Copia del RUC,Documento habitual para «Licencia de funcionamiento».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0474,documentos,req.LICENCIA_FUNCIONAMIENTO = 

True,docs.LICENCIA_FUNCIONAMIENTO = DNI o vigencia de poder del 

representante (persona jurídica),Documento habitual para «Licencia de funcionamiento».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0475,documentos,req.LICENCIA_FUNCIONAMIENTO = 

True,docs.LICENCIA_FUNCIONAMIENTO = Declaración jurada de condiciones de seguridad o certificado ITSE según riesgo,Documento habitual para «Licencia de funcionamiento».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0476,documentos,req.LICENCIA_FUNCIONAMIENTO = 

True,docs.LICENCIA_FUNCIONAMIENTO = Pago de la tasa,Documento habitual para «Licencia de funcionamiento».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R0477,documentos,req.AUTORIZ_ALCOHOL = True,docs.AUTORIZ_ALCOHOL = Solicitud municipal,Documento habitual para «Autorización municipal para venta de bebidas alcohólicas».,Ley 28681 (bebidas alcohólicas) y ordenanza municipal - - contrastar con TUPA 

R0478,documentos,req.AUTORIZ_ALCOHOL = True,docs.AUTORIZ_ALCOHOL = Licencia de funcionamiento con el giro autorizado,Documento habitual para «Autorización municipal para venta de bebidas alcohólicas».,Ley 28681 (bebidas alcohólicas) y ordenanza municipal -- contrastar con TUPA 

R0479,documentos,req.AUTORIZ_ALCOHOL = True,docs.AUTORIZ_ALCOHOL = Cumplir horarios y distancias de la ordenanza,Documento habitual para «Autorización municipal para venta de bebidas alcohólicas».,Ley 28681 (bebidas alcohólicas) y ordenanza municipal -- contrastar con TUPA 

R0480,documentos,req.AUTORIZ_ANUNCIO = True,docs.AUTORIZ_ANUNCIO = Solicitud,Documento habitual para «Autorización de anuncio/letrero publicitario».,Ordenanza municipal de anuncios y avisos publicitarios -- contrastar con TUPA 

R0481,documentos,req.AUTORIZ_ANUNCIO = True,docs.AUTORIZ_ANUNCIO = Diseño y medidas del anuncio,Documento habitual para «Autorización de anuncio/letrero publicitario».,Ordenanza municipal de anuncios y avisos publicitarios -- contrastar con TUPA 

R0482,documentos,req.AUTORIZ_ANUNCIO = True,docs.AUTORIZ_ANUNCIO = Autorización del propietario del inmueble,Documento habitual para «Autorización de anuncio/letrero publicitario».,Ordenanza municipal de anuncios y avisos publicitarios -- contrastar con TUPA 

R0483,documentos,req.LIBRO_RECLAMACIONES = True,docs.LIBRO_RECLAMACIONES = Libro físico o virtual,Documento habitual para «Libro de Reclamaciones (físico o virtual)».,Ley 29571 (Código de Protección y Defensa del Consumidor) -- contrastar con TUPA 

R0484,documentos,req.LIBRO_RECLAMACIONES = True,docs.LIBRO_RECLAMACIONES = Aviso visible sobre la existencia del libro,Documento habitual para «Libro de Reclamaciones (físico o virtual)».,Ley 29571 (Código de Protección y Defensa del Consumidor) -- contrastar con TUPA 

R0485,documentos,req.LIBRO_RECLAMACIONES = True,docs.LIBRO_RECLAMACIONES = Hoja de reclamación conforme al reglamento,Documento habitual para «Libro de Reclamaciones (físico o virtual)».,Ley 29571 (Código de Protección y Defensa del Consumidor) -- contrastar con TUPA 

R0486,documentos,req.REMYPE = True,docs.REMYPE = RUC y Clave SOL,Documento habitual para «Inscripción en el REMYPE».,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- contrastar con TUPA 

R0487,documentos,req.REMYPE = True,docs.REMYPE = Declaración jurada de ser MYPE,Documento habitual para «Inscripción en el REMYPE».,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- contrastar con TUPA 

R0488,documentos,req.REMYPE = True,docs.REMYPE = Al menos un trabajador registrado en T-Registro,Documento habitual para «Inscripción en el REMYPE».,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- contrastar con TUPA 

R0489,documentos,req.CONTRATOS_LABORALES = 

True,docs.CONTRATOS_LABORALES = Contrato escrito según la modalidad,Documento habitual para «Contratos de trabajo y boletas de pago».,D.S. 003-97-TR (TUO de la Ley de Productividad y Competitividad Laboral) -- contrastar con TUPA 

R0490,documentos,req.CONTRATOS_LABORALES = 

True,docs.CONTRATOS_LABORALES = Boletas de pago mensuales,Documento habitual para «Contratos de trabajo y boletas de pago».,D.S. 003-97-TR (TUO de la Ley de Productividad y Competitividad Laboral) -- contrastar con TUPA 

R0491,documentos,req.CONTRATOS_LABORALES = True,docs.CONTRATOS_LABORALES = Registro del contrato en el MTPE si es modal,Documento habitual para «Contratos de trabajo y boletas de pago».,D.S. 003-97-TR (TUO de la Ley de Productividad y Competitividad Laboral) -- contrastar con TUPA 

R0492,documentos,req.T_REGISTRO = True,docs.T_REGISTRO = Clave SOL,Documento habitual para «Registro de trabajadores en T-Registro/PLAME y EsSalud».,D.S. 018-2007-TR (T-Registro y PLAME) -- contrastar con TUPA 

R0493,documentos,req.T_REGISTRO = True,"docs.T_REGISTRO = Datos de cada trabajador (DNI, fecha de ingreso, remuneración)",Documento habitual para «Registro de trabajadores en T-Registro/PLAME y EsSalud».,D.S. 018-2007-TR (TRegistro y PLAME) -- contrastar con TUPA 

R0494,documentos,req.T_REGISTRO = True,docs.T_REGISTRO = Alta en PLAME / planilla electrónica,Documento habitual para «Registro de trabajadores en T- Registro/PLAME y EsSalud».,D.S. 018-2007-TR (T-Registro y PLAME) -- contrastar con TUPA 

R0495,documentos,req.SST_BASICO = True,docs.SST_BASICO = Política de seguridad y salud,Documento habitual para «Sistema básico de seguridad y salud en el trabajo».,Ley 29783 (Seguridad y Salud en el Trabajo) -- contrastar con TUPA 

R0496,documentos,req.SST_BASICO = True,docs.SST_BASICO = Matriz IPERC,Documento habitual para «Sistema básico de seguridad y salud en el trabajo».,Ley 29783 (Seguridad y Salud en el Trabajo) -- contrastar con TUPA 

R0497,documentos,req.SST_BASICO = True,docs.SST_BASICO = Registro de inducción y capacitaciones,Documento habitual para «Sistema básico de seguridad y salud en el trabajo».,Ley 29783 (Seguridad y Salud en el Trabajo) -- contrastar con TUPA 

R0498,documentos,req.SCTR = True,docs.SCTR = Contratar con EsSalud o aseguradora privada,Documento habitual para «Seguro complementario de trabajo de riesgo (SCTR)».,Ley 26790 y D.S. 003-98-SA (SCTR) -- contrastar con TUPA 

R0499,documentos,req.SCTR = True,docs.SCTR = Lista de trabajadores en actividad de riesgo,Documento habitual para «Seguro complementario de trabajo de riesgo (SCTR)».,Ley 26790 y D.S. 003-98-SA (SCTR) -- contrastar con TUPA 

R0500,documentos,req.LIBROS_CONTABLES = True,docs.LIBROS_CONTABLES = Registro de ventas e ingresos,Documento habitual para «Llevar libros y registros contables según el régimen».,R.S. 234-2006/SUNAT (libros y registros vinculados a asuntos tributarios) -- contrastar con TUPA 

R0501,documentos,req.LIBROS_CONTABLES = True,docs.LIBROS_CONTABLES = Registro de compras,Documento habitual para «Llevar libros y registros contables según el régimen».,R.S. 234-2006/SUNAT (libros y registros vinculados a asuntos tributarios) -- contrastar con TUPA 

R0502,documentos,req.LIBROS_CONTABLES = True,docs.LIBROS_CONTABLES = Libro diario/mayor si el régimen lo exige,Documento habitual para «Llevar libros y registros contables según el régimen».,R.S. 234-2006/SUNAT (libros y registros vinculados a asuntos tributarios) -- contrastar con TUPA 

R0503,documentos,req.DECLARACION_MENSUAL = True,docs.DECLARACION_MENSUAL = Calendario de vencimientos SUNAT,Documento habitual para «Declarar y pagar impuestos mensualmente».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R0504,documentos,req.DECLARACION_MENSUAL = True,docs.DECLARACION_MENSUAL = Declaración y pago con Clave SOL,Documento habitual para «Declarar y pagar impuestos mensualmente».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R0505,documentos,req.REG_MARCA = True,docs.REG_MARCA = Búsqueda de antecedentes fonéticos y figurativos,Documento habitual para «Registro de marca (recomendado)».,D.Leg. 1075 y Decisión Andina 486 (propiedad industrial) -- contrastar con TUPA 

R0506,documentos,req.REG_MARCA = True,docs.REG_MARCA = Solicitud de registro en INDECOPI,Documento habitual para «Registro de marca (recomendado)».,D.Leg. 1075 y Decisión Andina 486 (propiedad industrial) -- contrastar con TUPA 

R0507,documentos,req.REG_MARCA = True,docs.REG_MARCA = Pago de la tasa,Documento habitual para «Registro de marca (recomendado)».,D.Leg. 1075 y Decisión Andina 486 (propiedad industrial) -- contrastar con TUPA 

R0508,documentos,req.REG_ARTESANO = True,docs.REG_ARTESANO = Solicitud ante la autoridad competente,Documento habitual para «Registro Nacional del Artesano (recomendado)».,Ley 29073 (Ley del Artesano) -- contrastar con TUPA 

R0509,documentos,req.REG_ARTESANO = True,docs.REG_ARTESANO = Declaración de actividad artesanal,Documento habitual para «Registro Nacional del Artesano (recomendado)».,Ley 29073 (Ley del Artesano) -- contrastar con TUPA 

R0510,documentos,req.REG_ARTESANO = True,docs.REG_ARTESANO = Fotografías o muestras de la producción,Documento habitual para «Registro Nacional del Artesano (recomendado)».,Ley 29073 (Ley del Artesano) -- contrastar con TUPA 

R0511,avisos,rubro = restaurante,"avisos = [Restaurante / cevichería / menú] Aplique Buenas Prácticas de Manipulación, higiene del personal y un programa de 

limpieza y desinfección; conserve certificados de fumigación y limpieza de tanque.",Obligación o buena práctica propia del giro (BPM).,Normativa sectorial -- validar con el experto 

R0512,avisos,rubro = restaurante,avisos = [Restaurante / cevichería / menú] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0513,avisos,rubro = restaurante,avisos = [Restaurante / cevichería / menú] Mantenga la cadena de frío y lleve un registro de temperaturas de refrigeración/congelación.,Obligación o buena práctica propia del giro (cadena_frio).,Normativa sectorial -- validar con el experto 

R0514,avisos,rubro = restaurante,avisos = [Restaurante / cevichería / menú] Controle ruido y emisiones según la ordenanza municipal; puede restringirse el horario o la zona.,Obligación o buena práctica propia del giro (ruido).,Normativa sectorial -- validar con el experto 

R0515,avisos,rubro = restaurante Y trabajadores = t1,"avisos = [Restaurante / cevichería / menú] Peligros típicos: quemaduras, cortes e incendio por gas. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0516,avisos,rubro = restaurante Y trabajadores = t2,"avisos = [Restaurante / cevichería / menú] Peligros típicos: quemaduras, cortes e incendio por gas. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0517,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = restaurante Y area = a2","avisos = [Restaurante / cevichería / menú] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0518,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = restaurante Y area = a3","avisos = [Restaurante / cevichería / menú] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0519,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = restaurante Y nivel_riesgo = bajo","avisos = [Restaurante / cevichería / 

menú / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: quemaduras, cortes e incendio por gas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0520,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = restaurante Y nivel_riesgo = medio","avisos = [Restaurante / cevichería / menú / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: quemaduras, cortes e incendio por gas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0521,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = restaurante Y nivel_riesgo = alto","avisos = [Restaurante / cevichería / menú / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: quemaduras, cortes e incendio por gas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0522,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = restaurante Y nivel_riesgo = muy_alto","avisos = [Restaurante / cevichería / menú / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: quemaduras, cortes e incendio por gas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0523,avisos,rubro = restaurante Y local = propio,avisos = [Restaurante / cevichería / menú / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0524,avisos,rubro = restaurante Y local = alquilado,avisos = [Restaurante / cevichería / menú / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0525,avisos,rubro = restaurante Y local = domicilio,avisos = [Restaurante / cevichería / menú / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0526,avisos,rubro = restaurante Y local = mercado,avisos = [Restaurante / cevichería / menú / puesto en mercado o galería] Pida la constancia de 

conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0527,avisos,rubro = restaurante Y local = ambulante,avisos = [Restaurante / cevichería / menú / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0528,avisos,rubro = restaurante Y local = ninguno_aun,"avisos = [Restaurante / cevichería / menú / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0529,avisos,rubro = restaurante Y persona = natural,"avisos = [Restaurante / cevichería / menú] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0530,avisos,rubro = restaurante Y persona = juridica,avisos = [Restaurante / cevichería / menú] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0531,avisos,rubro = polleria,"avisos = [Pollería / parrilla] Aplique Buenas Prácticas de Manipulación, higiene del personal y un programa de limpieza y desinfección; conserve certificados de fumigación y limpieza de tanque.",Obligación o buena práctica propia del giro (BPM).,Normativa sectorial -- validar con el experto 

R0532,avisos,rubro = polleria,avisos = [Pollería / parrilla] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0533,avisos,rubro = polleria,avisos = [Pollería / parrilla] Mantenga la cadena de frío y lleve un registro de temperaturas de refrigeración/congelación.,Obligación o buena práctica propia del giro (cadena_frio).,Normativa sectorial -- validar con el experto 

R0534,avisos,rubro = polleria,avisos = [Pollería / parrilla] Controle ruido y emisiones según la ordenanza municipal; puede restringirse el horario o la zona.,Obligación o buena práctica propia del giro (ruido).,Normativa sectorial -- validar con el experto 

R0535,avisos,rubro = polleria Y trabajadores = t1,"avisos = [Pollería / parrilla] Peligros típicos: incendio por gas y grasas, quemaduras. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0536,avisos,rubro = polleria Y trabajadores = t2,"avisos = [Pollería / parrilla] Peligros típicos: incendio por gas y grasas, quemaduras. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0537,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = polleria Y area = a2","avisos = [Pollería / parrilla] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0538,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = polleria Y area = a3","avisos = [Pollería / parrilla] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0539,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = polleria Y nivel_riesgo = bajo","avisos = [Pollería / parrilla / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: incendio por gas y grasas, quemaduras.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0540,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = polleria Y nivel_riesgo = medio","avisos = [Pollería / parrilla / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: incendio por gas y grasas, quemaduras.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0541,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = polleria Y nivel_riesgo = alto","avisos = [Pollería / parrilla / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: incendio por gas y 

grasas, quemaduras.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0542,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = polleria Y nivel_riesgo = muy_alto","avisos = [Pollería / parrilla / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: incendio por gas y grasas, quemaduras.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0543,avisos,rubro = polleria Y local = propio,avisos = [Pollería / parrilla / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0544,avisos,rubro = polleria Y local = alquilado,avisos = [Pollería / parrilla / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0545,avisos,rubro = polleria Y local = domicilio,avisos = [Pollería / parrilla / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0546,avisos,rubro = polleria Y local = mercado,avisos = [Pollería / parrilla / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0547,avisos,rubro = polleria Y local = ambulante,avisos = [Pollería / parrilla / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0548,avisos,rubro = polleria Y local = ninguno_aun,"avisos = [Pollería / parrilla / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0549,avisos,rubro = polleria Y persona = natural,"avisos = [Pollería / parrilla] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0550,avisos,rubro = polleria Y persona = juridica,avisos = [Pollería / parrilla] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0551,avisos,rubro = cafeteria,"avisos = [Cafetería / juguería / snack] Aplique Buenas Prácticas de Manipulación, higiene del personal y un programa de limpieza y desinfección; conserve certificados de fumigación y limpieza de tanque.",Obligación o buena práctica propia del giro (BPM).,Normativa sectorial -- validar con el experto 

R0552,avisos,rubro = cafeteria,avisos = [Cafetería / juguería / snack] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0553,avisos,rubro = cafeteria Y trabajadores = t1,avisos = [Cafetería / juguería / snack] Peligros típicos: quemaduras y resbalones. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0554,avisos,rubro = cafeteria Y trabajadores = t2,avisos = [Cafetería / juguería / snack] Peligros típicos: quemaduras y resbalones. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0555,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = cafeteria Y area = a2","avisos = [Cafetería / juguería / snack] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0556,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = cafeteria Y area = a3","avisos = [Cafetería / juguería / snack] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0557,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = cafeteria Y nivel_riesgo = bajo","avisos = [Cafetería / juguería / snack / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: quemaduras y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0558,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = cafeteria Y nivel_riesgo = medio","avisos = [Cafetería / juguería / snack / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: quemaduras y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0559,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = cafeteria Y nivel_riesgo = alto","avisos = [Cafetería / juguería / snack / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: quemaduras y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0560,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = cafeteria Y nivel_riesgo = muy_alto","avisos = [Cafetería / juguería / snack / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: quemaduras y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0561,avisos,rubro = cafeteria Y local = propio,avisos = [Cafetería / juguería / snack / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0562,avisos,rubro = cafeteria Y local = alquilado,avisos = [Cafetería / juguería / snack / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0563,avisos,rubro = cafeteria Y local = domicilio,avisos = [Cafetería / juguería / snack / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0564,avisos,rubro = cafeteria Y local = mercado,avisos = [Cafetería / juguería / snack / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0565,avisos,rubro = cafeteria Y local = ambulante,"avisos = [Cafetería / juguería / snack / ambulante (sin local fijo)] Necesita autorización municipal de comercio ambulatorio, solo en zonas y horarios permitidos; no se tramita licencia de funcionamiento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0566,avisos,rubro = cafeteria Y local = ninguno_aun,"avisos = [Cafetería / juguería / snack / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0567,avisos,rubro = cafeteria Y persona = natural,"avisos = [Cafetería / juguería / snack] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0568,avisos,rubro = cafeteria Y persona = juridica,avisos = [Cafetería / juguería / snack] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0569,avisos,rubro = panaderia,"avisos = [Panadería / pastelería] Aplique Buenas Prácticas de Manipulación, higiene del personal y un programa de limpieza y desinfección; conserve certificados de fumigación y limpieza de tanque.",Obligación o buena práctica propia del giro (BPM).,Normativa sectorial -- validar con el experto 

R0570,avisos,rubro = panaderia,avisos = [Panadería / pastelería] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0571,avisos,rubro = panaderia,avisos = [Panadería / pastelería] Controle ruido y emisiones según la ordenanza municipal; puede restringirse el horario o la zona.,Obligación o buena práctica propia del giro (ruido).,Normativa sectorial -- validar con el experto 

R0572,avisos,rubro = panaderia Y trabajadores = t1,"avisos = [Panadería / pastelería] Peligros típicos: hornos: quemaduras, incendio, polvo de harina. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0573,avisos,rubro = panaderia Y trabajadores = t2,"avisos = [Panadería / pastelería] Peligros típicos: hornos: quemaduras, incendio, polvo de harina. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0574,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = panaderia Y area = a2","avisos = [Panadería / pastelería] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0575,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = panaderia Y area = a3","avisos = [Panadería / pastelería] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0576,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = panaderia Y nivel_riesgo = bajo","avisos = [Panadería / pastelería / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: hornos: quemaduras, incendio, polvo de harina.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0577,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = panaderia Y nivel_riesgo = medio","avisos = [Panadería / pastelería / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: hornos: quemaduras, incendio, polvo de harina.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0578,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = panaderia Y nivel_riesgo = alto","avisos = [Panadería / pastelería / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: hornos: quemaduras, incendio, polvo de harina.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0579,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = panaderia Y nivel_riesgo = muy_alto","avisos = [Panadería / pastelería / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: hornos: quemaduras, incendio, polvo de harina.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0580,avisos,rubro = panaderia Y local = propio,avisos = [Panadería / pastelería / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0581,avisos,rubro = panaderia Y local = alquilado,avisos = [Panadería / pastelería / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0582,avisos,rubro = panaderia Y local = domicilio,avisos = [Panadería / pastelería / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0583,avisos,rubro = panaderia Y local = mercado,avisos = [Panadería / pastelería / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0584,avisos,rubro = panaderia Y local = ambulante,avisos = [Panadería / pastelería / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0585,avisos,rubro = panaderia Y local = ninguno_aun,"avisos = [Panadería / pastelería / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0586,avisos,rubro = panaderia Y persona = natural,"avisos = [Panadería / pastelería] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad 

según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0587,avisos,rubro = panaderia Y persona = juridica,avisos = [Panadería / pastelería] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0588,avisos,rubro = bodega,avisos = [Bodega / tienda de abarrotes] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0589,avisos,rubro = bodega,avisos = [Bodega / tienda de abarrotes] Mantenga la cadena de frío y lleve un registro de temperaturas de refrigeración/congelación.,Obligación o buena práctica propia del giro (cadena_frio).,Normativa sectorial -- validar con el experto 

R0590,avisos,rubro = bodega Y trabajadores = t1,avisos = [Bodega / tienda de abarrotes] Peligros típicos: caídas y manipulación manual de cargas. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0591,avisos,rubro = bodega Y trabajadores = t2,avisos = [Bodega / tienda de abarrotes] Peligros típicos: caídas y manipulación manual de cargas. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0592,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = bodega Y area = a2","avisos = [Bodega / tienda de abarrotes] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0593,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = bodega Y area = a3","avisos = [Bodega / tienda de abarrotes] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0594,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = bodega Y nivel_riesgo = bajo","avisos = [Bodega / tienda de abarrotes / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y 

botiquín. Peligros del giro: caídas y manipulación manual de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0595,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = bodega Y nivel_riesgo = medio","avisos = [Bodega / tienda de abarrotes / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: caídas y manipulación manual de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0596,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = bodega Y nivel_riesgo = alto","avisos = [Bodega / tienda de abarrotes / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: caídas y manipulación manual de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0597,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = bodega Y nivel_riesgo = muy_alto","avisos = [Bodega / tienda de abarrotes / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: caídas y manipulación manual de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0598,avisos,rubro = bodega Y local = propio,avisos = [Bodega / tienda de abarrotes / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0599,avisos,rubro = bodega Y local = alquilado,avisos = [Bodega / tienda de abarrotes / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0600,avisos,rubro = bodega Y local = domicilio,avisos = [Bodega / tienda de abarrotes / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0601,avisos,rubro = bodega Y local = mercado,avisos = [Bodega / tienda de abarrotes / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la 

combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0602,avisos,rubro = bodega Y local = ambulante,avisos = [Bodega / tienda de abarrotes / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0603,avisos,rubro = bodega Y local = ninguno_aun,"avisos = [Bodega / tienda de abarrotes / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0604,avisos,rubro = bodega Y persona = natural,"avisos = [Bodega / tienda de abarrotes] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0605,avisos,rubro = bodega Y persona = juridica,avisos = [Bodega / tienda de abarrotes] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0606,avisos,rubro = minimarket,avisos = [Minimarket / autoservicio] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0607,avisos,rubro = minimarket,avisos = [Minimarket / autoservicio] Mantenga la cadena de frío y lleve un registro de temperaturas de refrigeración/congelación.,Obligación o buena práctica propia del giro (cadena_frio).,Normativa sectorial -- validar con el experto 

R0608,avisos,rubro = minimarket Y trabajadores = t1,"avisos = [Minimarket / autoservicio] Peligros típicos: caídas, cargas e incendio. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0609,avisos,rubro = minimarket Y trabajadores = t2,"avisos = [Minimarket / autoservicio] Peligros típicos: caídas, cargas e incendio. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 

29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0610,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = minimarket Y area = a2","avisos = [Minimarket / autoservicio] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0611,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = minimarket Y area = a3","avisos = [Minimarket / autoservicio] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0612,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = minimarket Y nivel_riesgo = bajo","avisos = [Minimarket / autoservicio / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: caídas, cargas e incendio.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0613,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = minimarket Y nivel_riesgo = medio","avisos = [Minimarket / autoservicio / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: caídas, cargas e incendio.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0614,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = minimarket Y nivel_riesgo = alto","avisos = [Minimarket / autoservicio / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: caídas, cargas e incendio.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0615,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = minimarket Y nivel_riesgo = muy_alto","avisos = [Minimarket / autoservicio / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: caídas, cargas e incendio.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0616,avisos,rubro = minimarket Y local = propio,avisos = [Minimarket / autoservicio / local propio] Tenga a mano el título o partida registral y revise cargas 

y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0617,avisos,rubro = minimarket Y local = alquilado,avisos = [Minimarket / autoservicio / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0618,avisos,rubro = minimarket Y local = domicilio,avisos = [Minimarket / autoservicio / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0619,avisos,rubro = minimarket Y local = mercado,avisos = [Minimarket / autoservicio / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0620,avisos,rubro = minimarket Y local = ambulante,avisos = [Minimarket / autoservicio / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0621,avisos,rubro = minimarket Y local = ninguno_aun,"avisos = [Minimarket / autoservicio / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0622,avisos,rubro = minimarket Y persona = natural,"avisos = [Minimarket / autoservicio] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0623,avisos,rubro = minimarket Y persona = juridica,avisos = [Minimarket / autoservicio] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0624,avisos,rubro = pescaderia,"avisos = [Pescadería / venta de mariscos] Aplique Buenas Prácticas de Manipulación, higiene del personal y un programa de limpieza y desinfección; conserve certificados de fumigación y limpieza de tanque.",Obligación o buena práctica propia del giro (BPM).,Normativa sectorial -- validar con el experto 

R0625,avisos,rubro = pescaderia,avisos = [Pescadería / venta de mariscos] Mantenga la cadena de frío y lleve un registro de temperaturas de refrigeración/congelación.,Obligación o buena práctica propia del giro (cadena_frio).,Normativa sectorial -- validar con el experto 

R0626,avisos,rubro = pescaderia,avisos = [Pescadería / venta de mariscos] Compre productos hidrobiológicos solo a proveedores con habilitación sanitaria de SANIPES y conserve comprobantes de compra (trazabilidad).,Obligación o buena práctica propia del giro (pesca).,Normativa sectorial -- validar con el experto 

R0627,avisos,rubro = pescaderia,avisos = [Pescadería / venta de mariscos] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0628,avisos,rubro = pescaderia Y trabajadores = t1,"avisos = [Pescadería / venta de mariscos] Peligros típicos: cortes, resbalones y frío. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0629,avisos,rubro = pescaderia Y trabajadores = t2,"avisos = [Pescadería / venta de mariscos] Peligros típicos: cortes, resbalones y frío. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0630,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = pescaderia Y area = a2","avisos = [Pescadería / venta de mariscos] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0631,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = pescaderia Y area = a3","avisos = [Pescadería / venta de mariscos] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0632,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = pescaderia Y nivel_riesgo = bajo","avisos = [Pescadería / venta de mariscos / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: cortes, resbalones y frío.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0633,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = pescaderia Y nivel_riesgo = medio","avisos = [Pescadería / venta de mariscos / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: cortes, resbalones y frío.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0634,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = pescaderia Y nivel_riesgo = alto","avisos = [Pescadería / venta de mariscos / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: cortes, resbalones y frío.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0635,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = pescaderia Y nivel_riesgo = muy_alto","avisos = [Pescadería / venta de mariscos / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: cortes, resbalones y frío.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0636,avisos,rubro = pescaderia Y local = propio,avisos = [Pescadería / venta de mariscos / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0637,avisos,rubro = pescaderia Y local = alquilado,avisos = [Pescadería / venta de mariscos / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0638,avisos,rubro = pescaderia Y local = domicilio,avisos = [Pescadería / venta de mariscos / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0639,avisos,rubro = pescaderia Y local = mercado,avisos = [Pescadería / venta de mariscos / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0640,avisos,rubro = pescaderia Y local = ambulante,avisos = [Pescadería / venta de mariscos / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0641,avisos,rubro = pescaderia Y local = ninguno_aun,"avisos = [Pescadería / venta de mariscos / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0642,avisos,rubro = pescaderia Y persona = natural,"avisos = [Pescadería / venta de mariscos] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0643,avisos,rubro = pescaderia Y persona = juridica,avisos = [Pescadería / venta de mariscos] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0644,avisos,rubro = carniceria,"avisos = [Carnicería / venta de aves] Aplique Buenas Prácticas de Manipulación, higiene del personal y un programa de limpieza y desinfección; conserve certificados de fumigación y limpieza de tanque.",Obligación o buena práctica propia del giro (BPM).,Normativa sectorial -- validar con el experto 

R0645,avisos,rubro = carniceria,avisos = [Carnicería / venta de aves] Mantenga la cadena de frío y lleve un registro de temperaturas de refrigeración/congelación.,Obligación o buena práctica propia del giro (cadena_frio).,Normativa sectorial -- validar con el experto 

R0646,avisos,rubro = carniceria,avisos = [Carnicería / venta de aves] Compre carne solo de camales autorizados (SENASA/municipal) y conserve la guía de transporte y comprobante.,Obligación o buena práctica propia del giro (carne).,Normativa sectorial -- validar con el experto 

R0647,avisos,rubro = carniceria,avisos = [Carnicería / venta de aves] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0648,avisos,rubro = carniceria Y trabajadores = t1,avisos = [Carnicería / venta de aves] Peligros típicos: cortes y resbalones. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0649,avisos,rubro = carniceria Y trabajadores = t2,avisos = [Carnicería / venta de aves] Peligros típicos: cortes y resbalones. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0650,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = carniceria Y area = a2","avisos = [Carnicería / venta de aves] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0651,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = carniceria Y area = a3","avisos = [Carnicería / venta de aves] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0652,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = carniceria Y nivel_riesgo = bajo","avisos = [Carnicería / venta de aves / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: cortes y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0653,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = carniceria Y nivel_riesgo = medio","avisos = [Carnicería / venta de aves / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: cortes y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018PCM (Reglamento de ITSE) 

R0654,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = carniceria Y nivel_riesgo = alto","avisos = [Carnicería / venta de aves / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: cortes y 

resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0655,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = carniceria Y nivel_riesgo = muy_alto","avisos = [Carnicería / venta de aves / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: cortes y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018PCM (Reglamento de ITSE) 

R0656,avisos,rubro = carniceria Y local = propio,avisos = [Carnicería / venta de aves / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0657,avisos,rubro = carniceria Y local = alquilado,avisos = [Carnicería / venta de aves / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0658,avisos,rubro = carniceria Y local = domicilio,avisos = [Carnicería / venta de aves / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0659,avisos,rubro = carniceria Y local = mercado,avisos = [Carnicería / venta de aves / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0660,avisos,rubro = carniceria Y local = ambulante,avisos = [Carnicería / venta de aves / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0661,avisos,rubro = carniceria Y local = ninguno_aun,"avisos = [Carnicería / venta de aves / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0662,avisos,rubro = carniceria Y persona = natural,"avisos = [Carnicería / venta de aves] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0663,avisos,rubro = carniceria Y persona = juridica,avisos = [Carnicería / venta de aves] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0664,avisos,rubro = prod_alimentos,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Aplique Buenas Prácticas de Manipulación, higiene del personal y un programa de limpieza y desinfección; conserve certificados de fumigación y limpieza de tanque.",Obligación o buena práctica propia del giro (BPM).,Normativa sectorial -- validar con el experto 

R0665,avisos,rubro = prod_alimentos,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Cumpla las normas de etiquetado aplicables (alimentos envasados: Ley 30021; textiles y calzado: norma técnica de etiquetado vigente).",Obligación o buena práctica propia del giro (etiquetado).,Normativa sectorial -- validar con el experto 

R0666,avisos,rubro = prod_alimentos,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Considere registrar su marca en INDECOPI antes de invertir en publicidad o empaques.",Obligación o buena práctica propia del giro (marca).,Normativa sectorial -- validar con el experto 

R0667,avisos,rubro = prod_alimentos,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).",Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0668,avisos,rubro = prod_alimentos Y trabajadores = t1,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Peligros típicos: quemaduras, cortes y maquinaria. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0669,avisos,rubro = prod_alimentos Y trabajadores = t2,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Peligros típicos: quemaduras, cortes y maquinaria. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0670,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prod_alimentos Y area = a2","avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0671,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prod_alimentos Y area = a3","avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0672,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prod_alimentos Y nivel_riesgo = bajo","avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: quemaduras, cortes y maquinaria.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0673,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prod_alimentos Y nivel_riesgo = medio","avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: quemaduras, cortes y maquinaria.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0674,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prod_alimentos Y nivel_riesgo = alto","avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: quemaduras, cortes y maquinaria.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0675,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prod_alimentos Y nivel_riesgo = muy_alto","avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: quemaduras, cortes y maquinaria.",La ITSE verifica 

las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0676,avisos,rubro = prod_alimentos Y local = propio,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0677,avisos,rubro = prod_alimentos Y local = alquilado,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0678,avisos,rubro = prod_alimentos Y local = domicilio,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0679,avisos,rubro = prod_alimentos Y local = mercado,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0680,avisos,rubro = prod_alimentos Y local = ambulante,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0681,avisos,rubro = prod_alimentos Y local = ninguno_aun,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0682,avisos,rubro = prod_alimentos Y persona = natural,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe 

constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0683,avisos,rubro = prod_alimentos Y persona = juridica,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.",Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0684,avisos,rubro = molino_arroz,avisos = [Molino / pilado de arroz y granos] Controle ruido y emisiones según la ordenanza municipal; puede restringirse el horario o la zona.,Obligación o buena práctica propia del giro (ruido).,Normativa sectorial -- validar con el experto 

R0685,avisos,rubro = molino_arroz,avisos = [Molino / pilado de arroz y granos] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0686,avisos,rubro = molino_arroz,avisos = [Molino / pilado de arroz y granos] Controle el polvo y mantenga limpias las máquinas: el polvo orgánico/de madera es inflamable.,Obligación o buena práctica propia del giro (polvo).,Normativa sectorial -- validar con el experto 

R0687,avisos,rubro = molino_arroz Y trabajadores = t1,"avisos = [Molino / pilado de arroz y granos] Peligros típicos: maquinaria, polvo y ruido. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0688,avisos,rubro = molino_arroz Y trabajadores = t2,"avisos = [Molino / pilado de arroz y granos] Peligros típicos: maquinaria, polvo y ruido. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0689,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = molino_arroz Y area = a2","avisos = [Molino / pilado de arroz y granos] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0690,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = molino_arroz Y area = a3","avisos = [Molino / pilado de arroz y granos] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de 

emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0691,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = molino_arroz Y nivel_riesgo = bajo","avisos = [Molino / pilado de arroz y granos / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: maquinaria, polvo y ruido.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0692,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = molino_arroz Y nivel_riesgo = medio","avisos = [Molino / pilado de arroz y granos / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: maquinaria, polvo y ruido.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0693,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = molino_arroz Y nivel_riesgo = alto","avisos = [Molino / pilado de arroz y granos / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: maquinaria, polvo y ruido.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0694,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = molino_arroz Y nivel_riesgo = muy_alto","avisos = [Molino / pilado de arroz y granos / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: maquinaria, polvo y ruido.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0695,avisos,rubro = molino_arroz Y local = propio,avisos = [Molino / pilado de arroz y granos / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0696,avisos,rubro = molino_arroz Y local = alquilado,avisos = [Molino / pilado de arroz y granos / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0697,avisos,rubro = molino_arroz Y local = domicilio,avisos = [Molino / pilado de arroz y granos / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida 

antes el certificado de zonificación.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0698,avisos,rubro = molino_arroz Y local = mercado,avisos = [Molino / pilado de arroz y granos / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0699,avisos,rubro = molino_arroz Y local = ambulante,avisos = [Molino / pilado de arroz y granos / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0700,avisos,rubro = molino_arroz Y local = ninguno_aun,"avisos = [Molino / pilado de arroz y granos / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0701,avisos,rubro = molino_arroz Y persona = natural,"avisos = [Molino / pilado de arroz y granos] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0702,avisos,rubro = molino_arroz Y persona = juridica,avisos = [Molino / pilado de arroz y granos] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0703,avisos,rubro = ropa,avisos = [Venta de ropa y calzado] Cumpla las normas de etiquetado aplicables (alimentos envasados: Ley 30021; textiles y calzado: norma técnica de etiquetado vigente).,Obligación o buena práctica propia del giro (etiquetado).,Normativa sectorial -- validar con el experto 

R0704,avisos,rubro = ropa Y trabajadores = t1,avisos = [Venta de ropa y calzado] Peligros típicos: caídas y manipulación de cargas. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0705,avisos,rubro = ropa Y trabajadores = t2,avisos = [Venta de ropa y calzado] Peligros típicos: caídas y manipulación de cargas. Elabore la matriz IPERC y con 20 

o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0706,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ropa Y area = a2","avisos = [Venta de ropa y calzado] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0707,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ropa Y area = a3","avisos = [Venta de ropa y calzado] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0708,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ropa Y nivel_riesgo = bajo","avisos = [Venta de ropa y calzado / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: caídas y manipulación de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0709,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ropa Y nivel_riesgo = medio","avisos = [Venta de ropa y calzado / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: caídas y manipulación de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0710,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ropa Y nivel_riesgo = alto","avisos = [Venta de ropa y calzado / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: caídas y manipulación de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0711,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ropa Y nivel_riesgo = muy_alto","avisos = [Venta de ropa y calzado / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: caídas y manipulación de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0712,avisos,rubro = ropa Y local = propio,avisos = [Venta de ropa y calzado / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del 

predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0713,avisos,rubro = ropa Y local = alquilado,avisos = [Venta de ropa y calzado / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0714,avisos,rubro = ropa Y local = domicilio,avisos = [Venta de ropa y calzado / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0715,avisos,rubro = ropa Y local = mercado,avisos = [Venta de ropa y calzado / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0716,avisos,rubro = ropa Y local = ambulante,"avisos = [Venta de ropa y calzado / ambulante (sin local fijo)] Necesita autorización municipal de comercio ambulatorio, solo en zonas y horarios permitidos; no se tramita licencia de funcionamiento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0717,avisos,rubro = ropa Y local = ninguno_aun,"avisos = [Venta de ropa y calzado / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0718,avisos,rubro = ropa Y persona = natural,"avisos = [Venta de ropa y calzado] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0719,avisos,rubro = ropa Y persona = juridica,avisos = [Venta de ropa y calzado] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0720,avisos,rubro = ferreteria,avisos = [Ferretería / materiales de construcción] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión 

Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0721,avisos,rubro = ferreteria,"avisos = [Ferretería / materiales de construcción] Almacene productos químicos con hojas de seguridad (SDS), envases rotulados y ventilación adecuada.",Obligación o buena práctica propia del giro (quimicos).,Normativa sectorial -- validar con el experto 

R0722,avisos,rubro = ferreteria Y trabajadores = t1,avisos = [Ferretería / materiales de construcción] Peligros típicos: cargas pesadas e incendio por inflamables. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0723,avisos,rubro = ferreteria Y trabajadores = t2,avisos = [Ferretería / materiales de construcción] Peligros típicos: cargas pesadas e incendio por inflamables. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0724,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ferreteria Y area = a2","avisos = [Ferretería / materiales de construcción] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0725,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ferreteria Y area = a3","avisos = [Ferretería / materiales de construcción] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0726,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ferreteria Y nivel_riesgo = bajo","avisos = [Ferretería / materiales de construcción / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: cargas pesadas e incendio por inflamables.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018PCM (Reglamento de ITSE) 

R0727,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ferreteria Y nivel_riesgo = medio","avisos = [Ferretería / materiales de construcción / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: cargas pesadas e incendio por inflamables.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0728,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ferreteria Y nivel_riesgo = alto","avisos = [Ferretería / materiales de construcción / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: cargas pesadas e incendio por inflamables.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0729,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ferreteria Y nivel_riesgo = muy_alto","avisos = [Ferretería / materiales de construcción / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: cargas pesadas e incendio por inflamables.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0730,avisos,rubro = ferreteria Y local = propio,avisos = [Ferretería / materiales de construcción / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0731,avisos,rubro = ferreteria Y local = alquilado,avisos = [Ferretería / materiales de construcción / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0732,avisos,rubro = ferreteria Y local = domicilio,avisos = [Ferretería / materiales de construcción / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0733,avisos,rubro = ferreteria Y local = mercado,avisos = [Ferretería / materiales de construcción / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0734,avisos,rubro = ferreteria Y local = ambulante,avisos = [Ferretería / materiales de construcción / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0735,avisos,rubro = ferreteria Y local = ninguno_aun,"avisos = [Ferretería / materiales de construcción / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0736,avisos,rubro = ferreteria Y persona = natural,"avisos = [Ferretería / materiales de construcción] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0737,avisos,rubro = ferreteria Y persona = juridica,avisos = [Ferretería / materiales de construcción] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0738,avisos,rubro = tecnologia,"avisos = [Venta o reparación de celulares y tecnología] Si guarda datos personales de clientes, cumpla la Ley 29733 (Protección de Datos Personales): consentimiento y medidas de seguridad.",Obligación o buena práctica propia del giro (datos).,Normativa sectorial -- validar con el experto 

R0739,avisos,rubro = tecnologia,avisos = [Venta o reparación de celulares y tecnología] Los residuos de aparatos eléctricos y electrónicos deben entregarse a operadores autorizados (D.S. 009-2019-MINAM).,Obligación o buena práctica propia del giro (raee).,Normativa sectorial -- validar con el experto 

R0740,avisos,rubro = tecnologia Y trabajadores = t1,avisos = [Venta o reparación de celulares y tecnología] Peligros típicos: descargas eléctricas. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0741,avisos,rubro = tecnologia Y trabajadores = t2,avisos = [Venta o reparación de celulares y tecnología] Peligros típicos: descargas eléctricas. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0742,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = tecnologia Y area = a2","avisos = [Venta o reparación de celulares y tecnología] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área 

aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0743,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = tecnologia Y area = a3","avisos = [Venta o reparación de celulares y tecnología] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0744,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = tecnologia Y nivel_riesgo = bajo","avisos = [Venta o reparación de celulares y tecnología / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: descargas eléctricas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0745,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = tecnologia Y nivel_riesgo = medio","avisos = [Venta o reparación de celulares y tecnología / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: descargas eléctricas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0746,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = tecnologia Y nivel_riesgo = alto","avisos = [Venta o reparación de celulares y tecnología / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: descargas eléctricas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0747,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = tecnologia Y nivel_riesgo = muy_alto","avisos = [Venta o reparación de celulares y tecnología / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: descargas eléctricas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0748,avisos,rubro = tecnologia Y local = propio,avisos = [Venta o reparación de celulares y tecnología / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0749,avisos,rubro = tecnologia Y local = alquilado,avisos = [Venta o reparación de celulares y tecnología / local alquilado] Verifique que el contrato autorice el uso 

comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0750,avisos,rubro = tecnologia Y local = domicilio,avisos = [Venta o reparación de celulares y tecnología / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0751,avisos,rubro = tecnologia Y local = mercado,avisos = [Venta o reparación de celulares y tecnología / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0752,avisos,rubro = tecnologia Y local = ambulante,avisos = [Venta o reparación de celulares y tecnología / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0753,avisos,rubro = tecnologia Y local = ninguno_aun,"avisos = [Venta o reparación de celulares y tecnología / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0754,avisos,rubro = tecnologia Y persona = natural,"avisos = [Venta o reparación de celulares y tecnología] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0755,avisos,rubro = tecnologia Y persona = juridica,avisos = [Venta o reparación de celulares y tecnología] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0756,avisos,rubro = libreria,avisos = [Librería / bazar / útiles] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0757,avisos,rubro = libreria Y trabajadores = t1,avisos = [Librería / bazar / útiles] Peligros típicos: caídas e incendio por papel. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0758,avisos,rubro = libreria Y trabajadores = t2,avisos = [Librería / bazar / útiles] Peligros típicos: caídas e incendio por papel. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0759,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = libreria Y area = a2","avisos = [Librería / bazar / útiles] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0760,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = libreria Y area = a3","avisos = [Librería / bazar / útiles] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0761,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = libreria Y nivel_riesgo = bajo","avisos = [Librería / bazar / útiles / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: caídas e incendio por papel.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0762,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = libreria Y nivel_riesgo = medio","avisos = [Librería / bazar / útiles / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: caídas e incendio por papel.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0763,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = libreria Y nivel_riesgo = alto","avisos = [Librería / bazar / útiles / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: caídas e incendio por papel.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0764,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = libreria Y nivel_riesgo = muy_alto","avisos = [Librería / bazar / útiles / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de 

especialistas y plan de contingencia. Peligros del giro: caídas e incendio por papel.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0765,avisos,rubro = libreria Y local = propio,avisos = [Librería / bazar / útiles / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0766,avisos,rubro = libreria Y local = alquilado,avisos = [Librería / bazar / útiles / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0767,avisos,rubro = libreria Y local = domicilio,avisos = [Librería / bazar / útiles / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0768,avisos,rubro = libreria Y local = mercado,avisos = [Librería / bazar / útiles / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0769,avisos,rubro = libreria Y local = ambulante,"avisos = [Librería / bazar / útiles / ambulante (sin local fijo)] Necesita autorización municipal de comercio ambulatorio, solo en zonas y horarios permitidos; no se tramita licencia de funcionamiento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0770,avisos,rubro = libreria Y local = ninguno_aun,"avisos = [Librería / bazar / útiles / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0771,avisos,rubro = libreria Y persona = natural,"avisos = [Librería / bazar / útiles] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0772,avisos,rubro = libreria Y persona = juridica,avisos = [Librería / bazar / útiles] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0773,avisos,rubro = agroinsumos,"avisos = [Venta de agroinsumos y plaguicidas] Almacene productos químicos con hojas de seguridad (SDS), envases rotulados y ventilación adecuada.",Obligación o buena práctica propia del giro (quimicos).,Normativa sectorial -- validar con el experto 

R0774,avisos,rubro = agroinsumos,avisos = [Venta de agroinsumos y plaguicidas] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0775,avisos,rubro = agroinsumos Y trabajadores = t1,"avisos = [Venta de agroinsumos y plaguicidas] Peligros típicos: intoxicación, incendio y derrames. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0776,avisos,rubro = agroinsumos Y trabajadores = t2,"avisos = [Venta de agroinsumos y plaguicidas] Peligros típicos: intoxicación, incendio y derrames. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0777,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agroinsumos Y area = a2","avisos = [Venta de agroinsumos y plaguicidas] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0778,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agroinsumos Y area = a3","avisos = [Venta de agroinsumos y plaguicidas] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0779,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agroinsumos Y nivel_riesgo = bajo","avisos = [Venta de agroinsumos y plaguicidas / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: intoxicación, incendio y derrames.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0780,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agroinsumos Y nivel_riesgo = medio","avisos = [Venta de agroinsumos y plaguicidas / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: intoxicación, incendio y derrames.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0781,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agroinsumos Y nivel_riesgo = alto","avisos = [Venta de agroinsumos y plaguicidas / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: intoxicación, incendio y derrames.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0782,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agroinsumos Y nivel_riesgo = muy_alto","avisos = [Venta de agroinsumos y plaguicidas / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: intoxicación, incendio y derrames.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0783,avisos,rubro = agroinsumos Y local = propio,avisos = [Venta de agroinsumos y plaguicidas / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0784,avisos,rubro = agroinsumos Y local = alquilado,avisos = [Venta de agroinsumos y plaguicidas / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0785,avisos,rubro = agroinsumos Y local = domicilio,avisos = [Venta de agroinsumos y plaguicidas / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0786,avisos,rubro = agroinsumos Y local = mercado,avisos = [Venta de agroinsumos y plaguicidas / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0787,avisos,rubro = agroinsumos Y local = ambulante,avisos = [Venta de agroinsumos y plaguicidas / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0788,avisos,rubro = agroinsumos Y local = ninguno_aun,"avisos = [Venta de agroinsumos y plaguicidas / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0789,avisos,rubro = agroinsumos Y persona = natural,"avisos = [Venta de agroinsumos y plaguicidas] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0790,avisos,rubro = agroinsumos Y persona = juridica,avisos = [Venta de agroinsumos y plaguicidas] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0791,avisos,rubro = botica,"avisos = [Botica / farmacia] Si guarda datos personales de clientes, cumpla la Ley 29733 (Protección de Datos Personales): consentimiento y medidas de seguridad.",Obligación o buena práctica propia del giro (datos).,Normativa sectorial -- validar con el experto 

R0792,avisos,rubro = botica,avisos = [Botica / farmacia] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0793,avisos,rubro = botica,avisos = [Botica / farmacia] Debe contar con director técnico (químico-farmacéutico) presente en el horario de atención y cumplir las Buenas Prácticas de Oficina Farmacéutica.,Nota específica del giro.,Normativa sectorial -- validar con el experto 

R0794,avisos,rubro = botica Y trabajadores = t1,"avisos = [Botica / farmacia] Peligros típicos: pinchazos, caídas y manejo de productos controlados. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0795,avisos,rubro = botica Y trabajadores = t2,"avisos = [Botica / farmacia] Peligros típicos: pinchazos, caídas y manejo de productos controlados. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0796,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = botica Y area = a2","avisos = [Botica / farmacia] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0797,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = botica Y area = a3","avisos = [Botica / farmacia] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0798,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = botica Y nivel_riesgo = bajo","avisos = [Botica / farmacia / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: pinchazos, caídas y manejo de productos controlados.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0799,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = botica Y nivel_riesgo = medio","avisos = [Botica / farmacia / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: pinchazos, caídas y manejo de productos controlados.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0800,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = botica Y nivel_riesgo = alto","avisos = [Botica / farmacia / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: pinchazos, caídas y manejo de productos controlados.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0801,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = botica Y nivel_riesgo = muy_alto","avisos = [Botica / farmacia / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: pinchazos, caídas y manejo 

de productos controlados.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0802,avisos,rubro = botica Y local = propio,avisos = [Botica / farmacia / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0803,avisos,rubro = botica Y local = alquilado,avisos = [Botica / farmacia / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0804,avisos,rubro = botica Y local = domicilio,avisos = [Botica / farmacia / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0805,avisos,rubro = botica Y local = mercado,avisos = [Botica / farmacia / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0806,avisos,rubro = botica Y local = ambulante,avisos = [Botica / farmacia / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0807,avisos,rubro = botica Y local = ninguno_aun,"avisos = [Botica / farmacia / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0808,avisos,rubro = botica Y persona = natural,"avisos = [Botica / farmacia] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0809,avisos,rubro = botica Y persona = juridica,avisos = [Botica / farmacia] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las 

pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0810,avisos,rubro = online,"avisos = [Venta por internet / redes sociales] En su tienda virtual publique razón social, RUC, precios con IGV, plazos de entrega y política de cambios (Código del Consumidor).",Obligación o buena práctica propia del giro (comercio_electronico).,Normativa sectorial -- validar con el experto 

R0811,avisos,rubro = online,"avisos = [Venta por internet / redes sociales] Si guarda datos personales de clientes, cumpla la Ley 29733 (Protección de Datos Personales): consentimiento y medidas de seguridad.",Obligación o buena práctica propia del giro (datos).,Normativa sectorial -- validar con el experto 

R0812,avisos,rubro = online,"avisos = [Venta por internet / redes sociales] Aunque venda solo por internet necesita RUC, comprobantes de pago y Libro de Reclamaciones virtual.",Nota específica del giro.,Normativa sectorial -- validar con el experto 

R0813,avisos,rubro = online Y trabajadores = t1,avisos = [Venta por internet / redes sociales] Peligros típicos: ergonomía y manipulación de cargas. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0814,avisos,rubro = online Y trabajadores = t2,avisos = [Venta por internet / redes sociales] Peligros típicos: ergonomía y manipulación de cargas. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0815,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = online Y area = a2","avisos = [Venta por internet / redes sociales] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0816,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = online Y area = a3","avisos = [Venta por internet / redes sociales] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0817,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = online Y nivel_riesgo = bajo","avisos = [Venta por internet / redes sociales / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: ergonomía y manipulación de cargas.",La ITSE verifica 

las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0818,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = online Y nivel_riesgo = medio","avisos = [Venta por internet / redes sociales / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: ergonomía y manipulación de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0819,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = online Y nivel_riesgo = alto","avisos = [Venta por internet / redes sociales / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: ergonomía y manipulación de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0820,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = online Y nivel_riesgo = muy_alto","avisos = [Venta por internet / redes sociales / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: ergonomía y manipulación de cargas.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0821,avisos,rubro = online Y local = propio,avisos = [Venta por internet / redes sociales / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0822,avisos,rubro = online Y local = alquilado,avisos = [Venta por internet / redes sociales / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0823,avisos,rubro = online Y local = domicilio,avisos = [Venta por internet / redes sociales / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0824,avisos,rubro = online Y local = mercado,avisos = [Venta por internet / redes sociales / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la 

combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0825,avisos,rubro = online Y local = ambulante,"avisos = [Venta por internet / redes sociales / ambulante (sin local fijo)] Necesita autorización municipal de comercio ambulatorio, solo en zonas y horarios permitidos; no se tramita licencia de funcionamiento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0826,avisos,rubro = online Y local = ninguno_aun,"avisos = [Venta por internet / redes sociales / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0827,avisos,rubro = online Y persona = natural,"avisos = [Venta por internet / redes sociales] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0828,avisos,rubro = online Y persona = juridica,avisos = [Venta por internet / redes sociales] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0829,avisos,rubro = peluqueria,"avisos = [Peluquería / salón de belleza / barbería] Almacene productos químicos con hojas de seguridad (SDS), envases rotulados y ventilación adecuada.",Obligación o buena práctica propia del giro (quimicos).,Normativa sectorial -- validar con el experto 

R0830,avisos,rubro = peluqueria,avisos = [Peluquería / salón de belleza / barbería] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0831,avisos,rubro = peluqueria Y trabajadores = t1,"avisos = [Peluquería / salón de belleza / barbería] Peligros típicos: químicos, cortes y ergonomía. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0832,avisos,rubro = peluqueria Y trabajadores = t2,"avisos = [Peluquería / salón de belleza / barbería] Peligros típicos: químicos, cortes y ergonomía. Elabore la 

matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0833,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = peluqueria Y area = a2","avisos = [Peluquería / salón de belleza / barbería] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0834,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = peluqueria Y area = a3","avisos = [Peluquería / salón de belleza / barbería] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0835,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = peluqueria Y nivel_riesgo = bajo","avisos = [Peluquería / salón de belleza / barbería / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: químicos, cortes y ergonomía.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0836,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = peluqueria Y nivel_riesgo = medio","avisos = [Peluquería / salón de belleza / barbería / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: químicos, cortes y ergonomía.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0837,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = peluqueria Y nivel_riesgo = alto","avisos = [Peluquería / salón de belleza / barbería / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: químicos, cortes y ergonomía.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0838,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = peluqueria Y nivel_riesgo = muy_alto","avisos = [Peluquería / salón de belleza / barbería / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: químicos, cortes y ergonomía.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0839,avisos,rubro = peluqueria Y local = propio,avisos = [Peluquería / salón de belleza / barbería / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0840,avisos,rubro = peluqueria Y local = alquilado,avisos = [Peluquería / salón de belleza / barbería / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0841,avisos,rubro = peluqueria Y local = domicilio,avisos = [Peluquería / salón de belleza / barbería / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0842,avisos,rubro = peluqueria Y local = mercado,avisos = [Peluquería / salón de belleza / barbería / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0843,avisos,rubro = peluqueria Y local = ambulante,avisos = [Peluquería / salón de belleza / barbería / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0844,avisos,rubro = peluqueria Y local = ninguno_aun,"avisos = [Peluquería / salón de belleza / barbería / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0845,avisos,rubro = peluqueria Y persona = natural,"avisos = [Peluquería / salón de belleza / barbería] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o 

SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0846,avisos,rubro = peluqueria Y persona = juridica,avisos = [Peluquería / salón de belleza / barbería] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona 

jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0847,avisos,rubro = taller,"avisos = [Taller mecánico / mecánica automotriz] Aceites usados, baterías y trapos con hidrocarburos son residuos peligrosos: entréguelos a una empresa operadora de residuos sólidos (EO-RS) registrada.",Obligación o buena práctica propia del giro (residuos_pel).,Normativa sectorial -- validar con el experto 

R0848,avisos,rubro = taller,avisos = [Taller mecánico / mecánica automotriz] Controle ruido y emisiones según la ordenanza municipal; puede restringirse el horario o la zona.,Obligación o buena práctica propia del giro (ruido).,Normativa sectorial -- validar con el experto 

R0849,avisos,rubro = taller,"avisos = [Taller mecánico / mecánica automotriz] Almacene productos químicos con hojas de seguridad (SDS), envases rotulados y ventilación adecuada.",Obligación o buena práctica propia del giro (quimicos).,Normativa sectorial -- validar con el experto 

R0850,avisos,rubro = taller Y trabajadores = t1,"avisos = [Taller mecánico / mecánica automotriz] Peligros típicos: aceites usados, incendio, atrapamiento y ruido. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0851,avisos,rubro = taller Y trabajadores = t2,"avisos = [Taller mecánico / mecánica automotriz] Peligros típicos: aceites usados, incendio, atrapamiento y ruido. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0852,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = taller Y area = a2","avisos = [Taller mecánico / mecánica automotriz] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0853,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = taller Y area = a3","avisos = [Taller mecánico / mecánica automotriz] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0854,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = taller Y nivel_riesgo = bajo","avisos = [Taller mecánico / mecánica 

automotriz / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: aceites usados, incendio, atrapamiento y ruido.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0855,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = taller Y nivel_riesgo = medio","avisos = [Taller mecánico / mecánica automotriz / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: aceites usados, incendio, atrapamiento y ruido.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0856,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = taller Y nivel_riesgo = alto","avisos = [Taller mecánico / mecánica automotriz / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: aceites usados, incendio, atrapamiento y ruido.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0857,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = taller Y nivel_riesgo = muy_alto","avisos = [Taller mecánico / mecánica automotriz / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: aceites usados, incendio, atrapamiento y ruido.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0858,avisos,rubro = taller Y local = propio,avisos = [Taller mecánico / mecánica automotriz / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0859,avisos,rubro = taller Y local = alquilado,avisos = [Taller mecánico / mecánica automotriz / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0860,avisos,rubro = taller Y local = domicilio,avisos = [Taller mecánico / mecánica automotriz / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0861,avisos,rubro = taller Y local = mercado,avisos = [Taller mecánico / mecánica automotriz / puesto en mercado o galería] Alerta: este giro normalmente 

no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0862,avisos,rubro = taller Y local = ambulante,avisos = [Taller mecánico / mecánica automotriz / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0863,avisos,rubro = taller Y local = ninguno_aun,"avisos = [Taller mecánico / mecánica automotriz / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0864,avisos,rubro = taller Y persona = natural,"avisos = [Taller mecánico / mecánica automotriz] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0865,avisos,rubro = taller Y persona = juridica,avisos = [Taller mecánico / mecánica automotriz] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0866,avisos,rubro = hospedaje,"avisos = [Hospedaje (hostal, alojamiento)] Si guarda datos personales de clientes, cumpla la Ley 29733 (Protección de Datos Personales): consentimiento y medidas de seguridad.",Obligación o buena práctica propia del giro (datos).,Normativa sectorial -- validar con el experto 

R0867,avisos,rubro = hospedaje,"avisos = [Hospedaje (hostal, alojamiento)] Mantenga rutas de evacuación libres, luces de emergencia, extintores y detectores; la ITSE verifica estos puntos.",Obligación o buena práctica propia del giro (seg_estructural).,Normativa sectorial -- validar con el experto 

R0868,avisos,rubro = hospedaje,"avisos = [Hospedaje (hostal, alojamiento)] Lleve el registro de huéspedes y cumpla las exigencias de seguridad para evacuación.",Nota específica del giro.,Normativa sectorial -- validar con el experto 

R0869,avisos,rubro = hospedaje Y trabajadores = t1,"avisos = [Hospedaje (hostal, alojamiento)] Peligros típicos: incendio, evacuación y resbalones. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 

obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0870,avisos,rubro = hospedaje Y trabajadores = t2,"avisos = [Hospedaje (hostal, alojamiento)] Peligros típicos: incendio, evacuación y resbalones. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0871,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = hospedaje Y area = a2","avisos = [Hospedaje (hostal, alojamiento)] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0872,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = hospedaje Y area = a3","avisos = [Hospedaje (hostal, alojamiento)] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0873,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = hospedaje Y nivel_riesgo = bajo","avisos = [Hospedaje (hostal, alojamiento) / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: incendio, evacuación y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0874,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = hospedaje Y nivel_riesgo = medio","avisos = [Hospedaje (hostal, alojamiento) / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: incendio, evacuación y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0875,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = hospedaje Y nivel_riesgo = alto","avisos = [Hospedaje (hostal, alojamiento) / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: incendio, evacuación y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0876,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = hospedaje Y nivel_riesgo = muy_alto","avisos = [Hospedaje (hostal, alojamiento) / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, 

informes de especialistas y plan de contingencia. Peligros del giro: incendio, evacuación y resbalones.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0877,avisos,rubro = hospedaje Y local = propio,"avisos = [Hospedaje (hostal, alojamiento) / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0878,avisos,rubro = hospedaje Y local = alquilado,"avisos = [Hospedaje (hostal, alojamiento) / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0879,avisos,rubro = hospedaje Y local = domicilio,"avisos = [Hospedaje (hostal, alojamiento) / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.",Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0880,avisos,rubro = hospedaje Y local = mercado,"avisos = [Hospedaje (hostal, alojamiento) / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0881,avisos,rubro = hospedaje Y local = ambulante,"avisos = [Hospedaje (hostal, alojamiento) / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0882,avisos,rubro = hospedaje Y local = ninguno_aun,"avisos = [Hospedaje (hostal, alojamiento) / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0883,avisos,rubro = hospedaje Y persona = natural,"avisos = [Hospedaje (hostal, alojamiento)] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0884,avisos,rubro = hospedaje Y persona = juridica,"avisos = [Hospedaje (hostal, alojamiento)] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.",Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0885,avisos,rubro = prof,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Si guarda datos personales de clientes, cumpla la Ley 29733 (Protección de Datos Personales): consentimiento y medidas de seguridad.",Obligación o buena práctica propia del giro (datos).,Normativa sectorial -- validar con el experto 

R0886,avisos,rubro = prof,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Si su profesión lo exige, mantenga colegiatura y habilidad vigentes.",Nota específica del giro.,Normativa sectorial -- validar con el experto 

R0887,avisos,rubro = prof Y trabajadores = t1,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Peligros típicos: ergonomía y estrés. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0888,avisos,rubro = prof Y trabajadores = t2,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Peligros típicos: ergonomía y estrés. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0889,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prof Y area = a2","avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0890,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prof Y area = a3","avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0891,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prof Y nivel_riesgo = bajo","avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / riesgo bajo] Prepare para la ITSE: extintor 

vigente, señalización de salida y botiquín. Peligros del giro: ergonomía y estrés.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018PCM (Reglamento de ITSE) 

R0892,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prof Y nivel_riesgo = medio","avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: ergonomía y estrés.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0893,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prof Y nivel_riesgo = alto","avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: ergonomía y estrés.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0894,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prof Y nivel_riesgo = muy_alto","avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: ergonomía y estrés.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0895,avisos,rubro = prof Y local = propio,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0896,avisos,rubro = prof Y local = alquilado,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0897,avisos,rubro = prof Y local = domicilio,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.",Condición 

propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0898,avisos,rubro = prof Y local = mercado,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0899,avisos,rubro = prof Y local = ambulante,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0900,avisos,rubro = prof Y local = ninguno_aun,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0901,avisos,rubro = prof Y persona = natural,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0902,avisos,rubro = prof Y persona = juridica,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.",Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0903,avisos,rubro = lavanderia,"avisos = [Lavandería] Almacene productos químicos con hojas de seguridad (SDS), envases rotulados y ventilación adecuada.",Obligación o buena práctica propia del giro (quimicos).,Normativa sectorial -- validar con el experto 

R0904,avisos,rubro = lavanderia,avisos = [Lavandería] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0905,avisos,rubro = lavanderia Y trabajadores = t1,"avisos = [Lavandería] Peligros típicos: vapor, químicos y maquinaria. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0906,avisos,rubro = lavanderia Y trabajadores = t2,"avisos = [Lavandería] Peligros típicos: vapor, químicos y maquinaria. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0907,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = lavanderia Y area = a2","avisos = [Lavandería] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0908,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = lavanderia Y area = a3","avisos = [Lavandería] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0909,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = lavanderia Y nivel_riesgo = bajo","avisos = [Lavandería / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: vapor, químicos y maquinaria.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0910,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = lavanderia Y nivel_riesgo = medio","avisos = [Lavandería / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: vapor, químicos y maquinaria.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018PCM (Reglamento de ITSE) 

R0911,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = lavanderia Y nivel_riesgo = alto","avisos = [Lavandería / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: vapor, químicos y maquinaria.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0912,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = lavanderia Y nivel_riesgo = muy_alto","avisos = [Lavandería / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de 

especialistas y plan de contingencia. Peligros del giro: vapor, químicos y maquinaria.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0913,avisos,rubro = lavanderia Y local = propio,avisos = [Lavandería / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0914,avisos,rubro = lavanderia Y local = alquilado,avisos = [Lavandería / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0915,avisos,rubro = lavanderia Y local = domicilio,avisos = [Lavandería / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0916,avisos,rubro = lavanderia Y local = mercado,avisos = [Lavandería / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0917,avisos,rubro = lavanderia Y local = ambulante,avisos = [Lavandería / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0918,avisos,rubro = lavanderia Y local = ninguno_aun,"avisos = [Lavandería / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese 

documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0919,avisos,rubro = lavanderia Y persona = natural,"avisos = [Lavandería] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0920,avisos,rubro = lavanderia Y persona = juridica,avisos = [Lavandería] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0921,avisos,rubro = gimnasio,"avisos = [Gimnasio / centro deportivo] Si guarda datos personales de clientes, cumpla la Ley 29733 (Protección de Datos Personales): consentimiento y medidas de seguridad.",Obligación o buena práctica propia del giro (datos).,Normativa sectorial -- validar con el experto 

R0922,avisos,rubro = gimnasio,avisos = [Gimnasio / centro deportivo] Controle el aforo y mantenga botiquín y personal con primeros auxilios.,Obligación o buena práctica propia del giro (seguridad_publica).,Normativa sectorial -- validar con el experto 

R0923,avisos,rubro = gimnasio Y trabajadores = t1,avisos = [Gimnasio / centro deportivo] Peligros típicos: lesiones y sobreaforo. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0924,avisos,rubro = gimnasio Y trabajadores = t2,avisos = [Gimnasio / centro deportivo] Peligros típicos: lesiones y sobreaforo. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0925,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = gimnasio Y area = a2","avisos = [Gimnasio / centro deportivo] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0926,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = gimnasio Y area = a3","avisos = [Gimnasio / centro deportivo] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0927,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = gimnasio Y nivel_riesgo = bajo","avisos = [Gimnasio / centro deportivo / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: lesiones y sobreaforo.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0928,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = gimnasio Y nivel_riesgo = medio","avisos = [Gimnasio / centro deportivo / 

riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: lesiones y sobreaforo.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0929,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = gimnasio Y nivel_riesgo = alto","avisos = [Gimnasio / centro deportivo / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: lesiones y sobreaforo.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0930,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = gimnasio Y nivel_riesgo = muy_alto","avisos = [Gimnasio / centro deportivo / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: lesiones y sobreaforo.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018PCM (Reglamento de ITSE) 

R0931,avisos,rubro = gimnasio Y local = propio,avisos = [Gimnasio / centro deportivo / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0932,avisos,rubro = gimnasio Y local = alquilado,avisos = [Gimnasio / centro deportivo / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0933,avisos,rubro = gimnasio Y local = domicilio,avisos = [Gimnasio / centro deportivo / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0934,avisos,rubro = gimnasio Y local = mercado,avisos = [Gimnasio / centro deportivo / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0935,avisos,rubro = gimnasio Y local = ambulante,avisos = [Gimnasio / centro deportivo / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación 

giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0936,avisos,rubro = gimnasio Y local = ninguno_aun,"avisos = [Gimnasio / centro deportivo / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0937,avisos,rubro = gimnasio Y persona = natural,"avisos = [Gimnasio / centro deportivo] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0938,avisos,rubro = gimnasio Y persona = juridica,avisos = [Gimnasio / centro deportivo] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0939,avisos,rubro = agencia,"avisos = [Agencia de viajes y turismo] Si guarda datos personales de clientes, cumpla la Ley 29733 (Protección de Datos Personales): consentimiento y medidas de seguridad.",Obligación o buena práctica propia del giro (datos).,Normativa sectorial -- validar con el experto 

R0940,avisos,rubro = agencia Y trabajadores = t1,avisos = [Agencia de viajes y turismo] Peligros típicos: ergonomía. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0941,avisos,rubro = agencia Y trabajadores = t2,avisos = [Agencia de viajes y turismo] Peligros típicos: ergonomía. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0942,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agencia Y area = a2","avisos = [Agencia de viajes y turismo] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0943,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agencia Y area = a3","avisos = [Agencia de viajes y turismo] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la 

ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0944,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agencia Y nivel_riesgo = bajo","avisos = [Agencia de viajes y turismo / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: ergonomía.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0945,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agencia Y nivel_riesgo = medio","avisos = [Agencia de viajes y turismo / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: ergonomía.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0946,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agencia Y nivel_riesgo = alto","avisos = [Agencia de viajes y turismo / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: ergonomía.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0947,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agencia Y nivel_riesgo = muy_alto","avisos = [Agencia de viajes y turismo / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: ergonomía.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0948,avisos,rubro = agencia Y local = propio,avisos = [Agencia de viajes y turismo / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0949,avisos,rubro = agencia Y local = alquilado,avisos = [Agencia de viajes y turismo / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0950,avisos,rubro = agencia Y local = domicilio,avisos = [Agencia de viajes y turismo / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la 

junta de propietarios.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0951,avisos,rubro = agencia Y local = mercado,avisos = [Agencia de viajes y turismo / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0952,avisos,rubro = agencia Y local = ambulante,avisos = [Agencia de viajes y turismo / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0953,avisos,rubro = agencia Y local = ninguno_aun,"avisos = [Agencia de viajes y turismo / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0954,avisos,rubro = agencia Y persona = natural,"avisos = [Agencia de viajes y turismo] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0955,avisos,rubro = agencia Y persona = juridica,avisos = [Agencia de viajes y turismo] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0956,avisos,rubro = metalmecanica,avisos = [Carpintería metálica / de madera] Controle ruido y emisiones según la ordenanza municipal; puede restringirse el horario o la zona.,Obligación o buena práctica propia del giro (ruido).,Normativa sectorial -- validar con el experto 

R0957,avisos,rubro = metalmecanica,"avisos = [Carpintería metálica / de madera] Almacene productos químicos con hojas de seguridad (SDS), envases rotulados y ventilación adecuada.",Obligación o buena práctica propia del giro (quimicos).,Normativa sectorial -- validar con el experto 

R0958,avisos,rubro = metalmecanica,avisos = [Carpintería metálica / de madera] Controle el polvo y mantenga limpias las máquinas: el polvo orgánico/de madera 

es inflamable.,Obligación o buena práctica propia del giro (polvo).,Normativa sectorial -- validar con el experto 

R0959,avisos,rubro = metalmecanica,avisos = [Carpintería metálica / de madera] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R0960,avisos,rubro = metalmecanica Y trabajadores = t1,"avisos = [Carpintería metálica / de madera] Peligros típicos: cortes, atrapamiento, ruido y soldadura. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0961,avisos,rubro = metalmecanica Y trabajadores = t2,"avisos = [Carpintería metálica / de madera] Peligros típicos: cortes, atrapamiento, ruido y soldadura. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0962,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = metalmecanica Y area = a2","avisos = [Carpintería metálica / de madera] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0963,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = metalmecanica Y area = a3","avisos = [Carpintería metálica / de madera] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0964,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = metalmecanica Y nivel_riesgo = bajo","avisos = [Carpintería metálica / de madera / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: cortes, atrapamiento, ruido y soldadura.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0965,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = metalmecanica Y nivel_riesgo = medio","avisos = [Carpintería metálica / de madera / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: cortes, atrapamiento, ruido y soldadura.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0966,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = metalmecanica Y nivel_riesgo = alto","avisos = [Carpintería metálica / de madera / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: cortes, atrapamiento, ruido y soldadura.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0967,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = metalmecanica Y nivel_riesgo = muy_alto","avisos = [Carpintería metálica / de madera / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: cortes, atrapamiento, ruido y soldadura.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0968,avisos,rubro = metalmecanica Y local = propio,avisos = [Carpintería metálica / de madera / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0969,avisos,rubro = metalmecanica Y local = alquilado,avisos = [Carpintería metálica / de madera / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0970,avisos,rubro = metalmecanica Y local = domicilio,avisos = [Carpintería metálica / de madera / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0971,avisos,rubro = metalmecanica Y local = mercado,avisos = [Carpintería metálica / de madera / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0972,avisos,rubro = metalmecanica Y local = ambulante,avisos = [Carpintería metálica / de madera / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0973,avisos,rubro = metalmecanica Y local = ninguno_aun,"avisos = [Carpintería metálica / de madera / aún no tengo local] Antes de alquilar o comprar, solicite el 

certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0974,avisos,rubro = metalmecanica Y persona = natural,"avisos = [Carpintería metálica / de madera] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0975,avisos,rubro = metalmecanica Y persona = juridica,avisos = [Carpintería metálica / de madera] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0976,avisos,rubro = artesania,"avisos = [Artesanía (textil, paja, cerámica)] Considere registrar su marca en INDECOPI antes de invertir en publicidad o empaques.",Obligación o buena práctica propia del giro (marca).,Normativa sectorial -- validar con el experto 

R0977,avisos,rubro = artesania Y trabajadores = t1,"avisos = [Artesanía (textil, paja, cerámica)] Peligros típicos: posturas forzadas y herramientas cortantes. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0978,avisos,rubro = artesania Y trabajadores = t2,"avisos = [Artesanía (textil, paja, cerámica)] Peligros típicos: posturas forzadas y herramientas cortantes. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0979,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = artesania Y area = a2","avisos = [Artesanía (textil, paja, cerámica)] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0980,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = artesania Y area = a3","avisos = [Artesanía (textil, paja, cerámica)] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0981,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = artesania Y nivel_riesgo = bajo","avisos = [Artesanía (textil, paja, cerámica) / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: posturas forzadas y herramientas cortantes.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0982,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = artesania Y nivel_riesgo = medio","avisos = [Artesanía (textil, paja, cerámica) / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: posturas forzadas y herramientas cortantes.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0983,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = artesania Y nivel_riesgo = alto","avisos = [Artesanía (textil, paja, cerámica) / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: posturas forzadas y herramientas cortantes.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0984,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = artesania Y nivel_riesgo = muy_alto","avisos = [Artesanía (textil, paja, cerámica) / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: posturas forzadas y herramientas cortantes.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0985,avisos,rubro = artesania Y local = propio,"avisos = [Artesanía (textil, paja, cerámica) / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0986,avisos,rubro = artesania Y local = alquilado,"avisos = [Artesanía (textil, paja, cerámica) / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0987,avisos,rubro = artesania Y local = domicilio,"avisos = [Artesanía (textil, paja, cerámica) / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0988,avisos,rubro = artesania Y local = mercado,"avisos = [Artesanía (textil, paja, cerámica) / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0989,avisos,rubro = artesania Y local = ambulante,"avisos = [Artesanía (textil, paja, cerámica) / ambulante (sin local fijo)] Necesita autorización municipal de comercio ambulatorio, solo en zonas y horarios permitidos; no se tramita licencia de funcionamiento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0990,avisos,rubro = artesania Y local = ninguno_aun,"avisos = [Artesanía (textil, paja, cerámica) / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R0991,avisos,rubro = artesania Y persona = natural,"avisos = [Artesanía (textil, paja, cerámica)] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R0992,avisos,rubro = artesania Y persona = juridica,"avisos = [Artesanía (textil, paja, cerámica)] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.",Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R0993,avisos,rubro = confecciones,avisos = [Confección de prendas y calzado] Cumpla las normas de etiquetado aplicables (alimentos envasados: Ley 30021; textiles y calzado: norma técnica de etiquetado vigente).,Obligación o buena práctica propia del giro (etiquetado).,Normativa sectorial -- validar con el experto 

R0994,avisos,rubro = confecciones,avisos = [Confección de prendas y calzado] Considere registrar su marca en INDECOPI antes de invertir en publicidad o empaques.,Obligación o buena práctica propia del giro (marca).,Normativa sectorial -- validar con el experto 

R0995,avisos,rubro = confecciones,avisos = [Confección de prendas y calzado] Controle ruido y emisiones según la ordenanza municipal; puede restringirse el horario o la zona.,Obligación o buena práctica propia del giro (ruido).,Normativa sectorial -- validar con el experto 

R0996,avisos,rubro = confecciones Y trabajadores = t1,"avisos = [Confección de prendas y calzado] Peligros típicos: maquinaria, cortes, pinchazos e incendio. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0997,avisos,rubro = confecciones Y trabajadores = t2,"avisos = [Confección de prendas y calzado] Peligros típicos: maquinaria, cortes, pinchazos e incendio. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R0998,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = confecciones Y area = a2","avisos = [Confección de prendas y calzado] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R0999,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = confecciones Y area = a3","avisos = [Confección de prendas y calzado] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1000,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = confecciones Y nivel_riesgo = bajo","avisos = [Confección de prendas y calzado / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: maquinaria, cortes, pinchazos e incendio.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1001,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = confecciones Y nivel_riesgo = medio","avisos = [Confección de prendas y calzado / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: maquinaria, cortes, pinchazos e incendio.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1002,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = confecciones Y nivel_riesgo = alto","avisos = [Confección de prendas y calzado / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: maquinaria, cortes, pinchazos e incendio.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1003,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = confecciones Y nivel_riesgo = muy_alto","avisos = [Confección de prendas y calzado / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: maquinaria, cortes, pinchazos e incendio.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1004,avisos,rubro = confecciones Y local = propio,avisos = [Confección de prendas y calzado / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1005,avisos,rubro = confecciones Y local = alquilado,avisos = [Confección de prendas y calzado / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1006,avisos,rubro = confecciones Y local = domicilio,avisos = [Confección de prendas y calzado / en mi domicilio / vivienda] Verifique que la zonificación residencial admita el giro; si vive en edificio o condominio puede necesitar autorización de la junta de propietarios.,Condición propia de la combinación girolocal.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1007,avisos,rubro = confecciones Y local = mercado,avisos = [Confección de prendas y calzado / puesto en mercado o galería] Pida la constancia de conducción del puesto y cumpla el reglamento interno del mercado.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1008,avisos,rubro = confecciones Y local = ambulante,avisos = [Confección de prendas y calzado / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1009,avisos,rubro = confecciones Y local = ninguno_aun,"avisos = [Confección de prendas y calzado / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1010,avisos,rubro = confecciones Y persona = natural,"avisos = [Confección de prendas y calzado] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad 

según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R1011,avisos,rubro = confecciones Y persona = juridica,avisos = [Confección de prendas y calzado] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R1012,avisos,rubro = licores,avisos = [Distribuidora / venta de licores] Está prohibido vender bebidas alcohólicas a menores de edad y fuera del horario autorizado.,Obligación o buena práctica propia del giro (alcohol_menores).,Normativa sectorial -- validar con el experto 

R1013,avisos,rubro = licores,avisos = [Distribuidora / venta de licores] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R1014,avisos,rubro = licores Y trabajadores = t1,"avisos = [Distribuidora / venta de licores] Peligros típicos: caídas, cargas y rotura de envases. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R1015,avisos,rubro = licores Y trabajadores = t2,"avisos = [Distribuidora / venta de licores] Peligros típicos: caídas, cargas y rotura de envases. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.",Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R1016,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = licores Y area = a2","avisos = [Distribuidora / venta de licores] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1017,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = licores Y area = a3","avisos = [Distribuidora / venta de licores] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1018,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = licores Y nivel_riesgo = bajo","avisos = [Distribuidora / venta de licores / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y 

botiquín. Peligros del giro: caídas, cargas y rotura de envases.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1019,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = licores Y nivel_riesgo = medio","avisos = [Distribuidora / venta de licores / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: caídas, cargas y rotura de envases.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1020,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = licores Y nivel_riesgo = alto","avisos = [Distribuidora / venta de licores / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: caídas, cargas y rotura de envases.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1021,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = licores Y nivel_riesgo = muy_alto","avisos = [Distribuidora / venta de licores / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: caídas, cargas y rotura de envases.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1022,avisos,rubro = licores Y local = propio,avisos = [Distribuidora / venta de licores / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1023,avisos,rubro = licores Y local = alquilado,avisos = [Distribuidora / venta de licores / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1024,avisos,rubro = licores Y local = domicilio,avisos = [Distribuidora / venta de licores / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1025,avisos,rubro = licores Y local = mercado,avisos = [Distribuidora / venta de licores / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia 

de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1026,avisos,rubro = licores Y local = ambulante,avisos = [Distribuidora / venta de licores / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1027,avisos,rubro = licores Y local = ninguno_aun,"avisos = [Distribuidora / venta de licores / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1028,avisos,rubro = licores Y persona = natural,"avisos = [Distribuidora / venta de licores] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R1029,avisos,rubro = licores Y persona = juridica,avisos = [Distribuidora / venta de licores] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R1030,avisos,rubro = autopartes,avisos = [Venta de repuestos y autopartes] Segregue y disponga sus residuos sólidos según el D.Leg. 1278 (Ley de Gestión Integral de Residuos Sólidos).,Obligación o buena práctica propia del giro (residuos).,Normativa sectorial -- validar con el experto 

R1031,avisos,rubro = autopartes,"avisos = [Venta de repuestos y autopartes] Almacene productos químicos con hojas de seguridad (SDS), envases rotulados y ventilación adecuada.",Obligación o buena práctica propia del giro (quimicos).,Normativa sectorial -- validar con el experto 

R1032,avisos,rubro = autopartes Y trabajadores = t1,avisos = [Venta de repuestos y autopartes] Peligros típicos: cargas pesadas y químicos. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R1033,avisos,rubro = autopartes Y trabajadores = t2,avisos = [Venta de repuestos y autopartes] Peligros típicos: cargas pesadas y químicos. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R1034,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = autopartes Y area = a2","avisos = [Venta de repuestos y autopartes] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1035,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = autopartes Y area = a3","avisos = [Venta de repuestos y autopartes] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1036,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = autopartes Y nivel_riesgo = bajo","avisos = [Venta de repuestos y autopartes / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: cargas pesadas y químicos.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1037,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = autopartes Y nivel_riesgo = medio","avisos = [Venta de repuestos y autopartes / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: cargas pesadas y químicos.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1038,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = autopartes Y nivel_riesgo = alto","avisos = [Venta de repuestos y autopartes / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: cargas pesadas y químicos.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1039,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = autopartes Y nivel_riesgo = muy_alto","avisos = [Venta de repuestos y autopartes / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de especialistas y plan de contingencia. Peligros del giro: cargas pesadas y químicos.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1040,avisos,rubro = autopartes Y local = propio,avisos = [Venta de repuestos y autopartes / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1041,avisos,rubro = autopartes Y local = alquilado,avisos = [Venta de repuestos y autopartes / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1042,avisos,rubro = autopartes Y local = domicilio,avisos = [Venta de repuestos y autopartes / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1043,avisos,rubro = autopartes Y local = mercado,avisos = [Venta de repuestos y autopartes / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1044,avisos,rubro = autopartes Y local = ambulante,avisos = [Venta de repuestos y autopartes / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1045,avisos,rubro = autopartes Y local = ninguno_aun,"avisos = [Venta de repuestos y autopartes / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1046,avisos,rubro = autopartes Y persona = natural,"avisos = [Venta de repuestos y autopartes] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R1047,avisos,rubro = autopartes Y persona = juridica,avisos = [Venta de repuestos y autopartes] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R1048,avisos,rubro = veterinaria,"avisos = [Veterinaria / pet shop] Los residuos biocontaminados (jeringas, restos orgánicos) deben segregarse y entregarse a una EO-RS.",Obligación o buena práctica propia del giro (residuos_bio).,Normativa sectorial -- validar con el experto 

R1049,avisos,rubro = veterinaria Y trabajadores = t1,avisos = [Veterinaria / pet shop] Peligros típicos: mordeduras y zoonosis. Elabore la matriz IPERC y designe un supervisor de seguridad y salud en el trabajo.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R1050,avisos,rubro = veterinaria Y trabajadores = t2,avisos = [Veterinaria / pet shop] Peligros típicos: mordeduras y zoonosis. Elabore la matriz IPERC y con 20 o más trabajadores corresponde un comité de seguridad y salud.,Ley 29783 obliga a identificar peligros y evaluar riesgos.,Ley 29783 (Seguridad y Salud en el Trabajo) 

R1051,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = veterinaria Y area = a2","avisos = [Veterinaria / pet shop] Con de 101 a 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1052,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = veterinaria Y area = a3","avisos = [Veterinaria / pet shop] Con más de 500 m² prepare plan de seguridad, extintores, señalización y luces de emergencia; la ITSE será más exigente.",A mayor área aumenta el nivel de riesgo y las exigencias de seguridad.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1053,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = veterinaria Y nivel_riesgo = bajo","avisos = [Veterinaria / pet shop / riesgo bajo] Prepare para la ITSE: extintor vigente, señalización de salida y botiquín. Peligros del giro: mordeduras y zoonosis.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1054,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = veterinaria Y nivel_riesgo = medio","avisos = [Veterinaria / pet shop / riesgo medio] Prepare para la ITSE: extintores, señalización, luces de emergencia y revisión de instalaciones eléctricas/gas. Peligros del giro: mordeduras y zoonosis.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1055,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = veterinaria Y nivel_riesgo = alto","avisos = [Veterinaria / pet shop / riesgo alto] Prepare para la ITSE: planos de distribución y evacuación, plan de seguridad, sistemas de detección y extinción operativos. Peligros del giro: mordeduras y zoonosis.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1056,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = veterinaria Y nivel_riesgo = muy_alto","avisos = [Veterinaria / pet shop / riesgo muy_alto] Prepare para la ITSE: expediente técnico completo, informes de 

especialistas y plan de contingencia. Peligros del giro: mordeduras y zoonosis.",La ITSE verifica las condiciones de seguridad según el nivel de riesgo.,D.S. 002-2018PCM (Reglamento de ITSE) 

R1057,avisos,rubro = veterinaria Y local = propio,avisos = [Veterinaria / pet shop / local propio] Tenga a mano el título o partida registral y revise cargas y zonificación del predio.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1058,avisos,rubro = veterinaria Y local = alquilado,avisos = [Veterinaria / pet shop / local alquilado] Verifique que el contrato autorice el uso comercial para este giro y obtenga la autorización del propietario con firma legalizada para la licencia.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1059,avisos,rubro = veterinaria Y local = domicilio,avisos = [Veterinaria / pet shop / en mi domicilio / vivienda] Alerta: es poco probable que este giro sea compatible con una vivienda; evalúe un local comercial o industrial y pida antes el certificado de zonificación.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1060,avisos,rubro = veterinaria Y local = mercado,avisos = [Veterinaria / pet shop / puesto en mercado o galería] Alerta: este giro normalmente no se desarrolla en puestos de mercado; consulte a la municipalidad.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1061,avisos,rubro = veterinaria Y local = ambulante,avisos = [Veterinaria / pet shop / ambulante (sin local fijo)] Alerta: este giro no puede ejercerse de forma ambulatoria; necesita un establecimiento.,Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1062,avisos,rubro = veterinaria Y local = ninguno_aun,"avisos = [Veterinaria / pet shop / aún no tengo local] Antes de alquilar o comprar, solicite el certificado de zonificación y compatibilidad de uso para el giro; no pague adelantos sin ese documento.",Condición propia de la combinación giro-local.,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1063,avisos,rubro = veterinaria Y persona = natural,"avisos = [Veterinaria / pet shop] Como persona natural responde con su patrimonio personal; si el negocio crece o hay riesgo, evalúe constituir una EIRL o SAC.",Responsabilidad según Ley General de Sociedades / EIRL,Ley 26887 (LGS) y D.Ley 21621 (EIRL) -- verificar 

R1064,avisos,rubro = veterinaria Y persona = juridica,avisos = [Veterinaria / pet shop] Mantenga vigente la vigencia de poder del representante y el libro de actas; se las pedirán en licencias y trámites.,Los trámites de una persona jurídica los realiza su representante.,Ley General de Sociedades (Ley 26887); SUNARP 

R1065,avisos,regimen = NRUS,avisos = [Régimen NRUS] El NRUS solo permite emitir boletas y tiene tope de compras y ventas; si lo supera debe cambiar de régimen.,Cada régimen tiene obligaciones distintas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta 

R1066,avisos,regimen = RER,avisos = [Régimen RER] En el RER debe llevar registros de compras y ventas y vigilar el tope de ingresos anuales.,Cada régimen tiene obligaciones distintas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta 

R1067,avisos,regimen = RMT,avisos = [Régimen RMT] En el RMT las obligaciones varían según el nivel de ingresos; pida orientación a un contador.,Cada régimen tiene obligaciones distintas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta 

R1068,avisos,regimen = RG,avisos = [Régimen RG] En el Régimen General debe llevar contabilidad completa; contrate un contador.,Cada régimen tiene obligaciones distintas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta 

R1069,avisos,tamano = fuera_mype,avisos = Sus ventas superan el límite de la pequeña empresa: no califica como MYPE para beneficios MYPE.,El tamaño se define por ventas anuales.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1070,documentos,persona = natural Y req.RUC = True,"docs.RUC = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «Inscripción en el RUC».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R1071,documentos,persona = juridica Y req.RUC = True,docs.RUC = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «Inscripción en el RUC».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R1072,documentos,persona = natural Y req.CLAVE_SOL = True,"docs.CLAVE_SOL = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de 

persona para «Obtener la Clave SOL».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R1073,documentos,persona = juridica Y req.CLAVE_SOL = True,docs.CLAVE_SOL = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «Obtener la Clave SOL».,"Normativa SUNAT (RUC, comprobantes, regímenes) -- contrastar con TUPA" 

R1074,documentos,persona = natural Y req.COMPROBANTES = True,"docs.COMPROBANTES = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «Habilitar la emisión de comprobantes de pago electrónicos».,Reglamento de Comprobantes de Pago (R.S. 007-99/SUNAT) -- contrastar con TUPA 

R1075,documentos,persona = juridica Y req.COMPROBANTES = True,docs.COMPROBANTES = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «Habilitar la emisión de comprobantes de pago electrónicos».,Reglamento de Comprobantes de Pago (R.S. 007-99/SUNAT) -- contrastar con TUPA 

R1076,documentos,persona = natural Y req.REMYPE = True,"docs.REMYPE = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «Inscripción en el REMYPE».,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- contrastar con TUPA 

R1077,documentos,persona = juridica Y req.REMYPE = True,docs.REMYPE = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «Inscripción en el REMYPE».,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- contrastar con TUPA 

R1078,documentos,persona = natural Y req.LICENCIA_FUNCIONAMIENTO = True,"docs.LICENCIA_FUNCIONAMIENTO = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «Licencia de funcionamiento».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R1079,documentos,persona = juridica Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de 

identidad/representación según el tipo de persona para «Licencia de funcionamiento».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R1080,documentos,persona = natural Y req.CERT_ZONIFICACION = True,"docs.CERT_ZONIFICACION = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «Certificado de zonificación y compatibilidad de uso».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R1081,documentos,persona = juridica Y req.CERT_ZONIFICACION = True,docs.CERT_ZONIFICACION = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «Certificado de zonificación y compatibilidad de uso».,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- contrastar con TUPA 

R1082,documentos,persona = natural Y req.ITSE_BASICA = True,"docs.ITSE_BASICA = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «ITSE básica (inspección técnica de seguridad en edificaciones)».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R1083,documentos,persona = juridica Y req.ITSE_BASICA = 

True,docs.ITSE_BASICA = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «ITSE básica (inspección técnica de seguridad en edificaciones)».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R1084,documentos,persona = natural Y req.ITSE_DETALLE = True,"docs.ITSE_DETALLE = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «ITSE de detalle».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R1085,documentos,persona = juridica Y req.ITSE_DETALLE = 

True,docs.ITSE_DETALLE = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «ITSE de detalle».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R1086,documentos,persona = natural Y req.ITSE_MULTI = True,"docs.ITSE_MULTI = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder 

o carta poder.",Documento de identidad/representación según el tipo de persona para «ITSE multidisciplinaria».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R1087,documentos,persona = juridica Y req.ITSE_MULTI = True,docs.ITSE_MULTI = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «ITSE multidisciplinaria».,D.S. 002-2018-PCM (Reglamento de ITSE) -- contrastar con TUPA 

R1088,documentos,persona = natural Y req.INSPECCION_SANITARIA = True,"docs.INSPECCION_SANITARIA = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «Inspección/autorización sanitaria del establecimiento».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R1089,documentos,persona = juridica Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «Inspección/autorización sanitaria del establecimiento».,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- contrastar con TUPA 

R1090,documentos,persona = natural Y req.AUTORIZ_ALCOHOL = True,"docs.AUTORIZ_ALCOHOL = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «Autorización municipal para venta de bebidas alcohólicas».,Ley 28681 (bebidas alcohólicas) y ordenanza municipal -- contrastar con TUPA 

R1091,documentos,persona = juridica Y req.AUTORIZ_ALCOHOL = True,docs.AUTORIZ_ALCOHOL = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «Autorización municipal para venta de bebidas alcohólicas».,Ley 28681 (bebidas alcohólicas) y ordenanza municipal -- contrastar con TUPA 

R1092,documentos,persona = natural Y req.AUTORIZ_ANUNCIO = True,"docs.AUTORIZ_ANUNCIO = Persona natural: copia de su DNI; si otra persona tramita por usted, adjunte poder o carta poder.",Documento de identidad/representación según el tipo de persona para «Autorización de anuncio/letrero publicitario».,Ordenanza municipal de anuncios y avisos publicitarios -- contrastar con TUPA 

R1093,documentos,persona = juridica Y req.AUTORIZ_ANUNCIO = True,docs.AUTORIZ_ANUNCIO = Persona jurídica: vigencia de poder del representante legal (partida registral) y su DNI.,Documento de identidad/representación según el tipo de persona para «Autorización de anuncio/letrero publicitario».,Ordenanza municipal de anuncios y avisos publicitarios -- contrastar con TUPA 

R1094,documentos,local = propio Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Título de propiedad o partida registral del local.,Prueba del local exigible según el tipo de local (local propio).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1095,documentos,local = alquilado Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Contrato de alquiler y autorización del propietario con firma legalizada.,Prueba del local exigible según el tipo de local (local alquilado).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1096,documentos,local = domicilio Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Constancia de propiedad o posesión de la vivienda (y autorización de la junta de propietarios si es multifamiliar).,Prueba del local exigible según el tipo de local (en mi domicilio / vivienda).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1097,documentos,local = mercado Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Constancia de conducción del puesto emitida por la administración del mercado.,Prueba del local exigible según el tipo de local (puesto en mercado o galería).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1098,documentos,local = ninguno_aun Y req.LICENCIA_FUNCIONAMIENTO = True,"docs.LICENCIA_FUNCIONAMIENTO = Documento que acredite el local, exigible al presentar la solicitud.",Prueba del local exigible según el tipo de local (aún no tengo local).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1099,documentos,local = propio Y req.CERT_ZONIFICACION = True,docs.CERT_ZONIFICACION = Título de propiedad o partida registral del local.,Prueba del local exigible según el tipo de local (local propio).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1100,documentos,local = alquilado Y req.CERT_ZONIFICACION = True,docs.CERT_ZONIFICACION = Contrato de alquiler y autorización del propietario con firma legalizada.,Prueba del local exigible según el tipo de local 

(local alquilado).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1101,documentos,local = domicilio Y req.CERT_ZONIFICACION = True,docs.CERT_ZONIFICACION = Constancia de propiedad o posesión de la vivienda (y autorización de la junta de propietarios si es multifamiliar).,Prueba del local exigible según el tipo de local (en mi domicilio / vivienda).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1102,documentos,local = mercado Y req.CERT_ZONIFICACION = True,docs.CERT_ZONIFICACION = Constancia de conducción del puesto emitida por la administración del mercado.,Prueba del local exigible según el tipo de local (puesto en mercado o galería).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1103,documentos,local = ninguno_aun Y req.CERT_ZONIFICACION = True,"docs.CERT_ZONIFICACION = Documento que acredite el local, exigible al presentar la solicitud.",Prueba del local exigible según el tipo de local (aún no tengo local).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal 

R1104,documentos,local = propio Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Título de propiedad o partida registral del local.,Prueba del local exigible según el tipo de local (local propio).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1105,documentos,local = alquilado Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Contrato de alquiler y autorización del propietario con firma legalizada.,Prueba del local exigible según el tipo de local (local alquilado).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1106,documentos,local = domicilio Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Constancia de propiedad o posesión de la vivienda (y autorización de la junta de propietarios si es multifamiliar).,Prueba del local exigible según el tipo de local (en mi domicilio / vivienda).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1107,documentos,local = mercado Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Constancia de conducción del puesto emitida por la administración del mercado.,Prueba del local exigible según el tipo de local (puesto en mercado o galería).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1108,documentos,local = ninguno_aun Y req.ITSE_BASICA = 

True,"docs.ITSE_BASICA = Documento que acredite el local, exigible al presentar la solicitud.",Prueba del local exigible según el tipo de local (aún no tengo local).,D.S. 002-2018-PCM (Reglamento de ITSE) 

R1109,documentos,rubro = restaurante Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Programa de higiene y saneamiento (BPM) del establecimiento,Documento propio del giro «Restaurante / cevichería / menú» (BPM).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1110,documentos,rubro = restaurante Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Restaurante / cevichería / menú» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1111,documentos,rubro = restaurante Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Descripción de equipos de refrigeración y formato de registro de temperaturas,Documento propio del giro «Restaurante / cevichería / menú» (cadena_frio).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1112,documentos,rubro = restaurante Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Declaración de medidas de control de ruido (según ordenanza),Documento propio del giro «Restaurante / cevichería / menú» (ruido).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1113,avisos,rubro = restaurante Y regimen = NRUS,avisos = [Restaurante / cevichería / menú / NRUS] Emita boleta o ticket por cada venta y guarde los comprobantes de sus insumos; vigile el tope mensual.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1114,avisos,rubro = restaurante Y regimen = RER,avisos = [Restaurante / cevichería / menú / RER] Registre compras de insumos y ventas diarias; vigile el tope anual de ingresos del rer.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1115,avisos,rubro = restaurante Y regimen = RMT,avisos = [Restaurante / cevichería / menú / RMT] Sustente con comprobantes la compra de insumos y mantenga registros de ventas y compras al día.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1116,avisos,rubro = restaurante Y regimen = RG,avisos = [Restaurante / cevichería / menú / RG] Lleve contabilidad completa y costeo de insumos; 

contrate un contador.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1117,avisos,rubro = restaurante Y tamano = micro,avisos = [Restaurante / cevichería / menú] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1118,avisos,rubro = restaurante Y tamano = pequena,"avisos = [Restaurante / cevichería / menú] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1119,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = restaurante Y tiene_letrero = si",avisos = [Restaurante / cevichería / menú] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1120,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = restaurante Y area = a1","avisos = [Restaurante / cevichería / menú] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1121,avisos,rubro = restaurante Y trabajadores = t0,"avisos = [Restaurante / cevichería / menú] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1122,documentos,rubro = polleria Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Programa de higiene y saneamiento (BPM) del establecimiento,Documento propio del giro «Pollería / parrilla» (BPM).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1123,documentos,rubro = polleria Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Pollería / 

parrilla» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1124,documentos,rubro = polleria Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Descripción de equipos de refrigeración y formato de registro de temperaturas,Documento propio del giro «Pollería / parrilla» (cadena_frio).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1125,documentos,rubro = polleria Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Declaración de medidas de control de ruido (según ordenanza),Documento propio del giro «Pollería / parrilla» (ruido).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1126,avisos,rubro = polleria Y regimen = NRUS,avisos = [Pollería / parrilla / NRUS] Emita boleta o ticket por cada venta y guarde los comprobantes de sus insumos; vigile el tope mensual.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1127,avisos,rubro = polleria Y regimen = RER,avisos = [Pollería / parrilla / RER] Registre compras de insumos y ventas diarias; vigile el tope anual de ingresos del rer.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1128,avisos,rubro = polleria Y regimen = RMT,avisos = [Pollería / parrilla / RMT] Sustente con comprobantes la compra de insumos y mantenga registros de ventas y compras al día.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1129,avisos,rubro = polleria Y regimen = RG,avisos = [Pollería / parrilla / RG] Lleve contabilidad completa y costeo de insumos; contrate un contador.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1130,avisos,rubro = polleria Y tamano = micro,avisos = [Pollería / parrilla] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1131,avisos,rubro = polleria Y tamano = pequena,"avisos = [Pollería / parrilla] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1132,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = polleria Y tiene_letrero = si",avisos = [Pollería / parrilla] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1133,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = polleria Y area = a1","avisos = [Pollería / parrilla] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1134,avisos,rubro = polleria Y trabajadores = t0,"avisos = [Pollería / parrilla] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (TRegistro y PLAME) 

R1135,documentos,rubro = cafeteria Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Programa de higiene y saneamiento (BPM) del establecimiento,Documento propio del giro «Cafetería / juguería / snack» (BPM).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1136,documentos,rubro = cafeteria Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Cafetería / juguería / snack» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1137,avisos,rubro = cafeteria Y regimen = NRUS,avisos = [Cafetería / juguería / snack / NRUS] Emita boleta o ticket por cada venta y guarde los comprobantes de sus insumos; vigile el tope mensual.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1138,avisos,rubro = cafeteria Y regimen = RER,avisos = [Cafetería / juguería / snack / RER] Registre compras de insumos y ventas diarias; vigile el tope anual de ingresos del rer.,Obligaciones tributarias típicas de un negocio de tipo alimentos 

en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1139,avisos,rubro = cafeteria Y regimen = RMT,avisos = [Cafetería / juguería / snack / RMT] Sustente con comprobantes la compra de insumos y mantenga registros de ventas y compras al día.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1140,avisos,rubro = cafeteria Y regimen = RG,avisos = [Cafetería / juguería / snack / RG] Lleve contabilidad completa y costeo de insumos; contrate un contador.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1141,avisos,rubro = cafeteria Y tamano = micro,avisos = [Cafetería / juguería / snack] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1142,avisos,rubro = cafeteria Y tamano = pequena,"avisos = [Cafetería / juguería / snack] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1143,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = cafeteria Y tiene_letrero = si",avisos = [Cafetería / juguería / snack] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1144,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = cafeteria Y area = a1","avisos = [Cafetería / juguería / snack] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1145,avisos,rubro = cafeteria Y trabajadores = t0,"avisos = [Cafetería / juguería / snack] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1146,documentos,rubro = panaderia Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Programa de higiene y saneamiento (BPM) del establecimiento,Documento propio del giro «Panadería / pastelería» (BPM).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1147,documentos,rubro = panaderia Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Panadería / pastelería» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1148,documentos,rubro = panaderia Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Declaración de medidas de control de ruido (según ordenanza),Documento propio del giro «Panadería / pastelería» (ruido).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1149,avisos,rubro = panaderia Y regimen = NRUS,avisos = [Panadería / pastelería / NRUS] Emita boleta o ticket por cada venta y guarde los comprobantes de sus insumos; vigile el tope mensual.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1150,avisos,rubro = panaderia Y regimen = RER,avisos = [Panadería / pastelería / RER] Registre compras de insumos y ventas diarias; vigile el tope anual de ingresos del rer.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1151,avisos,rubro = panaderia Y regimen = RMT,avisos = [Panadería / pastelería / RMT] Sustente con comprobantes la compra de insumos y mantenga registros de ventas y compras al día.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1152,avisos,rubro = panaderia Y regimen = RG,avisos = [Panadería / pastelería / RG] Lleve contabilidad completa y costeo de insumos; contrate un contador.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1153,avisos,rubro = panaderia Y tamano = micro,avisos = [Panadería / pastelería] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción 

en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1154,avisos,rubro = panaderia Y tamano = pequena,"avisos = [Panadería / pastelería] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1155,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = panaderia Y tiene_letrero = si",avisos = [Panadería / pastelería] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1156,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = panaderia Y area = a1","avisos = [Panadería / pastelería] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1157,avisos,rubro = panaderia Y trabajadores = t0,"avisos = [Panadería / pastelería] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1158,documentos,rubro = bodega Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Bodega / tienda de abarrotes» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1159,documentos,rubro = bodega Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Descripción de equipos de refrigeración y formato de registro de temperaturas,Documento propio del giro «Bodega / tienda de abarrotes» (cadena_frio).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1160,avisos,rubro = bodega Y regimen = NRUS,avisos = [Bodega / tienda de abarrotes / NRUS] Emita boleta o ticket por cada venta y guarde los comprobantes de sus insumos; vigile el tope mensual.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1161,avisos,rubro = bodega Y regimen = RER,avisos = [Bodega / tienda de abarrotes / RER] Registre compras de insumos y ventas diarias; vigile el tope anual de ingresos del rer.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1162,avisos,rubro = bodega Y regimen = RMT,avisos = [Bodega / tienda de abarrotes / RMT] Sustente con comprobantes la compra de insumos y mantenga registros de ventas y compras al día.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1163,avisos,rubro = bodega Y regimen = RG,avisos = [Bodega / tienda de abarrotes / RG] Lleve contabilidad completa y costeo de insumos; contrate un contador.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1164,avisos,rubro = bodega Y tamano = micro,avisos = [Bodega / tienda de abarrotes] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1165,avisos,rubro = bodega Y tamano = pequena,"avisos = [Bodega / tienda de abarrotes] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1166,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = bodega Y tiene_letrero = si",avisos = [Bodega / tienda de abarrotes] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1167,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = bodega Y area = a1","avisos = [Bodega / tienda de abarrotes] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1168,avisos,rubro = bodega Y trabajadores = t0,"avisos = [Bodega / tienda de abarrotes] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud 

independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1169,documentos,rubro = minimarket Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Minimarket / autoservicio» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1170,documentos,rubro = minimarket Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Descripción de equipos de refrigeración y formato de registro de temperaturas,Documento propio del giro «Minimarket / autoservicio» (cadena_frio).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1171,avisos,rubro = minimarket Y regimen = NRUS,avisos = [Minimarket / autoservicio / NRUS] Emita boleta o ticket por cada venta y guarde los comprobantes de sus insumos; vigile el tope mensual.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1172,avisos,rubro = minimarket Y regimen = RER,avisos = [Minimarket / autoservicio / RER] Registre compras de insumos y ventas diarias; vigile el tope anual de ingresos del rer.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1173,avisos,rubro = minimarket Y regimen = RMT,avisos = [Minimarket / autoservicio / RMT] Sustente con comprobantes la compra de insumos y mantenga registros de ventas y compras al día.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1174,avisos,rubro = minimarket Y regimen = RG,avisos = [Minimarket / autoservicio / RG] Lleve contabilidad completa y costeo de insumos; contrate un contador.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1175,avisos,rubro = minimarket Y tamano = micro,avisos = [Minimarket / autoservicio] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1176,avisos,rubro = minimarket Y tamano = pequena,"avisos = [Minimarket / autoservicio] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1177,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = minimarket Y tiene_letrero = si",avisos = [Minimarket / autoservicio] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1178,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = minimarket Y area = a1","avisos = [Minimarket / autoservicio] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1179,avisos,rubro = minimarket Y trabajadores = t0,"avisos = [Minimarket / autoservicio] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1180,documentos,rubro = pescaderia Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Programa de higiene y saneamiento (BPM) del establecimiento,Documento propio del giro «Pescadería / venta de mariscos» (BPM).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1181,documentos,rubro = pescaderia Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Descripción de equipos de refrigeración y formato de registro de temperaturas,Documento propio del giro «Pescadería / venta de mariscos» (cadena_frio).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1182,documentos,rubro = pescaderia Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Comprobantes de compra a proveedores con habilitación sanitaria SANIPES,Documento propio del giro «Pescadería / venta de mariscos» (pesca).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1183,documentos,rubro = pescaderia Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Pescadería / 

venta de mariscos» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1184,avisos,rubro = pescaderia Y regimen = NRUS,avisos = [Pescadería / venta de mariscos / NRUS] Emita boleta o ticket por cada venta y guarde los comprobantes de sus insumos; vigile el tope mensual.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1185,avisos,rubro = pescaderia Y regimen = RER,avisos = [Pescadería / venta de mariscos / RER] Registre compras de insumos y ventas diarias; vigile el tope anual de ingresos del rer.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1186,avisos,rubro = pescaderia Y regimen = RMT,avisos = [Pescadería / venta de mariscos / RMT] Sustente con comprobantes la compra de insumos y mantenga registros de ventas y compras al día.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1187,avisos,rubro = pescaderia Y regimen = RG,avisos = [Pescadería / venta de mariscos / RG] Lleve contabilidad completa y costeo de insumos; contrate un contador.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1188,avisos,rubro = pescaderia Y tamano = micro,avisos = [Pescadería / venta de mariscos] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1189,avisos,rubro = pescaderia Y tamano = pequena,"avisos = [Pescadería / venta de mariscos] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1190,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = pescaderia Y tiene_letrero = si",avisos = [Pescadería / venta de mariscos] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1191,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = pescaderia Y area = a1","avisos = [Pescadería / venta de mariscos] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1192,avisos,rubro = pescaderia Y trabajadores = t0,"avisos = [Pescadería / venta de mariscos] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1193,documentos,rubro = carniceria Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Programa de higiene y saneamiento (BPM) del establecimiento,Documento propio del giro «Carnicería / venta de aves» (BPM).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1194,documentos,rubro = carniceria Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Descripción de equipos de refrigeración y formato de registro de temperaturas,Documento propio del giro «Carnicería / venta de aves» (cadena_frio).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1195,documentos,rubro = carniceria Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Comprobantes de compra a camales autorizados,Documento propio del giro «Carnicería / venta de aves» (carne).,D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1196,documentos,rubro = carniceria Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Carnicería / venta de aves» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1197,avisos,rubro = carniceria Y regimen = NRUS,avisos = [Carnicería / venta de aves / NRUS] Emita boleta o ticket por cada venta y guarde los comprobantes de sus insumos; vigile el tope mensual.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1198,avisos,rubro = carniceria Y regimen = RER,avisos = [Carnicería / venta de aves / RER] Registre compras de insumos y ventas diarias; vigile el tope anual de ingresos del rer.,Obligaciones tributarias típicas de un negocio de tipo alimentos 

en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1199,avisos,rubro = carniceria Y regimen = RMT,avisos = [Carnicería / venta de aves / RMT] Sustente con comprobantes la compra de insumos y mantenga registros de ventas y compras al día.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1200,avisos,rubro = carniceria Y regimen = RG,avisos = [Carnicería / venta de aves / RG] Lleve contabilidad completa y costeo de insumos; contrate un contador.,Obligaciones tributarias típicas de un negocio de tipo alimentos en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1201,avisos,rubro = carniceria Y tamano = micro,avisos = [Carnicería / venta de aves] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1202,avisos,rubro = carniceria Y tamano = pequena,"avisos = [Carnicería / venta de aves] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1203,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = carniceria Y tiene_letrero = si",avisos = [Carnicería / venta de aves] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1204,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = carniceria Y area = a1","avisos = [Carnicería / venta de aves] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1205,avisos,rubro = carniceria Y trabajadores = t0,"avisos = [Carnicería / venta de aves] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1206,documentos,rubro = prod_alimentos Y req.INSPECCION_SANITARIA = True,docs.INSPECCION_SANITARIA = Programa de higiene y saneamiento (BPM) del establecimiento,"Documento propio del giro «Producción de alimentos envasados (dulces, conservas, snacks)» (BPM).",D.S. 007-98-SA (Reglamento sobre vigilancia y control sanitario de alimentos y bebidas) -- puede variar según el TUPA 

R1207,documentos,rubro = prod_alimentos Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Muestra de etiqueta o ficha de productos (si se solicita),"Documento propio del giro «Producción de alimentos envasados (dulces, conservas, snacks)» (etiquetado).",Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1208,documentos,rubro = prod_alimentos Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Denominación comercial/marca que se usará en el letrero,"Documento propio del giro «Producción de alimentos envasados (dulces, conservas, snacks)» (marca).",Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1209,documentos,rubro = prod_alimentos Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),"Documento propio del giro «Producción de alimentos envasados (dulces, conservas, snacks)» (residuos).",Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1210,avisos,rubro = prod_alimentos Y regimen = NRUS,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / NRUS] El nrus limita compras y ventas mensuales; si produce y compra insumos en volumen, probablemente deba cambiar de régimen.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1211,avisos,rubro = prod_alimentos Y regimen = RER,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / RER] Registre compras de materia prima y ventas; valore sus activos fijos frente al tope del régimen.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1212,avisos,rubro = prod_alimentos Y regimen = RMT,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / RMT] Lleve registros de compras y ventas y sustente la materia prima con comprobantes para deducir costos.",Obligaciones tributarias típicas de un negocio de tipo produccion en el 

régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1213,avisos,rubro = prod_alimentos Y regimen = RG,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks) / RG] Lleve contabilidad completa con costos de producción e inventarios.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1214,avisos,rubro = prod_alimentos Y tamano = micro,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 0132013-PRODUCE) -- verificar vigencia 

R1215,avisos,rubro = prod_alimentos Y tamano = pequena,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013PRODUCE) -- verificar vigencia 

R1216,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prod_alimentos Y tiene_letrero = si","avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.",El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1217,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prod_alimentos Y area = a1","avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1218,avisos,rubro = prod_alimentos Y trabajadores = t0,"avisos = [Producción de alimentos envasados (dulces, conservas, snacks)] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1219,documentos,rubro = molino_arroz Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Declaración de medidas de control de 

ruido (según ordenanza),Documento propio del giro «Molino / pilado de arroz y granos» (ruido).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1220,documentos,rubro = molino_arroz Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Molino / pilado de arroz y granos» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1221,documentos,rubro = molino_arroz Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Descripción de control de polvo y mantenimiento de maquinaria,Documento propio del giro «Molino / pilado de arroz y granos» (polvo).,D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1222,avisos,rubro = molino_arroz Y regimen = NRUS,"avisos = [Molino / pilado de arroz y granos / NRUS] El nrus limita compras y ventas mensuales; si produce y compra insumos en volumen, probablemente deba cambiar de régimen.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1223,avisos,rubro = molino_arroz Y regimen = RER,avisos = [Molino / pilado de arroz y granos / RER] Registre compras de materia prima y ventas; valore sus activos fijos frente al tope del régimen.,Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1224,avisos,rubro = molino_arroz Y regimen = RMT,avisos = [Molino / pilado de arroz y granos / RMT] Lleve registros de compras y ventas y sustente la materia prima con comprobantes para deducir costos.,Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1225,avisos,rubro = molino_arroz Y regimen = RG,avisos = [Molino / pilado de arroz y granos / RG] Lleve contabilidad completa con costos de producción e inventarios.,Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1226,avisos,rubro = molino_arroz Y tamano = micro,avisos = [Molino / pilado de arroz y granos] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1227,avisos,rubro = molino_arroz Y tamano = pequena,"avisos = [Molino / pilado de arroz y granos] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1228,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = molino_arroz Y tiene_letrero = si",avisos = [Molino / pilado de arroz y granos] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1229,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = molino_arroz Y area = a1","avisos = [Molino / pilado de arroz y granos] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1230,avisos,rubro = molino_arroz Y trabajadores = t0,"avisos = [Molino / pilado de arroz y granos] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1231,documentos,rubro = ropa Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Muestra de etiqueta o ficha de productos (si se solicita),Documento propio del giro «Venta de ropa y calzado» (etiquetado).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1232,avisos,rubro = ropa Y regimen = NRUS,avisos = [Venta de ropa y calzado / NRUS] Emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1233,avisos,rubro = ropa Y regimen = RER,"avisos = [Venta de ropa y calzado / RER] Registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1234,avisos,rubro = ropa Y regimen = RMT,avisos = [Venta de ropa y calzado / RMT] Lleve los registros exigidos según su nivel de ingresos y sustente sus compras con comprobantes para deducir gastos.,Obligaciones tributarias típicas 

de un negocio de tipo comercio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1235,avisos,rubro = ropa Y regimen = RG,avisos = [Venta de ropa y calzado / RG] Lleve contabilidad completa con control de inventarios y pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1236,avisos,rubro = ropa Y tamano = micro,avisos = [Venta de ropa y calzado] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1237,avisos,rubro = ropa Y tamano = pequena,"avisos = [Venta de ropa y calzado] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1238,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ropa Y tiene_letrero = si",avisos = [Venta de ropa y calzado] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1239,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ropa Y area = a1","avisos = [Venta de ropa y calzado] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1240,avisos,rubro = ropa Y trabajadores = t0,"avisos = [Venta de ropa y calzado] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1241,documentos,rubro = ferreteria Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Ferretería / materiales de construcción» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1242,documentos,rubro = ferreteria Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Hojas de seguridad (SDS) y relación de productos químicos almacenados,Documento propio del giro «Ferretería / materiales de construcción» (quimicos).,D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1243,avisos,rubro = ferreteria Y regimen = NRUS,avisos = [Ferretería / materiales de construcción / NRUS] Emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1244,avisos,rubro = ferreteria Y regimen = RER,"avisos = [Ferretería / materiales de construcción / RER] Registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1245,avisos,rubro = ferreteria Y regimen = RMT,avisos = [Ferretería / materiales de construcción / RMT] Lleve los registros exigidos según su nivel de ingresos y sustente sus compras con comprobantes para deducir gastos.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1246,avisos,rubro = ferreteria Y regimen = RG,avisos = [Ferretería / materiales de construcción / RG] Lleve contabilidad completa con control de inventarios y pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1247,avisos,rubro = ferreteria Y tamano = micro,avisos = [Ferretería / materiales de construcción] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1248,avisos,rubro = ferreteria Y tamano = pequena,"avisos = [Ferretería / materiales de construcción] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1249,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ferreteria Y tiene_letrero = si",avisos = [Ferretería / materiales de construcción] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1250,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = ferreteria Y area = a1","avisos = [Ferretería / materiales de construcción] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1251,avisos,rubro = ferreteria Y trabajadores = t0,"avisos = [Ferretería / materiales de construcción] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1252,documentos,rubro = tecnologia Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Política de privacidad o aviso de tratamiento de datos (si almacena datos de clientes),Documento propio del giro «Venta o reparación de celulares y tecnología» (datos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1253,documentos,rubro = tecnologia Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de entrega de residuos electrónicos a operador autorizado,Documento propio del giro «Venta o reparación de celulares y tecnología» (raee).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1254,avisos,rubro = tecnologia Y regimen = NRUS,avisos = [Venta o reparación de celulares y tecnología / NRUS] Emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1255,avisos,rubro = tecnologia Y regimen = RER,"avisos = [Venta o reparación de celulares y tecnología / RER] Registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1256,avisos,rubro = tecnologia Y regimen = RMT,avisos = [Venta o reparación de celulares y tecnología / RMT] Lleve los registros exigidos según su nivel de ingresos 

y sustente sus compras con comprobantes para deducir gastos.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1257,avisos,rubro = tecnologia Y regimen = RG,avisos = [Venta o reparación de celulares y tecnología / RG] Lleve contabilidad completa con control de inventarios y pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1258,avisos,rubro = tecnologia Y tamano = micro,avisos = [Venta o reparación de celulares y tecnología] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1259,avisos,rubro = tecnologia Y tamano = pequena,"avisos = [Venta o reparación de celulares y tecnología] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1260,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = tecnologia Y tiene_letrero = si",avisos = [Venta o reparación de celulares y tecnología] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1261,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = tecnologia Y area = a1","avisos = [Venta o reparación de celulares y tecnología] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1262,avisos,rubro = tecnologia Y trabajadores = t0,"avisos = [Venta o reparación de celulares y tecnología] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1263,documentos,rubro = libreria Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Librería / bazar / útiles» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1264,avisos,rubro = libreria Y regimen = NRUS,avisos = [Librería / bazar / útiles / NRUS] Emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1265,avisos,rubro = libreria Y regimen = RER,"avisos = [Librería / bazar / útiles / RER] Registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1266,avisos,rubro = libreria Y regimen = RMT,avisos = [Librería / bazar / útiles / RMT] Lleve los registros exigidos según su nivel de ingresos y sustente sus compras con comprobantes para deducir gastos.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1267,avisos,rubro = libreria Y regimen = RG,avisos = [Librería / bazar / útiles / RG] Lleve contabilidad completa con control de inventarios y pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1268,avisos,rubro = libreria Y tamano = micro,avisos = [Librería / bazar / útiles] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1269,avisos,rubro = libreria Y tamano = pequena,"avisos = [Librería / bazar / útiles] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1270,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = libreria Y tiene_letrero = si",avisos = [Librería / bazar / útiles] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El 

anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1271,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = libreria Y area = a1","avisos = [Librería / bazar / útiles] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1272,avisos,rubro = libreria Y trabajadores = t0,"avisos = [Librería / bazar / útiles] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1273,documentos,rubro = agroinsumos Y req.ITSE_BASICA = 

True,docs.ITSE_BASICA = Hojas de seguridad (SDS) y relación de productos químicos almacenados,Documento propio del giro «Venta de agroinsumos y plaguicidas» (quimicos).,D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1274,documentos,rubro = agroinsumos Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Venta de agroinsumos y plaguicidas» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1275,avisos,rubro = agroinsumos Y regimen = NRUS,avisos = [Venta de agroinsumos y plaguicidas / NRUS] Emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1276,avisos,rubro = agroinsumos Y regimen = RER,"avisos = [Venta de agroinsumos y plaguicidas / RER] Registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1277,avisos,rubro = agroinsumos Y regimen = RMT,avisos = [Venta de agroinsumos y plaguicidas / RMT] Lleve los registros exigidos según su nivel de ingresos y sustente sus compras con comprobantes para deducir gastos.,Obligaciones tributarias típicas de un negocio de tipo comercio en el 

régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1278,avisos,rubro = agroinsumos Y regimen = RG,avisos = [Venta de agroinsumos y plaguicidas / RG] Lleve contabilidad completa con control de inventarios y pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1279,avisos,rubro = agroinsumos Y tamano = micro,avisos = [Venta de agroinsumos y plaguicidas] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1280,avisos,rubro = agroinsumos Y tamano = pequena,"avisos = [Venta de agroinsumos y plaguicidas] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1281,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agroinsumos Y tiene_letrero = si",avisos = [Venta de agroinsumos y plaguicidas] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1282,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agroinsumos Y area = a1","avisos = [Venta de agroinsumos y plaguicidas] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1283,avisos,rubro = agroinsumos Y trabajadores = t0,"avisos = [Venta de agroinsumos y plaguicidas] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1284,documentos,rubro = botica Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Política de privacidad o aviso de tratamiento de datos (si almacena datos de clientes),Documento propio del giro «Botica / farmacia» (datos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1285,documentos,rubro = botica Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Botica / farmacia» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1286,avisos,rubro = botica Y regimen = NRUS,avisos = [Botica / farmacia / NRUS] Emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1287,avisos,rubro = botica Y regimen = RER,"avisos = [Botica / farmacia / RER] Registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1288,avisos,rubro = botica Y regimen = RMT,avisos = [Botica / farmacia / RMT] Lleve los registros exigidos según su nivel de ingresos y sustente sus compras con comprobantes para deducir gastos.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1289,avisos,rubro = botica Y regimen = RG,avisos = [Botica / farmacia / RG] Lleve contabilidad completa con control de inventarios y pagos a cuenta 

mensuales.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1290,avisos,rubro = botica Y tamano = micro,avisos = [Botica / farmacia] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1291,avisos,rubro = botica Y tamano = pequena,"avisos = [Botica / farmacia] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1292,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = botica Y tiene_letrero = si",avisos = [Botica / farmacia] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El 

anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1293,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = botica Y area = a1","avisos = [Botica / farmacia] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1294,avisos,rubro = botica Y trabajadores = t0,"avisos = [Botica / farmacia] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (TRegistro y PLAME) 

R1295,documentos,rubro = online Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Dirección web o redes de venta del negocio,Documento propio del giro «Venta por internet / redes sociales» (comercio_electronico).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1296,documentos,rubro = online Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Política de privacidad o aviso de tratamiento de datos (si almacena datos de clientes),Documento propio del giro «Venta por internet / redes sociales» (datos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1297,avisos,rubro = online Y regimen = NRUS,avisos = [Venta por internet / redes sociales / NRUS] Emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1298,avisos,rubro = online Y regimen = RER,"avisos = [Venta por internet / redes sociales / RER] Registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1299,avisos,rubro = online Y regimen = RMT,avisos = [Venta por internet / redes sociales / RMT] Lleve los registros exigidos según su nivel de ingresos y sustente sus compras con comprobantes para deducir gastos.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1300,avisos,rubro = online Y regimen = RG,avisos = [Venta por internet / redes sociales / RG] Lleve contabilidad completa con control de inventarios y pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1301,avisos,rubro = online Y tamano = micro,avisos = [Venta por internet / redes sociales] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1302,avisos,rubro = online Y tamano = pequena,"avisos = [Venta por internet / redes sociales] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1303,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = online Y tiene_letrero = si",avisos = [Venta por internet / redes sociales] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1304,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = online Y area = a1","avisos = [Venta por internet / redes sociales] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1305,avisos,rubro = online Y trabajadores = t0,"avisos = [Venta por internet / redes sociales] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1306,documentos,rubro = peluqueria Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Hojas de seguridad (SDS) y relación de productos químicos almacenados,Documento propio del giro «Peluquería / salón de belleza / barbería» (quimicos).,D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1307,documentos,rubro = peluqueria Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Peluquería / 

salón de belleza / barbería» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1308,avisos,rubro = peluqueria Y regimen = NRUS,avisos = [Peluquería / salón de belleza / barbería / NRUS] Emita boleta por cada servicio; si presta servicios a empresas que piden factura deberá cambiar de régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1309,avisos,rubro = peluqueria Y regimen = RER,avisos = [Peluquería / salón de belleza / barbería / RER] Emita comprobantes por cada servicio y registre ingresos y compras; vigile el tope del régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1310,avisos,rubro = peluqueria Y regimen = RMT,avisos = [Peluquería / salón de belleza / barbería / RMT] Registre ingresos y gastos con comprobantes; los pagos de honorarios y servicios deben sustentarse.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1311,avisos,rubro = peluqueria Y regimen = RG,avisos = [Peluquería / salón de belleza / barbería / RG] Lleve contabilidad completa; los servicios facturados generan pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1312,avisos,rubro = peluqueria Y tamano = micro,avisos = [Peluquería / salón de belleza / barbería] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1313,avisos,rubro = peluqueria Y tamano = pequena,"avisos = [Peluquería / salón de belleza / barbería] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1314,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = peluqueria Y tiene_letrero = si",avisos = [Peluquería / salón de belleza / barbería] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1315,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = peluqueria Y area = a1","avisos = [Peluquería / salón de belleza / barbería] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1316,avisos,rubro = peluqueria Y trabajadores = t0,"avisos = [Peluquería / salón de belleza / barbería] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1317,documentos,rubro = taller Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Contrato o compromiso con EO-RS para residuos peligrosos,Documento propio del giro «Taller mecánico / mecánica automotriz» (residuos_pel).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1318,documentos,rubro = taller Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Declaración de medidas de control de ruido (según ordenanza),Documento propio del giro «Taller mecánico / mecánica automotriz» (ruido).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1319,documentos,rubro = taller Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Hojas de seguridad (SDS) y relación de productos químicos almacenados,Documento propio del giro «Taller mecánico / mecánica automotriz» (quimicos).,D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1320,avisos,rubro = taller Y regimen = NRUS,avisos = [Taller mecánico / mecánica automotriz / NRUS] Emita boleta por cada servicio; si presta servicios a empresas que piden factura deberá cambiar de régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1321,avisos,rubro = taller Y regimen = RER,avisos = [Taller mecánico / mecánica automotriz / RER] Emita comprobantes por cada servicio y registre ingresos y compras; vigile el tope del régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1322,avisos,rubro = taller Y regimen = RMT,avisos = [Taller mecánico / mecánica automotriz / RMT] Registre ingresos y gastos con comprobantes; los pagos de honorarios y servicios deben sustentarse.,Obligaciones tributarias típicas de un 

negocio de tipo servicio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1323,avisos,rubro = taller Y regimen = RG,avisos = [Taller mecánico / mecánica automotriz / RG] Lleve contabilidad completa; los servicios facturados generan pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1324,avisos,rubro = taller Y tamano = micro,avisos = [Taller mecánico / mecánica automotriz] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1325,avisos,rubro = taller Y tamano = pequena,"avisos = [Taller mecánico / mecánica automotriz] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1326,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = taller Y tiene_letrero = si",avisos = [Taller mecánico / mecánica automotriz] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1327,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = taller Y area = a1","avisos = [Taller mecánico / mecánica automotriz] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1328,avisos,rubro = taller Y trabajadores = t0,"avisos = [Taller mecánico / mecánica automotriz] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1329,documentos,rubro = hospedaje Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Política de privacidad o aviso de tratamiento de datos (si almacena datos de clientes),"Documento propio del giro «Hospedaje (hostal, alojamiento)» (datos).",Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1330,documentos,rubro = hospedaje Y req.ITSE_DETALLE = True,docs.ITSE_DETALLE = Plano de evacuación con rutas y salidas de emergencia,"Documento propio del giro «Hospedaje (hostal, alojamiento)» (seg_estructural).",D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1331,avisos,rubro = hospedaje Y regimen = NRUS,"avisos = [Hospedaje (hostal, alojamiento) / NRUS] Emita boleta por cada servicio; si presta servicios a empresas que piden factura deberá cambiar de régimen.",Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1332,avisos,rubro = hospedaje Y regimen = RER,"avisos = [Hospedaje (hostal, alojamiento) / RER] Emita comprobantes por cada servicio y registre ingresos y compras; vigile el tope del régimen.",Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1333,avisos,rubro = hospedaje Y regimen = RMT,"avisos = [Hospedaje (hostal, alojamiento) / RMT] Registre ingresos y gastos con comprobantes; los pagos de honorarios y servicios deben sustentarse.",Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1334,avisos,rubro = hospedaje Y regimen = RG,"avisos = [Hospedaje (hostal, alojamiento) / RG] Lleve contabilidad completa; los servicios facturados generan pagos a cuenta mensuales.",Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1335,avisos,rubro = hospedaje Y tamano = micro,"avisos = [Hospedaje (hostal, alojamiento)] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1336,avisos,rubro = hospedaje Y tamano = pequena,"avisos = [Hospedaje (hostal, alojamiento)] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1337,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = hospedaje Y tiene_letrero = si","avisos = [Hospedaje (hostal, alojamiento)] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no 

autorizadas.",El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1338,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = hospedaje Y area = a1","avisos = [Hospedaje (hostal, alojamiento)] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1339,avisos,rubro = hospedaje Y trabajadores = t0,"avisos = [Hospedaje (hostal, alojamiento)] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1340,documentos,rubro = prof Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Política de privacidad o aviso de tratamiento de datos (si almacena datos de clientes),"Documento propio del giro «Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)» (datos).",Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal - - puede variar según el TUPA 

R1341,avisos,rubro = prof Y regimen = NRUS,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / NRUS] Emita boleta por cada servicio; si presta servicios a empresas que piden factura deberá cambiar de régimen.",Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1342,avisos,rubro = prof Y regimen = RER,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / RER] Emita comprobantes por cada servicio y registre ingresos y compras; vigile el tope del régimen.",Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1343,avisos,rubro = prof Y regimen = RMT,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / RMT] Registre ingresos y gastos con comprobantes; los pagos de honorarios y servicios deben sustentarse.",Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1344,avisos,rubro = prof Y regimen = RG,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría) / RG] Lleve contabilidad completa; 

los servicios facturados generan pagos a cuenta mensuales.",Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1345,avisos,rubro = prof Y tamano = micro,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 0132013-PRODUCE) -- verificar vigencia 

R1346,avisos,rubro = prof Y tamano = pequena,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013PRODUCE) -- verificar vigencia 

R1347,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prof Y tiene_letrero = si","avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.",El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1348,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = prof Y area = a1","avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1349,avisos,rubro = prof Y trabajadores = t0,"avisos = [Servicios profesionales (contabilidad, derecho, ingeniería, consultoría)] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1350,documentos,rubro = lavanderia Y req.ITSE_BASICA = 

True,docs.ITSE_BASICA = Hojas de seguridad (SDS) y relación de productos químicos almacenados,Documento propio del giro «Lavandería» (quimicos).,D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1351,documentos,rubro = lavanderia Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos 

sólidos (si la municipalidad lo solicita),Documento propio del giro «Lavandería» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1352,avisos,rubro = lavanderia Y regimen = NRUS,avisos = [Lavandería / NRUS] Emita boleta por cada servicio; si presta servicios a empresas que piden factura deberá cambiar de régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1353,avisos,rubro = lavanderia Y regimen = RER,avisos = [Lavandería / RER] Emita comprobantes por cada servicio y registre ingresos y compras; vigile el tope del régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1354,avisos,rubro = lavanderia Y regimen = RMT,avisos = [Lavandería / RMT] Registre ingresos y gastos con comprobantes; los pagos de honorarios y servicios deben sustentarse.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1355,avisos,rubro = lavanderia Y regimen = RG,avisos = [Lavandería / RG] Lleve contabilidad completa; los servicios facturados generan pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1356,avisos,rubro = lavanderia Y tamano = micro,avisos = [Lavandería] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1357,avisos,rubro = lavanderia Y tamano = pequena,"avisos = [Lavandería] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1358,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = lavanderia Y tiene_letrero = si",avisos = [Lavandería] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1359,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = lavanderia Y area = a1","avisos = [Lavandería] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1360,avisos,rubro = lavanderia Y trabajadores = t0,"avisos = [Lavandería] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (TRegistro y PLAME) 

R1361,documentos,rubro = gimnasio Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Política de privacidad o aviso de tratamiento de datos (si almacena datos de clientes),Documento propio del giro «Gimnasio / centro deportivo» (datos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1362,documentos,rubro = gimnasio Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Aforo máximo declarado y botiquín,Documento propio del giro «Gimnasio / centro deportivo» (seguridad_publica).,D.S. 002-2018-PCM (Reglamento de ITSE) - - puede variar según el TUPA 

R1363,avisos,rubro = gimnasio Y regimen = NRUS,avisos = [Gimnasio / centro deportivo / NRUS] Emita boleta por cada servicio; si presta servicios a empresas que piden factura deberá cambiar de régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1364,avisos,rubro = gimnasio Y regimen = RER,avisos = [Gimnasio / centro deportivo / RER] Emita comprobantes por cada servicio y registre ingresos y compras; vigile el tope del régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1365,avisos,rubro = gimnasio Y regimen = RMT,avisos = [Gimnasio / centro deportivo / RMT] Registre ingresos y gastos con comprobantes; los pagos de honorarios y servicios deben sustentarse.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1366,avisos,rubro = gimnasio Y regimen = RG,avisos = [Gimnasio / centro deportivo / RG] Lleve contabilidad completa; los servicios facturados generan pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo 

servicio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1367,avisos,rubro = gimnasio Y tamano = micro,avisos = [Gimnasio / centro deportivo] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1368,avisos,rubro = gimnasio Y tamano = pequena,"avisos = [Gimnasio / centro deportivo] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1369,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = gimnasio Y tiene_letrero = si",avisos = [Gimnasio / centro deportivo] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1370,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = gimnasio Y area = a1","avisos = [Gimnasio / centro deportivo] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1371,avisos,rubro = gimnasio Y trabajadores = t0,"avisos = [Gimnasio / centro deportivo] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1372,documentos,rubro = agencia Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Política de privacidad o aviso de tratamiento de datos (si almacena datos de clientes),Documento propio del giro «Agencia de viajes y turismo» (datos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1373,avisos,rubro = agencia Y regimen = NRUS,avisos = [Agencia de viajes y turismo / NRUS] Emita boleta por cada servicio; si presta servicios a empresas que piden factura deberá cambiar de régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1374,avisos,rubro = agencia Y regimen = RER,avisos = [Agencia de viajes y turismo / RER] Emita comprobantes por cada servicio y registre ingresos y compras; vigile el tope del régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1375,avisos,rubro = agencia Y regimen = RMT,avisos = [Agencia de viajes y turismo / RMT] Registre ingresos y gastos con comprobantes; los pagos de honorarios y servicios deben sustentarse.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1376,avisos,rubro = agencia Y regimen = RG,avisos = [Agencia de viajes y turismo / RG] Lleve contabilidad completa; los servicios facturados generan pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1377,avisos,rubro = agencia Y tamano = micro,avisos = [Agencia de viajes y turismo] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1378,avisos,rubro = agencia Y tamano = pequena,"avisos = [Agencia de viajes y turismo] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1379,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agencia Y tiene_letrero = si",avisos = [Agencia de viajes y turismo] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1380,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = agencia Y area = a1","avisos = [Agencia de viajes y turismo] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1381,avisos,rubro = agencia Y trabajadores = t0,"avisos = [Agencia de viajes y turismo] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud 

independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1382,documentos,rubro = metalmecanica Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Declaración de medidas de control de ruido (según ordenanza),Documento propio del giro «Carpintería metálica / de madera» (ruido).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1383,documentos,rubro = metalmecanica Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Hojas de seguridad (SDS) y relación de productos químicos almacenados,Documento propio del giro «Carpintería metálica / de madera» (quimicos).,D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1384,documentos,rubro = metalmecanica Y req.ITSE_BASICA = True,docs.ITSE_BASICA = Descripción de control de polvo y mantenimiento de maquinaria,Documento propio del giro «Carpintería metálica / de madera» (polvo).,D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1385,documentos,rubro = metalmecanica Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Carpintería metálica / de madera» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1386,avisos,rubro = metalmecanica Y regimen = NRUS,"avisos = [Carpintería metálica / de madera / NRUS] El nrus limita compras y ventas mensuales; si produce y compra insumos en volumen, probablemente deba cambiar de régimen.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1387,avisos,rubro = metalmecanica Y regimen = RER,avisos = [Carpintería metálica / de madera / RER] Registre compras de materia prima y ventas; valore sus activos fijos frente al tope del régimen.,Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1388,avisos,rubro = metalmecanica Y regimen = RMT,avisos = [Carpintería metálica / de madera / RMT] Lleve registros de compras y ventas y sustente la materia prima con comprobantes para deducir costos.,Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1389,avisos,rubro = metalmecanica Y regimen = RG,avisos = [Carpintería metálica / de madera / RG] Lleve contabilidad completa con costos de producción e inventarios.,Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1390,avisos,rubro = metalmecanica Y tamano = micro,avisos = [Carpintería metálica / de madera] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1391,avisos,rubro = metalmecanica Y tamano = pequena,"avisos = [Carpintería metálica / de madera] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1392,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = metalmecanica Y tiene_letrero = si",avisos = [Carpintería metálica / de madera] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1393,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = metalmecanica Y area = a1","avisos = [Carpintería metálica / de madera] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1394,avisos,rubro = metalmecanica Y trabajadores = t0,"avisos = [Carpintería metálica / de madera] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1395,documentos,rubro = artesania Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Denominación comercial/marca que se usará en el letrero,"Documento propio del giro «Artesanía (textil, paja, cerámica)» (marca).",Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1396,avisos,rubro = artesania Y regimen = NRUS,"avisos = [Artesanía (textil, paja, cerámica) / NRUS] El nrus limita compras y ventas mensuales; si produce y 

compra insumos en volumen, probablemente deba cambiar de régimen.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1397,avisos,rubro = artesania Y regimen = RER,"avisos = [Artesanía (textil, paja, cerámica) / RER] Registre compras de materia prima y ventas; valore sus activos fijos frente al tope del régimen.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1398,avisos,rubro = artesania Y regimen = RMT,"avisos = [Artesanía (textil, paja, cerámica) / RMT] Lleve registros de compras y ventas y sustente la materia prima con comprobantes para deducir costos.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1399,avisos,rubro = artesania Y regimen = RG,"avisos = [Artesanía (textil, paja, cerámica) / RG] Lleve contabilidad completa con costos de producción e inventarios.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1400,avisos,rubro = artesania Y tamano = micro,"avisos = [Artesanía (textil, paja, cerámica)] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1401,avisos,rubro = artesania Y tamano = pequena,"avisos = [Artesanía (textil, paja, cerámica)] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1402,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = artesania Y tiene_letrero = si","avisos = [Artesanía (textil, paja, cerámica)] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.",El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1403,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = artesania Y area = a1","avisos = [Artesanía (textil, paja, cerámica)] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener 

extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1404,avisos,rubro = artesania Y trabajadores = t0,"avisos = [Artesanía (textil, paja, cerámica)] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1405,documentos,rubro = confecciones Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Muestra de etiqueta o ficha de productos (si se solicita),Documento propio del giro «Confección de prendas y calzado» (etiquetado).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1406,documentos,rubro = confecciones Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Denominación comercial/marca que se usará en el letrero,Documento propio del giro «Confección de prendas y calzado» (marca).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1407,documentos,rubro = confecciones Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Declaración de medidas de control de ruido (según ordenanza),Documento propio del giro «Confección de prendas y calzado» (ruido).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1408,avisos,rubro = confecciones Y regimen = NRUS,"avisos = [Confección de prendas y calzado / NRUS] El nrus limita compras y ventas mensuales; si produce y compra insumos en volumen, probablemente deba cambiar de régimen.",Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1409,avisos,rubro = confecciones Y regimen = RER,avisos = [Confección de prendas y calzado / RER] Registre compras de materia prima y ventas; valore sus activos fijos frente al tope del régimen.,Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1410,avisos,rubro = confecciones Y regimen = RMT,avisos = [Confección de prendas y calzado / RMT] Lleve registros de compras y ventas y sustente la materia prima con comprobantes para deducir costos.,Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1411,avisos,rubro = confecciones Y regimen = RG,avisos = [Confección de prendas y calzado / RG] Lleve contabilidad completa con costos de producción e inventarios.,Obligaciones tributarias típicas de un negocio de tipo produccion en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1412,avisos,rubro = confecciones Y tamano = micro,avisos = [Confección de prendas y calzado] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1413,avisos,rubro = confecciones Y tamano = pequena,"avisos = [Confección de prendas y calzado] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1414,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = confecciones Y tiene_letrero = si",avisos = [Confección de prendas y calzado] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1415,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = confecciones Y area = a1","avisos = [Confección de prendas y calzado] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1416,avisos,rubro = confecciones Y trabajadores = t0,"avisos = [Confección de prendas y calzado] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1417,documentos,rubro = licores Y req.AUTORIZ_ALCOHOL = 

True,docs.AUTORIZ_ALCOHOL = Compromiso de no vender a menores y respetar horarios,Documento propio del giro «Distribuidora / venta de licores» (alcohol_menores).,Ley 28681 (bebidas alcohólicas) y ordenanza municipal -- puede variar según el TUPA 

R1418,documentos,rubro = licores Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos 

sólidos (si la municipalidad lo solicita),Documento propio del giro «Distribuidora / venta de licores» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1419,avisos,rubro = licores Y regimen = NRUS,avisos = [Distribuidora / venta de licores / NRUS] Emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1420,avisos,rubro = licores Y regimen = RER,"avisos = [Distribuidora / venta de licores / RER] Registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1421,avisos,rubro = licores Y regimen = RMT,avisos = [Distribuidora / venta de licores / RMT] Lleve los registros exigidos según su nivel de ingresos y sustente sus compras con comprobantes para deducir gastos.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1422,avisos,rubro = licores Y regimen = RG,avisos = [Distribuidora / venta de licores / RG] Lleve contabilidad completa con control de inventarios y pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1423,avisos,rubro = licores Y tamano = micro,avisos = [Distribuidora / venta de licores] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1424,avisos,rubro = licores Y tamano = pequena,"avisos = [Distribuidora / venta de licores] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1425,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = licores Y tiene_letrero = si",avisos = [Distribuidora / venta de licores] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no 

autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1426,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = licores Y area = a1","avisos = [Distribuidora / venta de licores] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1427,avisos,rubro = licores Y trabajadores = t0,"avisos = [Distribuidora / venta de licores] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1428,documentos,rubro = autopartes Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Compromiso de manejo de residuos sólidos (si la municipalidad lo solicita),Documento propio del giro «Venta de repuestos y autopartes» (residuos).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1429,documentos,rubro = autopartes Y req.ITSE_BASICA = 

True,docs.ITSE_BASICA = Hojas de seguridad (SDS) y relación de productos químicos almacenados,Documento propio del giro «Venta de repuestos y autopartes» (quimicos).,D.S. 002-2018-PCM (Reglamento de ITSE) -- puede variar según el TUPA 

R1430,avisos,rubro = autopartes Y regimen = NRUS,avisos = [Venta de repuestos y autopartes / NRUS] Emita boleta por cada venta y conserve sus comprobantes de compra; las compras mensuales también tienen tope.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1431,avisos,rubro = autopartes Y regimen = RER,"avisos = [Venta de repuestos y autopartes / RER] Registre compras y ventas, emita comprobantes y vigile los topes de ingresos y de compras del régimen.",Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1432,avisos,rubro = autopartes Y regimen = RMT,avisos = [Venta de repuestos y autopartes / RMT] Lleve los registros exigidos según su nivel de ingresos y sustente sus compras con comprobantes para deducir gastos.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1433,avisos,rubro = autopartes Y regimen = RG,avisos = [Venta de repuestos y autopartes / RG] Lleve contabilidad completa con control de inventarios y pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo comercio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1434,avisos,rubro = autopartes Y tamano = micro,avisos = [Venta de repuestos y autopartes] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1435,avisos,rubro = autopartes Y tamano = pequena,"avisos = [Venta de repuestos y autopartes] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1436,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = autopartes Y tiene_letrero = si",avisos = [Venta de repuestos y autopartes] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1437,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = autopartes Y area = a1","avisos = [Venta de repuestos y autopartes] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1438,avisos,rubro = autopartes Y trabajadores = t0,"avisos = [Venta de repuestos y autopartes] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1439,documentos,rubro = veterinaria Y req.LICENCIA_FUNCIONAMIENTO = True,docs.LICENCIA_FUNCIONAMIENTO = Contrato o compromiso con EO-RS para residuos biocontaminados,Documento propio del giro «Veterinaria / pet shop» (residuos_bio).,Ley 28976 (Ley Marco de Licencia de Funcionamiento) y TUPA municipal -- puede variar según el TUPA 

R1440,avisos,rubro = veterinaria Y regimen = NRUS,avisos = [Veterinaria / pet shop / NRUS] Emita boleta por cada servicio; si presta servicios a empresas que piden factura deberá cambiar de régimen.,Obligaciones tributarias típicas de un negocio 

de tipo servicio en el régimen NRUS.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1441,avisos,rubro = veterinaria Y regimen = RER,avisos = [Veterinaria / pet shop / RER] Emita comprobantes por cada servicio y registre ingresos y compras; vigile el tope del régimen.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RER.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1442,avisos,rubro = veterinaria Y regimen = RMT,avisos = [Veterinaria / pet shop / RMT] Registre ingresos y gastos con comprobantes; los pagos de honorarios y servicios deben sustentarse.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RMT.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1443,avisos,rubro = veterinaria Y regimen = RG,avisos = [Veterinaria / pet shop / RG] Lleve contabilidad completa; los servicios facturados generan pagos a cuenta mensuales.,Obligaciones tributarias típicas de un negocio de tipo servicio en el régimen RG.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- validar con el contador experto 

R1444,avisos,rubro = veterinaria Y tamano = micro,avisos = [Veterinaria / pet shop] Como microempresa puede acogerse al régimen laboral especial MYPE (con beneficios laborales reducidos frente al régimen general); acredite su inscripción en el REMYPE.,El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1445,avisos,rubro = veterinaria Y tamano = pequena,"avisos = [Veterinaria / pet shop] Como pequeña empresa puede acogerse al régimen laboral especial MYPE, con más beneficios que la microempresa; acredite su inscripción en el REMYPE.",El tamaño de la empresa define el régimen laboral especial aplicable.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) -- verificar vigencia 

R1446,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = veterinaria Y tiene_letrero = si",avisos = [Veterinaria / pet shop] El letrero debe coincidir con el giro de la licencia; no anuncie actividades no autorizadas.,El anuncio se autoriza según el giro y las dimensiones permitidas.,Ordenanza municipal de anuncios y avisos publicitarios 

R1447,avisos,"local ∈ ('propio', 'alquilado', 'domicilio', 'mercado', 'ninguno_aun') Y rubro = veterinaria Y area = a1","avisos = [Veterinaria / pet shop] Con hasta 100 m² el trámite de seguridad suele ser más simple, pero igual debe tener extintor, señalización y salida despejada.","Menor área reduce el nivel de riesgo, no elimina las exigencias.",D.S. 002-2018-PCM (Reglamento de ITSE) 

R1448,avisos,rubro = veterinaria Y trabajadores = t0,"avisos = [Veterinaria / pet shop] Si familiares o ayudantes reciben pago regular, deben registrarse como trabajadores; si trabaja solo, considere aun así un seguro de salud (EsSalud independiente o SIS).",Toda relación laboral remunerada genera obligaciones.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1449,distrito,distrito = Chiclayo Y local = propio,avisos = [Chiclayo / local propio] Presente los trámites municipales en la Municipalidad Provincial de Chiclayo; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1450,distrito,distrito = Chiclayo Y local = alquilado,avisos = [Chiclayo / local alquilado] Presente los trámites municipales en la Municipalidad Provincial de Chiclayo; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1451,distrito,distrito = Chiclayo Y local = domicilio,avisos = [Chiclayo / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Provincial de Chiclayo; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1452,distrito,distrito = Chiclayo Y local = mercado,avisos = [Chiclayo / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Provincial de Chiclayo; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1453,distrito,distrito = Chiclayo Y local = ambulante,avisos = [Chiclayo / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Provincial de Chiclayo; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1454,distrito,distrito = Chiclayo Y local = ninguno_aun,avisos = [Chiclayo / aún no tengo local] Presente los trámites municipales en la Municipalidad Provincial de Chiclayo; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1455,distrito,distrito = José Leonardo Ortiz Y local = propio,avisos = [José Leonardo Ortiz / local propio] Presente los trámites municipales en la Municipalidad Distrital de José Leonardo Ortiz; tenga a mano el título o partida del 

local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1456,distrito,distrito = José Leonardo Ortiz Y local = alquilado,avisos = [José Leonardo Ortiz / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de José Leonardo Ortiz; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1457,distrito,distrito = José Leonardo Ortiz Y local = domicilio,avisos = [José Leonardo Ortiz / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de José Leonardo Ortiz; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1458,distrito,distrito = José Leonardo Ortiz Y local = mercado,avisos = [José Leonardo Ortiz / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de José Leonardo Ortiz; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1459,distrito,distrito = José Leonardo Ortiz Y local = ambulante,avisos = [José Leonardo Ortiz / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de José Leonardo Ortiz; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1460,distrito,distrito = José Leonardo Ortiz Y local = ninguno_aun,avisos = [José Leonardo Ortiz / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de José Leonardo Ortiz; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1461,distrito,distrito = La Victoria Y local = propio,avisos = [La Victoria / local propio] Presente los trámites municipales en la Municipalidad Distrital de La Victoria; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1462,distrito,distrito = La Victoria Y local = alquilado,avisos = [La Victoria / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de La Victoria; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1463,distrito,distrito = La Victoria Y local = domicilio,avisos = [La Victoria / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de La Victoria; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1464,distrito,distrito = La Victoria Y local = mercado,avisos = [La Victoria / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de La Victoria; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1465,distrito,distrito = La Victoria Y local = ambulante,avisos = [La Victoria / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de La Victoria; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1466,distrito,distrito = La Victoria Y local = ninguno_aun,avisos = [La Victoria / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de La Victoria; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1467,distrito,distrito = Pimentel Y local = propio,avisos = [Pimentel / local propio] Presente los trámites municipales en la Municipalidad Distrital de Pimentel; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1468,distrito,distrito = Pimentel Y local = alquilado,avisos = [Pimentel / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Pimentel; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1469,distrito,distrito = Pimentel Y local = domicilio,avisos = [Pimentel / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Pimentel; pregunte si su zona permite actividad comercial en vivienda. 

Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1470,distrito,distrito = Pimentel Y local = mercado,avisos = [Pimentel / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Pimentel; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1471,distrito,distrito = Pimentel Y local = ambulante,avisos = [Pimentel / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Pimentel; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1472,distrito,distrito = Pimentel Y local = ninguno_aun,avisos = [Pimentel / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Pimentel; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1473,distrito,distrito = Monsefú Y local = propio,avisos = [Monsefú / local propio] Presente los trámites municipales en la Municipalidad Distrital de Monsefú; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1474,distrito,distrito = Monsefú Y local = alquilado,avisos = [Monsefú / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Monsefú; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1475,distrito,distrito = Monsefú Y local = domicilio,avisos = [Monsefú / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Monsefú; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1476,distrito,distrito = Monsefú Y local = mercado,avisos = [Monsefú / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Monsefú; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1477,distrito,distrito = Monsefú Y local = ambulante,avisos = [Monsefú / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Monsefú; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1478,distrito,distrito = Monsefú Y local = ninguno_aun,avisos = [Monsefú / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Monsefú; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1479,distrito,distrito = Reque Y local = propio,avisos = [Reque / local propio] Presente los trámites municipales en la Municipalidad Distrital de Reque; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1480,distrito,distrito = Reque Y local = alquilado,avisos = [Reque / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Reque; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1481,distrito,distrito = Reque Y local = domicilio,avisos = [Reque / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Reque; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1482,distrito,distrito = Reque Y local = mercado,avisos = [Reque / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Reque; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1483,distrito,distrito = Reque Y local = ambulante,avisos = [Reque / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Reque; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1484,distrito,distrito = Reque Y local = ninguno_aun,avisos = [Reque / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Reque; consulte el certificado de zonificación antes de elegir el local. Revise el 

TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1485,distrito,distrito = Pomalca Y local = propio,avisos = [Pomalca / local propio] Presente los trámites municipales en la Municipalidad Distrital de Pomalca; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1486,distrito,distrito = Pomalca Y local = alquilado,avisos = [Pomalca / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Pomalca; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1487,distrito,distrito = Pomalca Y local = domicilio,avisos = [Pomalca / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Pomalca; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1488,distrito,distrito = Pomalca Y local = mercado,avisos = [Pomalca / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Pomalca; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1489,distrito,distrito = Pomalca Y local = ambulante,avisos = [Pomalca / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Pomalca; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1490,distrito,distrito = Pomalca Y local = ninguno_aun,avisos = [Pomalca / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Pomalca; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1491,distrito,distrito = Tumán Y local = propio,avisos = [Tumán / local propio] Presente los trámites municipales en la Municipalidad Distrital de Tumán; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1492,distrito,distrito = Tumán Y local = alquilado,avisos = [Tumán / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Tumán; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1493,distrito,distrito = Tumán Y local = domicilio,avisos = [Tumán / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Tumán; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1494,distrito,distrito = Tumán Y local = mercado,avisos = [Tumán / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Tumán; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1495,distrito,distrito = Tumán Y local = ambulante,avisos = [Tumán / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Tumán; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1496,distrito,distrito = Tumán Y local = ninguno_aun,avisos = [Tumán / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Tumán; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1497,distrito,distrito = Santa Rosa Y local = propio,avisos = [Santa Rosa / local propio] Presente los trámites municipales en la Municipalidad Distrital de Santa Rosa; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1498,distrito,distrito = Santa Rosa Y local = alquilado,avisos = [Santa Rosa / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Santa Rosa; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1499,distrito,distrito = Santa Rosa Y local = domicilio,avisos = [Santa Rosa / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Santa Rosa; pregunte si su zona permite actividad comercial en 

vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1500,distrito,distrito = Santa Rosa Y local = mercado,avisos = [Santa Rosa / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Santa Rosa; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1501,distrito,distrito = Santa Rosa Y local = ambulante,avisos = [Santa Rosa / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Santa Rosa; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1502,distrito,distrito = Santa Rosa Y local = ninguno_aun,avisos = [Santa Rosa / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Santa Rosa; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1503,distrito,distrito = Eten Y local = propio,avisos = [Eten / local propio] Presente los trámites municipales en la Municipalidad Distrital de Eten; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1504,distrito,distrito = Eten Y local = alquilado,avisos = [Eten / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Eten; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1505,distrito,distrito = Eten Y local = domicilio,avisos = [Eten / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Eten; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1506,distrito,distrito = Eten Y local = mercado,avisos = [Eten / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Eten; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1507,distrito,distrito = Eten Y local = ambulante,avisos = [Eten / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Eten; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1508,distrito,distrito = Eten Y local = ninguno_aun,avisos = [Eten / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Eten; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1509,distrito,distrito = Lambayeque Y local = propio,avisos = [Lambayeque / local propio] Presente los trámites municipales en la Municipalidad Provincial de Lambayeque; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1510,distrito,distrito = Lambayeque Y local = alquilado,avisos = [Lambayeque / local alquilado] Presente los trámites municipales en la Municipalidad Provincial de Lambayeque; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1511,distrito,distrito = Lambayeque Y local = domicilio,avisos = [Lambayeque / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Provincial de Lambayeque; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1512,distrito,distrito = Lambayeque Y local = mercado,avisos = [Lambayeque / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Provincial de Lambayeque; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1513,distrito,distrito = Lambayeque Y local = ambulante,avisos = [Lambayeque / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Provincial de Lambayeque; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1514,distrito,distrito = Lambayeque Y local = ninguno_aun,avisos = [Lambayeque / aún no tengo local] Presente los trámites municipales en la Municipalidad Provincial de Lambayeque; consulte el certificado de zonificación antes de elegir 

el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1515,distrito,distrito = Mochumí Y local = propio,avisos = [Mochumí / local propio] Presente los trámites municipales en la Municipalidad Distrital de Mochumí; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1516,distrito,distrito = Mochumí Y local = alquilado,avisos = [Mochumí / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Mochumí; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1517,distrito,distrito = Mochumí Y local = domicilio,avisos = [Mochumí / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Mochumí; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1518,distrito,distrito = Mochumí Y local = mercado,avisos = [Mochumí / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Mochumí; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1519,distrito,distrito = Mochumí Y local = ambulante,avisos = [Mochumí / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Mochumí; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1520,distrito,distrito = Mochumí Y local = ninguno_aun,avisos = [Mochumí / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Mochumí; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1521,distrito,distrito = Túcume Y local = propio,avisos = [Túcume / local propio] Presente los trámites municipales en la Municipalidad Distrital de Túcume; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1522,distrito,distrito = Túcume Y local = alquilado,avisos = [Túcume / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Túcume; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1523,distrito,distrito = Túcume Y local = domicilio,avisos = [Túcume / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Túcume; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1524,distrito,distrito = Túcume Y local = mercado,avisos = [Túcume / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Túcume; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1525,distrito,distrito = Túcume Y local = ambulante,avisos = [Túcume / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Túcume; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1526,distrito,distrito = Túcume Y local = ninguno_aun,avisos = [Túcume / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Túcume; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1527,distrito,distrito = Ferreñafe Y local = propio,avisos = [Ferreñafe / local propio] Presente los trámites municipales en la Municipalidad Provincial de Ferreñafe; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1528,distrito,distrito = Ferreñafe Y local = alquilado,avisos = [Ferreñafe / local alquilado] Presente los trámites municipales en la Municipalidad Provincial de Ferreñafe; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1529,distrito,distrito = Ferreñafe Y local = domicilio,avisos = [Ferreñafe / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Provincial de Ferreñafe; pregunte si su zona permite actividad comercial en 

vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1530,distrito,distrito = Ferreñafe Y local = mercado,avisos = [Ferreñafe / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Provincial de Ferreñafe; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1531,distrito,distrito = Ferreñafe Y local = ambulante,avisos = [Ferreñafe / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Provincial de Ferreñafe; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1532,distrito,distrito = Ferreñafe Y local = ninguno_aun,avisos = [Ferreñafe / aún no tengo local] Presente los trámites municipales en la Municipalidad Provincial de Ferreñafe; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1533,distrito,distrito = Pueblo Nuevo Y local = propio,avisos = [Pueblo Nuevo / local propio] Presente los trámites municipales en la Municipalidad Distrital de Pueblo Nuevo; tenga a mano el título o partida del local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1534,distrito,distrito = Pueblo Nuevo Y local = alquilado,avisos = [Pueblo Nuevo / local alquilado] Presente los trámites municipales en la Municipalidad Distrital de Pueblo Nuevo; lleve el contrato de alquiler y la autorización del propietario legalizada. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1535,distrito,distrito = Pueblo Nuevo Y local = domicilio,avisos = [Pueblo Nuevo / en mi domicilio / vivienda] Presente los trámites municipales en la Municipalidad Distrital de Pueblo Nuevo; pregunte si su zona permite actividad comercial en vivienda. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1536,distrito,distrito = Pueblo Nuevo Y local = mercado,avisos = [Pueblo Nuevo / puesto en mercado o galería] Presente los trámites municipales en la Municipalidad Distrital de Pueblo Nuevo; coordine primero con la administración del mercado. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1537,distrito,distrito = Pueblo Nuevo Y local = ambulante,avisos = [Pueblo Nuevo / ambulante (sin local fijo)] Presente los trámites municipales en la Municipalidad Distrital de Pueblo Nuevo; pregunte por las zonas y horarios habilitados para comercio ambulatorio. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1538,distrito,distrito = Pueblo Nuevo Y local = ninguno_aun,avisos = [Pueblo Nuevo / aún no tengo local] Presente los trámites municipales en la Municipalidad Distrital de Pueblo Nuevo; consulte el certificado de zonificación antes de elegir el local. Revise el TUPA vigente en su portal institucional.,Cada municipalidad tiene su propio TUPA y ordenanzas.,TUPA de la municipalidad 

R1539,avisos,regimen = NRUS Y trabajadores = t0,avisos = [Régimen NRUS / solo yo (o familiares sin planilla)] Como está sin planilla: sus ingresos y compras siguen sujetos a los topes del régimen.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1540,avisos,regimen = NRUS Y trabajadores = t1,avisos = [Régimen NRUS / de 1 a 10 trabajadores] Como está con personal: declare planilla electrónica (PLAME) y pague aportes mensuales además del impuesto del régimen.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1541,avisos,regimen = NRUS Y trabajadores = t2,avisos = [Régimen NRUS / más de 10 trabajadores] Como está con más de 10 trabajadores: revise obligaciones laborales y tributarias reforzadas; se recomienda contador y asesoría laboral.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (TRegistro y PLAME) 

R1542,avisos,regimen = RER Y trabajadores = t0,avisos = [Régimen RER / solo yo (o familiares sin planilla)] Como está sin planilla: sus ingresos y compras siguen sujetos a los topes del régimen.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1543,avisos,regimen = RER Y trabajadores = t1,avisos = [Régimen RER / de 1 a 10 trabajadores] Como está con personal: declare planilla electrónica (PLAME) y pague aportes mensuales además del impuesto del régimen.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1544,avisos,regimen = RER Y trabajadores = t2,avisos = [Régimen RER / más de 10 trabajadores] Como está con más de 10 trabajadores: revise obligaciones laborales y tributarias reforzadas; se recomienda contador y asesoría laboral.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (TRegistro y PLAME) 

R1545,avisos,regimen = RMT Y trabajadores = t0,avisos = [Régimen RMT / solo yo (o familiares sin planilla)] Como está sin planilla: sus ingresos y compras siguen sujetos a los topes del régimen.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1546,avisos,regimen = RMT Y trabajadores = t1,avisos = [Régimen RMT / de 1 a 10 trabajadores] Como está con personal: declare planilla electrónica (PLAME) y pague aportes mensuales además del impuesto del régimen.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1547,avisos,regimen = RMT Y trabajadores = t2,avisos = [Régimen RMT / más de 10 trabajadores] Como está con más de 10 trabajadores: revise obligaciones laborales y tributarias reforzadas; se recomienda contador y asesoría laboral.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (TRegistro y PLAME) 

R1548,avisos,regimen = RG Y trabajadores = t0,avisos = [Régimen RG / solo yo (o familiares sin planilla)] Como está sin planilla: sus ingresos y compras siguen sujetos a los topes del régimen.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1549,avisos,regimen = RG Y trabajadores = t1,avisos = [Régimen RG / de 1 a 10 trabajadores] Como está con personal: declare planilla electrónica (PLAME) y pague aportes mensuales además del impuesto del régimen.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (T-Registro y PLAME) 

R1550,avisos,regimen = RG Y trabajadores = t2,avisos = [Régimen RG / más de 10 trabajadores] Como está con más de 10 trabajadores: revise obligaciones laborales y tributarias reforzadas; se recomienda contador y asesoría laboral.,El régimen tributario y la planilla se declaran por separado.,D.S. 018-2007-TR (TRegistro y PLAME) 

R1551,avisos,ingresos = B1 Y trabajadores = t0,avisos = [Ventas B1 / solo yo (o familiares sin planilla)] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1552,avisos,ingresos = B1 Y trabajadores = t1,avisos = [Ventas B1 / de 1 a 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1553,avisos,ingresos = B1 Y trabajadores = t2,avisos = [Ventas B1 / más de 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar 

contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1554,avisos,ingresos = B2 Y trabajadores = t0,avisos = [Ventas B2 / solo yo (o familiares sin planilla)] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1555,avisos,ingresos = B2 Y trabajadores = t1,avisos = [Ventas B2 / de 1 a 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1556,avisos,ingresos = B2 Y trabajadores = t2,avisos = [Ventas B2 / más de 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1557,avisos,ingresos = B3 Y trabajadores = t0,avisos = [Ventas B3 / solo yo (o familiares sin planilla)] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1558,avisos,ingresos = B3 Y trabajadores = t1,avisos = [Ventas B3 / de 1 a 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1559,avisos,ingresos = B3 Y trabajadores = t2,avisos = [Ventas B3 / más de 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1560,avisos,ingresos = B4 Y trabajadores = t0,avisos = [Ventas B4 / solo yo (o familiares sin planilla)] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1561,avisos,ingresos = B4 Y trabajadores = t1,avisos = [Ventas B4 / de 1 a 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1562,avisos,ingresos = B4 Y trabajadores = t2,avisos = [Ventas B4 / más de 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar 

contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1563,avisos,ingresos = B5 Y trabajadores = t0,avisos = [Ventas B5 / solo yo (o familiares sin planilla)] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1564,avisos,ingresos = B5 Y trabajadores = t1,avisos = [Ventas B5 / de 1 a 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1565,avisos,ingresos = B5 Y trabajadores = t2,avisos = [Ventas B5 / más de 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1566,avisos,ingresos = B6 Y trabajadores = t0,avisos = [Ventas B6 / solo yo (o familiares sin planilla)] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1567,avisos,ingresos = B6 Y trabajadores = t1,avisos = [Ventas B6 / de 1 a 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1568,avisos,ingresos = B6 Y trabajadores = t2,avisos = [Ventas B6 / más de 10 trabajadores] Compare el costo de planilla con sus ventas anuales al planificar contrataciones y su régimen.,La carga laboral incide en la viabilidad del negocio.,TUO Ley MYPE (D.S. 013-2013-PRODUCE) 

R1569,avisos,ingresos = B1 Y persona = natural,"avisos = [Ventas: hasta s/ 96,000 al año (≈ s/ 8,000 al mes)] Está en el nivel más bajo de ventas: vigile mes a mes sus ventas y compras para saber cuándo debe cambiar de régimen.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1570,avisos,ingresos = B1 Y persona = juridica,"avisos = [Ventas: hasta s/ 96,000 al año (≈ s/ 8,000 al mes)] Está en el nivel más bajo de ventas: vigile mes a mes sus ventas y compras para saber cuándo debe cambiar de régimen.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1571,avisos,ingresos = B2 Y persona = natural,"avisos = [Ventas: de s/ 96,001 a s/ 240,000 al año (≈ hasta s/ 20,000 al mes)] Está cerca del tope del NRUS: si lo supera deberá pasar al RER o RMT.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1572,avisos,ingresos = B2 Y persona = juridica,"avisos = [Ventas: de s/ 96,001 a s/ 240,000 al año (≈ hasta s/ 20,000 al mes)] Está cerca del tope del NRUS: si lo supera deberá pasar al RER o RMT.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1573,avisos,ingresos = B3 Y persona = natural,"avisos = [Ventas: de s/ 240,001 a s/ 525,000 al año] Con ventas sobre el tope del NRUS corresponde RER o RMT; compare cuotas y obligaciones con un contador.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1574,avisos,ingresos = B3 Y persona = juridica,"avisos = [Ventas: de s/ 240,001 a s/ 525,000 al año] Con ventas sobre el tope del NRUS corresponde RER o RMT; compare cuotas y obligaciones con un contador.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1575,avisos,ingresos = B4 Y persona = natural,"avisos = [Ventas: de s/ 525,001 a s/ 825,000 al año (hasta 150 uit)] Con estas ventas el RMT es el régimen habitual y exige más registros.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1576,avisos,ingresos = B4 Y persona = juridica,"avisos = [Ventas: de s/ 525,001 a s/ 825,000 al año (hasta 150 uit)] Con estas ventas el RMT es el régimen habitual y exige más registros.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1577,avisos,ingresos = B5 Y persona = natural,"avisos = [Ventas: de s/ 825,001 a s/ 9,350,000 al año (hasta 1,700 uit)] Con estas ventas se aplica el RMT con tasas por tramos; se recomienda contador.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1578,avisos,ingresos = B5 Y persona = juridica,"avisos = [Ventas: de s/ 825,001 a s/ 9,350,000 al año (hasta 1,700 uit)] Con estas ventas se aplica el RMT con tasas por tramos; se recomienda contador.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1579,avisos,ingresos = B6 Y persona = natural,"avisos = [Ventas: más de s/ 9,350,000 al año] Con estas ventas se aplica el Régimen General y se sale de las definiciones MYPE.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

R1580,avisos,ingresos = B6 Y persona = juridica,"avisos = [Ventas: más de s/ 9,350,000 al año] Con estas ventas se aplica el Régimen General y se sale de las definiciones MYPE.",El régimen depende del nivel de ventas.,D.Leg. 937 (NRUS/RER) y D.Leg. 1269 (RMT); Ley del Impuesto a la Renta -- verificar topes 

