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

    return column, line


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

    # Try to create an intersecao with the values and evaluate the situation
    try:
        cria_intersecao(inter[0], inter[1])
        return True
    except:
        return False


# Verify if the intersections are equal
def intersecoes_iguais(inter1: any, inter2: any) -> bool:
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
    collumn, line = convert_intersecao(inter)
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
    return p in (0, 1, 2)


# Verify if pedra is white
def eh_pedra_branca(p: pedra) -> bool:
    return p == 1


# Verify if pedra is black
def eh_pedra_preta(p: pedra) -> bool:
    return p == 2


# Verify if the stones are equal
def pedras_iguais(p1: any, p2: any) -> bool:
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
) -> goban:
    # Check if size is an integer
    if type(size) != int:
        raise ValueError("cria_goban_vazio: argumento invalido")

    # Check if size is a valid size
    if size not in (9, 13, 19):
        raise ValueError("cria_goban_vazio: argumento invalido")

    # Create all the columns
    return [[cria_pedra_neutra() for i in range(size)] for i in range(size)]


# Create a goban with set values
def cria_goban(
    size: int, brancas: tuple[intersecao], pretas: tuple[intersecao]
) -> goban:
    # Check if size is valid
    try:
        go = cria_goban_vazio(size)
    except:
        raise ValueError("cria_goban: argumentos invalidos")

    # Verify if both arguments are tuples
    if not isinstance(brancas, tuple) or not isinstance(pretas, tuple):
        raise ValueError("cria_goban: argumentos invalidos")

    # Check if there are any duplicates in the tuples
    if len(brancas) != len(set(brancas)) or len(pretas) != len(set(pretas)):
        raise ValueError("cria_goban: argumentos invalidos")

    # Verify if each item is an intersecao
    for inter in brancas + pretas:
        if not eh_intersecao(inter):
            raise ValueError("cria_goban: argumentos invalidos")

        # Check if intersesao is valid for the terrain
        if not eh_intersecao_valida(go, inter):
            raise ValueError("cria_goban: argumentos invalidos")

    # Place the white pedras
    for inter in brancas:
        # Verify if there are no stones that share the same intersecao
        if inter in pretas:
            raise ValueError("cria_goban: argumentos invalidos")
        go = coloca_pedra(go, inter, cria_pedra_branca())

    # Place the black pedras
    for inter in pretas:
        go = coloca_pedra(go, inter, cria_pedra_preta())

    return go


# Creates a copy of the goban
def cria_copia_goban(go: goban) -> goban:
    return [[go[column][line] for line in range(len(go))] for column in range(len(go))]


# Return a valid last intersection (top right) based on the territory
def obtem_ultima_intersecao(go: goban) -> intersecao:
    """
    Returns the coordinates of the last intersection (top right) based on the given goban.

    Args:
    - go: A goban, where each element is a list representing a column of the territory.
    Each cell of the column can be either a black, white, or neutral stone.

    Returns:
    - A intersecao with a string and an integer representing the coordinates of the last intersection (top right) of the goban.
    """
    return cria_intersecao(chr((ord("A") - 1) + len(go)), len(go))


# Return the pedra in a given intersecao
def obtem_pedra(go: goban, inter: intersecao) -> pedra:
    inter = convert_intersecao(inter)
    return go[inter[0]][inter[1]]


# Return the chain of intersections
def obtem_cadeia(go: goban, inter: intersecao) -> tuple[intersecao]:
    """
    Returns a sequence of adjacent intersections that have the same value in a goban.

    Args:
    - go: a goban, where each element is a intersecao representing a column of the goban.
    Each cell of the column can be either a black, white, or neutral stone.
    - inter: A intersecao containing a string and an integer

    Returns:
    - A tuple of intersections representing a sequence of adjacent intersections that have the same value in the goban.

    Raises:
    - ValueError: If the given goban or intersection are invalid.
    """
    # Check if intersecao is free
    is_free = obtem_pedra(go, inter)
    visited = []

    # Create recursive function to check if the adjacent intersections are also the same as freedom
    def recursive_check(go, inter, visited):
        # Add the intersecao to the list
        chain = (inter,)
        visited += chain

        # Check if the adjacent intersections are equal to the pedra
        for inter in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(go)):
            if inter not in visited and obtem_pedra(go, inter) == is_free:
                chain += recursive_check(go, inter, visited)

        return chain

    # Get the list of intersections
    chain = recursive_check(go, inter, visited)

    return ordena_intersecoes(chain)


