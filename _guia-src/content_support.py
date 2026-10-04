from template import h2, p, ul, ol, call, table

PAGES = {}

PAGES["soporte.html"] = dict(
    title="Soporte",
    nav="Soporte",
    desc="Cómo contactar al equipo de Facturanza y qué información enviar para que te ayudemos más rápido.",
    body=call("info", "Antes de escribirnos", "Revisa <a class='underline' href='ayuda.html'>Ayuda</a>: la mayoría de los casos (factura rechazada, credenciales inválidas, límites) tienen solución paso a paso.")
    + h2("canales", "1. Canales de contacto")
    + table(["Canal", "Cuándo usarlo"], [
        ["<a class='underline' href='https://wa.me/50670202151' target='_blank' rel='noopener noreferrer'>WhatsApp: +506 7020 2151</a>", "Consultas sobre planes, el plan Empresarial y ayuda con tu cuenta."],
    ])
    + "<!-- TBD: confirmar canales oficiales de soporte (correo, horario, SLA para soporte prioritario) -->\n"
    + p("Los planes de pago incluyen <strong>soporte prioritario</strong>. Ver <a class='underline' href='planes.html'>Planes y pagos</a>.")
    + h2("datos", "2. Qué datos enviar")
    + ul([
        "Nombre de la empresa y <strong>cédula</strong>.",
        "Correo con el que inicias sesión y plataforma (web, Android o iPhone).",
        "Qué intentabas hacer y el <strong>estado o mensaje</strong> que aparece (por ejemplo, <em>Rechazado</em> o <em>Credenciales inválidas</em>).",
        "Número de consecutivo o clave del documento, si aplica, y una captura de pantalla.",
    ])
    + call("danger", "Nunca compartas", "Tu <strong>contraseña</strong>, el <strong>PIN</strong> de la llave criptográfica ni el archivo <code class=\"code-font\">.p12</code>. El equipo de Facturanza no te los pedirá.")
    + h2("fiscal", "3. Consultas tributarias")
    + p("Soporte te ayuda con el uso de la plataforma. Para decisiones fiscales (tarifas aplicables, deducibilidad, declaración) consulta a tu contador o a Hacienda; Facturito ofrece orientación general."),
)
