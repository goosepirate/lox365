# import functools
import pprint

ERR_CALC = '#CALC!'
ERR_NA = '#N/A'

try:
    import imagefn
    IMAGE = imagefn.IMAGE
except ImportError: pass

def TEXTSPLIT(text, colDelimiter):
    if text == '' or text == '0': return ((0,),) # Compensate for when LO Calc converts a blank cell to a '0' string.
    t2 = text.split(colDelimiter)
    if len(t2) == 1: t2.append(0) # If output is only one item, append a zero to ensure the array function works as intended.
    return (tuple(t2),)

def TOCOL(array):
    result = []
    for row in array:
        for item in row:
            result.append((item,))
    return tuple(result)
