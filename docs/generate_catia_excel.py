# -*- coding: utf-8 -*-
"""
Generador del Ecosistema de Archivos Excel para CATIA / 3DEXPERIENCE (Dassault Systèmes)
basado en Requisitos.md

Genera:
1. docs/Requisitos_Sistema_UGV_3DEXPERIENCE.xlsx (Libro maestro de requisitos MBSE / TRM / Cameo / CAD)
2. docs/CATIA_Design_Table_UGV.xlsx (Archivo directo monoplantilla para Tabla de Diseño de CATIA V5 / 3DEXPERIENCE)
"""
import re
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Estilos Corporativos inspirados en Dassault Systèmes
DS_BLUE_DARK = "003D66"     # Azul corporativo oscuro
DS_BLUE_PRIMARY = "005689"  # Azul primario 3DS
DS_BLUE_ACCENT = "007AA6"   # Azul acento
DS_BLUE_LIGHT = "E6F0F6"    # Fondo azul muy suave
DS_GRAY_HEADER = "4A5568"   # Gris encabezado alternativo
DS_GRAY_LIGHT = "F8FAFC"    # Fila alterna
DS_WHITE = "FFFFFF"
BORDER_GRAY = "D1D5DB"

font_title = Font(name="Segoe UI", size=14, bold=True, color=DS_WHITE)
font_subtitle = Font(name="Segoe UI", size=11, bold=True, color="1E293B")
font_header = Font(name="Segoe UI", size=10, bold=True, color=DS_WHITE)
font_data = Font(name="Segoe UI", size=9, bold=False, color="1E293B")
font_bold_data = Font(name="Segoe UI", size=9, bold=True, color="0F172A")
font_small = Font(name="Segoe UI", size=8, italic=True, color="64748B")

fill_primary_header = PatternFill(start_color=DS_BLUE_PRIMARY, end_color=DS_BLUE_PRIMARY, fill_type="solid")
fill_dark_header = PatternFill(start_color=DS_BLUE_DARK, end_color=DS_BLUE_DARK, fill_type="solid")
fill_accent_header = PatternFill(start_color=DS_BLUE_ACCENT, end_color=DS_BLUE_ACCENT, fill_type="solid")
fill_zebra = PatternFill(start_color=DS_GRAY_LIGHT, end_color=DS_GRAY_LIGHT, fill_type="solid")
fill_highlight = PatternFill(start_color=DS_BLUE_LIGHT, end_color=DS_BLUE_LIGHT, fill_type="solid")

thin_border_side = Side(border_style="thin", color=BORDER_GRAY)
border_cell = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
border_bottom_double = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=Side(border_style="double", color=DS_BLUE_DARK))

align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
align_right = Alignment(horizontal="right", vertical="center", wrap_text=True)
align_header = Alignment(horizontal="center", vertical="center", wrap_text=True)


