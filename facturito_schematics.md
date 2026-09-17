# 🚀 Propuesta Técnica y Roadmap: Facturito para Usuarios Finales 🤖✨

¡Hola, equipo de **Facturanza**! 🌟 Aquí les presento la especificación técnica completa y el plan de ruta para llevar a **Facturito** (nuestro tierno y brillante asistente de IA) directamente a la palma de la mano de nuestros usuarios finales en las versiones **V1.8** y **V2.0**. 🌸

---

## 🛠️ 1. Arquitectura de Implementación

Para asegurar que la plataforma sea escalable, segura y no represente un costo desmedido de infraestructura, utilizaremos nuestra arquitectura modular existente en Flutter y Firebase. 💻🔥

### 🔄 Flujo de Datos Arquitectónico:
1. **Capa de Presentación (`facturanza_common`):** Escucha en tiempo real los cambios en la base de datos de Firestore. 📱
2. **Base de Datos (Firestore):** Almacena las conversaciones de forma segura en la ruta de la empresa. 🗄️
3. **Capa de Orquestación (`facturanza_backend`):** Se activa mediante un trigger de escritura en Firestore y ejecuta la lógica de Genkit con el Quota Gate. 🤖
4. **Validaciones e Integración (`facturanza_common`):** Valida límites de suscripción, inyecta el contexto de negocio y conecta de forma segura con el proveedor del LLM. 📦☁️

---

### 🔒 A. Capa de Datos y Seguridad (Firestore)
*   **Ruta de Colección:** `/enterprises/{enterpriseId}/facturito_sessions/{sessionId}/messages`
*   **Reglas de Seguridad (Firestore Rules):** Solo los usuarios autenticados que pertenezcan a la empresa (`enterpriseId`) mediante roles válidos en sus claims de Firebase Auth podrán leer y escribir en esta ruta. 🛡️
*   **Estructura del Mensaje (JSON):**
    ```json
    {
      "id": "msg_12345",
      "sender": "user",
      "text": "Sugerime un código CABYS para desarrollo de software",
      "timestamp": "FieldValue.serverTimestamp()",
      "metadata": {
        "intent": "cabys_search",
        "referenced_document_id": "doc_abc123" 
      }
    }
    ```

---

### ⚙️ B. Backend Orchestration (`facturanza_backend` con Genkit)
*   **Quota Gate (Control de Consumo):** Una función intermedia verificará que el plan de suscripción de la empresa tenga créditos disponibles para consultas de IA antes de procesar el prompt y llamar a la API del LLM. 💳⚠️
*   **Genkit Flow (`facturitoUserFlow`):** 
    1. Recibe el mensaje del usuario y el ID de su empresa. 🏢
    2. Inyecta el contexto del sistema (esquema CABYS de Costa Rica, catálogo de productos del cliente y directrices de Hacienda). 🇨🇷
    3. Llama al LLM de manera segura. 🤖
    4. Guarda la respuesta directamente en la subcolección de Firestore como `"sender": "facturito"`. 📝

---

### 📱 C. Front-End (`facturanza_common`)
*   **Módulo Reutilizable:** `facturanza_common/lib/src/features/facturito_chat` 📦
*   **Manejo de Estado:** `FacturitoChatCubit` para manejar la carga de mensajes en tiempo real, estados de "escribiendo..." (`isTyping`) y reintentos en caso de fallos de red. 🔄

---

## ✨ 2. Funcionalidades de Alto Valor para el Usuario

Nuestra meta es transformar la facturación de una obligación tributaria aburrida a una experiencia de gestión sumamente sencilla y amigable. 🥰

*   **🔍 Buscador Inteligente de CABYS:** El usuario describe su producto en lenguaje natural y Facturito le sugiere el código CABYS exacto con su tarifa de IVA correspondiente para guardarlo en su catálogo con un solo clic.
*   **❌ Traductor de Errores de Hacienda:** Explica de forma sencilla por qué se rechazó un documento (XML de Hacienda) y le da los pasos exactos para solucionarlo y volver a enviarlo. 📝
*   **📑 Creación de Cotizaciones por Chat (V1.8):** Creación de proformas mediante instrucciones de texto simples y conversión inmediata a factura electrónica una vez aprobadas por su cliente. 💸
*   **⛽ Categorización Inteligente de Gastos (V2.0):** Clasificación automática de facturas de compras recibidas mediante nuestro flujo de ingesta de correos, facilitando la declaración del IVA. 📊
*   **📈 Reportes Rápidos de Negocio:** Consultas directas de desempeño comercial como *"¿Cuánto he facturado este mes?"* o *"¿Cuál es mi cliente top?"* presentadas en lindos resúmenes ejecutivos en el chat. 🏆

