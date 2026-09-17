# Modelos de arquitectura SysML

El modelo de arquitectura del equipo vive aquí, como datos planos (YAML), no como un
archivo binario de una herramienta gráfica. El YAML es la fuente de verdad — nunca se
edita el diagrama a mano, se edita el YAML y se regenera.

| Archivo | Qué es |
|---|---|
| `sistema.yaml` | El modelo: bloques, propiedades, interfaces, conexiones |
| `ARQUITECTURA.md` | Generado — diagramas BDD/IBD (Mermaid) + tablas. Se ve renderizado directamente en GitHub |
| `INFORME.md` | Observaciones e interdependencias, con una sección por hito (BDD, IBD) |

## Cómo usarlo

1. Copiar la versión base desde [`base/modelos/sistema.yaml`](../../base/modelos/) a esta carpeta, una sola vez.
2. Editar `sistema.yaml` (bloques y propiedades primero; interfaces y conexiones después — ver [Fase 2 — Arquitectura](../../fases/02-arquitectura/)).
3. Regenerar el diagrama:
   ```bash
   python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md
   ```
   El script también valida trazabilidad (propiedades sin requisito, interfaces no declaradas) y lo avisa por consola.
4. Commitear tanto `sistema.yaml` como `ARQUITECTURA.md` — así el diagrama se ve en GitHub sin que nadie tenga que ejecutar nada.

Al ser texto plano, varios roles pueden editar `sistema.yaml` en paralelo y fusionar sus cambios con git con normalidad — ver la política de ramas y commits en la [página del curso](../../index.html#repositorio).
