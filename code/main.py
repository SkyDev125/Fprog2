""" 
Author: 
- Diogo Santos (ist1110262)

Date:
- 03/11/2023 (Três de Novembro de 2023)

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
    """
    Creates an intersecao with the given column and line.

    Args:
    - column: A string representing the column of the intersection.
    - line: An integer representing the line of the intersection.

    Returns:
    - A new Data structure called "intersecao".

    Raises:
    - ValueError: If the given column or line are invalid.
    """
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
    """
    Gets the column of the given intersecao.

    Args:
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.

    Returns:
    - A string representing the column of the intersecao.
    """
    return inter[0]


# Return the line of intersecao
def obtem_lin(inter: intersecao) -> int:
    """
    Gets the line of the given intersecao.

    Args:
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.

    Returns:
    - An integer representing the line of the intersecao.
    """
    return inter[1]


# Verify if the intersecao is valid
def eh_intersecao(inter: any) -> bool:
    """
    Checks if the given intersecao is valid.

    Parameters:
    - inter: Any data type.

    Returns:
    - True if the argument is a valid intersecao, False otherwise.
    """
    # Check if the intersecao is a tuple
    if not isinstance(inter, tuple):
        return False

    # Check if the intersecao is the expected size
    if len(inter) != 2:
        return False

    # Try to create an intersecao with the values and evaluate
    # the situation
    try:
        cria_intersecao(inter[0], inter[1])
        return True
    except (ValueError, TypeError, IndexError):
        return False


# Verify if the intersections are equal
def intersecoes_iguais(inter1: any, inter2: any) -> bool:
    """
    Checks if the given intersections are equal.

    Args:
    - inter1: Any data type.
    - inter2: Any data type.

    Returns:
    - True if the arguments are intersections and equal,
    False otherwise.
    """
    if not eh_intersecao(inter1) or not eh_intersecao(inter2):
        return False

    return inter1 == inter2


# Tranform intersecao in string
def intersecao_para_str(inter: intersecao) -> str:
    """
    Transforms the given intersecao into a string.

    Args:
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.

    Returns:
    - A string representing the intersecao.
    """
    return obtem_col(inter) + str(obtem_lin(inter))


# Transform string into intersecao
def str_para_intersecao(inter: str) -> intersecao:
    """
    Transforms the given string into an intersecao.

    Args:
    - inter: A string representing an intersecao.

    Returns:
    - A new Data structure called "intersecao".
    """
    return cria_intersecao(inter[0], int(inter[1:]))


# Return the adjacent intersections
def obtem_intersecoes_adjacentes(
    inter: intersecao, last_inter: intersecao
) -> tuple[intersecao]:
    """
    Returns the adjacent intersections of the given intersecao based
    on a maximum intersecao.

    Args:
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.
    - last_inter: The top-right-most intersecao (maximum intersecao).

    Returns:
    - A tuple containing the adjacent intersections of the given
    intersecao within the maximum intersecao range.
    """
    collumn, line = convert_intersecao(inter)
    max_collumns, max_lines = (obtem_col(last_inter), obtem_lin(last_inter))
    inter_adjs = ()

    # Add the bottom adjacent intersection
    if line > 0:
        inter_adjs += (
            cria_intersecao(chr(collumn + (ord("A") - 1) + 1), line),
        )

    # Add the left adjacent intersection
    if collumn > 0:
        inter_adjs += (
            cria_intersecao(chr(collumn + (ord("A") - 1)), line + 1),
        )

    # Add the right adjacent intersection
    if collumn + 2 <= ord(max_collumns) - (ord("A") - 1):
        inter_adjs += (
            cria_intersecao(chr(collumn + (ord("A") - 1) + 2), line + 1),
        )

    # Add the top adjacent intersection
    if line + 2 <= max_lines:
        inter_adjs += (
            cria_intersecao(chr(collumn + (ord("A") - 1) + 1), line + 2),
        )

    return inter_adjs


# Order the Intersections by left to right, bottom to top
def ordena_intersecoes(intersecoes: tuple[intersecao]) -> tuple[intersecao]:
    """
    Sorts the intersections by their position from left to right
    and bottom to top.

    Args:
    - intersecoes: A tuple with intersections

    Returns:
    - A tuple of intersections sorted by their position from left to
    right and bottom to top (Alphabetically) then (Numerically).
    """
    # sort based on the number(line), then based on the letter(collumn)
    return tuple(
        sorted(intersecoes, key=lambda x: (obtem_lin(x), obtem_col(x)))
    )


"""
Defining Pedra structure
"""


# Create pedra_branca
def cria_pedra_branca() -> pedra:
    """
    Creates a white pedra.

    Returns:
    - A new Data structure called "pedra" representing a white pedra.
    """
    return 1


# Create pedra_preta
def cria_pedra_preta() -> pedra:
    """
    Creates a black pedra.

    Returns:
    - A new Data structure called "pedra" representing a black pedra.
    """
    return 2


# Create pedra_neutra
def cria_pedra_neutra() -> pedra:
    """
    Creates a neutral pedra.

    Returns:
    - A new Data structure called "pedra" representing a neutral pedra.
    """
    return 0


# Verify if is pedra
def eh_pedra(p: any) -> bool:
    """
    Checks if the given argument is a valid pedra.

    Args:
    - p: Any data type.

    Returns:
    - True if the argument is a valid pedra, False otherwise.
    """
    # Check if pedra is an integer
    if type(p) != int:
        return False

    # Check if pedra is one of the defined values
    return p in (0, 1, 2)


# Verify if pedra is white
def eh_pedra_branca(p: pedra) -> bool:
    """
    Checks if the given pedra is white.

    Args:
    - p: A new Data structure called "pedra" generated by any of the
    cria_pedra functions (branca, preta, neutra).

    Returns:
    - True if the pedra is white, False otherwise.
    """
    return p == 1


# Verify if pedra is black
def eh_pedra_preta(p: pedra) -> bool:
    """
    Checks if the given pedra is black.

    Args:
    - p: A new Data structure called "pedra" generated by any of the
    cria_pedra functions (branca, preta, neutra).

    Returns:
    - True if the pedra is black, False otherwise.
    """
    return p == 2


# Verify if the stones are equal
def pedras_iguais(p1: any, p2: any) -> bool:
    """
    Checks if the given stones are equal.

    Args:
    - p1: Any data type.
    - p2: Any data type.

    Returns:
    - True if the arguments are stones and equal, False otherwise.
    """
    if not eh_pedra(p1) or not eh_pedra(p2):
        return False

    return p1 == p2


# Transform pedra in string
def pedra_para_str(p: pedra) -> str:
    """
    Transforms the given pedra into a string.

    Args:
    - p: A new Data structure called "pedra" generated by any of the
    cria_pedra functions (branca, preta, neutra).

    Returns:
    - A string representing the pedra.
    """
    if eh_pedra_branca(p):
        return "O"
    elif eh_pedra_preta(p):
        return "X"
    else:
        return "."


# Check if pedra belongs to a player
def eh_pedra_jogador(p: pedra) -> bool:
    """
    Checks if the given pedra belongs to a player.

    Args:
    - p: A new Data structure called "pedra" generated by any of the
    cria_pedra functions (branca, preta, neutra).

    Returns:
    - True if the pedra belongs to a player, False otherwise.
    """
    return eh_pedra_branca(p) or eh_pedra_preta(p)


"""
Defining goban structure
"""


# Create empty goban
def cria_goban_vazio(
    size: int,
) -> goban:
    """
    Creates a goban with the given size.

    Args:
    - size: An integer representing the size of the goban.

    Returns:
    - A new Data structure called "goban".

    Raises:
    - ValueError: If the given size is invalid.
    """
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
    """
    Creates a goban with the given size and set values.

    Args:
    - size: An integer representing the size of the goban.
    - brancas: A tuple of intersections representing the white stones.
    - pretas: A tuple of intersections representing the black stones.

    Returns:
    - A new Data structure called "goban".

    Raises:
    - ValueError: If the given size, white stones or black stones
    are invalid.
    """
    # Check if size is valid
    try:
        go = cria_goban_vazio(size)
    except (ValueError, TypeError, IndexError):
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
    """
    Creates a copy of the given goban.

    Args:
    - go: A new Data structure called "goban" generated by any of the
    cria_goban functions.

    Returns:
    - A new Data structure called "goban".
    """
    new_go = cria_goban_vazio(len(go))

    # Copy the goban
    for column in range(len(go)):
        for line in range(len(go)):
            if eh_pedra_branca(go[column][line]):
                coloca_pedra(
                    new_go,
                    cria_intersecao(chr(ord("A") + column), line + 1),
                    cria_pedra_branca(),
                )
            elif eh_pedra_preta(go[column][line]):
                coloca_pedra(
                    new_go,
                    cria_intersecao(chr(ord("A") + column), line + 1),
                    cria_pedra_preta(),
                )

    return new_go


# Return a valid last intersection (top right) based on the territory
def obtem_ultima_intersecao(go: goban) -> intersecao:
    """
    Returns the coordinates of the last intersection (top right) of
    the given goban.

    Args:
    - go: A new Data structure called "goban" generated by any of the
    cria_goban functions.

    Returns:
    - A new Data structure called "intersecao".
    """
    return cria_intersecao(chr((ord("A") - 1) + len(go)), len(go))


# Return the pedra in a given intersecao
def obtem_pedra(go: goban, inter: intersecao) -> pedra:
    """
    Returns the pedra in the given intersecao.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.

    Returns:
    - A new Data structure called "pedra".
    """
    inter = convert_intersecao(inter)
    return go[inter[0]][inter[1]]


# Return the chain of intersections
def obtem_cadeia(go: goban, inter: intersecao) -> tuple[intersecao]:
    """
    Returns a sequence of adjacent intersections that have the same
    value in a goban.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.

    Returns:
    - A tuple of intersections representing a sequence of adjacent
    intersections that have the same value in the goban.
    """
    # Gets the pedra of the intersecao
    stone = obtem_pedra(go, inter)
    visited = []

    # Create recursive function to add the adjacent intersections
    # that are the same pedra
    def recursive_check(go, inter, visited):
        # Add the intersecao to the list
        chain = (inter,)
        visited += chain

        # Check if the adjacent intersections are equal to the pedra
        for intr in obtem_intersecoes_adjacentes(
            inter, obtem_ultima_intersecao(go)
        ):
            if intr not in visited and pedras_iguais(
                obtem_pedra(go, intr), stone
            ):
                chain += recursive_check(go, intr, visited)

        return chain

    # Get the list of intersections
    chain = recursive_check(go, inter, visited)

    return ordena_intersecoes(chain)


# Place a pedra in goban
def coloca_pedra(go: goban, inter: intersecao, p: pedra) -> goban:
    """
    Places a pedra in goban.

    Args:
    - go: A new Data structure called "goban" generated by any
    of the cria_goban functions.
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.
    - p: A new Data structure called "pedra" generated by any of
    the cria_pedra functions
    (branca, preta, neutra).

    Returns:
    - A new Data structure called "goban".
    """
    inter = convert_intersecao(inter)
    go[inter[0]][inter[1]] = p
    return go


# Remove a pedra in goban
def remove_pedra(go: goban, inter: intersecao) -> goban:
    """
    Removes a pedra in goban.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.

    Returns:
    - A new Data structure called "goban".
    """
    inter = convert_intersecao(inter)
    go[inter[0]][inter[1]] = cria_pedra_neutra()
    return go


# Remove a chain of stones in goban
def remove_cadeia(go: goban, chain: tuple[intersecao]) -> goban:
    """
    Removes a chain of stones in goban.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.
    - chain: A tuple of intersections.

    Returns:
    - A new Data structure called "goban".
    """
    for inter in chain:
        remove_pedra(go, inter)
    return go


# Verify if is goban
def eh_goban(go: any) -> bool:
    """
    Checks if the given goban is valid.

    Args:
    - go: Any data type.

    Returns:
    - True if the argument is a valid goban, False otherwise.
    """
    # Check if goban is list and not empty
    if not isinstance(go, list) or len(go) == 0:
        return False

    size = len(go)
    # Check if the goban is empty or larger than expected
    if size not in (9, 13, 19):
        return False

    # Check if the collumns have the same lenght
    for column in go:
        # Check if the arg is a list
        if not isinstance(column, list):
            return False

        # Check if the column is smaller or larger than expected
        if len(column) != size:
            return False

        # Check if the collumn has only stones
        for cell in column:
            # Check if cell is pedra
            if not eh_pedra(cell):
                return False

    return True


# Verify if the intersection is in the territory
def eh_intersecao_valida(go: goban, inter: intersecao) -> bool:
    """
    Verifies if the given intersecao is within the territory of
    the goban.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.

    Returns:
    - True if the intersecao is within the territory of the goban,
    False otherwise.
    """
    last_inter = obtem_ultima_intersecao(go)
    max_collumns, max_lines = obtem_col(last_inter), obtem_lin(last_inter)
    collumn, line = obtem_col(inter), obtem_lin(inter)

    # Check if the collumn is larger than the maximum allowed 
    # for collumns
    if collumn > max_collumns:
        return False

    # Check if the line is larger than the maximum allowed for lines
    return line <= max_lines


# Verify if gobans are equal
def gobans_iguais(go1: goban, go2: goban) -> bool:
    """
    Verifies if the given gobans are equal.

    Args:
    - go1: A new Data structure called "goban" generated by any of
    the cria_goban functions.
    - go2: A new Data structure called "goban" generated by any of
    the cria_goban functions.

    Returns:
    - True if the gobans are equal, False otherwise.
    """
    if not eh_goban(go1) or not eh_goban(go2):
        return False

    # Check if gobans have the same size
    if len(go1) != len(go2):
        return False

    # Check each stone in the goban
    for column in range(len(go1)):
        for line in range(len(go1)):
            if not pedras_iguais(go1[column][line], go2[column][line]):
                return False

    return True


# Return the territory as a string
def goban_para_str(go: goban) -> str:
    """
    Returns a string representation of a goban, where each intersecao
    is represented by an X, O or . depending on whether it is black,
    white or empty, respectively.
    The goban is formatted as a grid with letters representing columns
    and numbers representing rows.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.

    Returns:
    - A string representation of the goban.
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
            " "
            + pedra_para_str(
                obtem_pedra(go, cria_intersecao(chr(ord("A") + p), x))
            )
            for p in range(0, max_columns)
        ]

        # Add the lines to the string dynamically
        if x > 9:
            s += [str(x)] + string_terrain + [" " + str(x) + "\n"]
        else:
            s += [" " + str(x)] + string_terrain + ["  " + str(x) + "\n"]

    # Add a Letters line
    s += ["  "] + [
        " " + chr((ord("A") - 1) + x) for x in range(1, max_columns + 1)
    ]

    # Join the string
    return "".join(s)