# Place a pedra in goban
def coloca_pedra(go: goban, inter: intersecao, p: pedra) -> goban:
    inter = convert_intersecao(inter)
    go[inter[0]][inter[1]] = p
    return go


# Remove a pedra in goban
def remove_pedra(go: goban, inter: intersecao) -> goban:
    inter = convert_intersecao(inter)
    go[inter[0]][inter[1]] = cria_pedra_neutra()
    return go


# Remove a chain of stones in goban
def remove_cadeia(go: goban, chain: tuple[intersecao]) -> goban:
    for inter in chain:
        go = remove_pedra(go, inter)
    return go


# Verify if is goban
def eh_goban(go: any) -> bool:
    """
    Checks if the given goban is valid.

    Args:
    - go: A goban, where each element is a column of the goban.
    Each cell of the column can be either a black, white, or neutral stone.

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

        # Check if the column is smaller or larger than expected
        if len(column) not in (9, 13, 19):
            return False

        # Check if the collumn has the same lenght as the first collumn
        if len(column) != len(first_column):
            return False

        # Check if the collumn has only stones
        for cell in column:
            # Check if cell is int
            if type(cell) != int:
                return False

            if cell not in (
                cria_pedra_neutra(),
                cria_pedra_branca(),
                cria_pedra_preta(),
            ):
                return False

    return True


# Verify if the intersection is in the territory
def eh_intersecao_valida(go: goban, inter: intersecao) -> bool:
    """
    Verifies if the given intersecao is within the territory.

    Args:
    - go: a goban, where each element is a list representing a column of the goban.
    Each cell of the column can be either a black, white, or neutral stone.
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


# Verify if gobans are equal
def gobans_iguais(go1: goban, go2: goban) -> bool:
    if not eh_goban(go1) or not eh_goban(go2):
        return False

    return go1 == go2


# Return the territory as a string
def goban_para_str(go: goban) -> str:
    """
    Returns a string representation of a goban, where each intersection is represented by an X, O or . depending on
    whether it is black, white or empty, respectively.
    The goban is formatted as a grid with letters representing columns and numbers representing rows.

    Args:
    - go: a goban, where each element is a list representing a column of the goban.
    Each cell of the column can be either a black, white, or neutral stone.

    Returns:
    - A string representation of the goban, formatted as a grid with letters representing columns and numbers
    representing rows.
    """
    # Get the maximum collumns and lines
    last_inter = obtem_ultima_intersecao(go)
    max_columns, max_lines = obtem_col(last_inter), obtem_lin(last_inter)
    max_columns = ord(max_columns) - (ord("A") - 1)

    # Add a Letters line
    s = (
        ["  "]
        + [" " + chr((ord("A") - 1) + x) for x in range(1, max_columns + 1)]
        + ["\n"]
    )

    # Create the lines (number, values, number)
    for x in range(max_lines, 0, -1):
        # Create the values
        string_terrain = [
            " " + pedra_para_str(obtem_pedra(go, cria_intersecao(chr(ord("A") + p), x)))
            for p in range(0, max_columns)
        ]

        # Add the lines to the string dynamically
        if x > 9:
            s += [str(x)] + string_terrain + [" " + str(x) + "\n"]
        else:
            s += [" " + str(x)] + string_terrain + ["  " + str(x) + "\n"]

    # Add a Letters line
    s += ["  "] + [" " + chr((ord("A") - 1) + x) for x in range(1, max_columns + 1)]

    # Join the string
    return "".join(s)


# Return a tuple of intersections that are empty
def obtem_territorios(go: goban) -> tuple[tuple[intersecao]]:
    """
    Returns the free chains in a goban (territories).

    Args:
    - go: A goban, where each element is a line representing a column of the territory.
    Each cell of the column can be either a black, white, or neutral stone.

    Returns:
    - A tuple of tuples representing free chains in the goban, sorted by their position from left to right
    and bottom to top.
    """
    all_chains = get_chains(go)
    chains = ()

    # save all chains that are empty
    for chain in all_chains:
        if obtem_pedra(go, chain[0]) == cria_pedra_neutra():
            chains += (chain,)

    return chains


