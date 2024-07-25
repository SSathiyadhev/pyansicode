"""this file contains functions to control cursor"""


ESC = "\x1B["


def go_to_home() -> None:
    """
    this function sends cursor to home position ie (1,1)

    """
    print(f"{ESC}H", end="")


def go_to(ln:int, col:int) -> None:
    """
    this function sends cursor to specified position

    Arg:
        ln(int): the line to which the cursor to go
        col(int): to the column to which the cursor to go

    """
    print(f"{ESC}{ln};{col}H", end="")


def go_to_ln(ln:int) ->None:
    """
    this functions sends cursor to the specified line without
    changing the column

    Arg:
        ln(int): the line to which the cursor to go

    """
    print(f"go_to_ln({ln}) yet to be implemented")


def go_to_col(col:int) ->None:
    """
    this functions sends cursor to the specified column without
    changing the line

    Arg:
        ln(int): the column to which the cursor to go

    """
    print(f"{ESC}{col}G", end="")


def go_up(ln:int) -> None:
    """
    this function moves cursor up by the specified number of lines

    Arg:
        ln(int): number of lines by which cursor to move up

    """
    print(f"{ESC}{ln}A", end="")


def go_down(ln:int) -> None:
    """
    this function moves cursor down by the specified number of lines

    Arg:
        ln(int): number of lines by which cursor to move down

    """
    print(f"{ESC}{ln}B", end="")


def go_right(col:int) -> None:
    """
    this function moves cursor right by the specified number of columns

    Arg:
        col(int): number of columns by which cursor to move right

    """
    print(f"{ESC}{col}C", end="")


def go_left(col:int) -> None:
    """
    this function moves cursor left by the specified number of columns

    Arg:
        col(int): number of columns by which cursor to move left

    """
    print(f"{ESC}{col}D", end="")
