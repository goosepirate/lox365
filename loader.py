# LibreOffice 7.4 on Windows bundles Python 3.8, so import from __future__
# in order to use new type hinting.
# https://peps.python.org/pep-0585/
from __future__ import annotations

import uno
import unohelper
from org.openoffice.sheet.addin import XLox365
import lox365 as lx

class Lox365(unohelper.Base, XLox365):
    def __init__(self, ctx): self.ctx = ctx

    def _get_dataarray(self, cellrange, positions: dict) -> tuple[tuple]:
        """Return the DataArray for the given cell range object and
        desired corner positions, which must be a dict with the keys:
        left, top, right, bottom.
        """
        return cellrange.getCellRangeByPosition(
            positions['left'], positions['top'],
            positions['right'], positions['bottom'],).DataArray

    def _get_shrunk_corners(self, cellrange) -> dict:
        """Find the rectangular cell range that encloses all computable
        content by removing from the given cell range all empty cells
        from the bottom and right. Then, return its corner positions
        as a dict with the keys: left, top, right, bottom.

        Computable content here refers to cells that have:
        numeric value, datetime, string, or formula.
        """
        address = cellrange.RangeAddress
        useful_ranges = cellrange.queryContentCells(23).RangeAddresses
        useful_positions = {'left': 0, 'top': 0,
            'right':  max(range.EndColumn for range in useful_ranges) - address.StartColumn,
            'bottom': max(range.EndRow    for range in useful_ranges) - address.StartRow,
        }
        return useful_positions

    def IMAGE    (self, *args): return lx.IMAGE    (*args)
    def TEXTSPLIT(self, *args): return lx.TEXTSPLIT(*args)
    def TOCOL    (self, *args): return lx.TOCOL    (*args)


def createInstance(ctx):
    return Lox365(ctx)

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance, 'com.goosepirate.lox365.oxt',
    ('com.sun.star.sheet.AddIn',),)