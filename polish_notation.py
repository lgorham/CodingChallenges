
def polish_notation(operation):
    """
    >>> polish_notation("+ 1 2")
    3
    >>> polish_notation("* 2 + 1 2")
    6
    >>> polish_notation("+ 9 * 2 3")
    15
    >>> polish_notation("- 1 2")
    -1
    >>> polish_notation("- 9 * 2 3")
    3
    >>> polish_notation("/ 6 - 4 2")
    3
    """

    operands = []
    operators = []
    for char in operation:
        if char == " ":
            continue

        try:
            operands.append(int(char))

        except ValueError:
            operators.append(char)

    op2 = operands.pop()

    while operands:
        operator = operators.pop()
        op1 = operands.pop()

        if operator == "+":
            op2 = (op1 + op2)

        if operator == "-":
            op2 = (op1 - op2)

        if operator == "/":
            op2 = (op1 / op2)

        if operator == "*":
            op2 = (op1 * op2)

    return op2





if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n **ALL TESTS PASSED**"


