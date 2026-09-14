# Semana 2 — Entregables

Todo lo de esta semana es de **equipo** (un único modelo compartido, sin entregas individuales). El modelo y su documentación viven en [`modelos/sysml/`](../../modelos/sysml/), no en esta carpeta — es un paquete que se sigue construyendo en la Semana 3.

| Qué | Formato / nombre | Dónde |
|---|---|---|
| Modelo de arquitectura (BDD) | `sistema.yaml` — copiado desde `base/modelos/` y editado en el sitio | [`../../modelos/sysml/sistema.yaml`](../../modelos/sysml/sistema.yaml) |
| Diagrama + tablas (generado) | `ARQUITECTURA.md` — regenerar con `render_arquitectura.py`, no editar a mano | [`../../modelos/sysml/ARQUITECTURA.md`](../../modelos/sysml/ARQUITECTURA.md) |
| Informe de Arquitectura | sección «Semana 2» de `INFORME.md` | [`../../modelos/sysml/INFORME.md`](../../modelos/sysml/INFORME.md) |

## Cómo entregar

1. Copiar `base/modelos/sistema.yaml` a `modelos/sysml/` (una sola vez).
2. Cada rol añade las propiedades de su ámbito directamente en `sistema.yaml` (ver la sección «Semana 2» de `INFORME.md` para el reparto).
3. Regenerar la vista:
   ```bash
   python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md
   ```
   Revisar que no reporta problemas de trazabilidad.
4. Rellenar la sección «Semana 2» de `INFORME.md`: observaciones y checklist de cierre.
5. Al cerrar la semana: 1 Pull Request a `master` con 1 commit por rol: `feat([rol]): propiedades del BDD nivel 1 — semana 2`.

Ver las instrucciones completas de rama/commit en la [página del curso, sección Repositorio](../../index.html#repositorio).
