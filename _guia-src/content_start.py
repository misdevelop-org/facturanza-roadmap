from template import h2, h3, p, ul, ol, code, who, call, cards, table, matrix, shots, single

PAGES = {}

# ---------------------------------------------------------------- empieza
PAGES["empieza.html"] = dict(
    title="Empieza en 5 pasos",
    nav="Empieza en 5 pasos",
    desc="De cero a tu primera factura electrónica: cuenta, empresa, credenciales de Hacienda, cliente, producto y emisión.",
    body=call("info", "Antes de empezar", "Para emitir comprobantes necesitas estar <strong>inscrito en el RUT de Hacienda con al menos una actividad económica lucrativa</strong>. Sin eso, Hacienda no te permite generar las credenciales.")
    + h2("paso-1", "1. Crea tu cuenta e inicia sesión")
    + p("Entra a <a class='underline' href='https://app.facturanza.com'>app.facturanza.com</a> (o a la app de Android) y continúa con Google, Apple (iPhone/Mac) o tu correo y contraseña. Si usas correo, verifica tu dirección con el enlace que recibirás. <a class='underline' href='get-started.html'>Más detalles</a>.")
    + shots("cuenta_login", "Pantalla de inicio de sesión")
    + h2("paso-2", "2. Registra tu empresa")
    + p("En <strong>Mis Empresas</strong> toca el botón <strong>+</strong>, escribe la cédula y Facturanza trae el nombre legal y las actividades desde Hacienda. Completa nombre comercial, correo y teléfono. Tu empresa empieza en el <strong>plan gratuito</strong>.")
    + shots("cuenta_roles", "Registre su empresa: elige cómo te registras")
    + shots("cuenta_formulario", "Formulario Nueva empresa")
    + h2("paso-3", "3. Genera tus credenciales en TRIBU-CR")
    + p("Necesitas tres datos de Hacienda: <strong>usuario</strong>, <strong>contraseña</strong> y la <strong>llave criptográfica (.p12)</strong> con su PIN. Se generan en TRIBU-CR → <em>Tico Factura</em>. Sigue los pasos en <a class='underline' href='negocio.html#credenciales'>Negocio y credenciales</a>.")
    + shots("inicio_inhabilitada", "Sin credenciales, Inicio muestra Facturación inhabilitada")
    + h2("paso-4", "4. Cárgalas en Facturanza")
    + p("Ve a <strong>Negocio › Facturación</strong>, usa <strong>Pegar desde Hacienda</strong>, sube la llave y guarda el PIN. Cuando todo está completo, en <strong>Inicio</strong> verás la etiqueta <strong>Facturación habilitada</strong>.")
    + shots("negocio_facturacion", "Negocio › Facturación con las credenciales cargadas")
    + shots("inicio_habilitada", "Inicio con la facturación habilitada")
    + h2("paso-5", "5. Crea un cliente, un producto y emite")
    + ol([
        "<strong>Productos › Agregar</strong>: nombre, código CABYS (13 dígitos, con el buscador), precio y unidad.",
        "<strong>Clientes › Agregar</strong>: escribe la cédula y se completan los datos desde Hacienda. Si el cliente no tiene cédula, marca <em>El cliente no cuenta con cédula</em> (se emite Tiquete).",
        "<strong>Facturas › Crear factura</strong>: elige receptor, productos y correos; revisa el total y toca el botón de generar.",
    ])
    + call("ok", "¿Listo?", "Cuando el estado llegue a <strong>Completado</strong>, el cliente recibe el PDF y el XML por correo. Si algo falla, revisa <a class='underline' href='ayuda.html'>Ayuda y solución de problemas</a>."),
)

