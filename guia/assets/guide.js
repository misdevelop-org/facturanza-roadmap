/**
 * Facturanza Documentation Portal - Shared Navigation & Interactivity Engine
 * Inspired by Flutter Docs (docs.flutter.dev)
 */

const NAV_STRUCTURE = [
  {
    group: "Primeros pasos",
    items: [
      { title: "Catálogo de la guía", file: "index.html", icon: "book-open" },
      { title: "Empieza en 5 pasos", file: "empieza.html", icon: "user-plus" },
      { title: "Cuenta e inicio de sesión", file: "get-started.html", icon: "user" },
      { title: "Mis Empresas", file: "lobby.html", icon: "grid" }
    ]
  },
  {
    group: "Operación diaria",
    items: [
      { title: "Inicio", file: "dashboard.html", icon: "layout-dashboard" },
      { title: "Facturas", file: "facturas.html", icon: "receipt" },
      { title: "Notas de crédito", file: "notas-credito.html", icon: "receipt" },
      { title: "Clientes", file: "clientes.html", icon: "users" },
      { title: "Productos y CABYS", file: "productos.html", icon: "tag" },
      { title: "Compras", file: "compras.html", icon: "shopping-bag" },
      { title: "Facturito (IA)", file: "facturito.html", icon: "sparkles" }
    ]
  },
  {
    group: "Cierre fiscal",
    items: [
      { title: "Declaraciones", file: "reportes.html", icon: "bar-chart" }
    ]
  },
  {
    group: "Administración",
    items: [
      { title: "Negocio y credenciales", file: "negocio.html", icon: "briefcase" },
      { title: "Roles y acceso", file: "roles.html", icon: "users" },
      { title: "Sucursales y terminales", file: "sucursales.html", icon: "store" },
      { title: "Marcas", file: "marcas.html", icon: "tag" },
      { title: "Planes y pagos", file: "planes.html", icon: "briefcase" },
      { title: "Perfil", file: "perfil.html", icon: "user" }
    ]
  },
  {
    group: "Ayuda",
    items: [
      { title: "Ayuda", file: "ayuda.html", icon: "book-open" },
      { title: "Soporte", file: "soporte.html", icon: "user" }
    ]
  }
];

function getCurrentFile() {
  const path = window.location.pathname;
  const parts = path.split("/").filter(Boolean);
  const lastPart = parts[parts.length - 1] || "index.html";
  return lastPart.includes(".html") ? lastPart : "index.html";
}

function getIconSvg(iconName) {
  const icons = {
    "book-open": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>`,
    "user-plus": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" /></svg>`,
    "grid": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" /></svg>`,
    "sparkles": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0 text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" /></svg>`,
    "layout-dashboard": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>`,
    "receipt": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>`,
    "shopping-bag": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" /></svg>`,
    "users": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" /></svg>`,
    "tag": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" /></svg>`,
    "store": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" /></svg>`,
    "bar-chart": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>`,
    "briefcase": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>`,
    "user": `<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>`
  };
  return icons[iconName] || icons["book-open"];
}

function initNavigation() {
  const currentFile = getCurrentFile();
  const sidebarContainer = document.getElementById("doc-sidebar-nav");
  if (!sidebarContainer) return;

  let html = "";
  NAV_STRUCTURE.forEach((group) => {
    html += `<div class="nav-group-title">${group.group}</div><div class="space-y-0.5">`;
    group.items.forEach((item) => {
      const isActive = currentFile === item.file;
      html += `
        <a href="${item.file}" class="nav-item ${isActive ? 'active' : ''}">
          ${getIconSvg(item.icon)}
          <span class="truncate">${item.title}</span>
        </a>
      `;
    });
    html += `</div>`;
  });

  sidebarContainer.innerHTML = html;
}

function initTableOfContents() {
  const rightTocContainer = document.getElementById("right-toc-nav");
  if (!rightTocContainer) return;

  const contentArea = document.getElementById("doc-main-content");
  if (!contentArea) return;

  const headings = contentArea.querySelectorAll("h2, h3");
  if (headings.length === 0) {
    rightTocContainer.parentElement.style.display = "none";
    return;
  }

  let html = `<p class="text-xs uppercase font-extrabold tracking-wider text-slate-400 mb-3 px-2">En esta página</p><nav class="space-y-1">`;
  headings.forEach((heading, idx) => {
    if (!heading.id) {
      heading.id = "section-" + idx;
    }
    const isH3 = heading.tagName.toLowerCase() === "h3";
    html += `
      <a href="#${heading.id}" class="block text-xs py-1 px-2 rounded hover:text-[var(--brand-primary)] text-slate-500 dark:text-slate-400 transition-colors ${isH3 ? 'pl-4' : 'font-medium'} truncate" data-target="${heading.id}">
        ${heading.textContent.trim()}
      </a>
    `;
  });
  html += `</nav>`;
  rightTocContainer.innerHTML = html;

  // ScrollSpy for right TOC
  const links = rightTocContainer.querySelectorAll("a");
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        links.forEach((l) => {
          if (l.getAttribute("data-target") === id) {
            l.classList.add("text-[var(--brand-primary)]", "font-bold");
            l.classList.remove("text-slate-500", "dark:text-slate-400");
          } else {
            l.classList.remove("text-[var(--brand-primary)]", "font-bold");
            l.classList.add("text-slate-500", "dark:text-slate-400");
          }
        });
      }
    });
  }, { rootMargin: "-10% 0px -70% 0px", threshold: 0 });

  headings.forEach((h) => observer.observe(h));
}

