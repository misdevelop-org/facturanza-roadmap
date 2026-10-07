from template import h2, h3, p, ul, ol, code, who, call, cards, table, matrix, shots, single

PAGES = {}

# ---------------------------------------------------------------- negocio
PAGES["negocio.html"] = dict(
    title="Negocio y credenciales de Hacienda",
    nav="Negocio y credenciales",
    desc="Datos de tu empresa y, lo más importante, cómo conectar Facturanza con Hacienda para poder emitir.",
    body=shots("negocio_facturacion", "Negocio: Mi empresa")
    + p("<strong>Negocio</strong> (la pantalla se titula <em>Mi empresa</em>) tiene a la izquierda los datos de la empresa y a la derecha tres pestañas: <strong>Facturación</strong>, <strong>Roles</strong> y <strong>Membresía</strong>.")
    + h2("empresa", "1. Datos de la empresa")
    + who("ver: Propietario, Administrador, Contador y Gerente · editar: Propietario, Administrador y Contador")
    + ul([
        "<strong>Nombre comercial*</strong>, <strong>correo*</strong>, <strong>teléfono*</strong> y <strong>ubicación</strong>. Aparecen en tus facturas.",
        "<strong>Logo</strong>: PNG, JPG, WebP o SVG. Facturanza lo optimiza (máximo 600 px) para tus PDF.",
        "El <strong>nombre legal</strong>, el tipo de identificación y la cédula vienen de Hacienda y no se editan.",
        "Si tu plan lo permite, puedes agregar <a class='underline' href='marcas.html'>marcas</a>.",
    ])
    + single("negocio_info", "Datos de la empresa (escritorio)", width="max-w-[380px]")
    + single("negocio_info_movil", "Datos de la empresa (tablet y móvil)", width="max-w-[420px]")
    + h2("credenciales", "2. Conectar con Hacienda (credenciales)")
    + who("Propietario, Administrador y Contador")
    + p("Para firmar y enviar comprobantes necesitas tres cosas de Hacienda: <strong>usuario</strong>, <strong>contraseña</strong> y <strong>llave criptográfica (.p12) con su PIN</strong>. Desde el 6 de octubre de 2025 se generan en <strong>TRIBU-CR</strong> (reemplazó a ATV).")
    + call("info", "Requisito", "Estar inscrito en el RUT con al menos una actividad económica lucrativa. Sin ella Hacienda no genera las credenciales.")
    + h3("Paso 1 — Usuario y contraseña de producción")
    + ol([
        "Entra a la Oficina Virtual de TRIBU-CR (<a class='underline' href='https://ovitribucr.hacienda.go.cr' target='_blank' rel='noopener noreferrer'>ovitribucr.hacienda.go.cr</a>) con la cuenta del contribuyente que va a facturar.",
        "Abre el bloque <strong>Tico Factura</strong> y toca <strong>Crear usuario</strong>.",
        "Elige <strong>“No, voy a utilizar otro programa”</strong>.",
        "Hacienda envía el usuario y la contraseña al <strong>correo registrado en el RUT</strong> (también los ves en Tico Factura › Mi perfil). Guárdalos.",
    ])
    + h3("Paso 2 — Llave criptográfica")
    + ol([
        "En el mismo módulo de Tico Factura toca <strong>Generar llave criptográfica</strong>.",
        "Define un <strong>PIN</strong>, confírmalo y toca <strong>Generar</strong>. Anótalo: sin el PIN la llave no sirve.",
        "Toca <strong>Descargar</strong> y guarda el archivo <code class=\"code-font\">.p12</code>.",
    ])
    + call("warn", "Sobre el PIN y la vigencia", "La guía oficial de Hacienda (mayo de 2025) indica un PIN de 4 dígitos. Fuentes de la industria (blogs, no documentación oficial de Hacienda) reportan que desde el 27 de julio de 2026 se exige un PIN de mínimo 14 caracteres con mayúscula, minúscula, número y símbolo, y una vigencia de la llave de 4 años. Usa el PIN que te pida Hacienda al generarla. Generar una llave nueva puede dejar sin efecto la anterior: actualízala en todos los sistemas que la usen.")
    + "<!-- TBD: validar regla de PIN y vigencia contra comunicado oficial de Hacienda -->\n"
    + h3("Paso 3 — Cargar todo en Facturanza")
    + ol(["Ve a <strong>Negocio › Facturación</strong>."])
    + ol(["Toca <strong>Pegar desde Hacienda</strong> y pega el texto del correo que contiene <code class=\"code-font\">usuario:</code> y <code class=\"code-font\">contraseña:</code>; se llenan los campos solos. También puedes escribirlos en <em>Correo de facturación</em> y <em>Contraseña de correo</em> (con el botón de editar)."], start=2)
    + single("negocio_usuario", "Usuario y contraseña: Pegar desde Hacienda", width="max-w-[560px]")
    + ol(["En <strong>Llave criptográfica</strong> toca <strong>Actualizar</strong> y sube el archivo .p12.",
        "En <strong>Pin de la llave criptográfica</strong> toca editar, escribe el PIN y guarda."], start=3)
    + single("negocio_llave", "Llave criptográfica y PIN", width="max-w-[560px]")
    + ol(["Vuelve a <strong>Inicio</strong>: debe decir <strong>Facturación habilitada</strong>. La facturación se habilita sola cuando usuario, contraseña, PIN y llave están completos."], start=5)
    + p("Aquí ves y puedes cambiar la <strong>actividad económica predeterminada</strong>. Las actividades <strong>no se pueden eliminar</strong>: solo se actualizan con el ícono de actualizar junto a <strong>Actividades</strong>, que las consulta de nuevo en Hacienda. Con otra actividad puedes facturar eligiéndola en el formulario de la factura (todas las empresas) o con una <a class='underline' href='marcas.html'>marca</a> (plan de pago). En <strong>Sucursal y terminal predeterminada</strong> verás con cuál se emite por defecto (se administran en <a class='underline' href='sucursales.html'>Sucursales</a>).")
    + call("danger", "Protege tus credenciales", "Estos datos permiten emitir comprobantes a nombre de tu empresa. Solo compártelos con personas de confianza y dales el rol adecuado. Si sospechas que se filtraron, genera nuevas en TRIBU-CR."),
)