def parse_markdown(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    req_pattern = re.compile(r'\|\s*\*\*([A-Z0-9_\-]+)\*\*\s*\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|([^\|]*)\|')
    cp_pattern = re.compile(r'\|\s*\*\*([A-Z0-9_\-]+)\*\*\s*\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|([^\|]*)\|')
    e_pattern = re.compile(r'\|\s*\*\*([A-Z0-9_\-]+)\*\*\s*\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|\s*([^\|]+)\|([^\|]*)\|')

    requirements = []
    payloads = []
    deliverables = []

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
                req_id = m.group(1).strip()
                subsystem = m.group(2).strip()
                scope = m.group(3).strip()
                req_type = m.group(4).strip()
                desc = m.group(5).strip().replace('<br>', '\n').replace('&nbsp;', ' ')
                solution = m.group(6).strip()

                # Classification SysML Stereotype
                category = "Functional"
                if "RGEN" in req_id:
                    category = "GeneralRequirement"
                elif "RLT1" in req_id or "RLT2" in req_id:
                    category = "PerformanceRequirement" if any(w in desc.lower() for w in ["velocidad", "potencia", "masa", "peso", "capacidad", "vadeo", "pendiente"]) else "DesignConstraint"
                elif "ROPE" in req_id:
                    category = "OperationalRequirement"
                elif "RPdO" in req_id:
                    category = "InterfaceRequirement"
                elif "RNAV" in req_id:
                    category = "FunctionalRequirement"
                elif "RCOM" in req_id:
                    category = "InterfaceRequirement"
                elif "RSW" in req_id:
                    category = "SoftwareRequirement"
                elif "RPVyA" in req_id:
                    category = "VerificationRequirement"
                elif "RDOC" in req_id:
                    category = "DocumentationRequirement"

                # Verification Method
                d_low = desc.lower()
                if any(w in d_low for w in ["ensayo", "prueba", "velocidad", "potencia", "vadeo", "pendiente", "escalón", "autonomía", "tracción", "frenado", "recarga"]):
                    v_method = "Test"
                elif any(w in d_low for w in ["demostración", "modo", "operar", "conmutación", "teleoperado", "autónomo", "follow-me", "shuttle"]):
                    v_method = "Demonstration"
                elif any(w in d_low for w in ["masa", "peso", "dimensiones", "resistencia", "cálculo", "fops", "factores de carga", "stanag"]):
                    v_method = "Analysis"
                elif any(w in d_low for w in ["adhesivo", "rotulación", "escudo", "gancho", "conector", "formato", "plan", "documento", "código", "inventario"]):
                    v_method = "Inspection"
                else:
                    v_method = "Test"

                parent_map = {
                    "RGEN": "PKG_01_Requisitos_Generales",
                    "RLT1": "PKG_02_Lote_1_Ruedas",
                    "RLT2": "PKG_03_Lote_2_Cadenas",
                    "ROPE": "PKG_04_Operativos",
                    "RPdO": "PKG_05_Puesto_Operacion",
                    "RNAV": "PKG_06_Navegacion",
                    "RCOM": "PKG_07_Comunicaciones",
                    "RSW":  "PKG_08_Software",
                    "RPVyA":"PKG_09_Pruebas_Validacion",
                    "RDOC": "PKG_10_Documentales"
                }
                prefix = req_id.split('-')[0]
                parent_pkg = parent_map.get(prefix, "PKG_Sistema_UGV")
                priority = "Obligatorio" if "Obligatorio" in req_type else "Opcional"

                requirements.append({
                    "id": req_id,
                    "name": subsystem,
                    "text": desc,
                    "category": category,
                    "subsystem": subsystem,
                    "scope": scope,
                    "type": req_type,
                    "priority": priority,
                    "v_method": v_method,
                    "parent_pkg": parent_pkg,
                    "solution": solution,
                    "status": "Aprobado"
                })

        # CP Table
        if l.startswith('| **CP-'):
            m = cp_pattern.match(l)
            if m:
                payloads.append({
                    "id": m.group(1).strip(),
                    "name": m.group(2).strip(),
                    "lote": m.group(3).strip(),
                    "interface": m.group(4).strip(),
                    "caracter": m.group(5).strip(),
                    "specs": m.group(6).strip().replace('<br>', '\n').replace('&nbsp;', ' '),
                    "solution": m.group(7).strip()
                })

        # Deliverables Table
        if l.startswith('| **E'):
            m = e_pattern.match(l)
            if m:
                deliverables.append({
                    "id": m.group(1).strip(),
                    "name": m.group(2).strip(),
                    "hitos": m.group(3).strip(),
                    "reqs": m.group(4).strip(),
                    "desc": m.group(5).strip().replace('<br>', '\n').replace('&nbsp;', ' '),
                    "solution": m.group(6).strip()
                })

    # Criterios y baremo
    eval_items = []
    # ILT1
    ilt_pattern = re.compile(r'\|\s*\*\*([A-Z0-9_\-]+)\*\*\s*\|\s*([^\|]+)\|\s*([^\|]+)\|([^\|]*)\|')
    for line in lines:
        l = line.strip()
        if l.startswith('| **ILT1-') or l.startswith('| **OG-') or l.startswith('| **CdP-'):
            m = ilt_pattern.match(l)
            if m:
                eval_items.append({
                    "code": m.group(1).strip(),
                    "desc": m.group(2).strip(),
                    "points": m.group(3).strip(),
                    "solution": m.group(4).strip()
                })

    return requirements, payloads, deliverables, eval_items


def build_guide_sheet(ws):
    ws.views.sheetView[0].showGridLines = True
    ws.column_dimensions['A'].width = 6
    ws.column_dimensions['B'].width = 28
    ws.column_dimensions['C'].width = 45
    ws.column_dimensions['D'].width = 45

    # Title Banner
    ws.merge_cells("B2:D2")
    ws["B2"] = "GUÍA DE IMPORTACIÓN Y FORMATOS EN CATIA / 3DEXPERIENCE (DASSAULT SYSTÈMES)"
    ws["B2"].font = font_title
    ws["B2"].fill = fill_dark_header
    ws["B2"].alignment = align_center
    ws.row_dimensions[2].height = 40

    ws.merge_cells("B3:D3")
    ws["B3"] = "Proyecto UGV Dual (Anexo I CPP 01/2026 AB) — Ingeniería de Sistemas y CAD Paramétrico"
    ws["B3"].font = font_subtitle
    ws["B3"].fill = fill_highlight
    ws["B3"].alignment = align_center
    ws.row_dimensions[3].height = 25

    sections = [
        (
            "1. Tablas de Diseño en CATIA V5 / 3DEXPERIENCE (Design Table)",
            "¿Cómo ha de ser el archivo?",
            "• Formato: Archivo .xlsx, .xls o .csv plano.\n"
            "• Fila 1 (Cabecera): Debe contener nombres unívocos de parámetros. Si tienen unidad física, se añade con barra invertida: Parámetro\\Unidad (ej. Tara_Min\\kg, Vel_Max\\km_h, Potencia\\kW).\n"
            "• Filas de datos (2 en adelante): Cada fila representa una variante/configuración del UGV (ej. Lote 1 - Ruedas, Lote 2 - Cadenas).\n"
            "• Restricción crítica: No deben existir celdas combinadas ni fórmulas complejas en el rango de parámetros para evitar fallos en el motor OLE/COM de CATIA.",
            "Procedimiento de Importación en CATIA:\n"
            "1. Abrir la pieza (.CATPart) o conjunto (.CATProduct) en CATIA.\n"
            "2. Ir al banco de trabajo 'Part Design' o 'Knowledge Advisor'.\n"
            "3. Pulsar el icono 'Design Table' (o Menú: Insert > Knowledge > Design Table).\n"
            "4. Marcar 'Create a design table from a pre-existing file'.\n"
            "5. Seleccionar la hoja 'CATIA_Design_Table' de este libro o el archivo independiente 'CATIA_Design_Table_UGV.xlsx'.\n"
            "6. Asociar los parámetros del modelo CAD con las columnas de la tabla (Associations)."
        ),
        (
            "2. 3DEXPERIENCE: Traceable Requirements Management (TRM) & Requirement Capture",
            "¿Cómo ha de ser el archivo?",
            "• Hoja objetivo: 'SysML_Requirements'.\n"
            "• Columnas normalizadas:\n"
            "  - Requirement ID: Código único (RGEN-01, RLT1-01...).\n"
            "  - Title / Name: Subsistema o título formal.\n"
            "  - Requirement Text: Especificación completa y parámetros cuantitativos.\n"
            "  - Requirement Type / Category: Functional, Performance, Interface, etc.\n"
            "  - Priority: Obligatorio (High) / Opcional (Medium).\n"
            "  - Verification Method: Test, Inspection, Analysis, Demonstration.\n"
            "  - Parent ID / Package: Jerarquía del árbol de requisitos.",
            "Procedimiento de Importación en 3DEXPERIENCE:\n"
            "1. Entrar en la app 'Requirement Capture' o 'Traceable Requirements Management' (Rol Systems Engineer / Product Manager).\n"
            "2. Crear o abrir la Especificación de Requisitos del Sistema UGV.\n"
            "3. En la barra de herramientas, seleccionar 'Import from Excel'.\n"
            "4. Subir este archivo y seleccionar la pestaña 'SysML_Requirements'.\n"
            "5. En el asistente de mapeo, confirmar la correspondencia de columnas (ID -> Requirement ID, Title -> Title, Text -> Content, etc.).\n"
            "6. Ejecutar la importación para generar la estructura arbórea completa de requisitos."
        ),
        (
            "3. CATIA Magic / Cameo Systems Modeler (Modelado SysML)",
            "¿Cómo ha de ser el archivo?",
            "• Utiliza las columnas: id, name, text, owner, category, verificationMethod.\n"
            "• Compatible con el estándar OMG SysML v1.x / v2 y el plugin de importación de Excel de No Magic / Dassault Systèmes.\n"
            "• Permite generar automáticamente diagramas de requisitos (SysML Requirement Diagrams) y matrices de trazabilidad (Requirement Matrix).",
            "Procedimiento de Importación en Cameo / CATIA Magic:\n"
            "1. En el proyecto SysML, ir a Menú: File > Import From > Excel/CSV File > Import Using New Map.\n"
            "2. Seleccionar este archivo y la pestaña 'SysML_Requirements'.\n"
            "3. Indicar el Paquete de destino (Scope: UGV_Requirements).\n"
            "4. Asignar el tipo de elemento como 'SysML Requirement'.\n"
            "5. Mapear 'id' a Id, 'name' a Name, 'text' a Text, y 'owner' a Owner.\n"
            "6. Guardar el mapa de importación y finalizar."
        ),
        (
            "4. Dassault Systèmes Reqtify (Matriz de Cobertura y Trazabilidad)",
            "¿Cómo ha de ser el archivo?",
            "• Reqtify extrae requisitos de Excel mediante filtros de columnas definidos en el archivo de tipos (.reqtify).\n"
            "• La hoja 'Matriz_Verificacion' proporciona la asignación 1:1 entre requisitos del pliego, métodos de verificación formal (INCOSE/Sols) y fases contractuales (Fase II en fábrica / Fase III en campo con ET y UME).",
            "Procedimiento en Reqtify:\n"
            "1. Añadir este documento Excel como 'Document Type: MS Excel Spreadsheet'.\n"
            "2. Asignar la expresión regular o puntero de columna para ID y Text.\n"
            "3. Vincular los requisitos con los entregables E04 (Plan de Pruebas) y E05 (Protocolo de Pruebas) para análisis automático de cobertura."
        )
    ]

    current_row = 5
    for title, col_b, col_c, col_d in sections:
        ws.merge_cells(start_row=current_row, start_column=2, end_row=current_row, end_column=4)
        ws.cell(row=current_row, column=2, value=title).font = font_subtitle
        ws.cell(row=current_row, column=2).fill = fill_highlight
        ws.row_dimensions[current_row].height = 24
        current_row += 1

        headers = ["Aspecto Técnico", "¿Cómo ha de ser el archivo según Dassault Systèmes?", "Procedimiento Paso a Paso de Importación"]
        for c_idx, h in enumerate(headers, start=2):
            cell = ws.cell(row=current_row, column=c_idx, value=h)
            cell.font = font_header
            cell.fill = fill_primary_header
            cell.alignment = align_header
            cell.border = border_cell
        ws.row_dimensions[current_row].height = 24
        current_row += 1

        row_vals = [col_b, col_c, col_d]
        for c_idx, val in enumerate(row_vals, start=2):
            cell = ws.cell(row=current_row, column=c_idx, value=val)
            cell.font = font_data
            cell.alignment = align_left
            cell.border = border_cell
        ws.row_dimensions[current_row].height = 130
        current_row += 2


def build_sysml_requirements_sheet(ws, reqs):
    ws.views.sheetView[0].showGridLines = True

    headers = [
        ("id", "Identificador SysML / TRM ID", 14),
        ("name", "Nombre / Subsistema (SysML Name)", 26),
        ("text", "Texto del Requisito (SysML Text / Description)", 65),
        ("category", "Estereotipo SysML (Category)", 22),
        ("subsystem", "Subsistema Asignado", 22),
        ("scope", "Ámbito / Lote Aplicable", 18),
        ("type", "Carácter Contractual", 18),
        ("priority", "Prioridad (Priority)", 14),
        ("verificationMethod", "Método Verificación (INCOSE)", 18),
        ("owner", "Paquete Contenedor (SysML Owner)", 26),
        ("status", "Estado de Configuración", 14),
        ("solution_ideas", "Propuesta de Solución / Ideas del Equipo", 30)
    ]

    ws.row_dimensions[1].height = 28
    for col_idx, (col_key, col_label, col_width) in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=col_key)
        cell.font = font_header
        cell.fill = fill_dark_header
        cell.alignment = align_center
        cell.border = border_cell

        # Subheader with human-friendly label
        cell_sub = ws.cell(row=2, column=col_idx, value=col_label)
        cell_sub.font = Font(name="Segoe UI", size=8, italic=True, color=DS_WHITE)
        cell_sub.fill = fill_primary_header
        cell_sub.alignment = align_center
        cell_sub.border = border_cell

        ws.column_dimensions[get_column_letter(col_idx)].width = col_width

    ws.row_dimensions[2].height = 20

    row_num = 3
    for r in reqs:
        row_data = [
            r["id"],
            r["name"],
            r["text"],
            r["category"],
            r["subsystem"],
            r["scope"],
            r["type"],
            r["priority"],
            r["v_method"],
            r["parent_pkg"],
            r["status"],
            r["solution"]
        ]
        is_even = (row_num % 2 == 0)
        ws.row_dimensions[row_num].height = 55 if len(r["text"]) > 100 else 30

        for col_idx, val in enumerate(row_data, start=1):
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_bold_data if col_idx == 1 else font_data
            cell.border = border_cell
            if is_even:
                cell.fill = fill_zebra

            if col_idx in [1, 4, 6, 7, 8, 9, 10, 11]:
                cell.alignment = align_center
            else:
                cell.alignment = align_left

        row_num += 1

    # Freeze panes below headers
    ws.freeze_panes = "A3"
    # Auto-filter
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{row_num-1}"


