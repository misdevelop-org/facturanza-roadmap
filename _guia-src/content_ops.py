from template import h2, h3, p, ul, ol, code, who, call, cards, table, matrix, shots, single

PAGES = {}

# ---------------------------------------------------------------- clientes
PAGES["clientes.html"] = dict(
    title="Clientes",
    nav="Clientes",
    desc="Registra a tus clientes con datos oficiales de Hacienda para facturar sin errores.",
    body=shots("clientes_menu", "Clientes")
    + who("ver: todos los roles · crear y editar: Propietario, Administrador y Gerente")
    + h2("crear", "1. Agregar un cliente")
    + ol(["Ve a <strong>Clientes</strong> y toca <strong>Crear cliente</strong>."])
    + single("clientes_crear", "Botón Crear cliente en la pantalla Clientes", width="max-w-[690px]")
    + shots("clientes_form", "Formulario Nuevo cliente")
    + ol(["Escribe la <strong>cédula</strong>. Al llegar a 9 dígitos, Facturanza consulta a Hacienda y completa el nombre, el tipo de identificación y las actividades económicas. Se muestran también el <strong>régimen</strong> y la <strong>situación tributaria</strong> (solo lectura)."], start=2)
    + single("clientes_cedula", "Al escribir la cédula, Facturanza consulta a Hacienda", width="max-w-[560px]")
    + ol(["Si el cliente tiene varias actividades, elige la <strong>actividad económica prioritaria al facturar</strong>."], start=3)
    + single("clientes_actividad", "Elige la actividad económica prioritaria al facturar", width="max-w-[560px]")
    + ol(["Agrega <strong>correo</strong> y <strong>teléfono</strong> (con código de país)."], start=4)
    + single("clientes_contacto", "Información de contacto", width="max-w-[560px]")
    + ol(["Completa la <strong>ubicación</strong>: provincia, cantón, distrito y <strong>dirección exacta*</strong>. Toca <strong>Guardar</strong>."], start=5)
    + single("clientes_ubicacion", "Ubicación del cliente", width="max-w-[560px]")
    + call("warn", "Cliente sin cédula", "Marca <strong>El cliente no cuenta con cédula</strong> y escribe el <strong>nombre de la empresa</strong>. Estos clientes solo se pueden usar en <strong>Tiquetes</strong>; una Factura requiere cédula.")
    + p("No puedes registrar dos clientes con la misma cédula. Cada cliente guarda <strong>un correo</strong>; para enviar un documento a más personas, agrégalas como destinatarios al crear la factura o al reenviarla.")
    + h2("cedulas", "2. Tipos de identificación")
    + table(["Tipo", "Dígitos", "Ejemplo"], [
        ["Cédula física", "9", "1-1234-0567"],
        ["Cédula jurídica", "10", "3-101-123456"],
        ["DIMEX (extranjeros residentes)", "11 o 12", "—"],
        ["NITE", "10", "—"],
    ])
    + p("Ver las facturas de un cliente: filtra la lista de Facturas por ese cliente. Facturanza no maneja cuentas por cobrar ni saldos por cliente."),
)

# ---------------------------------------------------------------- productos
PAGES["productos.html"] = dict(
    title="Productos y CABYS",
    nav="Productos y CABYS",
    desc="Tu catálogo de bienes y servicios con código CABYS, impuesto, moneda y unidad de medida.",
    body=shots("productos_menu", "Productos")
    + who("ver: todos los roles · crear y editar: Propietario, Administrador y Gerente")
    + h2("cabys", "1. El código CABYS")
    + p("Todo producto o servicio facturado lleva un código del <strong>Catálogo de Bienes y Servicios (CABYS)</strong> de <strong>13 dígitos</strong>. El código define la tarifa de IVA. Facturanza valida que tenga 13 dígitos y te ofrece <strong>Buscar CABYS</strong>: escribe una descripción en palabras comunes y elige entre los resultados (se muestran código, tarifa, descripción y categorías).")
    + p("Toca <strong>Buscar CABYS</strong> en el formulario, describe el producto con palabras comunes (o escribe el código de 13 dígitos) y elige un resultado: se completan el código y la tarifa de IVA.")
    + single("productos_cabys", "Buscador de CABYS", width="max-w-[260px]")
    + h2("crear", "2. Crear un producto")
    + shots("productos_form", "Formulario Nuevo producto")
    + ul([
        "<strong>Nombre*</strong>, descripción y código interno del producto.",
        "<strong>Código CABYS*</strong>: tarifa y tipo de impuesto se completan según el código.",
        "<strong>Precio*</strong> y <strong>moneda</strong> (Colones o Dólares). Puedes definir <strong>descuento %</strong>; se muestran subtotal, monto de impuesto y total con impuestos.",
        "<strong>Unidad de medida*</strong>: por ejemplo <em>Sp</em> (servicios profesionales), <em>Os</em> (otro tipo de servicio), <em>Unid</em> (unidad), <em>h</em> (hora), <em>kg</em>, <em>m</em>. Usa la unidad oficial de Hacienda.",
    ])
    + p("Un precio en dólares se convierte a colones al emitir, con el tipo de cambio del documento. En cada producto del catálogo puedes <strong>Duplicar</strong> o <strong>Eliminar</strong>.")
    + h2("ia", "3. Generar con IA")
    + p("¿No sabes el código ni la tarifa? Toca <strong>Generar con IA</strong> y describe tu producto en una frase (hasta 100 caracteres). Facturito propone nombre, CABYS, impuesto y unidad. Cada intento descuenta de <strong>Cantidad de usos restantes</strong>, que depende de tu plan.")
    + single("productos_ia", "Asistente Facturito: describe tu producto", width="max-w-[420px]")
    + single("productos_ia_ok", "Producto generado con éxito: revisa y edita", width="max-w-[420px]")
    + call("warn", "Revisa siempre la tarifa", "La sugerencia de la IA es una ayuda. Confirma el código CABYS y la tarifa de IVA antes de facturar; si no coinciden con la ley, Hacienda puede rechazar el documento. Ver <a class='underline' href='ayuda.html#tarifas'>tarifas de IVA</a>."),
)

