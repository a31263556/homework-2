def get_even_squares(num_list: list[int]) -> list[int]:
    """
    Return a list of the squares of even numbers in the given list.

    Args:
        num_list (list[int]): The list of integers.

    Returns:
        list[int]: A list containing the squares of even numbers.
    """
    return [num**2 for num in num_list if num % 2 == 0]


def get_odd_cubes(num_list: list[int]) -> list[int]:
    """
    Return a list of the cubes of odd numbers in the given list.

    Args:
        num_list (list[int]): The list of integers.

    Returns:
        list[int]: A list containing the cubes of odd numbers.
    """
    return [num**3 for num in num_list if num % 2 != 0]


def get_sliced_list(num_list: list[int]) -> list[int]:
    """
    Return a sliced sublist starting from the 5th element to the last element.

    Args:
        num_list (list[int]): The list of integers.

    Returns:
        list[int]: A sublist of num_list.
    """
    return num_list[4:]


def format_numbers(numbers: list[int]) -> list[str]:
    """
    Format numbers to be right-aligned within 8 characters width.

    Args:
        numbers (list[int]): The list of integers.

    Returns:
        list[str]: A list containing formatted numbers.
    """
    return [f"{num:>{8}}" for num in numbers]


if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    even_squares = get_even_squares(num_list)
    odd_cubes = get_odd_cubes(num_list)
    sliced_list = get_sliced_list(num_list)

    formatted_numbers = format_numbers(even_squares + odd_cubes + sliced_list)

    for formatted_number in formatted_numbers:
        print(formatted_number, end=", ")