from typing import Iterable, Tuple, List, Union
TicTacToeRow = List[str]
TicTacToeBoard = Tuple[TicTacToeRow, TicTacToeRow, TicTacToeRow]


def tic_tac_toe_finish(board: TicTacToeBoard, pos_y: int, pos_x: int, symbol: str) -> None:
    """
    This function takes in a TicTacToeBoard and applies the finishing move based on the provided parameters pos_y,
    pos_x, and symbol.

    :param board: A tuple containing 3 TicTacToeRows. Each TicTacToeRow in turn is a list containing 3 strings
    :param pos_y: The position of the TicTacToeRow that needs to be modified
    :param pos_x: The position of the column within a TicTacToeRow that needs to be modified
    :param symbol: The symbol that should be placed in the column (X, or O)
    :return: None
    """

    board_list = list(board)
    # Update the specified position with the symbol
    board_list[pos_y][pos_x] = symbol
    # Convert the list back to a tuple
    board = tuple(board_list)


def count_instances(collection: Tuple, instance: Union[int, str]) -> int:
    """
    This function counts the number of occurrences of the instance value within the collection parameter.

    :param collection: A tuple containing 0 or more instances
    :param instance: An item in the collection parameter
    :return: An integer.
    """
    # num = count_instances(collection, instance)
    # return num
    num = 0
    for item in collection:
        if item == instance:
            num +=1
    return num

def print_indexes_and_entries(indexes: Iterable, entries: Iterable) -> None:
    """
    This function iterates through the given parameters and prints the items formatted according to the following rules:
    The index of the indexes iterable correspond to the index of the entries iterable.
    The index takes 10 places even if it doesn't need all 10 places.

    :param indexes: A list or tuple
    :param entries: A list or tuple
    :return: None
    """

    # for i ,(index, entry) in enumerate(zip(indexes, entries)):
    #     print(f"Index: {str(index):<10} : Entry: {entry}")

    for i, (index, entry) in enumerate(zip(indexes, entries)):
        # Print the index and entry, formatting the index to take 10 places
        print(f"Index: {str(index):<10} Entry: {entry}")

def print_items_with_index(items: Iterable):
    """
    This function iterates through the items parameter and prints the item formatted according to the following rules:
    Each item printed received the index 1-N where N is the size of the items parameter.
    Indexes start at 1.
    Each index and item are separated by a colon and a space.
    :param items: A tuple or a list
    :return: None
    """
    for i, item in enumerate(items, start=1):
        print(f"{i}: {item}")

