""" 
Author: 
- Diogo Santos (ist1110262)

Date:
- 23/10/2023 (Vinte e Três de Outubro de 2023)

Description: 
- This file contains the functions that are used on the FProg project2.

"""


"""
Setting Up classes to be used in type-hints.
"""


class intersecao:
    pass


class pedra:
    pass


class goban:
    pass


"""
Defining Intersecao structure
"""


# Create the intersecao
def cria_intersecao(column: str, line: int) -> intersecao:
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


# Return the column of intersecao
def obtem_col(intersecao: intersecao) -> str:
    return intersecao[0]


# Return the line of intersecao
def obtem_lin(intersecao: intersecao) -> int:
    return intersecao[1]


# Verify if the intercesao is valid
def eh_intersecao(intersecao: any) -> bool:
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


# Verify if the interceptions are equal
def intersecoes_iguais(intersecao1: any, intersecao2: any) -> bool:
    # Check if intersecao1 and intersecao2 are valid
    if not eh_intersecao(intersecao1) or not eh_intersecao(intersecao2):
        return False

    return intersecao1 == intersecao2


# Tranform intersecao in string
def intersecao_para_str(intersecao: intersecao) -> str:
    return obtem_col(intersecao) + str(obtem_lin(intersecao))


# Transform string into intersecao
def str_para_intersecao(intersecao: str) -> intersecao:
    return cria_intersecao(intersecao[0], int(intersecao[1:]))


# Return the adjacent interceptions
def obtem_intersecoes_adjacentes(
    intersecao: intersecao, last_inter: intersecao
) -> tuple:
    """
    Returns the adjacent intersections of the given intersection in the territory.

    Args:
    - intersecao: A tuple representing an intersection.
    - last_inter: A tuple representing the last intersection (top right)

    Returns:
    - A tuple containing the adjacent intersections of the given intersection in the territory,
    where each element is a tuple containing the column as a string and the line as an integer.
    """
    collumn, line = convert_intersecao((obtem_col(intersecao), obtem_lin(intersecao)))
    max_collumns, max_lines = (obtem_col(last_inter), obtem_lin(last_inter))
    inter_adjs = ()

    # Add the bottom adjacent interception
    if line > 0:
        inter_adjs += (cria_intersecao(chr(collumn + (ord("A") - 1) + 1), line),)

    # Add the left adjacent interception
    if collumn > 0:
        inter_adjs += (cria_intersecao(chr(collumn + (ord("A") - 1)), line + 1),)

    # Add the right adjacent interception
    if collumn + 2 <= ord(max_collumns) - (ord("A") - 1):
        inter_adjs += (cria_intersecao(chr(collumn + (ord("A") - 1) + 2), line + 1),)

    # Add the top adjacent interception
    if line + 2 <= max_lines:
        inter_adjs += (cria_intersecao(chr(collumn + (ord("A") - 1) + 1), line + 2),)

    return inter_adjs


# Order the Intersections by left to right, bottom to top
def ordena_intersecoes(intersecoes: tuple) -> tuple:
    """
    Sorts the intersections by their position from left to right and bottom to top.

    Args:
    - intersecoes: A tuple with intersections, where each inner tuple contains a string representing the
    intersection's collumn and an integer representing the intersection's line.

    Returns:
    - A tuple of tuples representing intersections sorted by their position from left to right and bottom to top.
    """
    # sort based on the number(line), then based on the letter(collumn)
    return tuple(sorted(intersecoes, key=lambda x: (obtem_lin(x), obtem_col(x))))


"""
Defining Pedra structure
"""


# Create pedra_branca
def cria_pedra_branca() -> pedra:
    return 1


# Create pedra_preta
def cria_pedra_preta() -> pedra:
    return 2


# Create pedra_neutra
def cria_pedra_neutra() -> pedra:
    return 0


# Verify if is pedra
def eh_pedra(pedra: any) -> bool:
    # Check if pedra is an integer
    if type(pedra) != int:
        return False

    # Check if pedra is one of the defined values
    return pedra in (1, 2, 3)


# Verify if pedra is white
def eh_pedra_branca(pedra: pedra) -> bool:
    return pedra == 1


# Verify if pedra is black
def eh_pedra_preta(pedra: pedra) -> bool:
    return pedra == 2


# Verify if the stones are equal
def pedras_iguais(pedra1: any, pedra2: any) -> bool:
    # Check if pedra1 and pedra 2 are valid
    if not eh_pedra(pedra1) or not eh_pedra(pedra2):
        return False

    return pedra1 == pedra2


# Transform pedra in string
def pedra_para_str(pedra: pedra) -> str:
    if eh_pedra_branca(pedra):
        return "O"
    elif eh_pedra_preta(pedra):
        return "X"
    else:
        return "."


# Check if pedra belongs to a player
def eh_pedra_jogador(pedra: pedra) -> bool:
    return eh_pedra_branca(pedra) or eh_pedra_preta(pedra)


"""
Defining goban structure
"""

# Create empty goban
def cria_goban_vazio(size: int) -> goban:
    if type(size) != int:
        raise ValueError('cria_goban_vazio: argumento invalido')

    if size not in (9,13,19):
        raise ValueError('cria_goban_vazio: argumento invalido')

    return [[ 0 for i in range(size)] for i in range(size)]

print(cria_goban_vazio(10))

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
