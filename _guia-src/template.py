"""Plantilla común + componentes HTML de la guía."""
import html as _h
import os

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "guia", "assets", "img")

BASE_URL = "https://roadmap.facturanza.com/guia/"
LOGO = "https://storage.googleapis.com/facturanza-cr-public/logo_horizontal.png"

P_CLS = "text-sm text-slate-600 dark:text-slate-300 mb-4 leading-relaxed"


def h2(i, t):
    return f'<h2 id="{i}" class="text-2xl font-bold mt-12 mb-4">{t}</h2>\n'


def h3(t):
    return f'<h3 class="text-base font-bold mt-6 mb-2">{t}</h3>\n'


def p(t):
    return f'<p class="{P_CLS}">{t}</p>\n'


def ul(items):
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'<ul class="list-disc pl-5 space-y-1.5 {P_CLS}">{lis}</ul>\n'


def ol(items, start=1):
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'<ol start="{start}" class="list-decimal pl-5 space-y-2 {P_CLS}">{lis}</ol>\n'


def code(t):
    return f'<code class="code-font bg-slate-100 dark:bg-slate-800 px-1.5 py-0.5 rounded text-xs text-sky-700 dark:text-sky-300">{t}</code>'


def who(t):
    return (
        '<p class="inline-block text-xs font-semibold px-3 py-1 rounded-full mb-5 '
        'bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-200">'
        f"Quién puede: {t}</p>\n"
    )


_CALL = {
    "info": ("border-sky-500 bg-sky-50 dark:bg-sky-950/20", "text-sky-900 dark:text-sky-300"),
    "warn": ("border-amber-500 bg-amber-50 dark:bg-amber-950/20", "text-amber-900 dark:text-amber-400"),
    "danger": ("border-rose-500 bg-rose-50 dark:bg-rose-950/20", "text-rose-900 dark:text-rose-300"),
    "ok": ("border-emerald-500 bg-emerald-50 dark:bg-emerald-950/20", "text-emerald-900 dark:text-emerald-300"),
    "premium": ("call-premium bg-[var(--card-bg)]", "text-[var(--text-primary)]"),
}


def call(kind, title, text):
    b, t = _CALL[kind]
    return (
        f'<div class="my-6 p-5 rounded-2xl border-l-4 {b} text-slate-700 dark:text-slate-300">'
        f'<h3 class="font-bold text-sm mb-1 {t}">{title}</h3>'
        f'<p class="text-xs sm:text-sm leading-relaxed">{text}</p></div>\n'
    )


def cards(items, cols=2):
    c = {2: "sm:grid-cols-2", 3: "sm:grid-cols-2 lg:grid-cols-3"}[cols]
    out = f'<div class="grid grid-cols-1 {c} gap-4 mb-8">'
    for title, text in items:
        out += (
            '<div class="p-5 rounded-2xl border border-[var(--border-color)] bg-[var(--card-bg)] shadow-sm">'
            f'<h3 class="font-bold text-sm mb-1">{title}</h3>'
            f'<p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">{text}</p></div>'
        )
    return out + "</div>\n"


def table(headers, rows):
    th = "".join(
        f'<th class="px-4 py-3 text-left text-xs font-bold uppercase tracking-wider text-slate-600 dark:text-slate-300">{x}</th>'
        for x in headers
    )
    body = ""
    for r in rows:
        tds = "".join(
            f'<td class="px-4 py-3 text-xs sm:text-sm text-slate-700 dark:text-slate-300 align-top">{x}</td>' for x in r
        )
        body += f'<tr class="border-t border-[var(--border-color)]">{tds}</tr>'
    return (
        '<div class="overflow-x-auto rounded-2xl border border-[var(--border-color)] bg-[var(--card-bg)] mb-8">'
        f'<table class="w-full"><thead class="bg-slate-50 dark:bg-slate-800/60"><tr>{th}</tr></thead>'
        f"<tbody>{body}</tbody></table></div>\n"
    )


def matrix(title):
    return f'<div data-matrix-title="{_h.escape(title)}"></div>\n'


def head_scripts():
    return """    <script>
      (function () {
        try {
          var t = localStorage.getItem("theme");
          if (t === "dark" || (!t && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
            document.documentElement.classList.add("dark");
          }
        } catch (e) {}
      })();
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        darkMode: 'class',
        theme: { extend: {
          fontFamily: { sans: ['Inter', 'system-ui', 'sans-serif'] },
          borderRadius: { xl: '15px', '2xl': '20px' },
          colors: {
            slate: { 50: '#F5F5F5', 100: '#EBEBEB', 200: '#E4E4E4', 300: '#D0D0D0', 400: '#B0B0B0', 500: '#6B6B6B', 600: '#616161', 700: '#545454', 800: '#4D4D4D', 900: '#414141', 950: '#2E2E2E' },
            sky: { 50: '#EEF7FA', 100: '#C3E1EA', 200: '#A4D2DF', 300: '#86C4D5', 400: '#63B9CF', 500: '#4AA6BF', 600: '#3A8FA6', 700: '#307588', 800: '#255B6A', 900: '#1B414B', 950: '#12303A' },
          },
        } },
      };
    </script>
"""