def build_catia_design_table_sheet(ws, is_standalone=False):
    r"""
    Construye la hoja con el formato oficial de CATIA Design Table (Knowledge Advisor).
    Fila 1: Parámetro\Unidad
    Filas 2+: Valores concretos para cada configuración.
    """
    ws.views.sheetView[0].showGridLines = True

    # Parámetros cuantitativos derivados estrictamente del Anexo I / Requisitos.md
    # Formato exacto de CATIA: Name\Unit
    columns = [
        ("PartNumber", "Identificador de Variante / Configuración", 28),
        ("Lote_Tipo", "Tipo de Plataforma", 18),
        ("Traccion_Config", "Configuración Cinemática", 18),
        ("Tara_Min\\kg", "Masa en Vacío Mínima [kg] (RLT1-06 / RLT2-04)", 16),
        ("Tara_Max\\kg", "Masa en Vacío Máxima [kg] (RLT1-06 / RLT2-04)", 16),
        ("Payload_Min\\kg", "Capacidad Carga Útil Mínima [kg] (RLT1-07 / RLT2-05)", 18),
        ("GVW_Max\\kg", "Peso Máximo de Misión [kg] (RLT1-08 / RLT2-06)", 16),
        ("Vel_Carretera_Min\\km_h", "Velocidad Máx Carretera [km/h] (RLT1-03 / RLT2-02)", 20),
        ("Vel_Offroad_Min\\km_h", "Velocidad Máx Campo a Través [km/h] (RLT1-03 / RLT2-02)", 20),
        ("Pendiente_Frontal_Max\\%", "Pendiente Frontal Máx [%] (RLT1-03 / RLT2-02)", 18),
        ("Pendiente_Lateral_Max\\%", "Pendiente Lateral Máx [%] (RLT1-03 / RLT2-02)", 18),
        ("Escalon_Vertical_Min\\mm", "Escalón Vertical Superable [mm] (RLT1-03 / RLT2-02)", 20),
        ("Vadeo_Profundidad_Min\\mm", "Capacidad Vadeo sin Preparación [mm] (RLT1-10 / RLT2-08)", 22),
        ("Potencia_Propulsion_Min\\kW", "Potencia Continua de Propulsión [kW] (RLT1-09 / RLT2-07)", 22),
        ("Capacidad_Remolque_Min\\kg", "Capacidad de Arrastre Remolque [kg] (RGEN-10 / RLT1-14)", 22),
        ("Autonomia_Global_Tiempo\\h", "Autonomía Continua Global [h] (RGEN-14)", 22),
        ("Autonomia_Global_Distancia\\km", "Autonomía Desplazamiento Global [km] (RGEN-14)", 24),
        ("Autonomia_Electrica_Tiempo\\h", "Autonomía Modo 100% Eléctrico [h] (RGEN-15)", 22),
        ("Autonomia_Electrica_Distancia\\km", "Autonomía Eléctrica Desplazamiento [km] (RGEN-15)", 24),
        ("Vel_Remolcado_Pasivo_Max\\km_h", "Velocidad Máx Remolcado Pasivo [km/h] (RGEN-16)", 24),
        ("Ancho_Transporte_Max\\mm", "Anchura Máx Transporte con Cargas [mm] (RLT2-09)", 22),
        ("Potencia_Exportable_Min\\kW", "Potencia Eléctrica Exportable [kW] (RGEN-19)", 22),
        ("Alcance_Comms_BLOS_Min\\km", "Alcance Enlace Comunicaciones BLOS [km] (RCOM-02)", 22),
        ("Navegacion_GNSS_Denegado_Min\\km", "Alcance Navegación sin GNSS [km] (RNAV-01)", 24),
        ("Presion_Rueda_Min\\bar", "Presión de Inflado Nominal [bar]", 18)
    ]

    # CATIA Design Table exige que la fila 1 sea el nombre del parámetro (o nombre\unidad)
    ws.row_dimensions[1].height = 32
    for col_idx, (p_name, p_desc, p_w) in enumerate(columns, start=1):
        cell = ws.cell(row=1, column=col_idx, value=p_name)
        cell.font = font_header
        cell.fill = fill_dark_header
        cell.alignment = align_center
        cell.border = border_cell
        ws.column_dimensions[get_column_letter(col_idx)].width = p_w

    # Filas de configuración
    # Fila 2: Configuración Lote 1 (Ruedas)
    row_lote1 = [
        "UGV_Lote_1_Ruedas",
        "Lote 1 (Ruedas)",
        "8x8 Direct Drive",
        3500,   # Tara_Min
        7000,   # Tara_Max
        2000,   # Payload_Min
        9000,   # GVW_Max
        75,     # Vel Carretera
        50,     # Vel Offroad
        60,     # Pendiente frontal %
        30,     # Pendiente lateral %
        300,    # Escalon vertical mm (30 cm)
        750,    # Vadeo mm (0.75 m)
        140,    # Potencia continua kW
        3000,   # Remolque kg
        8,      # Autonomia h
        400,    # Autonomia km
        2,      # Autonomia elec h
        100,    # Autonomia elec km
        65,     # Vel remolcado pasivo
        2450,   # Ancho transporte estimado ruedas
        120,    # Potencia exportable kW (Opcional OG-03)
        20,     # Comms BLOS km
        5,      # GNSS denegado km
        3.2     # Presión ruedas bar
    ]

    # Fila 3: Configuración Lote 2 (Cadenas)
    row_lote2 = [
        "UGV_Lote_2_Cadenas",
        "Lote 2 (Cadenas)",
        "Orugas Metálicas",
        9000,   # Tara_Min
        12000,  # Tara_Max
        4000,   # Payload_Min
        17000,  # GVW_Max
        50,     # Vel Carretera
        40,     # Vel Offroad
        60,     # Pendiente frontal %
        30,     # Pendiente lateral %
        400,    # Escalon vertical mm (40 cm)
        1200,   # Vadeo mm (1.2 m)
        200,    # Potencia continua kW
        3000,   # Remolque kg
        8,      # Autonomia h
        400,    # Autonomia km
        2,      # Autonomia elec h
        100,    # Autonomia elec km
        65,     # Vel remolcado pasivo
        3000,   # Ancho transporte mm (RLT2-09 con hoja y ripper)
        120,    # Potencia exportable kW
        20,     # Comms BLOS km
        5,      # GNSS denegado km
        0.0     # Orugas (sin presión neumáticos)
    ]

    # Fila 4: Configuración Lote 1 - Modo Sigiloso Eléctrico (Variante operacional)
    row_lote1_silent = [
        "UGV_Lote_1_Sigiloso",
        "Lote 1 (Ruedas)",
        "8x8 Eléctrico Puro",
        3500,
        7000,
        2000,
        9000,
        45,     # Limitado en modo puramente eléctrico
        30,
        60,
        30,
        300,
        750,
        90,     # Potencia entregada por batería
        3000,
        2,      # 2 horas en modo eléctrico
        100,    # 100 km
        2,
        100,
        65,
        2450,
        0,
        20,
        5,
        3.2
    ]

    rows = [row_lote1, row_lote2, row_lote1_silent]
    for r_idx, r_data in enumerate(rows, start=2):
        ws.row_dimensions[r_idx].height = 24
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = font_bold_data if c_idx == 1 else font_data
            cell.border = border_cell
            if r_idx % 2 == 1:
                cell.fill = fill_zebra
            if isinstance(val, (int, float)):
                cell.alignment = align_right
                cell.number_format = "#,##0" if isinstance(val, int) else "0.0"
            else:
                cell.alignment = align_center if c_idx > 1 else align_left

    ws.freeze_panes = "B2"


