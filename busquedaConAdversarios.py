from games import Game, play_game, alphabeta_search, random_player, human_player
import math

class Posicion:
    def __init__(self, n):
        self.n = n
        self.tablero = [0, n - 1]
        self.to_move = 'A'
        self.nodosVisitados = []

    def move(self, jugador, move):
        jugadorInicial = 0 if jugador == 'A' else 1
        self.tablero[jugadorInicial] = move
        self.nodosVisitados.append(tuple(self.tablero))

    def __str__(self):
        return f"Posicion: {self.tablero}, Juega: {self.to_move}"

class LinearBoardGame(Game):
    def __init__(self, n):
        self.n = n
        self.initial = Posicion(n)

    def actions(self, state):
        acciones = []
        # Jugador A es 0, Jugador B es 1
        jugador = 0 if state.to_move == 'A' else 1
        #EL Jugador A avanza hacia la derecha y retrocede hacia la izquierda, por esto se define la dirección como [1, -1], el jugador B avanza hacia la izquierda y retrocede hacia la derecha, por esto se define la dirección como [-1, 1]
        direccion = [1, -1] if state.to_move == 'A' else [-1, 1]
        oponente = 1 - jugador

        # Avanzar
        nuevoEstadoAvanzar = state.tablero[jugador] + direccion[0]
        if 0 <= nuevoEstadoAvanzar < self.n and nuevoEstadoAvanzar != state.tablero[oponente]:
            acciones.append(nuevoEstadoAvanzar)

        # Retroceder
        nuevoEstadoRetroceder = state.tablero[jugador] + direccion[1]
        if 0 <= nuevoEstadoRetroceder < self.n and nuevoEstadoRetroceder != state.tablero[oponente]:
            acciones.append(nuevoEstadoRetroceder)

        # SaltarAdelante
        saltoAdelante = state.tablero[jugador] + 2 * direccion[0]
        if 0 <= saltoAdelante < self.n and state.tablero[oponente] == state.tablero[jugador] + direccion[0]:
            acciones.append(saltoAdelante)
        
        # SaltarAtras
        saltoAtras = state.tablero[jugador] + 2 * direccion[1]
        if 0 <= saltoAtras < self.n and state.tablero[oponente] == state.tablero[jugador] + direccion[1]:
            acciones.append(saltoAtras)
        
        return acciones

    def result(self, state, move):
        nuevoEstado = state
        nuevoEstado.move(state.to_move, move)
        nuevoEstado.to_move = 'B' if state.to_move == 'A' else 'A'
        return nuevoEstado

    def is_terminal(self, state):
        if state.tablero[0] == self.n - 1 or state.tablero[1] == 0:
            return True
        if state.nodosVisitados.count(tuple(state.tablero)) > 1:
            return True
        if self.n <= 2:
            return True
        return False

    def utility(self, state, jugador):
        if state.tablero[0] == self.n - 1:
            return 1 if jugador == 'A' else -1
        if state.tablero[1] == 0:
            return 1 if jugador == 'B' else -1
        if state.nodosVisitados.count(tuple(state.tablero)) > 1:
            return 0
        return 0
    

    def funcion_evalucion(self, state):
        return 1 if state.tablero[0] == self.n - 1 else -1 if state.tablero[1] == 0 else 0
    
def alphabeta_search(game, state):

    def max_value(state, alpha, beta):
        if game.is_terminal(state):
            return LinearBoardGame.funcion_evalucion(state,state), None
        v, move = -math.inf, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    def min_value(state, alpha, beta):
        if game.is_terminal(state):
            return LinearBoardGame.funcion_evalucion(state,state), None
        v, move = +math.inf, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return max_value(state, -math.inf, +math.inf)


if __name__ == "__main__":
    game = LinearBoardGame(10)
    strategies = {'A': random_player, 'B': random_player}
    final_position = play_game(game, strategies, verbose=True)
    print("Final position:", final_position)
