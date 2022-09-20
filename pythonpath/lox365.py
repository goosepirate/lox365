# import functools

ERR_CALC = '#CALC!'
ERR_NA = '#N/A'

def DBG_ECHO(x1):
    return ((repr(x1),),)
def DBG_ECHO2(x1):
    return ((repr(x1),),)
def DBG_ECHO3(x1):
    return ((repr(x1),),)

def FILTER(array, include, ifEmpty=ERR_CALC):
    if not ifEmpty: ifEmpty = ERR_CALC
    lookup_direction = 0 # 0 is vertical; 1 is horizontal
    if len(include) == 1 and len(include[0]) > 1: lookup_direction = 1
    import itertools
    if lookup_direction == 0:
        ans = tuple(itertools.compress(array, [i[0] for i in include]))
    elif lookup_direction == 1:
        return tuple(tuple(itertools.compress(row, include[0])) for row in array)
    return ans if ans else ((ifEmpty,),)

def SORT(array, sortIndex=1, sortOrder=1):
    if not sortIndex: sortIndex = 1
    if not sortOrder or sortOrder == 1: reverse = False
    elif sortOrder == -1: reverse = True
    else: return ValueError
    return tuple(sorted(array,
        key=lambda r: str(r[sortIndex - 1]),
        reverse=reverse))

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

def UNIQUE(array):
    return tuple(dict.fromkeys(array))

def XLOOKUP(lookupValue, lookupArray, returnArray, ifNotFound=ERR_NA):
    if not ifNotFound: ifNotFound = ERR_NA
    lookup_direction = 0 # 0 is vertical; 1 is horizontal
    if len(lookupArray) == 1 and len(lookupArray[0]) > 1: lookup_direction = 1
    try:
        if lookup_direction == 0:
            return (returnArray[lookupArray.index((lookupValue,))],)
        if lookup_direction == 1:
            return tuple((row[lookupArray[0].index(lookupValue)],) for row in returnArray)
    except ValueError: return ((ifNotFound,),)

# Too slow
# def XLOOKUP_old1(lookup_value, lookup_array, return_array, if_not_found):
#     lookup_item = (lookup_value,)
#     for index, item in enumerate(lookup_array):
#         if item == lookup_item: return (return_array[index],)
#     return ((if_not_found,),)