def build_payloads_sheet(ws, payloads):
    ws.views.sheetView[0].showGridLines = True

    headers = [
        ("Código", 12),
        ("Carga de Pago / Implemento", 28),
        ("Lote Aplicable", 18),
        ("Punto de Interfaz / Ubicación", 24),
        ("Carácter Contractual", 18),
        ("Especificaciones Técnicas Clave", 55),
        ("Propuesta / Dimensiones para CAD", 30)
    ]

    ws.row_dimensions[1].height = 28
    for col_idx, (h_title, col_w) in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=h_title)
        cell.font = font_header
        cell.fill = fill_dark_header
        cell.alignment = align_center
        cell.border = border_cell
        ws.column_dimensions[get_column_letter(col_idx)].width = col_w

    row_num = 2
    for cp in payloads:
        row_data = [
            cp["id"],
            cp["name"],
            cp["lote"],
            cp["interface"],
            cp["caracter"],
            cp["specs"],
            cp["solution"]
        ]
        ws.row_dimensions[row_num].height = 45 if len(cp["specs"]) > 80 else 26
        is_even = (row_num % 2 == 0)

        for col_idx, val in enumerate(row_data, start=1):
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_bold_data if col_idx == 1 else font_data
            cell.border = border_cell
            if is_even:
                cell.fill = fill_zebra

            if col_idx in [1, 3, 4, 5]:
                cell.alignment = align_center
            else:
                cell.alignment = align_left

        row_num += 1

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{row_num-1}"