# ---------------------------------------------------------------- compras
PAGES["compras.html"] = dict(
    title="Compras",
    nav="Compras",
    desc="Registra las facturas de tus proveedores para tu reporte de IVA. La aceptación ante Hacienda se hace fuera de Facturanza.",
    body=shots("compras_menu", "Compras (agosto 2026)")
    + who("Propietario, Administrador y Contador")
    + call("info", "Mensaje Receptor en el correo de compra", "Cuando una compra entra por el buzón, Facturanza guarda el <strong>XML enviado</strong>, el <strong>XML recibido</strong> (Mensaje Receptor de Hacienda), el <strong>PDF</strong> y el <strong>cuerpo del correo</strong>. Facturanza no envía el Mensaje Receptor; no necesitas enviarlo por TRIBU-CR para registrar la compra. <strong>Próximamente:</strong> al subir una compra a mano también cargarás el XML recibido, y se creará una compra con ambos XML.")
    + h2("subir", "1. Subir facturas de proveedores")
    + shots("compras_subir", "Diálogo Facturas de compra")
    + ol([
        "En <strong>Compras</strong> (o desde Inicio) toca <strong>Subir compra</strong>.",
        "Toca <strong>Seleccionar archivos</strong> y elige uno o varios XML de <strong>Factura Electrónica</strong>.",
        "Toca <strong>Subir archivos</strong>. Facturanza lee emisor, fecha, clave, líneas e impuestos.",
    ])
    + p("Mensajes que puedes ver: <em>no es un XML de factura válido</em> (solo se aceptan Facturas Electrónicas), <em>el receptor no coincide con la identificación de la empresa</em> y <em>ya existe una factura con la clave …</em> (duplicada).")
    + h2("buzon", "2. Buzón automático")
    + who("planes de pago")
    + p("Pide a tus proveedores que envíen sus facturas (XML) a <strong>compras@facturanza.com</strong>. El correo es único para todos; Facturanza asigna cada factura a tu empresa por la <strong>cédula del receptor</strong> que aparece en el XML. La compra aparece en la lista con la leyenda <em>Ingresado automáticamente desde compras@facturanza.com</em>.")
    + ul([
        "En el plan gratuito el buzón no procesa tus correos.",
        "Los tiquetes electrónicos sin receptor identificado se descartan.",
        "Si un proveedor te emite una Factura Electrónica de Compra (FEC), también se registra.",
    ])
    + h2("lista", "3. Consultar y usar tus compras")
    + shots("compras_form", "Detalle de una compra")
    + p("La lista muestra el mes actual; filtra por fecha y busca por proveedor o clave. Las compras registradas alimentan la sección de compras del <a class='underline' href='reportes.html'>reporte de IVA</a> y el gráfico de Egresos de Inicio; también puedes exportarlas a Excel o PDF."),
)

