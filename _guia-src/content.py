import os
from content_start import PAGES as A
from content_ops import PAGES as B
from content_admin import PAGES as C
from content_support import PAGES as D

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
        ("soporte.html", "Soporte", "Cómo contactarnos y qué datos enviar."),
    ]),
]

PAGES = {}
PAGES.update(A); PAGES.update(B); PAGES.update(C); PAGES.update(D)

import re as _re
_js = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "guia", "assets", "guide.js")).read()
_ICONS = dict(_re.findall(r'"([a-z-]+)": `<svg[^>]*>(.*?)</svg>`', _js))
_ICONS.update({
    "bolt": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />',
    "key": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" />',
    "crown": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 16L3 6l5.5 4L12 4l3.5 6L21 6l-2 10H5zm0 3h14" />',
    "star": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />',
    "help": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />',
    "lifebuoy": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" />',
})

def _svg(name, cls="h-5 w-5"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" class="{cls}" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">{_ICONS[name]}</svg>'

# Colores de la paleta de la app (style.dart): green, blue, actionFill, orange, brown...
_G, _B, _T, _L, _O, _BR, _LG = "#00A791", "#005973", "#307588", "#3A8FA6", "#B8661A", "#B05704", "#2E9E5B"
CARD = {
    "empieza.html": ("bolt", _G, ""), "get-started.html": ("key", _B, ""), "lobby.html": ("grid", _L, ""),
    "dashboard.html": ("layout-dashboard", _T, ""), "facturas.html": ("receipt", _LG, ""),
    "notas-credito.html": ("receipt", _O, ""), "clientes.html": ("users", _L, ""),
    "productos.html": ("tag", _BR, ""), "compras.html": ("shopping-bag", _O, ""),
    "facturito.html": ("sparkles", _T, "ai"), "reportes.html": ("bar-chart", _B, ""),
    "negocio.html": ("briefcase", _T, ""), "roles.html": ("users", _L, ""), "sucursales.html": ("store", _LG, ""),
    "marcas.html": ("star", _T, "premium"), "planes.html": ("crown", _T, "premium"),
    "perfil.html": ("user", _B, ""), "ayuda.html": ("help", _O, ""), "soporte.html": ("lifebuoy", _G, ""),
}
GROUP = {
    "Primeros pasos": ("bolt", _G), "Operación diaria": ("receipt", _T), "Cierre fiscal": ("bar-chart", _B),
    "Administración": ("briefcase", _L), "Ayuda": ("help", _O),
}

cards = ""
for group, items in NAV:
    rows = [(f, t, d) for f, t, d in items if f != "index.html"]
    if not rows:
        continue
    gi, gc = GROUP[group]
    cards += (
        f'<h2 class="flex items-center gap-3 text-xl font-bold mt-10 mb-4"><span class="inline-flex items-center justify-center h-9 w-9 rounded-xl text-white" style="background:{gc}">{_svg(gi)}</span>{group}</h2>'
        '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">'
    )
    for f, t, d in rows:
        ic, col, kind = CARD[f]
        chip = {"": "", "ai": '<span class="chip-ai">IA</span>', "premium": '<span class="chip-premium">Premium</span>'}[kind]
        icon_cls = {"": "", "ai": " grad-ai", "premium": " grad-premium"}[kind]
        icon_style = "" if kind else f' style="background:{col}"'
        cards += (
            f'<a href="{f}" class="doc-card card-{kind or "plain"} p-5 flex flex-col justify-between group" style="--accent:{col}">'
            f'<div><div class="flex items-start justify-between mb-3"><span class="card-icon{icon_cls}"{icon_style}>{_svg(ic, "h-5 w-5")}</span>{chip}</div>'
            f'<h3 class="font-bold text-base mb-1 text-[var(--text-primary)]">{t}</h3>'
            f'<p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">{d}</p></div>'
            '<span class="text-xs font-bold text-[var(--brand-primary)]">Leer &rarr;</span></a>'
        )
    cards += "</div>"

PAGES["index.html"] = dict(
    title="Guía de uso de Facturanza",
    nav="Catálogo",
    desc="Guía oficial para facturar con Facturanza: configura Hacienda, emite, registra compras y prepara tu IVA.",
    body=(
        '<div class="bg-gradient-to-br from-sky-50 via-white to-sky-100 text-slate-900 dark:from-slate-900 dark:via-sky-950 dark:to-slate-900 dark:text-white rounded-3xl p-6 sm:p-10 mb-4 shadow-xl border border-sky-200 dark:border-sky-900/40">'
        '<div class="max-w-2xl"><span class="inline-block px-3 py-1 rounded-full bg-sky-100 text-sky-800 dark:bg-sky-500/20 dark:text-sky-200 text-xs font-bold tracking-wider uppercase mb-3 border border-sky-400/20">Guía oficial</span>'
        '<h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-3">Guía de uso de Facturanza</h1>'
        '<p class="text-slate-700 dark:text-slate-200 text-sm sm:text-base leading-relaxed mb-6">Todo lo que necesitas para facturar electrónicamente en Costa Rica: pasos claros, tal como los ves en la app.</p>'
        '<div class="flex flex-wrap items-center gap-3"><a href="empieza.html" class="px-4 py-2 rounded-xl text-xs font-bold bg-sky-600 text-white hover:bg-sky-500 dark:bg-sky-500 dark:text-slate-950 dark:hover:bg-sky-400 transition-colors">Empieza en 5 pasos &rarr;</a>'
        '<a href="ayuda.html" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-900/10 text-slate-900 hover:bg-slate-900/20 dark:bg-white/10 dark:text-white dark:hover:bg-white/20 transition-colors">Ayuda y solución de problemas</a></div></div></div>'
        + cards
        + f'<p class="mt-10 text-xs text-slate-500 dark:text-slate-400">Última revisión: {REVIEW_DATE}.</p>'
    ),
)
