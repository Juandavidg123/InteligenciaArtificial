import search4e

class problema(search4e.Problem):
    def __init__(self, initial=tuple, goal=tuple, **kwds):
        super().__init__(initial, goal, **kwds)

    def actions(self, state):
        acciones = []

        # Mover dos misioneros hacia la derecha
        if state[0] > 1:
            nuevoEstado = list(state)
            nuevoEstado[0] -= 2
            nuevoEstado[2] += 2
            nuevoEstado[4] = 1
            acciones.append(tuple(nuevoEstado))
        
        # Mover un misionero hacia la derecha
        if state[0] > 0:
            nuevoEstado = list(state)
            nuevoEstado[0] -= 1
            nuevoEstado[2] += 1
            nuevoEstado[4] = 1
            acciones.append(tuple(nuevoEstado))
        
        # Mover dos misioneros hacia la izquierda
        if state[2] > 1:
            nuevoEstado = list(state)
            nuevoEstado[2] -= 2
            nuevoEstado[0] += 2
            nuevoEstado[4] = 0
            acciones.append(tuple(nuevoEstado))
        
        # Mover un misionero hacia la izquierda
        if state[2] > 0:
            nuevoEstado = list(state)
            nuevoEstado[2] -= 1
            nuevoEstado[0] += 1
            nuevoEstado[4] = 0
            acciones.append(tuple(nuevoEstado))
        
        # Mover dos canibales hacia la derecha
        if state[1] > 1:
            nuevoEstado = list(state)
            nuevoEstado[1] -= 2
            nuevoEstado[3] += 2
            nuevoEstado[4] = 1
            acciones.append(tuple(nuevoEstado))
        
        # Mover un canibal hacia la derecha
        if state[1] > 0:
            nuevoEstado = list(state)
            nuevoEstado[1] -= 1
            nuevoEstado[3] += 1
            nuevoEstado[4] = 1
            acciones.append(tuple(nuevoEstado))

        # Mover dos canibales hacia la izquierda
        if state[3] > 1:
            nuevoEstado = list(state)
            nuevoEstado[3] -= 2
            nuevoEstado[1] += 2
            nuevoEstado[4] = 0
            acciones.append(tuple(nuevoEstado))
        
        # Mover un canibal hacia la izquierda
        if state[3] > 0:
            nuevoEstado = list(state)
            nuevoEstado[3] -= 1
            nuevoEstado[1] += 1
            nuevoEstado[4] = 0
            acciones.append(tuple(nuevoEstado))
        
        #Mover un misionero y un canibal hacia la derecha
        if state[0] > 0 and state[1] > 0:
            nuevoEstado = list(state)
            nuevoEstado[0] -= 1
            nuevoEstado[1] -= 1
            nuevoEstado[2] += 1
            nuevoEstado[3] += 1
            nuevoEstado[4] = 1
            acciones.append(tuple(nuevoEstado))

        #Mover un misionero y un canibal hacia la izquierda
        if state[2] > 0 and state[3] > 0:
            nuevoEstado = list(state)
            nuevoEstado[0] += 1
            nuevoEstado[1] += 1
            nuevoEstado[2] -= 1
            nuevoEstado[3] -= 1
            nuevoEstado[4] = 0
            acciones.append(tuple(nuevoEstado))
        
        return acciones

    def result(self, state, action):

        # Restriccion misioneros < canibales
        if state[0] < state[1] and state[0] > 0:
            return state

        # Restriccion del barco
        if action[4] == state[4]:
            return state
        else:
            return action
        

    def h(self, node):
        return node.state[0] + node.state[1]

    #Metodos de visualizacion:
    def visualize_node(node):
        print("Estado:", node.state)
        print("Accion:", node.action)
        print("Costo:", node.path_cost)
        print()


    def expand_and_visualize(self,problem, node):
        nodo = node.state
        for action in problem.actions(nodo):
            nodo1 = problem.result(nodo, action)
            cost = node.path_cost + problem.action_cost(nodo, action, nodo1)
            nuevoNodo = search4e.Node(nodo1, node, action, cost)
            self.visualize_node(nuevoNodo)
            yield nuevoNodo

    def visualize_path_states(node):
        estados = search4e.path_states(node)
        print("Secuencia de estados:")
        for estado in estados:
            print(estado)

p0 = problema((1,1,0,0,0), (0,0,1,1,1))    
p1 = problema((2,2,0,0,0), (0,0,2,2,1))
p2 = problema((3,3,0,0,0), (0,0,3,3,1))
p3 = problema((4,4,0,0,0), (0,0,4,4,1))
p4 = problema((5,5,0,0,0), (0,0,5,5,1))

search4e.report((search4e.depth_first_bfs, search4e.breadth_first_bfs, search4e.uniform_cost_search, search4e.iterative_deepening_search, search4e.greedy_bfs, search4e.astar_search), (p0,p1,p2,p3,p4))

solucion = search4e.astar_search(p3)
print(f"\n Solución: {solucion}\n")

problema.visualize_path_states(solucion)