# ---------------------------------------------------------------- roles
PAGES["roles.html"] = dict(
    title="Roles y acceso",
    nav="Roles y acceso",
    desc="Invita a tu equipo, asigna un rol y limita desde qué sucursal o terminal puede facturar cada persona.",
    body=shots("roles_tab", "Negocio › Roles")
    + h2("invitar", "1. Agregar a una persona")
    + who("ver: Propietario, Administrador, Contador y Gerente · editar roles: Propietario, Administrador y Gerente")
    + ol(["Ve a <strong>Negocio › Roles</strong> y agrega un usuario."])
    + single("roles_agregar", "Botón Agregar rol en la pestaña Roles", width="max-w-[560px]")
    + ol(["Elige el rol: <strong>Gerente, Administrador, Empleado o Contador</strong>."], start=2)
    + single("roles_dialogo_rol", "¿Qué rol desea agregar?", width="max-w-[560px]")
    + ol(["Escribe el <strong>correo</strong> de la persona y toca <strong>Invitar</strong>. La empresa aparecerá en su lista de <em>Mis Empresas</em>."], start=3)
    + single("roles_dialogo_correo", "Ingresa el correo de la persona e invítala", width="max-w-[420px]")
    + p("En el menú de cada usuario puedes <strong>Editar rol</strong>, <strong>Establecer nivel de acceso</strong>, <strong>Establecer terminal asignada</strong> o <strong>Eliminar usuario</strong>.")
    + h2("roles", "2. Qué ve y puede hacer cada rol")
    + table(["Pantalla o acción", "Propietario", "Administrador", "Contador", "Gerente", "Empleado"], [
        ["Inicio, Facturas (ver y emitir), Clientes y Productos (ver)", "✓", "✓", "✓", "✓", "✓"],
        ["Crear y editar clientes y productos", "✓", "✓", "–", "✓", "–"],
        ["Compras", "✓", "✓", "✓", "–", "–"],
        ["Declaraciones", "✓", "✓", "✓", "✓", "–"],
        ["Sucursales", "✓", "✓", "✓", "–", "–"],
        ["Negocio (ver)", "✓", "✓", "✓", "✓", "–"],
        ["Negocio: editar datos y credenciales de Hacienda", "✓", "✓", "✓", "–", "–"],
        ["Roles: editar el rol de un usuario", "✓", "✓", "–", "✓", "–"],
    ])
    + p("Los roles controlan <strong>qué pantallas ves y qué botones tienes</strong> dentro de la app. Asigna el rol más bajo que alguien necesite.")
    + h2("acceso", "3. Nivel de acceso: por sucursal o terminal")
    + p("Además del rol, cada usuario tiene un <strong>nivel de acceso</strong> que limita qué documentos puede ver y emitir:")
    + table(["Nivel", "Qué significa"], [
        ["Acceso completo", "Todas las sucursales y terminales."],
        ["Acceso a sucursales", "Una o varias sucursales."],
        ["Acceso a terminales", "Una o varias terminales dentro de una sucursal."],
    ])
    + single("roles_menu", "Menú de cada usuario: nivel de acceso y terminal asignada", width="max-w-[300px]")
    + p("Con <strong>Establecer terminal asignada</strong> defines la terminal desde la que factura por defecto. Así logras, por ejemplo, que un cajero solo emita desde su caja."),
)

