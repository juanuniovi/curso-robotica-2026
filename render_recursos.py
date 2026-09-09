#!/usr/bin/env python3
"""Convierte los .md de recursos/ en .html con el estilo del sitio.

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
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Robótica-MBSE</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=DM+Mono:wght@300;400&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--ink:#0d1117;--ink-soft:#3d4451;--ink-muted:#6e7787;--paper:#f6f4ef;--paper-warm:#ede9e0;
  --accent:#1a4f8a;--border:rgba(13,17,23,.12);
  --fd:'Syne',sans-serif;--fb:'DM Sans',sans-serif;--fm:'DM Mono',monospace}}
body{{font-family:var(--fb);background:var(--paper);color:var(--ink);line-height:1.65;font-size:16px}}
.topbar{{position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between;
  padding:0 2rem;height:52px;background:var(--ink);border-bottom:2px solid var(--accent)}}
.topbar a{{font-family:var(--fm);font-size:.72rem;color:rgba(246,244,239,.65);text-decoration:none;letter-spacing:.05em}}
.topbar a:hover{{color:#fff}}
.topbar .logo{{font-family:var(--fd);font-weight:700;font-size:1rem;color:var(--paper);letter-spacing:.08em}}
.topbar .logo span{{color:var(--accent)}}
.wrap{{max-width:860px;margin:0 auto;padding:2.5rem 2rem 5rem}}
h1{{font-family:var(--fd);font-weight:800;font-size:1.9rem;line-height:1.15;margin:2.2rem 0 1rem}}
h2{{font-family:var(--fd);font-weight:700;font-size:1.3rem;margin:2.4rem 0 .8rem;padding-top:1rem;border-top:1px solid var(--border)}}
h3{{font-family:var(--fd);font-weight:700;font-size:1.05rem;margin:1.6rem 0 .6rem}}
h4{{font-family:var(--fd);font-weight:600;font-size:.92rem;margin:1.2rem 0 .5rem;color:var(--ink-soft)}}
p{{margin:.7rem 0}}
ul,ol{{margin:.7rem 0 .7rem 1.4rem}}
li{{margin:.3rem 0}}
code{{font-family:var(--fm);font-size:.86em;background:var(--paper-warm);padding:.1em .35em;border-radius:4px}}
blockquote{{margin:1.2rem 0;padding:.9rem 1.1rem;background:#fff;border-left:4px solid var(--accent);
  border-radius:0 8px 8px 0;font-size:.92rem;color:var(--ink-soft)}}
blockquote p{{margin:.4rem 0}}
hr{{border:0;border-top:1px solid var(--border);margin:2.4rem 0}}
table{{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.86rem;display:block;overflow-x:auto}}
th,td{{border:1px solid var(--border);padding:.5rem .7rem;text-align:left;vertical-align:top}}
th{{background:var(--paper-warm);font-family:var(--fd);font-weight:700}}
tr:nth-child(even) td{{background:rgba(255,255,255,.5)}}
a{{color:var(--accent)}}
.meta{{font-family:var(--fm);font-size:.72rem;color:var(--ink-muted);letter-spacing:.04em;margin-top:.4rem}}
</style>
</head>
<body>
<nav class="topbar">
  <a class="logo" href="../index.html"><span>Robótica</span>-MBSE</a>
  <a href="../index.html#repositorio">← Volver al curso</a>
</nav>
<div class="wrap">
{body}
</div>
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
