import math




class ShapeException(Exception):
    pass


def dot(one_vector, two_vector):

    if len(one_vector) == len(two_vector):
        dots_one = [x for x in one_vector]
        dots_two = [x for x in two_vector]
        dots = [a*b for a,b in zip(dots_one, dots_two)]
        return dots
    else:
        pass

dot((1,2,3),(4,5,6))


def magnitude(one_vector):
    squares = [x**2 for x in one_vector]
    return (math.sqrt(sum(squares)))


def shape():
    pass


def vector_add():
    pass


def vector_sub():
    pass


def vector_sum():
    pass


def vector_multiply():
    pass


def vector_mean():
    pass


def matrix_row():
    pass


def matrix_col():
    pass


def matrix_scalar_multiply():
    pass


def matrix_vector_multiply():
    pass


def matrix_matrix_multiply():
    pass
