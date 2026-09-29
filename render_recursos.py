#!/usr/bin/env python3
"""Convierte los .md de recursos/ en .html que usan la hoja de estilo común (estilo.css).

Uso:  python3 render_recursos.py            → renderiza todos los recursos/*.md
      python3 render_recursos.py a.md b.md  → renderiza solo los indicados

Requiere:  pip install markdown
"""
import os, sys, html
import markdown

BASE = os.path.dirname(os.path.abspath(__file__))
REC = os.path.join(BASE, "recursos")

SHELL = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../estilo.css">
</head>
<body>

<nav><a href="../index.html">Ingeniería Robótica con MBSE</a> › <a href="../index.html#recursos">Recursos</a></nav>

{body}

</body>
</html>
"""


def render(md_path):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"])
    body = md.convert(text)
    # título = primer # del documento, si lo hay
    title = "Recurso"
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    out_path = os.path.splitext(md_path)[0] + ".html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(SHELL.format(title=html.escape(title), body=body))
    print(f"✓ {os.path.relpath(out_path, BASE)}")


def main():
    args = sys.argv[1:]
    if args:
        paths = [a if os.path.isabs(a) else os.path.join(REC, os.path.basename(a)) for a in args]
    else:
        paths = [os.path.join(REC, f) for f in sorted(os.listdir(REC)) if f.endswith(".md")]
    for p in paths:
        render(p)


if __name__ == "__main__":
    main()