# Return a tuple of intersections that are empty
def obtem_territorios(go: goban) -> tuple[tuple[intersecao]]:
    """
    Returns the free chains in a goban (territories).

    Args:
    - go: A new Data structure called "goban" generated by any of the
    cria_goban functions.

    Returns:
    - A tuple of tuples representing free chains in the goban.
    """
    all_chains = get_chains(go)
    chains = ()

    # save all chains that are empty
    for chain in all_chains:
        if pedras_iguais(obtem_pedra(go, chain[0]), cria_pedra_neutra()):
            chains += (chain,)

    return chains


# Return a tuple of different adjacent intersections
def obtem_adjacentes_diferentes(
    go: goban, chain: tuple[intersecao]
) -> tuple[intersecao]:
    """
    Returns a tuple of different adjacent intersections.

    Args:
    - go: A new Data structure called "goban" generated by any of the
    cria_goban functions.
    - chain: A tuple of intersections.

    Returns:
    - A tuple of intersections representing the adjacent intersections
    that are different from the given chain.
    """
    new_chain = ()

    # Check each intersection in chain and return only the oposite
    # adjacent intersections (if player -> non player).
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
                if intr not in new_chain and eh_pedra_jogador(
                    obtem_pedra(go, intr)
                ):
                    new_chain += (intr,)

    return ordena_intersecoes(new_chain)


