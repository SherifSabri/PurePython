
from monads import Maybe
from higher_order_functions import py_curry, py_foldr, py_apply, py_take_while

# res = py_map([1,2,3], (lambda x: x+1))
# print(type(res))
# [print(e) for e in res] # prints 2 3 4
#
# func_gen = py_curry(lambda x: x+1, lambda x: x*2, lambda x: x*x)
# for func in func_gen:
#     print(func(3))  # prints 4 6 9

maybe_num = Maybe(3)
maybe_nothing = Maybe(None)
# print(maybe_nothing)
# print(maybe_num)
# nothing_example = maybe_num.bind(lambda y: maybe_nothing).bind(lambda x: Maybe.return_maybe(7) + x)  # prints Nothing
# just_example = maybe_num.bind(lambda x: Maybe(7 + x))  # prints Just 10
# print(nothing_example)
# print(just_example)


filtered_list = py_foldr([8,12,24,4], lambda x, y: x / y, 2)    # prints 8
print(filtered_list)

doubleX = lambda x: x + x
squareX = lambda x: x * x
tripleX = lambda x: 3 * x

res = py_apply(tripleX, doubleX)
print(res(3))