def header_html():
    return f"""    <header class="sticky top-0 z-40 px-4 lg:px-8 py-3.5 flex items-center justify-between border-b border-[var(--border-color)] bg-[var(--bg-secondary)] shadow-sm">
      <div class="flex items-center space-x-3 sm:space-x-5">
        <button id="mobile-menu-btn" aria-label="Abrir índice" class="lg:hidden p-2 rounded-lg text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg>
        </button>
        <a href="index.html" class="flex items-center space-x-3">
          <img src="{LOGO}" alt="Facturanza" class="h-8" />
        </a>
        <div class="hidden sm:flex items-center pl-3 border-l border-slate-200 dark:border-slate-700">
          <span class="text-xs uppercase font-extrabold tracking-wider px-2.5 py-0.5 rounded-full bg-sky-100 text-sky-800 dark:bg-sky-900/60 dark:text-sky-300">Guía de uso</span>
        </div>
      </div>
      <div class="flex items-center space-x-3">
        <a href="../" class="hidden sm:inline-flex items-center text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-[var(--brand-primary)]">Novedades</a>
        <a href="https://app.facturanza.com" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 text-xs font-bold px-3.5 py-2 rounded-xl bg-sky-700 text-white hover:bg-sky-600 shadow-sm"><span>Ir a la app</span></a>
        <button id="theme-toggle" aria-label="Cambiar tema" class="relative inline-flex items-center h-6 rounded-full w-11 transition-colors bg-slate-300 dark:bg-sky-900">
          <span id="theme-toggle-indicator" class="inline-block w-4 h-4 transform bg-white rounded-full transition-transform duration-300 translate-x-1"></span>
        </button>
      </div>
    </header>
"""


def render_page(fname, page, nav, prev_, next_, review_date):
    title = page["title"]
    desc = page["desc"]
    full_title = f"{title} - Guía Facturanza" if fname != "index.html" else "Guía de uso - Facturanza"
    group = ""
    for g, items in nav:
        if any(f == fname for f, _, _ in items):
            group = g

    if fname == "index.html":
        main = page["body"]
    else:
        crumbs = (
            '<nav class="flex items-center space-x-2 text-xs text-slate-500 dark:text-slate-400 mb-4" aria-label="Ruta">'
            f'<a href="index.html" class="hover:underline">Guía</a><span>/</span><span>{group}</span><span>/</span>'
            f'<span class="text-[var(--brand-primary)] font-semibold">{page["nav"]}</span></nav>'
        )
        lead = f'<p class="text-base text-slate-600 dark:text-slate-300 leading-relaxed mb-8">{desc}</p>'
        pn = '<div class="mt-16 pt-6 border-t border-[var(--border-color)] flex flex-col sm:flex-row gap-3 sm:justify-between">'
        if prev_:
            pn += f'<a href="{prev_[0]}" class="px-4 py-3 rounded-xl border border-[var(--border-color)] text-xs font-semibold hover:border-[var(--brand-primary)]">&larr; {prev_[1]}</a>'
        else:
            pn += "<span></span>"
        if next_:
            pn += f'<a href="{next_[0]}" class="px-4 py-3 rounded-xl border border-[var(--border-color)] text-xs font-semibold hover:border-[var(--brand-primary)] text-right">Siguiente: {next_[1]} &rarr;</a>'
        pn += "</div>"
        foot = f'<p class="mt-8 text-xs text-slate-500 dark:text-slate-400">Última revisión: {review_date}. ¿Algo no coincide con lo que ves en la app? Revisa <a class="underline" href="ayuda.html">Ayuda</a>.</p>'
        main = (
            crumbs
            + f'<h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-3">{title}</h1>'
            + lead
            + page["body"]
            + pn
            + foot
        )

    return f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{_h.escape(full_title)}</title>
    <meta name="description" content="{_h.escape(desc)}" />
    <link rel="canonical" href="{BASE_URL}{fname if fname != 'index.html' else ''}" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="{_h.escape(full_title)}" />
    <meta property="og:description" content="{_h.escape(desc)}" />
    <meta property="og:url" content="{BASE_URL}{fname if fname != 'index.html' else ''}" />
{head_scripts()}    <link rel="icon" type="image/png" href="favicon.png" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="assets/guide.css" />
  </head>
  <body class="min-h-screen flex flex-col">
{header_html()}
    <div class="container mx-auto px-4 lg:px-8 py-8 flex-grow flex gap-8">
      <aside id="sidebar-drawer" class="fixed inset-y-0 left-0 z-30 w-72 bg-[var(--bg-secondary)] border-r border-[var(--border-color)] p-6 transform -translate-x-full transition-transform duration-300 lg:translate-x-0 lg:static lg:w-64 lg:p-0 lg:bg-transparent lg:border-none flex flex-col shrink-0">
        <div class="lg:hidden flex items-center justify-between pb-4 mb-4 border-b border-slate-200 dark:border-slate-700">
          <span class="font-bold text-lg">Índice</span>
          <button id="close-sidebar-btn" aria-label="Cerrar índice" class="p-1 rounded text-slate-500">✕</button>
        </div>
        <div class="sticky top-20 overflow-y-auto max-h-[calc(100vh-6rem)] pr-2 custom-scrollbar">
          <nav id="doc-sidebar-nav" class="space-y-4"></nav>
        </div>
      </aside>
      <div id="sidebar-backdrop" class="fixed inset-0 bg-slate-900/50 z-20 hidden lg:hidden"></div>

      <main id="doc-main-content" class="flex-1 min-w-0 max-w-4xl pb-16">
{main}
      </main>

      <aside class="hidden xl:block w-56 shrink-0">
        <div class="sticky top-20" id="right-toc-nav"></div>
      </aside>
    </div>

    <script src="assets/guide.js"></script>
  </body>
