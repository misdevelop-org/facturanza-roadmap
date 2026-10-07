"""Genera docs/plans/guia-review/screenshot_map.md desde guia/*.html. Ejecutar desde facturanza-roadmap."""
import re, os, sys, datetime
sys.path.insert(0, '_guia-src')
from content import NAV
IMG = 'guia/assets/img'
DRAWER_DESKTOP = {  # clave -> cómo llegar (Escritorio, con menú lateral)
 'inicio_habilitada': 'MIS Develop › Inicio', 'inicio_inhabilitada': 'AE Productions › Inicio', 'negocio_facturacion': 'MIS Develop › Negocio',
 'facturas_lista': 'MIS Develop › Facturas', 'nc_dialogo': 'Facturas › ⋮ › Crear nota de crédito (diálogo)', 'clientes_menu': 'Clientes',
 'productos_menu': 'Productos', 'compras_menu': 'Compras (agosto 2026)', 'compras_subir': 'Compras › Subir compra',
 'declaraciones_declaracion': 'Declaraciones › Declaración', 'declaraciones_historial': 'Declaraciones › Historial', 'roles_tab': 'Negocio › Roles',
 'sucursales_menu': 'Sucursales', 'planes_sin_facturas': 'Golden gard (0 facturas) › Crear factura'}
DRAWER_SINGLE = {'clientes_crear': 'Clientes con cuadro ámbar en Crear cliente (imagen única, incluye drawer)',
                 'marcas_drawer': 'Panel derecho de empresas (NO es el drawer izquierdo)'}
pages = [(f, t) for g, items in NAV for f, t, d in items]
out = ['# Mapa de capturas de la guía\n',
 f'Generado el {datetime.date.today()} con `_guia-src/build_map.py` desde `facturanza-roadmap/guia/*.html`. Imágenes en `guia/assets/img/` (copias sin recortar en `docs/plans/guia-review/screenshots/`). Cada captura existe en `_light` y `_dark`.\n',
 '**Tipo**: *Matriz* = Escritorio (`_chrome_`) + Tablet (`_tablet_`/`_fold_`) + Móvil (`_phone_`/`_iphone_`); *CLDSS* = recorte único claro/oscuro. **Conteo**: «capturas» cuenta cada par claro/oscuro como 1; «archivos» cuenta cada PNG.\n']
rows = []; total_c = total_f = 0; sections = []
for f, t in pages:
    h = open('guia/' + f).read()
    files = sorted(set(re.findall(r'assets/img/([a-z0-9_]+\.png)', h)))
    if not files: continue
    caps = {}
    for fn in files:
        m = re.match(r'(.+?)(?:_(chrome|tablet|fold|phone|iphone))?_(light|dark)\.png$', fn)
        k, dev = m.group(1), m.group(2)
        caps.setdefault((k, dev), set()).add(m.group(3))
    ncap = len(caps) // 1  # cada (clave,dispositivo) es una captura (par claro/oscuro)
    rows.append((t, f, ncap, len(files)))
    total_c += ncap; total_f += len(files)
    bykey = {}
    for (k, dev) in caps: bykey.setdefault(k, []).append(dev)
    sec = [f'\n## {t} (`{f}`) — {ncap} capturas · {len(files)} archivos\n', '| Clave | Tipo | Dispositivos | 🧭 Drawer | Capturas |', '|---|---|---|---|---|']
    for k, devs in bykey.items():
        crop = devs == [None]
        dr = ''
        if k in DRAWER_SINGLE: dr = '🧭 ' + ('panel derecho' if k == 'marcas_drawer' else 'sí (imagen única)')
        elif not crop and k in DRAWER_DESKTOP: dr = '🧭 solo Escritorio'
        elif not crop and k.startswith(('cuenta_', 'lobby')): dr = '— (sin empresa abierta)'
        elif not crop: dr = '— (pantalla completa)'
        sec.append(f'| `{k}` | {"CLDSS" if crop else "Matriz"} | {"recorte" if crop else ", ".join(sorted(devs))} | {dr} | {len(devs)} |')
    sections.append('\n'.join(sec))
out.append('## Resumen por página\n')
out.append('| Página | Archivo | Capturas | Archivos PNG |\n|---|---|---:|---:|')
for t, f, c, n in rows: out.append(f'| {t} | `{f}` | {c} | {n} |')
out.append(f'| **Total (con repeticiones entre páginas)** | | **{total_c}** | **{total_f}** |')
uniq = len([x for x in os.listdir(IMG) if x.endswith('.png')])
out.append(f'\nArchivos únicos en `guia/assets/img/`: **{uniq}** (algunas capturas se reutilizan en varias páginas, p. ej. Inicio y Negocio en Empieza e Inicio).\n')
out += sections
out.append('\n---\n\n## 🧭 Capturas que muestran el menú lateral (drawer) de la empresa\n')
out.append('Si cambia una etiqueta o se agrega/quita una opción del drawer izquierdo (Inicio, Facturas, Compras, Clientes, Productos, Sucursales, Declaraciones, Negocio, Perfil), hay que **retomar solo la versión Escritorio (`_chrome_`) en claro y oscuro** de estas claves. Tablet y móvil usan el botón de menú. Las pantallas completas (formularios, detalle de factura/compra/terminal, planes y pago), los recortes, login, registro y Mis Empresas no muestran el drawer.\n')
out.append('| Clave | Archivos a retomar | Cómo llegar |\n|---|---|---|')
for k, how in DRAWER_DESKTOP.items(): out.append(f'| `{k}` | `{k}_chrome_light.png`, `{k}_chrome_dark.png` | {how} |')
for k, how in DRAWER_SINGLE.items(): out.append(f'| `{k}` | `{k}_light.png`, `{k}_dark.png` | {how} |')
out.append('\n## Otras dependencias visibles a vigilar\n- **Tarjeta Nota de crédito / pestañas**: `nc_tarjeta`, `facturas_lista`.\n- **Panel derecho de empresas (Marcas)**: `marcas_drawer`.\n- **Datos personales a tapar con `redact`**: `roles_tab`, `nc_formulario`, `nc_adjunta`, `compras_form`, `declaraciones_historial`, `sucursales_terminal`, `perfil_pagina`, `perfil_datos`.\n- **Dispositivos especiales**: Perfil con Móvil en iPhone y Escritorio/Tablet en Chrome; Móvil en Chrome 390×844 (`_phone_`) donde iOS no puede mostrar la función (App Store).\n')
open('../docs/plans/guia-review/screenshot_map.md', 'w').write('\n'.join(out) + '\n')
print(total_c, total_f, uniq)