# ---------------------------------------------------------------- get-started
PAGES["get-started.html"] = dict(
    title="Cuenta, registro e inicio de sesión",
    nav="Cuenta e inicio de sesión",
    desc="Cómo entrar a Facturanza, registrar tu empresa con datos oficiales de Hacienda y qué puedes hacer en cada plataforma.",
    body=h2("metodos-acceso", "1. Formas de iniciar sesión")
    + cards([
        ("Google", "Continuar con Google en web, Android y iOS."),
        ("Apple", "Continuar con Apple, disponible solo en iPhone, iPad y Mac."),
        ("Correo y contraseña", "Contraseña de al menos 6 caracteres. Al registrarte debes verificar tu correo. ¿La olvidaste? Usa <em>¿Olvidaste tu contraseña?</em> y recibirás un enlace."),
        ("Biometría (Face ID / huella)", "Solo en las apps (no en la web). Primero asigna una contraseña y actívala en <strong>Perfil</strong>."),
    ])
    + shots("cuenta_login", "Opciones de inicio de sesión")
    + h2("registro-empresa", "2. Registrar tu empresa")
    + who("cualquier usuario con sesión iniciada (en iPhone/iPad, desde la web o Android)")
    + p("En <strong>Mis Empresas</strong> toca <strong>+</strong>. Primero eliges cómo te registras:")
    + ul([
        "<strong>Soy el Propietario</strong>: la empresa queda a tu nombre.",
        "<strong>Soy un Administrador</strong> o <strong>Soy un Contador</strong>: registras la empresa para otra persona; debes escribir el <strong>correo del propietario</strong>.",
    ])
    + shots("cuenta_roles", "Elige cómo te registras")
    + p("Luego completas el formulario:")
    + ol([
        "<strong>Cédula</strong>: Facturanza consulta a Hacienda y trae el <strong>nombre legal</strong> (bloqueado) y las <strong>actividades económicas</strong>. Elige la <strong>actividad principal</strong> (la predeterminada para facturar); las demás se guardan solas.",
        "<strong>Información del negocio</strong>: nombre comercial, correo* y teléfono* (con código de país).",
        "<strong>Nombre de dominio (opcional)</strong>: es el nombre corto que aparece en el enlace directo de tu empresa. Solo letras, números, guion y guion bajo. No existe un subdominio tipo <em>tumarca.facturanza.com</em>.",
        "<strong>Ubicación</strong>: provincia, cantón, distrito y dirección exacta*.",
    ])
    + shots("cuenta_formulario", "Formulario Nueva empresa")
    + call("warn", "Una empresa por cédula", "Si ya existe un negocio con esa cédula, Facturanza no te deja crear otro. Pide al propietario que te agregue desde <strong>Negocio › Roles</strong>.")
    + table(["Cédula", "Dígitos"], [
        ["Cédula física", "9"], ["Cédula jurídica", "10"], ["DIMEX", "11 o 12"], ["NITE", "10"],
    ])
    + h2("plataformas", "3. Qué puedes hacer en cada plataforma")
    + table(["Función", "Web", "Android", "iPhone / iPad"], [
        ["Crear cuenta con correo", "✓", "✓", "No (hazlo en la web)"],
        ["Registrar una empresa nueva", "✓", "✓", "No (hazlo en la web o Android)"],
        ["Facturar, clientes, productos, compras, reportes", "✓", "✓", "✓"],
        ["Comprar plan o paquetes de facturas", "✓", "✓", "No (desde el sitio web)"],
        ["Ingreso con biometría", "No", "✓", "✓"],
        ["Continuar con Apple", "No", "No", "✓"],
    ])
    + p("Las empresas registradas en la web aparecen automáticamente en tu app de iPhone o iPad al iniciar sesión."),
)