</html>
"""


def _v(fname):
    """Cache-buster: la fecha del archivo, para que los navegadores recarguen una captura reemplazada."""
    try:
        return int(os.path.getmtime(os.path.join(IMG_DIR, fname)))
    except OSError:
        return 0


def _pair(key, devs, alt, cls):
    """Devuelve el par claro/oscuro del primer dispositivo (de `devs`) que tenga ambas imágenes."""
    for dev in devs:
        lf, df = f"{key}_{dev}_light.png", f"{key}_{dev}_dark.png"
        if os.path.exists(os.path.join(IMG_DIR, lf)) and os.path.exists(os.path.join(IMG_DIR, df)):
            a = _h.escape(alt)
            return (
                f'<img src="assets/img/{lf}?v={_v(lf)}" alt="{a}" loading="lazy" class="{cls} block dark:hidden" />'
                f'<img src="assets/img/{df}?v={_v(df)}" alt="{a} (tema oscuro)" loading="lazy" class="{cls} hidden dark:block" />'
            )
    return ""


_BADGE = (
    '<span class="inline-block text-xs font-bold uppercase tracking-wider px-2.5 py-1 rounded-md '
    'bg-[var(--brand-secondary)]/15 text-[var(--brand-secondary)] dark:bg-[var(--brand-primary)]/20 '
    'dark:text-[var(--brand-primary)]">{}</span>'
)


def shots(key, caption):
    """Matriz real (Escritorio arriba; Tablet y Móvil debajo, mismo alto y bordes alineados), claro/oscuro.

    Móvil usa iphone y, si la función no existe en iOS, `phone` (Chrome/Android a tamaño teléfono).
    """
    desk = _pair(key, ["chrome"], caption + " - Escritorio", "w-full h-auto rounded-xl")
    h = "h-[300px] sm:h-[360px] md:h-[440px] lg:h-[480px]"
    tab = _pair(key, ["fold", "tablet"], caption + " - Tablet", "h-full w-auto object-contain rounded-xl")
    mob = _pair(key, ["iphone", "phone"], caption + " - Móvil", "h-full w-auto object-contain rounded-2xl")
    if not (desk or tab or mob):
        return ""
    frame = "rounded-xl shadow-lg border-2 border-[var(--bg-secondary)] overflow-hidden"
    out = (
        '<figure class="my-8 mx-auto w-full max-w-[425px] sm:max-w-[496px] md:max-w-[618px] lg:max-w-[690px] '
        'flex flex-col items-center gap-6">'
    )
    if desk:
        out += (
            '<div class="w-full flex flex-col items-start"><div class="mb-2">'
            + _BADGE.format("💻 Escritorio")
            + f'</div><div class="w-full {frame}">{desk}</div></div>'
        )
    if tab or mob:
        out += '<div class="flex flex-row justify-between items-end gap-6 w-full">'
        for badge, img, extra in (("📱 Tablet", tab, ""), ("📲 Móvil", mob, "")):
            if img:
                out += (
                    f'<div class="flex flex-col items-start"><div class="mb-2">{_BADGE.format(badge)}</div>'
                    f'<div class="{h} {frame} flex items-center justify-center">{img}</div></div>'
                )
        out += "</div>"
    out += f'<figcaption class="text-xs text-slate-500 dark:text-slate-400 self-start">{caption}</figcaption></figure>\n'
    return out


def single(key, caption, width="max-w-[230px]"):
    """Una sola imagen (recorte) con par claro/oscuro, sin matriz de dispositivos."""
    img = _pair(key, ["chrome"], caption, "w-full h-auto rounded-xl")
    # _pair solo mira {key}_chrome_*; para recortes usamos el nombre sin dispositivo
    lf, df = f"{key}_light.png", f"{key}_dark.png"
    a = _h.escape(caption)
    return (
        f'<figure class="my-8 mx-auto {width}">'
        f'<img src="assets/img/{lf}?v={_v(lf)}" alt="{a}" loading="lazy" class="w-full h-auto rounded-xl shadow-lg block dark:hidden" />'
        f'<img src="assets/img/{df}?v={_v(df)}" alt="{a} (tema oscuro)" loading="lazy" class="w-full h-auto rounded-xl shadow-lg hidden dark:block" />'
        f'<figcaption class="mt-2 text-xs text-slate-500 dark:text-slate-400">{caption}</figcaption></figure>\n'
    )
