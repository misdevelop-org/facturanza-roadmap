from content_start import PAGES as A
from content_ops import PAGES as B
from content_admin import PAGES as C

REVIEW_DATE = "4 de octubre de 2026"

# (archivo, título del menú, descripción corta para el catálogo)
NAV = [
    ("Primeros pasos", [
        ("index.html", "Catálogo de la guía", ""),
        ("empieza.html", "Empieza en 5 pasos", "De cero a tu primera factura electrónica."),
        ("get-started.html", "Cuenta e inicio de sesión", "Acceso, registro de empresa y qué hay en cada plataforma."),
        ("lobby.html", "Mis Empresas", "Varias empresas con un solo usuario."),
    ]),
    ("Operación diaria", [
        ("dashboard.html", "Inicio", "Estado de facturación, facturas disponibles, ingresos y egresos."),
        ("facturas.html", "Facturas", "Emitir, estados, programadas y qué hacer si algo falla."),
        ("notas-credito.html", "Notas de crédito", "Corrige o anula un documento ya aceptado."),
        ("clientes.html", "Clientes", "Datos oficiales desde Hacienda."),
        ("productos.html", "Productos y CABYS", "Catálogo, código CABYS y generación con IA."),
        ("compras.html", "Compras", "Registro de facturas de proveedores y buzón."),
        ("facturito.html", "Facturito (IA)", "Tu asistente para facturar y consultar."),
    ]),
    ("Cierre fiscal", [
        ("reportes.html", "Reportes e IVA", "Borrador del Formulario 150 y reportes mensuales."),
    ]),
    ("Administración", [
        ("negocio.html", "Negocio y credenciales", "Datos de empresa y conexión con Hacienda."),
        ("roles.html", "Roles y acceso", "Equipo, permisos y acceso por terminal."),
        ("sucursales.html", "Sucursales y terminales", "Numeración y consecutivos."),
        ("marcas.html", "Marcas", "Varios nombres y logos en una empresa."),
        ("planes.html", "Planes y pagos", "Cupo de facturas, planes y métodos de pago."),
        ("perfil.html", "Perfil", "Tus datos, métodos de acceso y cuenta."),
    ]),
    ("Ayuda", [
        ("ayuda.html", "Ayuda", "Preguntas frecuentes, tarifas de IVA, glosario y alcance."),
    ]),
]

PAGES = {}
PAGES.update(A); PAGES.update(B); PAGES.update(C)

cards = ""
for group, items in NAV:
    rows = [(f, t, d) for f, t, d in items if f != "index.html"]
    if not rows:
        continue
    cards += f'<h2 class="text-xl font-bold mt-10 mb-4">{group}</h2><div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">'
    for f, t, d in rows:
        cards += (
            f'<a href="{f}" class="doc-card p-5 flex flex-col justify-between group">'
            f'<div><h3 class="font-bold text-base mb-1 text-[var(--text-primary)] group-hover:text-[var(--brand-primary)] transition-colors">{t}</h3>'
            f'<p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed mb-4">{d}</p></div>'
            '<span class="text-xs font-bold text-[var(--brand-primary)]">Leer &rarr;</span></a>'
        )
    cards += "</div>"

PAGES["index.html"] = dict(
    title="Guía de uso de Facturanza",
    nav="Catálogo",
    desc="Guía oficial para facturar con Facturanza: configura Hacienda, emite, registra compras y prepara tu IVA.",
    body=(
        '<div class="bg-gradient-to-br from-slate-900 via-sky-950 to-slate-900 text-white rounded-3xl p-6 sm:p-10 mb-4 shadow-xl border border-sky-900/40">'
        '<div class="max-w-2xl"><span class="inline-block px-3 py-1 rounded-full bg-sky-500/20 text-sky-200 text-xs font-bold tracking-wider uppercase mb-3 border border-sky-400/20">Guía oficial</span>'
        '<h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-3">Guía de uso de Facturanza</h1>'
        '<p class="text-slate-200 text-sm sm:text-base leading-relaxed mb-6">Todo lo que necesitas para facturar electrónicamente en Costa Rica: pasos claros, tal como los ves en la app.</p>'
        '<div class="flex flex-wrap items-center gap-3"><a href="empieza.html" class="px-4 py-2 rounded-xl text-xs font-bold bg-sky-500 text-slate-950 hover:bg-sky-400 transition-colors">Empieza en 5 pasos &rarr;</a>'
        '<a href="ayuda.html" class="px-4 py-2 rounded-xl text-xs font-bold bg-white/10 text-white hover:bg-white/20 transition-colors">Ayuda y solución de problemas</a></div></div></div>'
        + cards
        + f'<p class="mt-10 text-xs text-slate-500 dark:text-slate-400">Última revisión: {REVIEW_DATE}.</p>'
    ),
)
