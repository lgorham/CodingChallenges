
def highest(lst):
    highest = lst[0]

    for i in lst[1:]:
        if i > highest:
            highest = i

    return highest



def k_highest(lst, k):
    """
    k_highest([5, 7, 9, 3, 10, 4, 8], 3)
    [10, 9, 8]

    k_highest([0, 0, 0, 0], 2)
    [0, 0]

    k_highest([])
    """

    # If I wanted this to be the unique highest, I could change this to a set
    k_high = []

    for i in range(k):
        high_num = highest(lst)
        k_high.append(high_num)
        lst = lst.remove(high_num)

    return k_high






if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n ***ALL TESTS PASSED**"
