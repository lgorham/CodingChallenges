"""Boggle word check.

Given a 5x5 boggle board, see if you can find a given word in it.

In Boggle, you can start with any letter, then move in any NEWS direction.
You can continue to change directions, but you cannot use the exact same
tile twice.

So, for example::

    N C A N E
    O U I O P
    Z Q Z O N
    F A D P L
    E D E A Z
 
In this grid, you could find `NOON* (start at the `N` in the top
row, head south, and turn east in the third row). You cannot find
the word `CANON` --- while you can find `CANO` by starting at the
top-left `C`, you can 't re-use the exact same `N` tile on the
front row, and there's no other `N` you can reach.

For example::

    >>> board = make_board('''
    ... N C A N E
    ... O U I O P
    ... Z Q Z O N
    ... F A D P L
    ... E D E A Z
    ... ''')

`NOON` should be found (0, 3) -> (1, 3) -> (2, 3) -> (2, 4)::
 
    >>> find(board, "NOON")
    True

`NOPE` should be found (0, 3) -> (1, 3) -> (1, 4) -> (0, 4)::

    >>> find(board, "NOPE")
    True

`CANON` can't be found (`CANO` starts at (0, 1) but can't find
the last `N` and can't re-use the N)::

    >>> find(board, "CANON")
    False

You cannot travel diagonally in one move, which would be required
to find `QUINE`::

    >>> find(board, "QUINE")
    False

We can recover if we start going down a false path (start 3, 0)::

    >>> find(board, "FADED")
    True
"""


def make_board(board_string):
    """Make a board from a string.

    For example::

        >>> board = make_board('''
        ... N C A N E
        ... O U I O P
        ... Z Q Z O N
        ... F A D P L
        ... E D E A Z
        ... ''')

        >>> len(board)
        5

        >>> board[0]
        ['N', 'C', 'A', 'N', 'E']
    """

    letters = board_string.split()

    board = [
        letters[0:5],
        letters[5:10],
        letters[10:15],
        letters[15:20],
        letters[20:25],
    ]

    return board


def find(board, word):
    """Can word be found in board?"""

    past_positions = []

    for i in range(5):
        for j in range(5):

            if used_squares(board, word, [(i, j)]):
                return True

    return False

    #         if word[0] == board[i][j]:
    #             past_positions.append((i, j))

    # return used_squares(board, word[1:], past_positions)



def used_squares(board, word, past_positions):

    # Base case - if we have gone through all the letter successfully
    if not word:
        return True

    
    # Recursive case: reduces the space, and the word
    prev = past_positions[-1]

    for i in range(5):
        for j in range(5):

            if (word[0] == board[i][j]) \
            and ((i, j) not in past_positions) \
            and ( abs( i - prev[0] ) + abs( j - prev[1] )  ) == 1:

                past_positions.append((i, j))
                if used_squares(board, word[1:], past_positions):
                    return True

    
    return False






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; YOU FOUND SUCCESS! ***\n"
