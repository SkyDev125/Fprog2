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
def obtem_col(inter: intersecao) -> str:
    return inter[0]


# Return the line of intersecao
def obtem_lin(inter: intersecao) -> int:
    return inter[1]


# Verify if the intersecao is valid
def eh_intersecao(inter: any) -> bool:
    """
    Verifies if the given intersection is valid.

    Parameters:
    - intersecao: A tuple containing a string and an integer, representing an intersection.

    Returns:
    - True if the intersection is valid, False otherwise.
    """
    # Check if the intersecao is a tuple
    if not isinstance(inter, tuple):
        return False

    # Check if the intersecao is the expected size
    if len(inter) != 2:
        return False

    # Create a set with all the valid strings
    valid_strings = {chr(ord("A") + i) for i in range(19)}

    # Check if the first element is a string
    if not isinstance(inter[0], str):
        return False

    # Check if the second element is a int
    if type(inter[1]) != int:
        return False

    # Check if the first element is a valid string
    if inter[0] not in valid_strings:
        return False

    # Check if the second element is a valid int
    return 1 <= inter[1] <= 19


# Verify if the intersections are equal
def intersecoes_iguais(inter1: any, inter2: any) -> bool:
    # Check if intersecao1 and intersecao2 are valid
    if not eh_intersecao(inter1) or not eh_intersecao(inter2):
        return False

    return inter1 == inter2


# Tranform intersecao in string
def intersecao_para_str(inter: intersecao) -> str:
    return obtem_col(inter) + str(obtem_lin(inter))


# Transform string into intersecao
def str_para_intersecao(inter: str) -> intersecao:
    return cria_intersecao(inter[0], int(inter[1:]))


# Return the adjacent intersections
def obtem_intersecoes_adjacentes(
    inter: intersecao, last_inter: intersecao
) -> tuple[intersecao]:
    """
    Returns the adjacent intersections of the given intersection in the territory.

    Args:
    - intersecao: A tuple representing an intersection.
    - last_inter: A tuple representing the last intersection (top right)

    Returns:
    - A tuple containing the adjacent intersections of the given intersection in the territory,
    where each element is a tuple containing the column as a string and the line as an integer.
    """
    collumn, line = convert_intersecao((obtem_col(inter), obtem_lin(inter)))
    max_collumns, max_lines = (obtem_col(last_inter), obtem_lin(last_inter))
    inter_adjs = ()

    # Add the bottom adjacent intersection
    if line > 0:
        inter_adjs += (cria_intersecao(chr(collumn + (ord("A") - 1) + 1), line),)

    # Add the left adjacent intersection
    if collumn > 0:
        inter_adjs += (cria_intersecao(chr(collumn + (ord("A") - 1)), line + 1),)

    # Add the right adjacent intersection
    if collumn + 2 <= ord(max_collumns) - (ord("A") - 1):
        inter_adjs += (cria_intersecao(chr(collumn + (ord("A") - 1) + 2), line + 1),)

    # Add the top adjacent intersection
    if line + 2 <= max_lines:
        inter_adjs += (cria_intersecao(chr(collumn + (ord("A") - 1) + 1), line + 2),)

    return inter_adjs


# Order the Intersections by left to right, bottom to top
def ordena_intersecoes(intersecoes: tuple[intersecao]) -> tuple[intersecao]:
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
def eh_pedra(p: any) -> bool:
    # Check if pedra is an integer
    if type(p) != int:
        return False

    # Check if pedra is one of the defined values
    return p in (1, 2, 3)


# Verify if pedra is white
def eh_pedra_branca(p: pedra) -> bool:
    return p == 1


# Verify if pedra is black
def eh_pedra_preta(p: pedra) -> bool:
    return p == 2


# Verify if the stones are equal
def pedras_iguais(p1: any, p2: any) -> bool:
    # Check if pedra1 and pedra 2 are valid
    if not eh_pedra(p1) or not eh_pedra(p2):
        return False

    return p1 == p2


# Transform pedra in string
def pedra_para_str(p: pedra) -> str:
    if eh_pedra_branca(p):
        return "O"
    elif eh_pedra_preta(p):
        return "X"
    else:
        return "."


# Check if pedra belongs to a player
def eh_pedra_jogador(p: pedra) -> bool:
    return eh_pedra_branca(p) or eh_pedra_preta(p)


"""
Defining goban structure
"""


