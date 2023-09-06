# https://stackoverflow.com/questions/75390577/python-copy-entire-row-with-formatting
from openpyxl.utils import rows_from_range
from openpyxl import load_workbook
from openpyxl.worksheet.cell_range import CellRange
from copy import copy


def copy_range(range_str, src_sheet, dst_sheet, offset):
    """ Copy cell values and style to the new row using offset"""
    for row in rows_from_range(range_str):
        for cell in row:
            if src_sheet[cell].value is not None:  # Don't copy other cells in merged unit
                dst_cell = dst_sheet[cell].offset(row=offset, column=0)
                src_cell = src_sheet[cell]

                ### Copy Cell value
                dst_cell.value = src_cell.value

                ### Copy Cell Styles
                dst_cell.font = copy(src_cell.font)
                dst_cell.alignment = copy(src_cell.alignment)
                dst_cell.border = copy(src_cell.border)
                dst_cell.fill = copy(src_cell.fill)

                dst_cell.number_format = src_cell.number_format

                # [JL] Add in
                # Read the original row height and column width of the source cell
                # dst_cell.height = src_cell.height
                # dst_sheet = src_sheet.row_dimensions.items().rd
                # Standardise the row and column dimensions across all sheets
                dst_sheet.column_dimensions[dst_cell.column_letter].width = src_sheet.column_dimensions[src_cell.column_letter].width

def get_merge_list(r_range, r_offset):
    """ Create a list of new cell merges from the existing row"""
    area = CellRange(r_range)  # Range to check for merged cells
    mlist = []  # List of merged cells on existing row offset to the new row
    for mc in ws.merged_cells:
        if mc.coord not in area:
            continue
        cr = CellRange(mc.coord)
        cr.shift(row_shift=r_offset)
        mlist.append(cr.coord)

    return mlist