function initTheme() {
  const themeToggle = document.getElementById("theme-toggle");
  const indicator = document.getElementById("theme-toggle-indicator");
  const body = document.documentElement;

  function updateIndicator(isDark) {
    if (indicator) {
      indicator.classList.toggle("translate-x-5", isDark);
      indicator.classList.toggle("translate-x-1", !isDark);
    }
  }

  function toggle() {
    body.classList.toggle("dark");
    const isDark = body.classList.contains("dark");
    localStorage.setItem("theme", isDark ? "dark" : "light");
    updateIndicator(isDark);
  }

  const isDark = localStorage.getItem("theme") === "dark" ||
    (!("theme" in localStorage) && window.matchMedia("(prefers-color-scheme: dark)").matches);

  if (isDark) body.classList.add("dark");
  updateIndicator(isDark);

  if (themeToggle) {
    themeToggle.addEventListener("click", toggle);
  }
}

function initMobileMenu() {
  const btn = document.getElementById("mobile-menu-btn");
  const sidebar = document.getElementById("sidebar-drawer");
  const backdrop = document.getElementById("sidebar-backdrop");
  const closeBtn = document.getElementById("close-sidebar-btn");

  if (!btn || !sidebar || !backdrop) return;

  function open() {
    sidebar.classList.remove("-translate-x-full");
    backdrop.classList.remove("hidden");
  }

  function close() {
    sidebar.classList.add("-translate-x-full");
    backdrop.classList.add("hidden");
  }

  btn.addEventListener("click", open);
  backdrop.addEventListener("click", close);
  if (closeBtn) closeBtn.addEventListener("click", close);
}

// 6-Screenshot Matrix Component Helper
function renderDevicePlaceholder(title, deviceType, isDark) {
  const bg = isDark ? "#4a4a4a" : "#f5f5f5";
  const border = isDark ? "#6f6f6f" : "#d0d0d0";
  const text = isDark ? "#e0e0e0" : "#616161";
  const badgeColor = isDark ? "#86c4d5" : "#255b6a";

  let dimension = "";
  if (deviceType === "desktop") dimension = "💻 ESCRITORIO (1440 × 900)";
  else if (deviceType === "tablet") dimension = "📱 TABLET (768 × 1024)";
  else dimension = "📲 MÓVIL (390 × 844)";

  return `
    <div class="w-full h-full flex flex-col items-center justify-center p-6 text-center device-placeholder" style="background-color: ${bg};">
      <span class="font-mono text-[11px] font-bold tracking-wider mb-1" style="color: ${badgeColor};">
        ${dimension}
      </span>
      <p class="text-xs font-semibold max-w-[260px] truncate" style="color: ${text};">
        ${title}
      </p>
      <span class="mt-2 text-[10px] font-mono px-2 py-0.5 rounded-full border border-dashed text-slate-400" style="border-color: ${border};">
        Captura Fase 2 (Marionette MCP)
      </span>
    </div>
  `;
}

function renderMatrix(title) {
  return `
    <div class="my-8 p-6 rounded-2xl border border-[var(--border-color)] bg-[var(--card-bg)] shadow-sm">
      <div class="flex items-center justify-between mb-4">
        <div>
          <h4 class="text-sm font-bold text-[var(--text-primary)]">Matriz Visual Multiplataforma (6 Screenshots)</h4>
          <p class="text-xs text-slate-500">Comprobación responsive en 3 dispositivos y 2 temas (Claro / Oscuro)</p>
        </div>
        <span class="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-sky-100 text-sky-800 dark:bg-sky-950 dark:text-sky-300">
          Modo Adaptativo
        </span>
      </div>
      <div class="flex flex-col 2xl:flex-row items-center 2xl:items-end justify-center gap-6 2xl:gap-8 mx-auto w-full">
        <!-- Fila 1: Escritorio -->
        <div class="w-full 2xl:w-[580px] flex flex-col items-start">
          <div class="w-full h-[280px] sm:h-[320px] rounded-xl shadow border border-slate-200 dark:border-slate-700 overflow-hidden">
            <div class="w-full h-full block dark:hidden">
              ${renderDevicePlaceholder(title, "desktop", false)}
            </div>
            <div class="w-full h-full hidden dark:block">
              ${renderDevicePlaceholder(title, "desktop", true)}
            </div>
          </div>
        </div>

        <!-- Fila 2: Tablet y Móvil -->
        <div class="flex flex-row justify-between items-center gap-4 w-full 2xl:w-auto">
          <!-- Tablet -->
          <div class="flex-1 2xl:w-[220px] h-[280px] sm:h-[320px] rounded-xl shadow border border-slate-200 dark:border-slate-700 overflow-hidden">
            <div class="w-full h-full block dark:hidden">
              ${renderDevicePlaceholder(title, "tablet", false)}
            </div>
            <div class="w-full h-full hidden dark:block">
              ${renderDevicePlaceholder(title, "tablet", true)}
            </div>
          </div>

          <!-- Móvil -->
          <div class="flex-1 2xl:w-[150px] h-[280px] sm:h-[320px] rounded-2xl shadow-lg border-2 border-slate-300 dark:border-slate-700 overflow-hidden">
            <div class="w-full h-full block dark:hidden">
              ${renderDevicePlaceholder(title, "mobile", false)}
            </div>
            <div class="w-full h-full hidden dark:block">
              ${renderDevicePlaceholder(title, "mobile", true)}
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  initTheme();
  initNavigation();
  initTableOfContents();
  initMobileMenu();

  // Inject matrix placeholders if container exists
  document.querySelectorAll("[data-matrix-title]").forEach((el) => {
    const title = el.getAttribute("data-matrix-title");
    el.innerHTML = renderMatrix(title);
  });
});