def build_deliverables_sheet(ws, deliverables):
    ws.views.sheetView[0].showGridLines = True

    headers = [
        ("Código", 12),
        ("Nombre del Entregable", 32),
        ("Hitos Contractuales de Entrega", 28),
        ("Requisitos Vinculados", 22),
        ("Descripción del Contenido", 55),
        ("Propuesta / Formato CAD o SW", 30)
    ]

    ws.row_dimensions[1].height = 28
    for col_idx, (h_title, col_w) in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=h_title)
        cell.font = font_header
        cell.fill = fill_dark_header
        cell.alignment = align_center
        cell.border = border_cell
        ws.column_dimensions[get_column_letter(col_idx)].width = col_w

    row_num = 2
    for e in deliverables:
        row_data = [
            e["id"],
            e["name"],
            e["hitos"],
            e["reqs"],
            e["desc"],
            e["solution"]
        ]
        ws.row_dimensions[row_num].height = 40 if len(e["desc"]) > 80 else 26
        is_even = (row_num % 2 == 0)

        for col_idx, val in enumerate(row_data, start=1):
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_bold_data if col_idx == 1 else font_data
            cell.border = border_cell
            if is_even:
                cell.fill = fill_zebra

            if col_idx in [1, 3, 4]:
                cell.alignment = align_center
            else:
                cell.alignment = align_left

        row_num += 1

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{row_num-1}"


