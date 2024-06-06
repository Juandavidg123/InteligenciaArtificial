import sys

# Definir las direcciones disponibles
direcciones = ["0", "1", "2", "3", "4", "5", "6", "7"]
posicionBalon = [0, 0]

# Lista para almacenar los movimientos y posiciones del balón
movimientos = []

# To score a goal!
my_id = int(input())

# game loop
while True:
    opponent_move_length = int(input())
    opponent_move = input()  # Your opponent's last move (or '-' if you are first player and this is first turn)

    # Si es el primer movimiento, no hay movimiento previo del oponente
    if opponent_move == '-':
        opponent_move = ''

    # Registrar el movimiento del oponente
    if opponent_move:
        for move in opponent_move:
            movimientos.append(posicionBalon.copy())
            if move == '0':
                posicionBalon[1] -= 1
            elif move == '1':
                posicionBalon[0] += 1
                posicionBalon[1] -= 1
            elif move == '2':
                posicionBalon[0] += 1
            elif move == '3':
                posicionBalon[0] += 1
                posicionBalon[1] += 1
            elif move == '4':
                posicionBalon[1] += 1
            elif move == '5':
                posicionBalon[0] -= 1
                posicionBalon[1] += 1
            elif move == '6':
                posicionBalon[0] -= 1
            elif move == '7':
                posicionBalon[0] -= 1
                posicionBalon[1] -= 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your move
    # Aquí debes implementar tu lógica para decidir el próximo movimiento
    # Por ahora, simplemente imprimir un movimiento de ejemplo (moviendo hacia arriba)
    print(movimientos)
    next_move = "0"
    movimientos.append(posicionBalon.copy())  # Registrar el propio movimiento
    print(next_move)