# Create empty goban
def cria_goban_vazio(
    size: int,
) -> goban:  # Verificar com o prof pois n é inicial, mas é vazio
    # Check if size is an integer
    if type(size) != int:
        raise ValueError("cria_goban_vazio: argumento invalido")

    # Check if size is a valid size
    if size not in (9, 13, 19):
        raise ValueError("cria_goban_vazio: argumento invalido")

    # Create all the columns
    return [[0 for i in range(size)] for i in range(size)]


# Create a goban with set values
def cria_goban(
    size: int, brancas: tuple[intersecao], pretas: tuple[intersecao]
) -> goban:
    try:
        go = cria_goban_vazio(size)
    except:
        raise ValueError("cria_goban_vazio: argumento invalido")

    # Verify if each item is an intersecao
    for inter in brancas + pretas:
        if not eh_intersecao(inter):
            raise ValueError("cria_goban_vazio: argumento invalido")

        # Check if intersesao is valid for the terrain
        if not eh_intersecao_valida(go, inter):
            raise ValueError("cria_goban_vazio: argumento invalido")

    # Place the white pedras
    for inter in brancas:
        # Verify if there are no stones that share the same intersecao
        if inter in pretas:
            raise ValueError("cria_goban_vazio: argumento invalido")
        go = coloca_pedra(inter)

    # Place the black pedras
    for inter in pretas:
        go = coloca_pedra(inter)

    return go

# Creates a copy of the goban
def cria_copia_goban(go: goban) -> goban:
    return go

# Return the pedra in a given intersecao

# Return a valid last intersection (top right) based on the territory
def obtem_ultima_intersecao(go: goban) -> intersecao:
    """
    Returns the coordinates of the last intersection (top right) based on the given goban.

    Args:
    - go: A goban, where each element is a list representing a column of the territory.
    Each cell of the column can be either 0, 1 or 2.

    Returns:
    - A intersecao with a string and an integer representing the coordinates of the last intersection (top right) of the goban.
    """
    return cria_intersecao(chr((ord("A") - 1) + len(go)), len(go[0]))


# Verify if is goban
def eh_goban(go: any) -> bool:
    """
    Checks if the given goban is valid.

    Args:
    - go: A goban, where each element is a column of the goban.
    Each cell of the column can be either 0, 1 or 2.

    Returns:
    - True if the goban is valid, False otherwise.
    """
    # Check if goban is list
    if not isinstance(go, list):
        return False

    first_column = go[0]
    # Check if the goban is empty or larger than expected
    if len(go) not in (9, 13, 19) or len(go) != len(first_column):
        return False

    # Check if the collumns have the same lenght
    for column in go:
        # Check if the arg is a list
        if not isinstance(column, list):
            return False

        # Check if the column is empty or larger than expected
        if len(column) not in (9, 13, 19):
            return False

        # Check if the collumn has the same lenght as the first collumn
        if len(column) != len(first_column):
            return False

        # Check if the collumn has only 0, 1 or 2
        for cell in column:
            # Check if cell is int
            if type(cell) != int:
                return False

            if cell not in (0, 1, 2):
                return False

    return True


# Verify if the intersection is in the territory
def eh_intersecao_valida(go: goban, inter: intersecao) -> bool:
    """
    Verifies if the given intersecao is within the territory.

    Args:
    - go: a goban, where each element is a list representing a column of the goban.
    Each cell of the column can be either 0, 1 or 2.
    - inter: A intersecao containing a string and an integer.

    Returns:
    - True if the intersection is within the territory, False otherwise.
    """
    last_inter = obtem_ultima_intersecao(go)
    max_collumns, max_lines = obtem_col(last_inter), obtem_lin(last_inter)
    collumn, line = obtem_col(inter), obtem_lin(inter)

    # Check if the collumn is larger than the maximum allowed for collumns
    if collumn > max_collumns:
        return False

    # Check if the line is larger than the maximum allowed for lines
    return line <= max_lines


# Place a pedra in goban
def coloca_pedra(go: goban, inter: intersecao, p: pedra) -> goban:
    inter = convert_intersecao(inter)
    go[inter[0]][inter[1]] = p
    return go


"""
Auxiliary Functions

"""


# Return the intersecao in usable values for coding (A -> 0) (1 -> 0)
def convert_intersecao(inter: intersecao) -> tuple[int, int]:
    """
    Converts the intersection coordinates from a tuple of strings and integers to a tuple of usable integers.

    Args:
    - intersecao: A tuple containing a string and an integer, representing an intersection.

    Returns:
    - A tuple containing the column number as an integer (starting from 0) and the line number as an integer (starting from 0).
    """
    collumn, line = obtem_col(inter), obtem_lin(inter)
    return (ord(collumn) - (ord("A") - 1) - 1, line - 1)
