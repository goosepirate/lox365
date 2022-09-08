# import functools

ERR_CALC = '#CALC!'
ERR_NA = '#N/A'

def DBG_ECHO(x1):
    # from icecream import ic
    # ic(x1)
    return ((repr(x1),),)
    # return ((repr(type(x1)) + ' ' + repr(x1),),)

def FILTER(array, include, if_empty=ERR_CALC):
    if not if_empty: if_empty = ERR_CALC
    lookup_direction = 0 # 0 is vertical; 1 is horizontal
    if len(include) == 1 and len(include[0]) > 1: lookup_direction = 1
    import itertools
    if lookup_direction == 0:
        ans = tuple(itertools.compress(array, [i[0] for i in include]))
    elif lookup_direction == 1:
        return tuple(tuple(itertools.compress(row, include[0])) for row in array)
    return ans if ans else ((if_empty,),)

def SORT(array, sort_index=1, sort_order=1):
    if not sort_index: sort_index = 1
    if not sort_order or sort_order == 1: reverse = False
    elif sort_order == -1: reverse = True
    else: return ValueError
    return tuple(sorted(array,
        key=lambda r: str(r[sort_index - 1]),
        reverse=reverse))

def XLOOKUP(lookup_value, lookup_array, return_array, if_not_found=ERR_NA):
    if not if_not_found: if_not_found = ERR_NA
    lookup_direction = 0 # 0 is vertical; 1 is horizontal
    if len(lookup_array) == 1 and len(lookup_array[0]) > 1: lookup_direction = 1
    try:
        if lookup_direction == 0:
            return (return_array[lookup_array.index((lookup_value,))],)
        if lookup_direction == 1:
            return tuple((row[lookup_array[0].index(lookup_value)],) for row in return_array)
    except ValueError: return ((if_not_found,),)

# Too slow
# def XLOOKUP_old1(lookup_value, lookup_array, return_array, if_not_found):
#     lookup_item = (lookup_value,)
#     for index, item in enumerate(lookup_array):
#         if item == lookup_item: return (return_array[index],)
#     return ((if_not_found,),)
