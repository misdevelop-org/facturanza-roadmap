#!/usr/bin/env python3
"""Genera las páginas de facturanza-roadmap/guia/*.html.

Uso:  python3 _guia-src/build_guia.py   (desde la raíz de facturanza-roadmap)

Fuente de verdad del contenido: la app real (facturanza_common) y docs/knowledge/product/*.md
del monorepo. Cuando cambie la UI, edita el contenido aquí y vuelve a generar.
Las capturas siguen como placeholders (data-matrix-title) hasta la fase de screenshots.
"""
import os
from content import PAGES, NAV, REVIEW_DATE
from template import render_page

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "guia")

flat = [(f, t) for _, items in NAV for (f, t, _d) in items if f != "index.html"]

for i, (fname, title) in enumerate(flat):
    prev_ = flat[i - 1] if i > 0 else None
    next_ = flat[i + 1] if i < len(flat) - 1 else None
    page = PAGES[fname]
    html = render_page(fname, page, NAV, prev_, next_, REVIEW_DATE)
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("ok", fname)

with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as fh:
    fh.write(render_page("index.html", PAGES["index.html"], NAV, None, None, REVIEW_DATE))
print("ok index.html")
