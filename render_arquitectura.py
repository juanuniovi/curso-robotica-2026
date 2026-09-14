#!/usr/bin/env python3
"""Genera el BDD y el IBD (diagramas Mermaid) + tablas de propiedades e interfaces
a partir de un modelo de arquitectura en YAML.

El YAML es la fuente de verdad. El .md generado es una vista — no se edita a mano.

Uso:
    python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md
"""
import sys
import yaml


def cargar(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def bdd_mermaid(data):
    raiz = data["sistema"]["id"]
    lines = ["graph TD", f'    {raiz}["{raiz}"]']
    for b in data["bloques"]:
        lines.append(f'    {b["padre"]} --> {b["id"]}["{b["id"]}"]')
    return "\n".join(lines)


def ibd_mermaid(data):
    conexiones = data.get("conexiones") or []
    if not conexiones:
        return "graph LR\n    SinConexiones[\"(sin conexiones todavía)\"]"
    lines = ["graph LR"]
    for c in conexiones:
        lines.append(f'    {c["origen"]} -->|{c["interfaz"]}| {c["destino"]}')
    return "\n".join(lines)


def tabla_propiedades(data):
    rows = ["| Bloque | Propiedad | Tipo | Valor | Unidad | Requisito |",
            "|---|---|---|---|---|---|"]
    alguna = False
    for b in data["bloques"]:
        for p in b.get("propiedades") or []:
            alguna = True
            rows.append(f'| {b["id"]} | {p["nombre"]} | {p["tipo"]} | {p["valor"]} | {p["unidad"]} | {p["requisito"]} |')
    return "\n".join(rows) if alguna else "*Sin propiedades todavía.*"


def tabla_interfaces(data):
    rows = ["| Interfaz | Qué transporta | Tipo / unidades | Requisito |",
            "|---|---|---|---|"]
    alguna = False
    for i in data.get("interfaces") or []:
        if i.get("que_transporta") or i.get("tipo_unidades") or i.get("requisito"):
            alguna = True
        rows.append(f'| {i["id"]} | {i.get("que_transporta") or "—"} | {i.get("tipo_unidades") or "—"} | {i.get("requisito") or "—"} |')
    return "\n".join(rows) if alguna else "\n".join(rows) + "\n\n*Interfaces declaradas, pendientes de caracterizar.*"


def validar(data):
    """Comprobaciones que una herramienta gráfica no te da gratis."""
    errores = []
    ids_bloques = {b["id"] for b in data["bloques"]} | {data["sistema"]["id"]}

    for b in data["bloques"]:
        if b["padre"] not in ids_bloques:
            errores.append(f'{b["id"]}: padre "{b["padre"]}" no existe')
        for p in b.get("propiedades") or []:
            if not p.get("requisito"):
                errores.append(f'{b["id"]}.{p["nombre"]}: sin requisito que la justifique')

    ids_interfaces = {i["id"] for i in data.get("interfaces") or []}
    for c in data.get("conexiones") or []:
        if c["origen"] not in ids_bloques:
            errores.append(f'conexión {c["origen"]}->{c["destino"]}: origen desconocido')
        if c["destino"] not in ids_bloques:
            errores.append(f'conexión {c["origen"]}->{c["destino"]}: destino desconocido')
        if c["interfaz"] not in ids_interfaces:
            errores.append(f'conexión {c["origen"]}->{c["destino"]}: interfaz "{c["interfaz"]}" no declarada')

    return errores


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    src = args[0] if args else "sistema.yaml"
    out = "ARQUITECTURA.md"
    if "-o" in sys.argv:
        out = sys.argv[sys.argv.index("-o") + 1]

    data = cargar(src)

    errores = validar(data)
    if errores:
        print(f"⚠ {len(errores)} problema(s) de trazabilidad:")
        for e in errores:
            print(f"  - {e}")
    else:
        print("✓ Sin problemas de trazabilidad estructural (padres e interfaces existen)")

    md = f"""# Arquitectura — {data["sistema"]["id"]}

{data["sistema"]["descripcion"]}

*Generado automáticamente desde `{src}` — no editar a mano, editar el YAML y regenerar con
`python3 render_arquitectura.py {src} -o {out}`.*

## BDD — bloques

```mermaid
{bdd_mermaid(data)}
```

### Propiedades

{tabla_propiedades(data)}

## IBD — conexiones

```mermaid
{ibd_mermaid(data)}
```

### Interfaces

{tabla_interfaces(data)}
"""
    with open(out, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✓ {out} generado")


if __name__ == "__main__":
    main()
