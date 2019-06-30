def func(x):
    return - (x - 12.4)**2 + 200


def derivative(x):
    """
    Derivative of func
    :param x: x at which to calculate derivative
    :return: float, the derivative at x.
    """
    return -2*(x - 12.4)


def find_arg_max(start, end, epsilon):
    """
    Binary search to find maximum of function 'func(x)'
    :param start: float, left boundary of search
    :param end: float, right boundary of search
    :param epsilon, float, precision, how closely to max want to be.
    :return: float, value of x which gives us the max of func within the specified precision
    """
    middle = (0.5 * (end + start))
    while middle - start > epsilon:

        deriv = derivative(middle)

        if deriv > 0:
            start = middle
        elif deriv < 0:
            end = middle
        else:
            return middle

        middle = (0.5 * (end + start))

    left = func(start)
    right = func(end)
    if left < right:
        return end
    else:
        return start


if __name__ == "__main__":
    result = find_arg_max(3, 4567, 0.001)
    print(result)