# ---------------------------------------------------------------- sucursales
PAGES["sucursales.html"] = dict(
    title="Sucursales y terminales",
    nav="Sucursales y terminales",
    desc="Cómo se numeran tus documentos: sucursales, terminales y consecutivos.",
    body=shots("sucursales_menu", "Sucursales")
    + who("Propietario, Administrador y Contador")
    + h2("estructura", "1. Cómo funciona")
    + p("Cada documento lleva un <strong>consecutivo de 20 dígitos</strong> compuesto por <strong>sucursal (3) + terminal (5) + tipo de documento (2) + número (10)</strong>. Facturanza lo administra por ti.")
    + cards([
        ("Sucursal", "Un establecimiento o sede. Tu empresa nace con la sucursal 001, llamada <strong>Principal</strong>. Tiene solo un nombre."),
        ("Terminal", "Un punto de emisión (caja). Cada sucursal nace con la terminal 00001, llamada <strong>Principal</strong>. Cada terminal lleva su propio consecutivo."),
    ])
    + h2("administrar", "2. Crear y administrar")
    + shots("sucursales_terminal", "Detalle de una terminal")
    + ul([
        "<strong>Crear sucursal</strong>: escribe el nombre. Se crea con la siguiente numeración (002, 003…) y una terminal Principal.",
        "Dentro de una sucursal, <strong>Crear terminal</strong>.",
        "En una terminal ves el <strong>Consecutivo</strong> actual y puedes <strong>Actualizar consecutivo</strong> (útil si vienes de otro facturador y debes continuar la numeración). Úsalo con cuidado: un número repetido genera rechazos.",
        "En <strong>Usuarios</strong> ves quiénes están <em>Asignados</em> y quiénes tienen <em>Acceso</em> (ver <a class='underline' href='roles.html'>Roles y acceso</a>).",
    ])
    + h2("clave", "3. La clave numérica de 50 dígitos")
    + p("Además del consecutivo, cada comprobante tiene una <strong>clave única de 50 dígitos</strong>: país (3) + fecha DDMMAA (6) + cédula del emisor (12) + consecutivo (20) + situación (1) + código de seguridad (8). Aparece en el XML y sirve para consultar el documento. En una nota de crédito, referencia la clave del documento original."),
)