# ---------------------------------------------------------------- lobby
PAGES["lobby.html"] = dict(
    title="Mis Empresas",
    nav="Mis Empresas",
    desc="Administra varias empresas con un solo usuario y cambia entre ellas sin volver a iniciar sesión.",
    body=shots("lobby", "Mis Empresas")
    + h2("lobby", "1. La pantalla Mis Empresas")
    + p("Después de iniciar sesión ves una tarjeta por cada empresa a la que tienes acceso (logo y nombre) y una tarjeta <strong>+</strong> para registrar otra. Toca una tarjeta para entrar a su <strong>Inicio</strong>.")
    + call("info", "En iPhone y iPad", "La tarjeta <strong>+</strong> no aparece en la app de iOS. Para registrar una empresa nueva usa la web (app.facturanza.com) o la app de Android; luego la verás en tu lista en todos tus dispositivos.")
    + h2("como-aparecen", "2. Cómo llega una empresa a tu lista")
    + ul([
        "<strong>Tú la registras</strong> con el botón + (ver <a class='underline' href='get-started.html#registro-empresa'>Registrar tu empresa</a>).",
        "<strong>Te agregan</strong> desde <strong>Negocio › Roles</strong> usando tu correo. Aparece en tu lista con el rol que te dieron.",
    ])
    + h2("cambiar-empresa", "3. Cambiar de empresa")
    + p("Dentro de una empresa, toca el <strong>logo (arriba a la derecha)</strong> para abrir el panel de empresas y elegir otra. No necesitas volver a iniciar sesión.")
    + h2("menu", "4. El menú de cada empresa")
    + p("El menú lateral (o el botón de menú en celular) tiene: <strong>Perfil, Inicio, Facturas, Compras, Clientes, Productos, Sucursales, Reportes y Negocio</strong>. Cada usuario ve solo lo que su rol permite (ver <a class='underline' href='roles.html'>Roles y acceso</a>).")
    + call("info", "Datos separados por empresa", "La información de cada empresa (clientes, productos, facturas, reportes) es independiente. Los usuarios de una empresa no ven los datos de otra."),
)

# ---------------------------------------------------------------- dashboard (Inicio)
PAGES["dashboard.html"] = dict(
    title="Inicio",
    nav="Inicio",
    desc="La pantalla principal de tu empresa: estado de facturación, facturas disponibles, ingresos, egresos y Facturito.",
    body=shots("inicio_habilitada", "Inicio de MIS Develop")
    + h2("que-ves", "1. Qué encuentras en Inicio")
    + cards([
        ("Estado de facturación", "Etiqueta <strong>Facturación habilitada</strong> o <strong>inhabilitada</strong>. Si está inhabilitada, tócala para ir a Negocio y completar las credenciales de Hacienda."),
        ("Crear factura y Subir compras", "Atajos a las dos acciones más usadas. <strong>Disponibles: N</strong> indica cuántas facturas te quedan en tu plan."),
        ("Ingresos y Egresos", "Dos gráficos del período. En cada uno, el botón de descarga ofrece Excel y PDF, y la <strong>Declaración IVA TRIBU-CR</strong> (PDF o Excel)."),
        ("Facturito", "Barra de chat en la parte inferior. Ver <a class='underline' href='facturito.html'>Facturito</a>."),
    ])
    + p("El gráfico de Egresos solo lo ven los roles con acceso a Compras. La primera vez que entras a una empresa verás un mensaje de bienvenida y, si faltan credenciales de Hacienda, un aviso para completarlas.")
    + h2("tipo-cambio", "2. Dólares y tipo de cambio")
    + p("Inicio no muestra el tipo de cambio. Al crear una factura en <strong>USD</strong>, el campo <strong>Tipo de cambio</strong> se llena automáticamente con el valor publicado por Hacienda y puedes ajustarlo antes de emitir."),
)