# Return a new goban after a determined play
def jogada(go: goban, inter: intersecao, p: pedra) -> goban:
    """
    Returns a new goban after a determined play.

    Args:
    - go: A new Data structure called "goban" generated by any of 
    the cria_goban functions.
    - inter: A new Data structure called "intersecao" generated 
    by cria_intersecao.
    - p: A new Data structure called "pedra" generated by any of 
    the cria_pedra functions
    (branca, preta, neutra).

    Returns:
    - A new Data structure called "goban".
    """
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
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.

    Returns:
    - A tuple of integers representing the black and white stones in
    the territory respectively (white, black).
    """
    # Create the lists of occupied intersections
    all_chains = get_chains(go)
    white_inters = ()
    black_inters = ()

    # save all chains that are empty
    for chain in all_chains:
        if pedras_iguais(obtem_pedra(go, chain[0]), cria_pedra_branca()):
            white_inters += chain
        elif pedras_iguais(obtem_pedra(go, chain[0]), cria_pedra_preta()):
            black_inters += chain

    return len(white_inters), len(black_inters)


"""
Game Functions

"""


# Calculate the total points for each player
def calcula_pontos(go: goban) -> tuple[int, int]:
    """
    Calculates the total points for each player.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.

    Returns:
    - A tuple of integers representing the black and white points
    respectively (white, black).
    """
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

            # Verify if all stones in the chain belong to the 
            # same player
            if not pedras_iguais(first_stone, obtem_pedra(go, inter)):
                return False

        return True

    for chain in chains:
        inters = obtem_adjacentes_diferentes(go, chain)

        # Add points to white
        if eh_pedra_branca(obtem_pedra(go, inters[0])) and same_player_chain(
            inters
        ):
            white_points += len(chain)

        # Add points to black
        if eh_pedra_preta(obtem_pedra(go, inters[0])) and same_player_chain(
            inters
        ):
            black_points += len(chain)

    return white_points, black_points


# Verify if the play is valid
def eh_jogada_legal(
    go: goban, inter: intersecao, p: pedra, prev_go: goban
) -> bool:
    """
    Verifies if the given play is valid.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.
    - p: A new Data structure called "pedra" generated by any of
    the cria_pedra functions (branca, preta, neutra).
    - prev_go: A new Data structure called "goban" generated by any of
    the cria_goban functions (Has to be the previous state of the game
    before the given goban).

    Returns:
    - True if the play is valid, False otherwise.
    """
    # Avoid Changing the goban by creating a copy
    go_copy = cria_copia_goban(go)

    # Verify if the intersecao is valid
    if not eh_intersecao_valida(go_copy, inter):
        return False

    # Verify if intersecao isnt occupied already
    if obtem_pedra(go_copy, inter) != cria_pedra_neutra():
        return False

    # Do the play
    jogada(go_copy, inter, p)

    # Verify if the play is repeated (ko rule)
    if gobans_iguais(go_copy, prev_go):
        return False

    # Verify if the play is suicidal
    inters = obtem_intersecoes_adjacentes(
        inter, obtem_ultima_intersecao(go_copy)
    )

    for intr in inters:
        if not eh_pedra_jogador(obtem_pedra(go_copy, intr)):
            return True

        if (
            pedras_iguais(obtem_pedra(go_copy, intr), p)
            and len(
                obtem_adjacentes_diferentes(
                    go_copy, obtem_cadeia(go_copy, intr)
                )
            )
            != 0
        ):
            return True

    return False


# Play a round of the game
def turno_jogador(go: goban, p: pedra, prev_go: goban) -> bool:
    """
    Plays a round of the game.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.
    - p: A new Data structure called "pedra" generated by any of
    the cria_pedra functions (branca, preta, neutra).
    - prev_go: A new Data structure called "goban" generated by any of
    the cria_goban functions (Has to be the previous state of the game
    before the given goban).

    Returns:
    - False if the player passed, True otherwise.
    """
    while True:
        # Get the input from the player
        play = input(
            "Escreva uma intersecao ou 'P' para passar ["
            + pedra_para_str(p)
            + "]:"
        )

        # Return if the player wants to pass
        if play == "P":
            return False

        # Try to create a intersecao with the input, reset if it
        # doesnt work
        try:
            inter = str_para_intersecao(play)
        except (ValueError, TypeError, IndexError):
            continue

        # Verify if the play is valid
        if not eh_jogada_legal(go, inter, p, prev_go):
            continue

        # Play the game and return
        jogada(go, inter, p)
        return True


# Main Game Function
def go(
    size: int, brancas: tuple[intersecao], pretas: tuple[intersecao]
) -> bool:
    """
    Plays a game of Go.

    Args:
    - size: An integer representing the size of the goban.
    - brancas: A tuple of intersections representing the white stones.
    - pretas: A tuple of intersections representing the black stones.

    Returns:
    - True if the white player won, False otherwise.

    Raises:
    - ValueError: If the given size, white stones or black stones
    are invalid.
    """
    # Verify if brancas or pretas are tuples
    if not isinstance(brancas, tuple) or not isinstance(pretas, tuple):
        raise ValueError("go: argumentos invalidos")

    # Verify the white intersections
    temp = ()
    for intr in brancas:
        if not eh_intersecao(intr):
            try:
                temp += (str_para_intersecao(intr),)
            except (ValueError, TypeError, IndexError):
                raise ValueError("go: argumentos invalidos")
        else:
            temp += (intr,)

    brancas = temp

    # Verify the black intersections
    temp = ()
    for intr in pretas:
        if not eh_intersecao(intr):
            try:
                temp += (str_para_intersecao(intr),)
            except (ValueError, TypeError, IndexError):
                raise ValueError("go: argumentos invalidos")
        else:
            temp += (intr,)

    pretas = temp

    # Try to create the goban
    try:
        go = cria_goban(size, brancas, pretas)
    except (ValueError, TypeError, IndexError):
        raise ValueError("go: argumentos invalidos")

    prev_go = cria_copia_goban(go)

    # Time to play the game
    switcher = False
    game_end = False
    while True:
        white_points, black_points = calcula_pontos(go)
        print("Branco (O) tem " + str(white_points) + " pontos")
        print("Preto (X) tem " + str(black_points) + " pontos")
        print(goban_para_str(go))

        temp_go = cria_copia_goban(go)

        # Play and switch player
        if switcher:
            temp = not turno_jogador(go, cria_pedra_branca(), prev_go)
            switcher = False
        else:
            temp = not turno_jogador(go, cria_pedra_preta(), prev_go)
            switcher = True

        prev_go = temp_go

        # Check if the game is over
        if temp and game_end:
            break
        else:
            game_end = temp

    print("Branco (O) tem " + str(white_points) + " pontos")
    print("Preto (X) tem " + str(black_points) + " pontos")
    print(goban_para_str(go))

    return white_points >= black_points


"""
Auxiliary Functions