# ---------------------------------------------------------------- marcas
PAGES["marcas.html"] = dict(
    title="Marcas",
    nav="Marcas",
    desc="Factura con distinto nombre, logo y datos de contacto dentro de una misma empresa.",
    body=single("negocio_info", "Datos de la empresa (escritorio)", width="max-w-[380px]")
    + single("negocio_info_movil", "Datos de la empresa (tablet y móvil)", width="max-w-[420px]")
    + who("planes de pago · crear y editar: Propietario, Administrador y Contador")
    + p("Una <strong>marca</strong> te permite emitir documentos con un nombre comercial, logo, correo y teléfono propios, por <strong>actividad económica</strong>, sin crear otra empresa. Es la forma de manejar varias actividades con distinta imagen. No es obligatoria: en el plan gratuito también puedes elegir otra actividad directamente en el formulario de la factura.")
    + h2("crear", "1. Crear una marca")
    + ol([
        "Ve a <strong>Negocio</strong> y, junto a los datos de la empresa, toca el <strong>+</strong> de las marcas.",
        "Completa <strong>Nombre de la marca</strong>, <strong>Actividad</strong>, logo, <strong>Sucursal y terminal predeterminadas</strong>, <strong>correo</strong> y <strong>teléfono</strong>.",
        "Guarda. Puedes eliminarla cuando quieras: las facturas ya emitidas no se afectan.",
    ])
    + h2("usar", "2. Usar una marca al facturar")
    + single("marcas_drawer", "Panel de empresas: sección Marcas", width="max-w-[380px]")
    + p("Elige la marca (con el selector del panel de Negocio) antes de crear la factura. El documento usará el nombre, contacto, logo y sucursal/terminal de esa marca. En el plan gratuito las marcas adicionales aparecen bloqueadas."),
)

# ---------------------------------------------------------------- planes
PAGES["planes.html"] = dict(
    title="Planes, facturas y pagos",
    nav="Planes y pagos",
    desc="Qué incluye cada plan, cuántas facturas te quedan y cómo pagar.",
    body=shots("planes_menu", "Planes de suscripción")
    + who("ver y contratar: Propietario, Administrador, Contador y Gerente")
    + h2("cupo", "1. Tu cupo de facturas")
    + ul([
        "Toda empresa nueva empieza en el <strong>plan gratuito</strong>.",
        "<strong>Disponibles: N</strong> (Inicio y Facturas) es la suma de tus facturas mensuales y de paquetes comprados.",
        "Una factura se descuenta al quedar <strong>Completada</strong>. Las <strong>notas de crédito no descuentan</strong>. Las rechazadas no descuentan, pero cuentan para el límite de rechazos.",
        "Cuando llegas a 0, la app te ofrece <strong>Planes de suscripción</strong> o <strong>Facturas unitarias</strong>.",
    ])
    + shots("planes_sin_facturas", "Diálogo ¡Sin facturas disponibles!")
    + h2("planes", "2. Qué incluye un plan")
    + single("planes_recomendado", "Plan recomendado: Crecimiento", width="max-w-[300px]")
    + call("ok", "Paga al año y ahorra 20%", "En la parte superior elige <strong>Mensual</strong> o <strong>Anual</strong>. Con el pago <strong>anual</strong> obtienes un <strong>20% de descuento</strong> sobre el precio mensual (por ejemplo, el plan Crecimiento baja de ₡10,000 a ₡8,000 por mes: ₡96,000 al año).")
    + single("planes_selector", "Selector Mensual / Anual con el 20% de ahorro", width="max-w-[380px]")
    + p("Cada plan define: <strong>facturas mensuales</strong>, <strong>usuarios</strong>, precio por <strong>factura extra</strong>, <strong>usos del creador de productos con IA</strong> y <strong>FacturiTokens</strong>. Los planes de pago agregan:")
    + ul([
        "Facturas programadas.",
        "Registro automático de compras (buzón).",
        "Marcas por actividad económica.",
        "Soporte prioritario.",
    ])
    + p("En <strong>Membresía</strong> ves tu plan actual, el uso de facturas, usuarios y FacturiTokens, y los botones <strong>Mejorar plan</strong>, <strong>Comprar facturas</strong>, <strong>Administrar mi plan</strong> e <strong>Historial de pagos</strong>. Puedes alternar precios mensuales y anuales. El plan <strong>Empresarial</strong> es a la medida: se coordina por contacto con ventas.")
    + h2("pagos", "3. Cómo pagar")
    + shots("planes_pago", "Desglose de pago del plan recomendado")
    + table(["Método", "Cómo funciona"], [
        ["Tarjeta", "Pago en línea. Monto mínimo ₡3,000. Al aprobarse se activa el plan o se acreditan las facturas y se emite tu comprobante."],
        ["Transferencia (IBAN)", "Transfieres a la cuenta indicada y adjuntas el comprobante. Un administrador de Facturanza aprueba el pago."],
        ["SINPE Móvil", "Pagas al número indicado y adjuntas el comprobante. Un administrador de Facturanza aprueba el pago."],
    ])
    + p("<strong>Paquetes de facturas</strong>: eliges la cantidad y no tienen fecha de vencimiento. En <strong>Historial de pagos</strong> consultas el estado de cada pago.")
    + call("info", "En iPhone y iPad", "Por las políticas de la tienda de aplicaciones no se pueden comprar planes ni facturas desde la app de iOS. Hazlo desde app.facturanza.com o desde Android."),
)

