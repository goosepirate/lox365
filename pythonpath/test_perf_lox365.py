# pytest-benchmark
from lox365 import *

def test_XLOOKUP_all_rows_early_match(benchmark):
    benchmark(XLOOKUP, 'C',
        tuple([('A',),('B',),('C',)] + [('',)] * (1048576 - 3)),
        tuple([('D',),('E',),('F',)] + [('',)] * (1048576 - 3)))

def test_XLOOKUP_all_rows_late_match(benchmark):
    benchmark(XLOOKUP, 'C',
        tuple([('',)] * (1048576 - 3) + [('A',),('B',),('C',)]),
        tuple([('',)] * (1048576 - 3) + [('D',),('E',),('F',)]))

# def test_XLOOKUP_repeated_lookups_on_same_array(benchmark):
#     import numpy as np
#     called = 0
#     rand_lookup_array = tuple()
#     def get_rand_lookup_array():
#         nonlocal called
#         nonlocal rand_lookup_array
#         if called % 100 == 0:
#             rand_lookup_array = tuple(map(tuple, np.random.uniform(0,100,100000).reshape(-1,1)))
#         called += 1
#         return rand_lookup_array
#     benchmark(XLOOKUP, np.random.uniform(0,100),
#         get_rand_lookup_array(),
#         tuple(map(tuple, np.random.uniform(0,100,100000).reshape(-1,1)))
#     )

# def test_TEXTSPLIT_large_string(benchmark):
#     import random, string
#     benchmark(TEXTSPLIT,
#         ' '.join(random.choice(string.ascii_lowercase) for i in range(500000)),
#         ' ',
#     )

# reshape is the fastest method to reshape arrays.

# def test_flatten_numpyreshape(benchmark):
#     import numpy as np
#     import random
#     def test1(array):
#         return np.array(array).reshape(-1,1)
#     benchmark(test1, np.random.uniform(0,100,[1000,1000]))

# def test_flatten_numpyravel(benchmark):
#     import numpy as np
#     import random
#     def test1(array):
#         return np.array(array).ravel()
#     benchmark(test1, np.random.uniform(0,100,[1000,1000]))

# def test_flatten_numpyflatten(benchmark):
#     import numpy as np
#     import random
#     def test1(array):
#         return np.array(array).flatten()
#     benchmark(test1, np.random.uniform(0,100,[1000,1000]))

# def test_flatten_loop(benchmark):
#     import numpy as np
#     import random
#     def test1(array):
#         result = []
#         for row in array: result.extend(row)
#         return result
#     benchmark(test1, np.random.uniform(0,100,[1000,1000]))

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