"""


# Return the intersecao in usable values for coding (A -> 0) (1 -> 0)
def convert_intersecao(inter: intersecao) -> tuple[int, int]:
    """
    Converts the intersecao coordinates to usable values
    (A -> 0) (1 -> 0).

    Args:
    - inter: A new Data structure called "intersecao" generated
    by cria_intersecao.

    Returns:
    - A tuple of integers representing the intersecao coordinates.
    """
    collumn, line = obtem_col(inter), obtem_lin(inter)
    return (ord(collumn) - (ord("A") - 1) - 1, line - 1)


# Return a tuple of all intersection
def get_chains(go: goban) -> tuple[tuple[intersecao]]:
    """
    Returns all chains in a goban.

    Args:
    - go: A new Data structure called "goban" generated by any of
    the cria_goban functions.

    Returns:
    - A tuple of tuples representing all the chains in the goban.
    """
    # Create a list of intersections
    chain = ()
    visited = ()

    size = obtem_lin(obtem_ultima_intersecao(go))
    # Check all the intersections
    for line in range(size):
        for collumn in range(size):
            # Convert to intercesao (0 -> A) (0 -> 1)
            inter = cria_intersecao(chr(ord("A") + collumn), 1 + line)

            if inter not in visited:
                temp = obtem_cadeia(go, inter)
                visited += temp
                chain += (temp,)

    return chain