---

## 🗺️ 3. Roadmap de Producto (Fases de Lanzamiento)

### 🟩 Fase 1: V1.8 (Cimiento y Utilidades Críticas) - Enfoque: Reducción de Soporte 🛠️
*   **Objetivo:** Aliviar los dolores de cabeza más comunes del usuario final (CABYS y Errores de Hacienda) y habilitar la interfaz básica de chat.
*   **Funcionalidades Clave:**
    *   Interfaz de chat flotante y persistente en la app móvil y web. 💬
    *   Buscador Inteligente de Códigos CABYS con asignación de IVA automática. 🔍
    *   Explicador de Errores de Hacienda (traducción de XML de rechazo). ❌
    *   Control básico de cuotas mensuales de IA por plan de suscripción. 💳

### 🟦 Fase 2: V2.0 (Productividad y Automatización) - Enfoque: Copiloto de Negocios 🚀
*   **Objetivo:** Convertir a Facturito en un asistente proactivo que automatice tareas administrativas complejas.
*   **Funcionalidades Clave:**
    *   Creación y gestión de Cotizaciones mediante lenguaje natural. 📑
    *   Conversión de Cotizaciones aprobadas a Facturas Electrónicas de Hacienda. 🔄
    *   Categorización inteligente de Gastos y Compras (Egresos) vía email parser. ⛽
    *   Reportes rápidos de ventas e impuestos por chat. 📊
    *   Tablero de control en el panel Admin para optimizar prompts y ver analíticas de tokens consumidos. 🎛️

---

## 📋 4. Desglose de Tareas por Equipo (WBS)

### 💻 Front-End (`facturanza` / `facturanza_common`)
- [ ] **FE-101:** Diseñar la interfaz de usuario de la burbuja y pantalla de chat de Facturito (diseño tierno, amigable y limpio en Flutter). 🎨
- [ ] **FE-102:** Implementar `FacturitoChatCubit` para escuchar la subcolección de Firestore en tiempo real. 🔄
- [ ] **FE-103:** Crear el widget de sugerencias rápidas (ej: botones de *"Buscar CABYS"*, *"Explicar último error de Hacienda"*). ⚡
- [ ] **FE-104:** Implementar el indicador visual de *"Facturito está escribiendo..."* para mejorar la experiencia de usuario (UX). 💬

### ⚙️ Back-End (`facturanza_backend`)
- [ ] **BE-201:** Desarrollar el Cloud Function `onUserMessageTrigger` que se activa al crearse un nuevo mensaje del usuario en Firestore. ☁️
- [ ] **BE-202:** Implementar el middleware de seguridad **Quota Gate** que consulte el plan activo de la empresa en Firestore antes de llamar al LLM. 🛡️
- [ ] **BE-203:** Configurar el flujo de Genkit con el System Prompt oficial de Facturito (personalidad, restricciones de seguridad y conocimiento de Hacienda de Costa Rica). 🤖
- [ ] **BE-204:** Integrar la API de búsqueda semántica de CABYS dentro del flujo de herramientas (Tools) del LLM. 🔍

### 👑 Admin App (`facturanza-admin`)
- [ ] **ADM-301:** Crear la pestaña de configuración global para Facturito (selección de modelo de lenguaje, temperatura y edición del System Prompt). 🎛️
- [ ] **ADM-302:** Diseñar el panel de control de límites de IA (asignar cuántas consultas mensuales gratuitas tiene cada plan de suscripción: Pro, Pyme, Enterprise). 📊
- [ ] **ADM-303:** Implementar pantalla de auditoría de costos de API de IA (monitoreo de tokens consumidos por empresa para evitar sorpresas financieras). 💸
