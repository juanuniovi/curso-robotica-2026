# Fase 2 — Arquitectura — Entregables

Todo lo de esta fase es de **equipo** (un único modelo compartido, sin entregas individuales). El modelo y su documentación viven en [`modelos/sysml/`](../../modelos/sysml/), no en esta carpeta.

| Qué | Formato / nombre | Dónde |
|---|---|---|
| Modelo de arquitectura (BDD + IBD) | `sistema.yaml` — copiado desde `base/modelos/` y editado en el sitio | [`../../modelos/sysml/sistema.yaml`](../../modelos/sysml/sistema.yaml) |
| Diagrama + tablas (generado) | `ARQUITECTURA.md` — regenerar con `render_arquitectura.py`, no editar a mano | [`../../modelos/sysml/ARQUITECTURA.md`](../../modelos/sysml/ARQUITECTURA.md) |
| Informe de Arquitectura | secciones «BDD» e «IBD» de `INFORME.md` | [`../../modelos/sysml/INFORME.md`](../../modelos/sysml/INFORME.md) |

## Cómo entregar

1. Copiar `base/modelos/sistema.yaml` a `modelos/sysml/` (una sola vez).
2. **BDD** — cada rol añade las propiedades de su ámbito directamente en `sistema.yaml` (ver la sección «BDD» de `INFORME.md` para el reparto). Regenerar la vista y revisar que no reporta problemas de trazabilidad.
3. **IBD** — cada rol caracteriza sus interfaces y añade las conexiones correspondientes en `sistema.yaml` (ver la sección «IBD» de `INFORME.md` para el reparto). Regenerar la vista de nuevo.
   ```bash
   python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md
   ```
4. Rellenar `INFORME.md`: observaciones y checklist de cierre de cada sección.
5. Al cerrar la fase: tag de git `baseline-v1.0` y 1 Pull Request a `master` con 1 commit por rol: `feat([rol]): arquitectura BDD+IBD nivel 1`.

Ver las instrucciones completas de rama/commit en la [página del curso, sección Repositorio](../../index.html#repositorio).
