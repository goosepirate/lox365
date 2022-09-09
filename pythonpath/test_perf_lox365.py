# pytest-benchmark
from lox365 import *

def test_XLOOKUP_large_arrays(benchmark):
    benchmark(XLOOKUP, 'C',
        tuple([()]*500000) + (('A',), ('C',), ('E',)) + tuple([()]*500000),
        tuple([()]*500000) + (('B',), ('D',), ('F',)) + tuple([()]*500000),
    )

# zip is the fastest method to transpose arrays.

# def test_transpose_zip(benchmark):
#     import random
#     def test1(array):
#         return tuple(zip(*array))
#     benchmark(test1, tuple([tuple([random.random()]*100)]*10000),
#     )

# def test_transpose_numpytransposearr(benchmark):
#     import random
#     import numpy as np
#     def test1(array):
#         return np.transpose(array)
#     benchmark(test1, tuple([tuple([random.random()]*100)]*10000),
#     )

# def test_transpose_numpyTarr(benchmark):
#     import random
#     import numpy as np
#     def test1(array):
#         return np.array(array).T
#     benchmark(test1, tuple([tuple([random.random()]*100)]*10000),
#     )

# def test_transpose_numpyTtup(benchmark):
#     import random
#     import numpy as np
#     def test1(array):
#         return tuple(map(tuple, np.array(array).T))
#     benchmark(test1, tuple([tuple([random.random()]*100)]*10000),
#     )