# ---------------------------------------------------------------- facturas
PAGES["facturas.html"] = dict(
    title="Facturas",
    nav="Facturas",
    desc="Crea y consulta facturas y tiquetes electrónicos, entiende cada estado y sabe qué hacer cuando algo falla.",
    body=shots("facturas_lista", "Lista de facturas")
    + h2("tipos", "1. Qué documentos puedes emitir")
    + table(["Documento", "Cómo se genera", "Estado"], [
        ["<strong>Factura Electrónica (FE)</strong>", "Facturas &rsaquo; Crear factura, con un cliente que tenga cédula.", "Disponible"],
        ["<strong>Tiquete Electrónico (TE)</strong>", "Facturas &rsaquo; Crear factura y cambia el tipo de documento (cliente sin cédula o consumidor final).", "Disponible"],
        ["<strong>Nota de Crédito (NC)</strong>", "Desde una factura o tiquete ya completado. Ver <a class='underline' href='notas-credito.html'>Notas de crédito</a>.", "Disponible"],
        ["Factura Electrónica de Compra (FEC)", "No se emite en Facturanza. Si te llega por el buzón de compras, se registra automáticamente.", "Solo registro"],
        ["Nota de Débito, Factura de Exportación, Recibo Electrónico de Pago", "Aún no disponibles en Facturanza.", "No disponible"],
    ])
    + p("Facturanza emite con el esquema <strong>v4.4</strong> de Hacienda, obligatorio desde el 1 de septiembre de 2025.")
    + h2("crear", "2. Crear una factura paso a paso")
    + who("todos los roles (según tu nivel de acceso a sucursales y terminales)")
    + shots("facturas_crear", "Formulario Crear factura")
    + ol([
        "Toca <strong>Crear factura</strong> en Inicio o en Facturas. Si ves un aviso de configuración, completa primero <a class='underline' href='negocio.html#credenciales'>las credenciales de Hacienda</a>.",
        "<strong>Tipo de documento</strong>: Factura o Tiquete.",
        "<strong>Actividad económica de mi empresa</strong> (si tienes varias).",
        "<strong>Receptor</strong>: elige un cliente o toca <em>Nuevo cliente</em>. Para Factura el cliente debe tener cédula. Si el cliente tiene varias actividades, elige la <strong>actividad económica del cliente</strong>.",
        "<strong>Correos de envío</strong>: agrega los destinatarios (puedes escribir varios, uno por uno). Recibirán el PDF y el XML.",
        "<strong>Condición de venta</strong> (Contado, Crédito y otras que define Hacienda) y <strong>Método de pago</strong>: Efectivo, Tarjeta, Cheque, Transferencia o depósito bancario, Recaudado por terceros, SINPE Móvil, Plataforma digital u Otro.",
        "<strong>Tipo de moneda</strong>: Colones o Dólares. En dólares, revisa el <strong>Tipo de cambio</strong> (se llena solo).",
        "<strong>Productos</strong>: agrega uno o más desde tu catálogo; puedes ajustar descuento y, si aplica, cargar una exoneración (abajo).",
        "Revisa <strong>Subtotal, Impuesto, Exonerado y Total</strong> y toca el botón verde para generar el documento. Puedes agregar notas.",
    ])
    + h3("Exoneraciones")
    + p("En la línea del producto activa la exoneración e ingresa el <strong>código de autorización</strong>. Facturanza lo consulta en Hacienda y muestra institución, porcentaje y vigencia. Se aplica por línea.")
    + h2("estados", "3. Estados de un documento")
    + table(["Estado", "Qué significa", "Qué hacer"], [
        ["Enviado / Procesando / XML firmado", "Facturanza está preparando y firmando el documento.", "Espera; se actualiza solo."],
        ["Procesando por Hacienda", "Hacienda lo está validando.", "Espera; se actualiza solo."],
        ["Aceptado por Hacienda → Creando PDF", "Hacienda lo aceptó; se genera el PDF y se envía el correo.", "Espera."],
        ["<strong>Completado</strong>", "Documento válido, con PDF y XML enviados a los correos.", "Puedes descargarlo, reenviarlo o crear una nota de crédito."],
        ["<strong>Rechazado</strong>", "Hacienda lo rechazó.", "Toca <strong>Explicar error</strong>, corrige y emite de nuevo (puedes usar <em>Duplicar</em>)."],
        ["Credenciales inválidas / Firma inválida", "Usuario, contraseña, llave o PIN incorrectos o vencidos.", "Actualízalos en Negocio › Facturación. Luego elimina el documento y emítelo otra vez."],
        ["Terminal incorrecta", "La sucursal/terminal del documento no es válida.", "Revisa Sucursales y tu terminal asignada."],
        ["Límite de suscripción alcanzado", "No te quedan facturas disponibles.", "Ver <a class='underline' href='planes.html'>Planes y facturas</a>."],
        ["Límite de facturas rechazadas alcanzado", "Acumulaste demasiados rechazos y la emisión se bloquea.", "Contáctanos; normalmente se reinicia con la renovación del plan."],
    ])
    + p("Los documentos en un estado de error (no en Rechazado ni Completado) se pueden <strong>Eliminar</strong> desde su menú. Los documentos aceptados por Hacienda no se eliminan: se corrigen con una nota de crédito.")
    + h2("lista", "4. Buscar y gestionar tus documentos")
    + ul([
        "La lista muestra el <strong>mes actual</strong> por defecto; cambia el rango de fechas arriba.",
        "Busca por cliente, correo, cédula o producto. El filtro (ícono de ajustes) muestra Tiquetes y Facturas; las <strong>Notas de crédito están ocultas por defecto</strong>.",
        "Menú de cada documento (⋮): <strong>Crear nota de crédito</strong>, <strong>Reenviar correo</strong> (separa varios correos con un espacio), <strong>Programar factura</strong>, <strong>Duplicar</strong>, <strong>Ver PDF</strong> y <strong>Explicar error</strong> (solo rechazados).",
        "En el detalle puedes <strong>descargar el PDF, el XML enviado y el XML de respuesta de Hacienda</strong>.",
    ])
    + call("info", "¿Cuándo se descuenta una factura de tu plan?", "Al quedar <strong>Completado</strong>. Las notas de crédito no descuentan. Una factura rechazada no descuenta, pero cuenta para el límite de rechazos.")
    + h2("programadas", "5. Facturas programadas")
    + who("planes de pago")
    + p("Desde un documento completado toca <strong>Programar factura</strong>. Defines un nombre, la <strong>frecuencia</strong> (<strong>Mensual, Semanal o Quincenal</strong>), el día, la <strong>hora de emisión</strong> y, opcionalmente, fecha de fin o número máximo de emisiones. Las programaciones aparecen en la pestaña <strong>Programadas</strong> con estado <em>Activa, Pausada, Completada o Error</em>. Si tu plan baja a gratuito, se conservan pausadas.")
    + p("Las facturas programadas en dólares usan el tipo de cambio al momento de emitirse."),
)

