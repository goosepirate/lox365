# pytest
from lox365 import *

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