# ---------------------------------------------------------------- perfil
PAGES["perfil.html"] = dict(
    title="Perfil de usuario",
    nav="Perfil",
    desc="Tus datos, tus formas de iniciar sesión, preferencias y cómo eliminar tu cuenta.",
    body=shots("perfil_pagina", "Perfil")
    + h2("datos", "1. Mis datos")
    + p("<strong>Nombre de usuario</strong>, <strong>teléfono</strong> (mínimo 8 dígitos) y <strong>correo electrónico</strong>. Desde aquí también puedes <strong>Cerrar sesión</strong> y abrir los términos y condiciones, la política de privacidad y la de cookies.")
    + single("perfil_datos", "Datos del usuario y avatar", width="max-w-[300px]")
    + h2("metodos", "2. Métodos de inicio de sesión")
    + single("perfil_metodos", "Métodos de inicio de sesión", width="max-w-[300px]")
    + ul([
        "<strong>Google</strong>: vincular o desvincular.",
        "<strong>Apple</strong>: aparece en dispositivos Apple o si ya está vinculado.",
        "<strong>Contraseña</strong>: <em>Asignar</em> una si entras solo con Google o Apple; <em>Cambiar</em> te envía un enlace por correo.",
        "<strong>Ingreso con biometría</strong> (solo apps): se activa aquí, requiere tener una contraseña y confirmarla.",
    ])
    + h2("preferencias", "3. Sonidos y vibración")
    + p("Puedes apagar los <strong>sonidos de la interfaz</strong> y la <strong>vibración háptica</strong>.")
    + single("perfil_sonidos", "Sonidos y vibración", width="max-w-[300px]")
    + h2("eliminar", "4. Eliminar tu cuenta")
    + single("perfil_peligro", "Zona de peligro", width="max-w-[300px]")
    + call("danger", "Es irreversible", "Eliminar tu cuenta significa perder los datos relacionados con ella, incluido el acceso a negocios, facturas, clientes, productos y suscripciones. Antes de hacerlo, descarga los PDF y XML que necesites: tienes la obligación legal de conservar tus comprobantes electrónicos.")
    + "<!-- TBD: confirmar con negocio/legal qué ocurre con empresas de las que el usuario es único propietario -->\n",
)

