# Informe de Arquitectura — Sistema UGV

*Ref. pliego: CPP 01/2026 AB — CDTI / Ministerio de Defensa de España*
*RDOC-13 — Vista de Sistemas y Subsistemas*

**Equipo:** ______________&nbsp;&nbsp;&nbsp; **Lote:** ☐ 1 (ruedas) ☐ 2 (cadenas)

Acompaña a [`sistema.yaml`](sistema.yaml) / [`ARQUITECTURA.md`](ARQUITECTURA.md): mientras esos dos son el modelo y su vista generada, este documento recoge las decisiones, observaciones y checklist de cada hito de la Fase 2 — Arquitectura. Una sección por hito.

## BDD

### Reparto de propiedades por rol

| Rol | Ámbito |
|---|---|
| IS | Propiedades de nivel sistema: masa, autonomía, modos |
| Simulación | Propulsión y movilidad: potencia, par, velocidad, pendiente |
| Taller | Chasis e interfaces: dimensiones, pesos, puntos de interfaz (RGEN-28) |
| Software | Comunicaciones y control: alcance BLOS (RCOM-02), latencia, software (RSW) |

### Observaciones

- Bloques con menos de 2 propiedades tipadas:

- Propiedades sin requisito que las justifique (pendientes de completar o descartar):

- Discrepancias detectadas entre el modelo base y el Anexo I:

### Checklist de cierre

| # | Verificación | OK |
|---|---|---|
| 1 | `sistema.yaml` tiene los 5 bloques de nivel 1 con los nombres exactos | ☐ |
| 2 | El bloque `UGV` tiene los 5 bloques internos con los nombres exactos | ☐ |
| 3 | Cada propiedad tiene tipo, valor, unidad y un `requisito` | ☐ |
| 4 | `python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md` corre sin problemas de trazabilidad | ☐ |
| 5 | `ARQUITECTURA.md` regenerado y comprobado en GitHub (el diagrama se ve bien) | ☐ |

## IBD

*(se rellena al trabajar el IBD)*
