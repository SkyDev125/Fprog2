""" 
Author: 
- Diogo Santos (ist1110262)

Date:
- 23/10/2023 (Vinte e Três de Outubro de 2023)

Description: 
- This file contains the functions that are used on the FProg project2.

"""


def cria_intersecao(column: str, line: int) -> tuple[str, int]:
    # Create a set with all the valid strings
    valid_strings = {chr(ord("A") + i) for i in range(19)}

    # Check if the first element is a string
    if not isinstance(column, str):
        raise ValueError("cria_intersecao: argumentos invalidos")

    # Check if the second element is a int
    if type(line) != int:
        raise ValueError("cria_intersecao: argumentos invalidos")

    # Check if the first element is a valid string
    if column not in valid_strings:
        raise ValueError("cria_intersecao: argumentos invalidos")

    # Check if the second element is a valid int
    if line < 1 or line > 19:
        raise ValueError("cria_intersecao: argumentos invalidos")

    return (column, line)


def obtem_col(intersecao: tuple) -> str:
    return intersecao[0]


def obtem_lin(intersecao: tuple) -> int:
    return intersecao[1]


# Verify if the interception is valid
def eh_intersecao(intersecao: tuple[str, int]) -> bool:
    """
    Verifies if the given intersection is valid.

    Parameters:
    - intersecao: A tuple containing a string and an integer, representing an intersection.

    Returns:
    - True if the intersection is valid, False otherwise.
    """
    # Check if the intersecao is a tuple
    if not isinstance(intersecao, tuple):
        return False

    # Check if the intersecao is the expected size
    if len(intersecao) != 2:
        return False

    # Create a set with all the valid strings
    valid_strings = {chr(ord("A") + i) for i in range(19)}

    # Check if the first element is a string
    if not isinstance(intersecao[0], str):
        return False

    # Check if the second element is a int
    if type(intersecao[1]) != int:
        return False

    # Check if the first element is a valid string
    if intersecao[0] not in valid_strings:
        return False

    # Check if the second element is a valid int
    return 1 <= intersecao[1] <= 19


def intersecoes_iguais(
    intersecao1: tuple[str, int], intersecao2: tuple[str, int]
) -> bool:
    # Check if intersecao1 and intersecao2 are valid
    if not eh_intersecao(intersecao1) or not eh_intersecao(intersecao2):
        raise ValueError("verifica_conexao: argumentos invalidos")

    return intersecao1 == intersecao2


def intersecao_para_str(intersecao: tuple) -> str:
    return intersecao[0] + str(intersecao[1])


def str_para_intersecao(intersecao: str) -> tuple[str, int]:
    return intersecao[0], int(intersecao[1:])


# Return the adjacent interceptions
def obtem_intersecoes_adjacentes(
    intersecao: tuple[str, int], last_inter: tuple[str, int]
) -> tuple[tuple[str, int]]:
    """
    Returns the adjacent intersections of the given intersection in the territory.

    Args:
    - last_inter: A tuple representing the last intersection (top right) 
    - intersecao: A tuple containing a string and an integer, representing an intersection.

    Returns:
    - A tuple containing the adjacent intersections of the given intersection in the territory,
    where each element is a tuple containing the column as a string and the line as an integer.
    """
    collumn, line = convert_intersecao(intersecao)
    max_collumns, max_lines = last_inter
    inter_adjs = ()

    # Add the bottom adjacent interception
    if line > 0:
        inter_adjs += ((chr(collumn + (ord("A") - 1) + 1), line),)

    # Add the left adjacent interception
    if collumn > 0:
        inter_adjs += ((chr(collumn + (ord("A") - 1)), line + 1),)

    # Add the right adjacent interception
    if collumn + 2 <= ord(max_collumns) - (ord("A") - 1):
        inter_adjs += ((chr(collumn + (ord("A") - 1) + 2), line + 1),)

    # Add the top adjacent interception
    if line + 2 <= max_lines:
        inter_adjs += ((chr(collumn + (ord("A") - 1) + 1), line + 2),)

    return inter_adjs


# Order the Intersections by left to right, bottom to top
def ordena_intersecoes(intersecoes: tuple[tuple[str, int]]) -> tuple[tuple[str, int]]:
    """
    Sorts the intersections by their position from left to right and bottom to top.

    Args:
    - intersecoes: A tuple of tuples representing intersections, where each inner tuple contains a string representing the
    intersection's collumn and an integer representing the intersection's line.

    Returns:
    - A tuple of tuples representing intersections sorted by their position from left to right and bottom to top.
    """
    # sort based on the number(line), then based on the letter(collumn)
    return tuple(sorted(intersecoes, key=lambda x: (x[1], x[0])))


"""
Auxiliary Functions

"""


# Return the interseption in usable values for coding (A -> 0) (1 -> 0)
def convert_intersecao(intersecao: tuple[str, int]) -> tuple[int, int]:
    """
    Converts the intersection coordinates from a tuple of strings and integers to a tuple of usable integers.

    Args:
    - intersecao: A tuple containing a string and an integer, representing an intersection.

    Returns:
    - A tuple containing the column number as an integer (starting from 0) and the line number as an integer (starting from 0).
    """
    collumn, line = intersecao
    return (ord(collumn) - (ord("A") - 1) - 1, line - 1)