def build_verification_matrix_sheet(ws, reqs):
    ws.views.sheetView[0].showGridLines = True

    headers = [
        ("ID Requisito", 14),
        ("Subsistema", 24),
        ("Enunciado Sintético", 45),
        ("Lote", 18),
        ("Tipo", 16),
        ("Método Verificación (INCOSE)", 20),
        ("Fase Contractual de Verificación", 25),
        ("Instalación / Entorno de Prueba", 26),
        ("Entregables Asociados", 18)
    ]

    ws.row_dimensions[1].height = 28
    for col_idx, (h_title, col_w) in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=h_title)
        cell.font = font_header
        cell.fill = fill_dark_header
        cell.alignment = align_center
        cell.border = border_cell
        ws.column_dimensions[get_column_letter(col_idx)].width = col_w

    row_num = 2
    for r in reqs:
        # Determination of Phase and Environment according to Pliego (RPVyA-04 a RPVyA-07)
        if "RPVyA" in r["id"] or "RDOC" in r["id"]:
            fase = "Fase I, II y III (Transversal)"
            entorno = "Revisión Documental / ERC"
            entregable = "E01, E03, E04"
        elif any(k in r["id"] for k in ["RLT1-03", "RLT1-10", "RLT2-02", "RLT2-08", "ROPE-09"]):
            fase = "Fase II (Fábrica) y Fase III (Validación ET/UME)"
            entorno = "Pistas de Ensayos / Campo de Maniobras"
            entregable = "E04, E05, E06, E11"
        elif "RSW" in r["id"]:
            fase = "Fase II (Fábrica)"
            entorno = "Laboratorio SW / HIL (Hardware-in-the-Loop)"
            entregable = "E09, E10"
        elif any(k in r["id"] for k in ["RCOM", "RNAV", "RPdO"]):
            fase = "Fase II (Fábrica) y Fase III (Validación)"
            entorno = "Campo Abierto / GNSS Denegado / Shelter"
            entregable = "E04, E05, E13"
        else:
            fase = "Fase II (Hito Final M25)"
            entorno = "Instalaciones del Contratista"
            entregable = "E04, E05, E11"

        row_data = [
            r["id"],
            r["name"],
            (r["text"][:120] + "...") if len(r["text"]) > 120 else r["text"],
            r["scope"],
            r["type"],
            r["v_method"],
            fase,
            entorno,
            entregable
        ]

        ws.row_dimensions[row_num].height = 28
        is_even = (row_num % 2 == 0)

        for col_idx, val in enumerate(row_data, start=1):
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_bold_data if col_idx == 1 else font_data
            cell.border = border_cell
            if is_even:
                cell.fill = fill_zebra

            if col_idx in [1, 4, 5, 6, 7, 9]:
                cell.alignment = align_center
            else:
                cell.alignment = align_left

        row_num += 1

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{row_num-1}"