# ---------------------------------------------------------------- ayuda
PAGES["ayuda.html"] = dict(
    title="Ayuda y solución de problemas",
    nav="Ayuda",
    desc="Respuestas rápidas, tarifas de IVA, glosario y lo que Facturanza todavía no hace.",
    body=h2("faq", "1. Preguntas frecuentes")
    + table(["Pregunta", "Respuesta"], [
        ["No puedo crear facturas.", "Revisa que Inicio diga <strong>Facturación habilitada</strong> (credenciales completas en Negocio › Facturación) y que tengas facturas <strong>Disponibles</strong>. Revisa también que tu terminal sea válida."],
        ["Mi factura salió Rechazada.", "Ábrela, toca <strong>Explicar error</strong>, corrige el dato y vuelve a emitir (<em>Duplicar</em> te ahorra captura). Los rechazos cuentan para un límite."],
        ["¿Cómo anulo una factura?", "Con una <a href='notas-credito.html' class='underline'>nota de crédito</a>. Los documentos aceptados no se eliminan."],
        ["¿Puedo facturar en dólares?", "Sí. Elige <em>Dólares</em> en el documento; el tipo de cambio se llena con el de Hacienda y es editable."],
        ["¿Cómo acepto las facturas de mis proveedores ante Hacienda?", "En TRIBU-CR (Tico Factura) o con otro software certificado. Facturanza solo registra las compras. Plazo: 8 días hábiles del mes siguiente. Ver <a href='compras.html' class='underline'>Compras</a>."],
        ["¿Dónde presento el IVA?", "En TRIBU-CR, Formulario 150. Facturanza te da el borrador en <a href='reportes.html' class='underline'>Reportes</a>."],
        ["No veo ‘Compras’, ‘Declaraciones’ o ‘Sucursales’ en el menú.", "Tu rol no tiene acceso. Pide al Propietario o Administrador que lo revise en <a href='roles.html' class='underline'>Roles</a>."],
        ["¿Puedo registrar mi empresa desde el iPhone?", "No. Regístrala desde la web o Android; luego aparece en tu iPhone."],
        ["¿Cuántos clientes o productos puedo tener?", "Depende de tu plan. Revisa Negocio › Membresía."],
        ["¿Qué hago si olvidé mi PIN de la llave?", "Genera una nueva llave en TRIBU-CR con un PIN nuevo y cárgala en Negocio › Facturación."],
    ])
    + h2("tarifas", "2. Tarifas de IVA (Ley 9635)")
    + "<!-- TBD: validación de esta tabla por asesor contable/tributario antes del cierre -->\n"
    + table(["Tarifa", "Aplica a (resumen)"], [
        ["13%", "General: la mayoría de bienes y servicios."],
        ["4%", "Servicios de salud privados y veterinarios; pasajes aéreos (base distinta para nacionales e internacionales)."],
        ["2%", "Medicamentos, primas de seguros personales y educación privada no regulada por MEP/CONESUP."],
        ["1%", "Canasta básica tributaria e insumos agropecuarios."],
        ["0.5%", "Pesca no deportiva y productos orgánicos certificados."],
        ["0% (con crédito)", "Exportaciones, ventas a zona franca, libros y otros definidos por ley."],
        ["8%", "Tarifa transitoria de ciertos servicios (turismo, ingeniería); su calendario cambia, consulta la vigencia."],
    ])
    + p("La tarifa la define el <strong>código CABYS</strong>. Si tienes dudas, consulta a tu contador.")
    + h2("alcance", "3. Lo que Facturanza todavía no hace")
    + ul([
        "Enviar el <strong>Mensaje Receptor</strong> (aceptación de compras): se hace en TRIBU-CR.",
        "Emitir <strong>Nota de Débito</strong>, <strong>Factura Electrónica de Exportación</strong> o <strong>Recibo Electrónico de Pago</strong>.",
        "Emitir Facturas Electrónicas de Compra.",
        "Presentar tu declaración de IVA ante Hacienda (te damos el borrador).",
        "Cuentas por cobrar o saldos por cliente.",
    ])
    + h2("glosario", "4. Glosario")
    + table(["Término", "Significado"], [
        ["CABYS", "Catálogo de Bienes y Servicios de 13 dígitos; define la tarifa de IVA."],
        ["FE / TE / NC / FEC", "Factura Electrónica / Tiquete Electrónico / Nota de Crédito / Factura Electrónica de Compra."],
        ["Clave numérica", "Identificador único de 50 dígitos de cada comprobante."],
        ["Consecutivo", "Número de 20 dígitos: sucursal, terminal, tipo y secuencia."],
        ["Llave criptográfica (.p12)", "Archivo con el que se firman tus comprobantes; se protege con un PIN."],
        ["TRIBU-CR / OVi", "Plataforma de Hacienda (desde octubre de 2025) donde generas credenciales y declaras."],
        ["Mensaje Receptor", "Respuesta del comprador a Hacienda (aceptación total, parcial o rechazo) sobre una factura recibida."],
        ["Formulario 150", "Declaración mensual de IVA en TRIBU-CR."],
    ])
    + h2("enlaces", "5. Enlaces útiles")
    + ul([
        "<a class='underline' href='https://ovitribucr.hacienda.go.cr' target='_blank' rel='noopener noreferrer'>TRIBU-CR (Oficina Virtual de Hacienda)</a>",
        "<a class='underline' href='https://app.facturanza.com' target='_blank' rel='noopener noreferrer'>Facturanza: app.facturanza.com</a>",
    ]),
)
