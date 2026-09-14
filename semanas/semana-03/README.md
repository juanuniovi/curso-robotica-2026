# Semana 3 — Entregables

Todo lo de esta semana es de **equipo**. Se sigue trabajando sobre el mismo paquete de la Semana 2, en [`modelos/sysml/`](../../modelos/sysml/).

| Qué | Formato / nombre | Dónde |
|---|---|---|
| Modelo de arquitectura (IBD) | `sistema.yaml` actualizado: interfaces + conexiones | [`../../modelos/sysml/sistema.yaml`](../../modelos/sysml/sistema.yaml) |
| Diagrama + tablas (generado) | `ARQUITECTURA.md` — regenerar con `render_arquitectura.py`, no editar a mano | [`../../modelos/sysml/ARQUITECTURA.md`](../../modelos/sysml/ARQUITECTURA.md) |
| Informe de Arquitectura | sección «Semana 3» de `INFORME.md` | [`../../modelos/sysml/INFORME.md`](../../modelos/sysml/INFORME.md) |
| Baseline | tag de git `baseline-v1.0` | historial del repositorio |

## Cómo entregar

1. Partir de `sistema.yaml` tal como quedó en la Semana 2.
2. Caracterizar cada interfaz (`que_transporta`, `tipo_unidades`, `requisito`) y añadir las conexiones del IBD (`{origen, destino, interfaz}`) — ver el reparto por rol en la sección «Semana 3» de `INFORME.md`.
3. Regenerar la vista:
   ```bash
   python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md
   ```
   Revisar el IBD y que ninguna interfaz se quede sin requisito.
4. Rellenar la sección «Semana 3» de `INFORME.md`.
5. Cerrar la semana con un tag de git:
   ```bash
   git tag -a baseline-v1.0 -m "Arquitectura v1.0 — BDD+IBD nivel 1"
   git push origin baseline-v1.0
   ```
6. 1 Pull Request a `master` con 1 commit por rol: `feat([rol]): interfaces del IBD nivel 1 — semana 3`.

Ver las instrucciones completas de rama/commit en la [página del curso, sección Repositorio](../../index.html#repositorio).
