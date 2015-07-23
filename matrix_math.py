from functools import reduce
import numpy as np
import operator



class ShapeException(Exception):
    pass


def shape_check(a, b):
    if len(a) != len(b):
        raise ShapeException
    else:
        pass


def dot(vect_one, vect_two):
    shape_check(vect_one, vect_two)
    hammer = []
    for x in range(len(vect_one)):
        num = vect_one[x] * vect_two[x]
        hammer.append(num)
    return sum(hammer)


def magnitude(vect):
    list = [x**2 for x in vect]
    return (sum(list))**.5


def shape(container):
    try:
        row = len(container[0])
    except TypeError:
        return len(container),
    return row, len(container)


def vector_add(vect_one, vect_two):
    shape_check(vect_one, vect_two)
    new_vect = []
    for x in range(len(vect_one)):
        num = vect_one[x] + vect_two[x]
        new_vect.append(num)
    return new_vect


def vector_sub(vect_one, vect_two):
    shape_check(vect_one, vect_two)
    new_vect = []
    for x in range(len(vect_one)):
        num = vect_one[x] - vect_two[x]
        new_vect.append(num)
    return new_vect


def vector_sum(*args):
    reduce(shape_check, tuple(args))
    values = [x for x in args]
    other = []
    for x in range(len(values[0])):
        num = sum(values[x-1])
        other.append(num)
    return other


def vector_multiply(vect, scalar):
    new_vect = [x * scalar for x in vect]
    return new_vect


def vector_mean(*args):
   reduce(shape_check, tuple(args))
   return (reduce(vector_add, tuple(args))) / len(args)


def matrix_row(matrix, row):
    return matrix[row]


def matrix_col(matrix, col):
    return [row[col] for row in matrix]


def matrix_scalar_multiply(matrix, scalar):
    return [[x * scalar for x in row]for row in matrix]



def matrix_vector_multiply(m, v):
    shape_check(matrix_row(m, 0), v)
    rows = len(m)
    w = [0]*rows
    irange = range(len(v))
    sum = 0
    for j in range(rows):
        r = m[j]
        for i in irange:
            sum += r[i]*v[i]
        w[j],sum = sum,0
    return w


def matrix_matrix_multiply(matrix_one, matrix_two):
    shape_check(matrix_one, matrix_two)


