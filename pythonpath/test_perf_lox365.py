# pytest-benchmark
from lox365 import *

# def test_XLOOKUP_large_arrays(benchmark):
#     benchmark(XLOOKUP, 'C',
#         tuple([()]*500000) + (('A',), ('C',), ('E',)) + tuple([()]*500000),
#         tuple([()]*500000) + (('B',), ('D',), ('F',)) + tuple([()]*500000),
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
