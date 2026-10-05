# -*- coding: utf-8 -*-
"""
Generador del Excel Maestro de Requisitos y Clasificacion UGV
Archivo generado: docs/Clasificacion_Requisitos_UGV.xlsx
"""
import re
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

def parse_markdown(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    req_pattern = re.compile(r'\|\s*\*\*([A-Z0-9_\-]+)\*\*\s*\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|([^\|]*)\|')

    requirements = []
    in_req_table = False
    for line in lines:
        l = line.strip()
        if "## 1. Matriz General de Requisitos" in l:
            in_req_table = True
            continue
        elif "## 2. Catálogo Desglosado de Cargas de Pago" in l:
            in_req_table = False
            continue

        if in_req_table and l.startswith('|') and not l.startswith('| ID') and not l.startswith('| :'):
            m = req_pattern.match(l)
            if m:
                raw_id = m.group(1).strip()
                # Quitar guiones para formato tipo RGEN07, RLT103, etc.
                req_id = raw_id.replace('-', '')
                subsystem = m.group(2).strip()
                scope = m.group(3).strip()
                req_type = m.group(4).strip().replace('**', '')
                desc = m.group(5).strip().replace('<br>', '\n').replace('&nbsp;', ' ')
                solution = m.group(6).strip()

                # Título derivado del subsistema o tema
                title = subsystem

                requirements.append({
                    'id': req_id,
                    'raw_id': raw_id,
                    'subsystem': subsystem,
                    'scope': scope,
                    'type': req_type,
                    'title': title,
                    'desc': desc,
                    'solution': solution
                })

    return requirements

def create_excel(requirements, output_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Matriz Requisitos UGV"
    ws.views.sheetView[0].showGridLines = True

    # Paleta de colores corporativos técnicos
    C_HEADER_FILL_TECH = "0F2942"      # Azul marino profundo para datos técnicos
    C_HEADER_FILL_CLASS = "1A4870"     # Azul pizarra para clasificación manual
    C_HEADER_FILL_NOTES = "2C3E50"     # Pizarra oscuro para notas
    C_WHITE = "FFFFFF"
    C_ZEBRA = "F8FAFC"
    C_BORDER = "CBD5E1"
    C_TEXT = "0F172A"
    C_BLOCK_RGEN = "EBF3FA"
    C_BLOCK_RLT1 = "EDF7ED"
    C_BLOCK_RLT2 = "FFF7ED"
    C_BLOCK_OTHER = "F5F3FF"

    font_title = Font(name="Segoe UI", size=14, bold=True, color=C_WHITE)
    font_subtitle = Font(name="Segoe UI", size=9, italic=True, color="E2E8F0")
    font_header = Font(name="Segoe UI", size=10, bold=True, color=C_WHITE)
    font_id = Font(name="Segoe UI", size=10, bold=True, color="0A2540")
    font_data = Font(name="Segoe UI", size=9, bold=False, color=C_TEXT)
    font_bold_data = Font(name="Segoe UI", size=9, bold=True, color=C_TEXT)
    font_check = Font(name="Segoe UI", size=11, bold=True, color="004085")

    fill_tech_header = PatternFill(start_color=C_HEADER_FILL_TECH, end_color=C_HEADER_FILL_TECH, fill_type="solid")
    fill_class_header = PatternFill(start_color=C_HEADER_FILL_CLASS, end_color=C_HEADER_FILL_CLASS, fill_type="solid")
    fill_notes_header = PatternFill(start_color=C_HEADER_FILL_NOTES, end_color=C_HEADER_FILL_NOTES, fill_type="solid")
    fill_zebra = PatternFill(start_color=C_ZEBRA, end_color=C_ZEBRA, fill_type="solid")
    fill_white = PatternFill(start_color=C_WHITE, end_color=C_WHITE, fill_type="solid")
    fill_title_banner = PatternFill(start_color="0A192F", end_color="0A192F", fill_type="solid")

    thin_side = Side(border_style="thin", color=C_BORDER)
    border_cell = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
    thick_bottom = Border(left=thin_side, right=thin_side, top=thin_side, bottom=Side(border_style="medium", color="0F2942"))

    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
    align_desc = Alignment(horizontal="left", vertical="top", wrap_text=True)
    align_header = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # 1. Banner superior informativo
    ws.merge_cells("A1:M1")
    title_cell = ws["A1"]
    title_cell.value = "MATRIZ MAESTRA DE ESPECIFICACIÓN Y CLASIFICACIÓN DE REQUISITOS — SISTEMA UGV DUAL"
    title_cell.font = font_title
    title_cell.fill = fill_title_banner
    title_cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[1].height = 32

    ws.merge_cells("A2:M2")
    sub_cell = ws["A2"]
    sub_cell.value = "Pliego de Prescripciones Técnicas (CPP 01/2026 AB CDTI - MINISDEF) | 122 Requisitos Contractuales | Ordenación y filtrado habilitados"
    sub_cell.font = font_subtitle
    sub_cell.fill = fill_title_banner
    sub_cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[2].height = 18

    # Fila vacía separadora
    ws.row_dimensions[3].height = 8

    # 2. Fila de Encabezados (Fila 4)
    headers = [
        # (Col, Titulo, TipoCabecera)
        ("A", "Requisito", "tech"),
        ("B", "Bloque / Subsistema", "tech"),
        ("C", "Título / Concepto", "tech"),
        ("D", "Descripción / Contenido", "tech"),
        ("E", "Ámbito / Lote", "tech"),
        ("F", "Tipo", "tech"),
        ("G", "Funcional [X]", "class"),
        ("H", "Paramétrica [X]", "class"),
        ("I", "Problema [X]", "class"),
        ("J", "Solución [X]", "class"),
        ("K", "General [X]", "class"),
        ("L", "Imprescindible [X]", "class"),
        ("M", "Propuesta de Solución / Ideas", "notes"),
    ]

    ws.row_dimensions[4].height = 30

    for col_letter, title, h_type in headers:
        cell = ws[f"{col_letter}4"]
        cell.value = title
        cell.font = font_header
        cell.alignment = align_header
        cell.border = thick_bottom
        if h_type == "tech":
            cell.fill = fill_tech_header
        elif h_type == "class":
            cell.fill = fill_class_header
        else:
            cell.fill = fill_notes_header

    # Validación de datos para columnas de clasificación (G a L): ÚNICAMENTE permite 'X' mayúscula o vacío
    # Al hacer clic en la celda, aparece la flecha desplegable para marcar 'X' con un clic
    dv = DataValidation(type="list", formula1='"X"', allow_blank=True)
    dv.error = 'Solo se permite marcar con una "X" mayúscula o dejar la celda en blanco.'
    dv.errorTitle = 'Valor no válido (Solo X)'
    dv.prompt = 'Haga clic en la flecha desplegable para marcar "X"'
    dv.promptTitle = 'Selección rápida'
    dv.showDropDown = False # False en openpyxl significa que NO oculta la flecha (es decir, muestra el botón desplegable en celda)
    ws.add_data_validation(dv)
    dv.add("G5:L109")

    # 3. Llenado de filas de datos
    current_row = 5
    for idx, req in enumerate(requirements):
        r = current_row
        ws.row_dimensions[r].height = None # Auto height

        # Determinar sombreado
        is_zebra = (idx % 2 == 1)
        row_fill = fill_zebra if is_zebra else fill_white

        # Col A: Requisito (ej. RGEN07)
        c_req = ws[f"A{r}"]
        c_req.value = req['id']
        c_req.font = font_id
        c_req.alignment = align_center
        c_req.fill = row_fill
        c_req.border = border_cell

        # Col B: Bloque / Subsistema
        c_sub = ws[f"B{r}"]
        c_sub.value = req['subsystem']
        c_sub.font = font_bold_data
        c_sub.alignment = align_left
        c_sub.fill = row_fill
        c_sub.border = border_cell

        # Col C: Título
        c_tit = ws[f"C{r}"]
        c_tit.value = req['title']
        c_tit.font = font_data
        c_tit.alignment = align_left
        c_tit.fill = row_fill
        c_tit.border = border_cell

        # Col D: Descripción / Contenido
        c_desc = ws[f"D{r}"]
        c_desc.value = req['desc']
        c_desc.font = font_data
        c_desc.alignment = align_desc
        c_desc.fill = row_fill
        c_desc.border = border_cell

        # Col E: Ámbito / Lote
        c_scope = ws[f"E{r}"]
        c_scope.value = req['scope']
        c_scope.font = font_data
        c_scope.alignment = align_center
        c_scope.fill = row_fill
        c_scope.border = border_cell

        # Col F: Tipo
        c_type = ws[f"F{r}"]
        c_type.value = req['type']
        c_type.font = font_bold_data if "Obligatorio" in req['type'] else font_data
        c_type.alignment = align_center
        c_type.fill = row_fill
        c_type.border = border_cell

        # Cols G a L: Clasificación en blanco
        for col_l in ["G", "H", "I", "J", "K", "L"]:
            c_class = ws[f"{col_l}{r}"]
            c_class.value = None
            c_class.font = font_check
            c_class.alignment = align_center
            c_class.fill = row_fill
            c_class.border = border_cell

        # Col M: Propuesta de Solución
        c_sol = ws[f"M{r}"]
        c_sol.value = req['solution'] if req['solution'] else None
        c_sol.font = font_data
        c_sol.alignment = align_left
        c_sol.fill = row_fill
        c_sol.border = border_cell

        current_row += 1

    last_row = current_row - 1

    # 4. Habilitar AutoFilter en toda la tabla (A4:M{last_row})
    ws.auto_filter.ref = f"A4:M{last_row}"

    # 5. Congelar paneles en fila 5 y columna B (para ver siempre cabecera y Requisito A)
    ws.freeze_panes = "B5"

    # 6. Anchos óptimos de columna
    col_widths = {
        "A": 15,  # Requisito (ej. RGEN07)
        "B": 24,  # Bloque / Subsistema
        "C": 26,  # Título / Concepto
        "D": 65,  # Descripción / Contenido completo
        "E": 20,  # Ámbito / Lote
        "F": 16,  # Tipo (Obligatorio/Opcional)
        "G": 14,  # Funcional [X]
        "H": 15,  # Paramétrica [X]
        "I": 13,  # Problema [X]
        "J": 13,  # Solución [X]
        "K": 13,  # General [X]
        "L": 17,  # Imprescindible [X]
        "M": 35   # Propuesta / Ideas
    }

    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = width

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    wb.save(output_path)
    print(f"Excel guardado exitosamente en: {output_path} ({len(requirements)} requisitos)")

if __name__ == '__main__':
    md_file = os.path.join(os.path.dirname(__file__), 'Requisitos.md')
    out_file = os.path.join(os.path.dirname(__file__), 'Clasificacion_Requisitos_UGV.xlsx')
    reqs = parse_markdown(md_file)
    create_excel(reqs, out_file)