# Return a tuple of different adjacent intersections
def obtem_adjacentes_diferentes(
    go: goban, chain: tuple[intersecao]
) -> tuple[intersecao]:
    new_chain = ()

    # Check each intersection in chain and return only the oposite adjacent intersections. (if player -> non player)
    for inter in chain:
        if eh_pedra_jogador(obtem_pedra(go, inter)):
            for intr in obtem_intersecoes_adjacentes(
                inter, obtem_ultima_intersecao(go)
            ):
                if intr not in new_chain and not eh_pedra_jogador(
                    obtem_pedra(go, intr)
                ):
                    new_chain += (intr,)
        else:
            for intr in obtem_intersecoes_adjacentes(
                inter, obtem_ultima_intersecao(go)
            ):
                if intr not in new_chain and eh_pedra_jogador(obtem_pedra(go, intr)):
                    new_chain += (intr,)

    return ordena_intersecoes(new_chain)


# Return a new goban after a determined play
def jogada(go: goban, inter: intersecao, p: pedra) -> goban:
    go = coloca_pedra(go, inter, p)
    intrs = obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(go))
    chains = ()

    # Get all the chains that are of the different player
    for intr in intrs:
        if (
            eh_pedra_jogador(obtem_pedra(go, intr))
            and (p != obtem_pedra(go, intr))
            and (intr not in chains)
        ):
            chains += (obtem_cadeia(go, intr),)

    # Substitute the trapped chain with empty intersections
    for chain in chains:
        adjacentes = obtem_adjacentes_diferentes(go, chain)
        # Verify if there are any empty adjacent intersections
        if len(adjacentes) == 0:
            for intr in chain:
                go = coloca_pedra(go, intr, cria_pedra_neutra())
    return go


# Return the ammount of white and black stones
def obtem_pedras_jogadores(go: goban) -> tuple[int, int]:
    """
    Returns the ammount of white and black stones in a goban.

    Args:
    - go: A goban, where each element is a line representing a column of the territory.
    Each cell of the column can be either a black, white, or neutral stone.

    Returns:
    - A tuple of integers representing the black and white stones in the territory respectively (white, black)
    and bottom to top.
    """
    # Create the lists of occupied intersections
    all_chains = get_chains(go)
    white_inters = ()
    black_inters = ()

    # save all chains that are empty
    for chain in all_chains:
        if obtem_pedra(go, chain[0]) == cria_pedra_branca():
            white_inters += chain
        elif obtem_pedra(go, chain[0]) == cria_pedra_preta():
            black_inters += chain

    return len(white_inters), len(black_inters)


"""
Game Functions

"""


# Calculate the total points for each player
def calcula_pontos(go: goban) -> tuple[int, int]:
    # Add the occupied intersections points
    inters_points = obtem_pedras_jogadores(go)
    if inters_points == (0, 0):
        return 0, 0
    white_points = inters_points[0]
    black_points = inters_points[1]

    # Check empty territories
    chains = obtem_territorios(go)

    def same_player_chain(chain: tuple[intersecao]) -> bool:
        first_stone = obtem_pedra(go, chain[0])
        for inter in chain:
            # Verify if all stones are from players
            if not eh_pedra_jogador(obtem_pedra(go, inter)):
                return False

            # Verify if all stones in the chain belong to the same player
            if not pedras_iguais(first_stone, obtem_pedra(go, inter)):
                return False

        return True

    for chain in chains:
        inters = obtem_adjacentes_diferentes(go, chain)

        # Add points to white
        if eh_pedra_branca(obtem_pedra(go, inters[0])) and same_player_chain(inters):
            white_points += len(chain)

        # Add points to black
        if eh_pedra_preta(obtem_pedra(go, inters[0])) and same_player_chain(inters):
            black_points += len(chain)

    return white_points, black_points


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


# Return a tuple of all intersection
def get_chains(go: goban) -> tuple[tuple[intersecao]]:
    """
    Returns the all chains in a goban.

    Args:
    - go: A goban, where each element is a line representing a column of the territory.
    Each cell of the column can be either a black, white, or neutral stone.

    Returns:
    - A tuple of tuples representing all the chains in the goban, sorted by their position from left to right
    and bottom to top.
    """
    # Create a list of intersections
    chain = ()
    visited = ()

    size = obtem_lin(obtem_ultima_intersecao(go))
    # Check all the intersections
    for cell in range(size):
        for collumn in range(size):
            # Convert to intercesao (0 -> A) (0 -> 1)
            inter = cria_intersecao(chr(ord("A") + collumn), 1 + cell)

            if inter not in visited:
                temp = obtem_cadeia(go, inter)
                visited += temp
                chain += (temp,)

    return chain