def build_evaluation_sheet(ws, eval_items):
    ws.views.sheetView[0].showGridLines = True

    headers = [
        ("Código Baremo", 16),
        ("Descripción y Criterio de Puntuación", 55),
        ("Puntuación Máxima", 18),
        ("Propuesta Técnica del Equipo", 35)
    ]

    ws.row_dimensions[1].height = 28
    for col_idx, (h_title, col_w) in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=h_title)
        cell.font = font_header
        cell.fill = fill_dark_header
        cell.alignment = align_center
        cell.border = border_cell
        ws.column_dimensions[get_column_letter(col_idx)].width = col_w

    row_num = 2
    for item in eval_items:
        row_data = [
            item["code"],
            item["desc"],
            item["points"],
            item["solution"]
        ]
        ws.row_dimensions[row_num].height = 26
        is_even = (row_num % 2 == 0)

        for col_idx, val in enumerate(row_data, start=1):
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            cell.font = font_bold_data if col_idx == 1 else font_data
            cell.border = border_cell
            if is_even:
                cell.fill = fill_zebra

            if col_idx in [1, 3]:
                cell.alignment = align_center
            else:
                cell.alignment = align_left

        row_num += 1

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{row_num-1}"


def main():
    md_path = "Requisitos.md"
    print(f"Parsing {md_path}...")
    reqs, payloads, deliverables, eval_items = parse_markdown(md_path)
    print(f"Captured: {len(reqs)} Requirements, {len(payloads)} Payloads, {len(deliverables)} Deliverables, {len(eval_items)} Evaluation Items.")

    # 1. GENERATE MASTER WORKBOOK FOR 3DEXPERIENCE / CATIA / CAMEO
    wb_master = openpyxl.Workbook()
    
    # Sheet 1: Guía de Importación Dassault Systèmes
    ws_guide = wb_master.active
    ws_guide.title = "GUIA_IMPORTACION_CATIA"
    build_guide_sheet(ws_guide)

    # Sheet 2: SysML Requirements
    ws_reqs = wb_master.create_sheet(title="SysML_Requirements")
    build_sysml_requirements_sheet(ws_reqs, reqs)

    # Sheet 3: CATIA Design Table (Parametric CAD)
    ws_dt = wb_master.create_sheet(title="CATIA_Design_Table")
    build_catia_design_table_sheet(ws_dt)

    # Sheet 4: Cargas de Pago CP
    ws_cp = wb_master.create_sheet(title="Cargas_Pago_CP")
    build_payloads_sheet(ws_cp, payloads)

    # Sheet 5: Entregables E
    ws_e = wb_master.create_sheet(title="Entregables_E")
    build_deliverables_sheet(ws_e, deliverables)

    # Sheet 6: Matriz de Verificación
    ws_vm = wb_master.create_sheet(title="Matriz_Verificacion")
    build_verification_matrix_sheet(ws_vm, reqs)

    # Sheet 7: Criterios de Evaluación y Baremo
    ws_eval = wb_master.create_sheet(title="Criterios_Evaluacion")
    build_evaluation_sheet(ws_eval, eval_items)

    master_filename = "Requisitos_Sistema_UGV_3DEXPERIENCE.xlsx"
    wb_master.save(master_filename)
    print(f"Master workbook saved: {master_filename}")

    # 2. GENERATE DEDICATED SINGLE-SHEET DESIGN TABLE FOR CATIA V5 / 3DEXPERIENCE PART DESIGN
    wb_cad = openpyxl.Workbook()
    ws_cad = wb_cad.active
    ws_cad.title = "DesignTable"
    build_catia_design_table_sheet(ws_cad, is_standalone=True)
    cad_filename = "CATIA_Design_Table_UGV.xlsx"
    wb_cad.save(cad_filename)
    print(f"Dedicated CAD Design Table saved: {cad_filename}")


if __name__ == "__main__":
    main()