# ---------------------------------------------------------------- facturito
PAGES["facturito.html"] = dict(
    title="Facturito, tu asistente con IA",
    nav="Facturito (IA)",
    desc="Pídele a Facturito que prepare facturas, registre clientes y productos, busque códigos CABYS, resuma ventas y responda dudas tributarias.",
    body=single("facturito_chat", "Chat de Facturito: opciones de inicio", width="max-w-[690px]")
    + h2("donde", "1. Dónde está")
    + p("En <strong>Inicio</strong>, como una barra en la parte inferior. Tócala para abrir el chat en pantalla completa. Si no la ves, actívala en <strong>Negocio › Membresía › Experimentos › Habilitar interfaz de chat Facturito</strong> (depende de tu plan).")
    + h2("hace", "2. Qué puede hacer")
    + cards([
        ("Preparar una factura", "“Facturar ₡45,000 a Juan Pérez por consultoría con 13% de IVA”. Facturito arma un <strong>borrador</strong> (FE o TE) con el IVA calculado."),
        ("Registrar clientes", "Valida la cédula y consulta el padrón de Hacienda."),
        ("Registrar productos y buscar CABYS", "“¿Cuál es el código CABYS para servicios de programación web?”"),
        ("Resumir ventas y gastos", "“¿Cuáles han sido mis ventas de este mes?” o “Generar reporte de gastos de este mes” (PDF)."),
        ("Buscar tus facturas", "Consulta y analiza documentos emitidos."),
        ("Resolver dudas tributarias", "IVA, notas de crédito, Formulario 150, datáfonos, regímenes y más."),
    ], cols=3)
    + call("ok", "Tú confirmas siempre", "Facturito <strong>nunca emite por su cuenta</strong>. Muestra una tarjeta con los datos y dos botones: <strong>Revisar en formulario</strong> o <strong>Emitir factura</strong>; al emitir te pide una confirmación (<em>¿Emitir Factura?</em> › <em>Confirmar y Emitir</em>).")
    + h2("tokens", "3. FacturiTokens y planes")
    + p("El uso de Facturito se mide en <strong>FacturiTokens</strong> (verás <em>⚡ usados / disponibles</em>). En el plan gratuito es una prueba hasta agotar los tokens; después se necesita un plan de pago. También puedes adjuntar archivos en el chat.")
    + h2("limites", "4. Qué no hace")
    + ul([
        "No envía el Mensaje Receptor a Hacienda (solo guarda el que viene en el correo de compra).",
        "No emite Notas de Débito ni Facturas de Exportación (no existen aún en Facturanza).",
        "No lleva cuentas por cobrar.",
        "Es una IA: puede equivocarse. Verifica montos, cédulas y tarifas antes de confirmar y consulta a tu contador en temas fiscales complejos.",
    ]),
)

# ---------------------------------------------------------------- reportes
PAGES["reportes.html"] = dict(
    title="Declaraciones (Formulario 150)",
    nav="Declaraciones",
    desc="Un borrador mensual de tu declaración de IVA, calculado con tus ventas y compras registradas, listo para exportar.",
    body=who("Propietario, Administrador, Contador y Gerente")
    + call("warn", "Es un apoyo, no la declaración", "El reporte <strong>no presenta nada ante Hacienda</strong>. Úsalo para llenar el <strong>Formulario 150 en TRIBU-CR</strong> (reemplazó al antiguo D-104 en octubre de 2025). El plazo es dentro de los <strong>primeros 15 días naturales</strong> del mes siguiente (si cae en feriado o fin de semana, pasa al siguiente día hábil).")
    + h2("declaracion", "1. Pestaña Declaración")
    + shots("declaraciones_declaracion", "Pestaña Declaración")
    + ul([
        "<strong>Liquidación final de IVA</strong>: Débito fiscal efectivo (ventas), Exceso de notas de crédito (Art. 22), Crédito fiscal soportado (compras) y <strong>Impuesto neto a pagar</strong> o <strong>Saldo a favor</strong>. Tócalo para copiar el valor.",
        "<strong>Paso 1</strong> (ventas) y <strong>Paso 3</strong> (compras) desglosados por tarifa: 0%, 0.5%, 1%, 2%, 4%, 8% y 13%, igual que en TRIBU-CR.",
        "<strong>Exportar</strong>: PDF o Excel.",
    ])
    + call("info", "Sobre las compras", "El crédito fiscal usa las compras que registraste o recibiste por el buzón. Facturanza <strong>no verifica</strong> que hayas enviado la aceptación a Hacienda: confírmalo en TRIBU-CR antes de declarar. Ver <a class='underline' href='compras.html'>Compras</a>.")
    + h2("historial", "2. Pestaña Historial y envío automático")
    + shots("declaraciones_historial", "Pestaña Historial")
    + p("El <strong>día 1 de cada mes a las 12:05 a. m.</strong> (hora de Costa Rica) Facturanza genera el reporte del mes anterior, lo guarda en <strong>Historial</strong> y lo envía por correo al Propietario, Administradores y Contadores. Desde Historial puedes descargarlo en PDF o Excel.")
    + h2("otros", "3. Reportes de ingresos y egresos")
    + p("En <strong>Inicio</strong>, los gráficos de Ingresos y Egresos permiten descargar el listado del período en Excel o PDF (por ejemplo, para tu contador). También puedes pedirle a Facturito un resumen de ventas o gastos.")
    + p("Conserva tus comprobantes electrónicos el tiempo que exige la ley (5 años según las fuentes consultadas; confírmalo con tu contador)."),
)