# ---------------------------------------------------------------- notas de crédito
PAGES["notas-credito.html"] = dict(
    title="Notas de crédito",
    nav="Notas de crédito",
    desc="Cómo corregir o anular una factura o tiquete ya aceptado por Hacienda.",
    body=p("Una factura o tiquete aceptado por Hacienda no se edita ni se elimina: se corrige con una <strong>nota de crédito (NC)</strong> que lo referencia.")
    + h2("cuando", "1. Cuándo puedes crearla")
    + ul([
        "El documento original es una <strong>Factura o Tiquete</strong> en estado <strong>Completado</strong>.",
        "No tiene ya una nota de crédito aceptada (si la anterior fue rechazada, puedes crear otra).",
    ])
    + h2("pasos", "2. Paso a paso")
    + ol([
        "Abre el menú (⋮) del documento y toca <strong>Crear nota de crédito</strong> (o el botón <em>Elaborar nota de crédito</em> dentro del detalle).",
        "Completa <strong>Razón</strong> y <strong>Motivo</strong> (máximo 50 caracteres).",
        "Revisa los montos: el <strong>total de la nota no puede superar el de la factura</strong>.",
        "Toca <strong>Crear nota de crédito</strong>. Se envía a Hacienda igual que cualquier documento.",
    ])
    + single("nc_menu", "Menú del documento: Crear nota de crédito")
    + shots("nc_dialogo", "Diálogo Nota de crédito: Razón y Motivo")
    + shots("nc_formulario", "Formulario de la nota de crédito")
    + call("ok", "Sin costo de cupo", "Las notas de crédito <strong>no descuentan</strong> facturas de tu plan.")
    + shots("nc_adjunta", "La nota de crédito queda enlazada a la factura original")
    + p("La factura original y su nota quedan enlazadas (pestaña <em>Nota de crédito</em> / <em>Referencia</em>). En el reporte de IVA, la nota reduce el débito fiscal del período. Si necesitas <em>aumentar</em> un monto ya facturado, consulta con tu contador: la Nota de Débito aún no está disponible en Facturanza."),
)
