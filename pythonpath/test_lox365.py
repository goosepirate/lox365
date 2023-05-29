# pytest
from lox365 import *

def test_FILTER():
    '''Typical'''
    assert FILTER(
        (('A', 3), ('C', 2), ('B', 4)),
        ((1,), (0,), (1,)),
    ) == (('A', 3), ('B', 4))

    '''Single row result'''
    assert FILTER((('A', 3), ('C', 2), ('B', 4)),
        ((0,), (0,), (1,)),
    ) == (('B', 4), (0, 0))

    '''Not found'''
    assert FILTER(
        (('A', 3), ('C', 2)),
        ((0,), (0,)),
    ) == (('#CALC!',),)

    '''Horizontal lookup'''
    assert FILTER(
        (('A', 3, 'D'), ('C', 2, 'E')),
        ((0,1,1),),
    ) == ((3, 'D'), (2, 'E'))

    '''Valid booleans'''
    assert FILTER(
        (('A', 3), ('C', 2), ('B', 4)),
        ((2,), (0,), ('e',)),
    ) == (('A', 3), ('B', 4))

    '''Custom message if not found'''
    assert FILTER(
        (('A', 3), ('C', 2), ('B', 4)),
        ((0,), (0,), (0,)),
        'Nope',
    ) == (('Nope',),)

def test_SORT():
    '''Simple'''
    assert SORT(
        (('C', 1), ('B', 4), ('A', 3)),
    ) == (('A', 3), ('B', 4), ('C', 1))

    '''Multiple datatypes in array'''
    assert SORT(
        (('C', 1), ('B', 4), ('A', 3), (1, 5)),
    ) == ((1, 5), ('A', 3), ('B', 4), ('C', 1))

    '''Sort by a different column'''
    assert SORT(
        (('A', 4), ('B', 3), ('D', 2)),
        2,
    ) == (('D', 2),('B', 3),('A', 4))

def test_TEXTSPLIT():
    '''Typical'''
    assert TEXTSPLIT('a/b/c', '/') == (('a', 'b', 'c'),)

    '''No split'''
    assert TEXTSPLIT('a', '/') == (('a', 0),)

    '''Empty text'''
    assert TEXTSPLIT('', '/') == ((0,),)

def test_TOCOL():
    '''Typical'''
    assert TOCOL((('a','b'),('c','d'))) == \
        (('a',),('b',),('c',),('d',))

    '''Blank cells'''
    assert TOCOL((('a',0),)) == (('a',),(0,))
    assert TOCOL(((0,'b'),('c',0))) == ((0,),('b',),('c',),(0,))
    assert TOCOL(((0,),)) == ((0,),)

def test_UNIQUE():
    '''Typical'''
    assert UNIQUE((('b',),('a',),('b',),('a',))) == \
        (('b',),('a',))

def test_XLOOKUP():
    '''Typical'''
    assert XLOOKUP('C',
        (('A',), ('C',), ('E',)),
        (('B',), ('D',), ('F',)),
    ) == (('D',),)

    '''Blank key'''
    assert XLOOKUP('',
        (('A',), ('',),  ('E',), ('',)),
        (('B',), ('D',), ('F',), ('H',)),
    ) == (('D',),)

    '''Not found'''
    assert XLOOKUP('J',
        (('A',), ('C',), ('E',)),
        (('B',), ('D',), ('F',)),
    ) == (('#N/A',),)

    '''Pick first valid result when multiple matches'''
    assert XLOOKUP('A',
        (('C',), ('A',), ('A',)),
        (('B',), ('D',), ('F',)),
    ) == (('D',),)

    '''Vertical lookup, multi-column output'''
    assert XLOOKUP('C',
        (('A',), ('C',), ('E',)),
        (('B', 'G'), ('D', 'H'), ('F', 'I')),
    ) == (('D', 'H'),)

    '''Horizontal lookup'''
    assert XLOOKUP('C',
        (('B', 'C', 'A'),),
        (('F', 'E', 'D'),),
    ) == (('E',),)

    '''Horizontal lookup, multi-row output'''
    assert XLOOKUP('C',
        (('B', 'C', 'A'),),
        (('F', 'E', 'D'), ('H', 'G', 'I')),
    ) == (('E',),('G',))

    '''Custom message if not found'''
    assert XLOOKUP('J',
        (('A',), ('C',), ('E',)),
        (('B',), ('D',), ('F',)),
        'Not found',
    ) == (('Not found',),)
    assert XLOOKUP('J',
        (('A',), ('C',)),
        (('B',), ('D',)),
        '',
    ) == (('',),)
