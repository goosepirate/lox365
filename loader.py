import uno
import unohelper
from org.openoffice.sheet.addin import XLox365
import lox365 as lx

class Lox365(unohelper.Base, XLox365):
    def __init__(self, ctx): self.ctx = ctx

    def DBG_ECHO (self, *args): return lx.DBG_ECHO(*args)
    def DBG_ECHO2(self, *args): return lx.DBG_ECHO2(*args)
    def DBG_ECHO3(self, *args): return lx.DBG_ECHO3(*args)

    def FILTER   (self, *args): return lx.FILTER(*args)
    def SORT     (self, *args): return lx.SORT(*args)
    def TEXTSPLIT(self, *args): return lx.TEXTSPLIT(*args)
    def TOCOL    (self, *args): return lx.TOCOL(*args)
    def UNIQUE   (self, *args): return lx.UNIQUE(*args)
    def XLOOKUP  (self, *args): return lx.XLOOKUP(*args)

def createInstance(ctx):
    return Lox365(ctx)

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance, 'com.goosepirate.lox365.oxt',
    ('com.sun.star.sheet.AddIn',),)