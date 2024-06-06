import search4e

class problema(search4e.Problem):   
    
    def __init__(self, initial=None, goal=(1,2,3,4,5,6,7,8,9), **kwds):
        super().__init__(initial, goal, **kwds)


    def actions(self, state):
        acciones = []
        ind = state.index(1) 
        row = ind // 3
        col = ind % 3
        
        # Izquierda
        if col > 0:
            nuevoEstado = list(state)
            nuevoEstado[ind], nuevoEstado[ind - 1] = nuevoEstado[ind - 1], nuevoEstado[ind]
            acciones.append(tuple(nuevoEstado))

        # Derecha
        if col < 2:
            nuevoEstado = list(state)
            nuevoEstado[ind], nuevoEstado[ind + 1] = nuevoEstado[ind + 1], nuevoEstado[ind]
            acciones.append(tuple(nuevoEstado))

        # Arriba
        if row > 0:
            nuevoEstado = list(state)
            nuevoEstado[ind], nuevoEstado[ind - 3] = nuevoEstado[ind - 3], nuevoEstado[ind]
            acciones.append(tuple(nuevoEstado))

        # Abajo
        if row < 2:
            nuevoEstado = list(state)
            nuevoEstado[ind], nuevoEstado[ind + 3] = nuevoEstado[ind + 3], nuevoEstado[ind]
            acciones.append(tuple(nuevoEstado))
        
        return acciones
    
    def result(self, state, action):
        def path_states(state):
            if state in (search4e.cutoff, search4e.failure, None): 
                return []
            return path_states(state.parent) + [state.state]
        
        return action
    
    def h(self, node):
        suma = sum(
            ci != cf
            for ci, cf in zip(node.state, self.goal)
        )
        return suma
    
    def f(self, node):
        return node.path_cost + self.h(node)


#print(search4e.report([search4e.depth_first_bfs],[problema((3,1,8,4,6,5,7,9,2))]))
#print(search4e.report([search4e.depth_first_bfs],[problema((9,8,7,6,5,4,3,2,1))]))
#print(search4e.report([search4e.depth_first_bfs],[problema((8,1,9,5,2,3,4,6,7))]))


#print(search4e.report([search4e.best_first_search],[problema((3,1,8,4,6,5,7,9,2))]))
#print(search4e.report([search4e.best_first_search],[problema((9,8,7,6,5,4,3,2,1))]))
#print(search4e.report([search4e.best_first_search],[problema((8,1,9,5,2,3,4,6,7))]))

#print("iterative_deepening_search")
#print(search4e.report([search4e.iterative_deepening_search],[problema((3,1,8,4,6,5,7,9,2))]))
#print(search4e.report([search4e.iterative_deepening_search],[problema((9,8,7,6,5,4,3,2,1))]))
#print(search4e.report([search4e.iterative_deepening_search],[problema((8,1,9,5,2,3,4,6,7))]))


#print("uniform_cost_search")
#print(search4e.report([search4e.uniform_cost_search],[problema((3,1,8,4,6,5,7,9,2))]))
#print(search4e.report([search4e.uniform_cost_search],[problema((9,8,7,6,5,4,3,2,1))]))
#print(search4e.report([search4e.uniform_cost_search],[problema((8,1,9,5,2,3,4,6,7))]))


#print("greedy_bfs")
print(search4e.report([search4e.greedy_bfs],[problema((3,1,8,4,6,5,7,9,2))]))
#print(search4e.report([search4e.greedy_bfs],[problema((9,8,7,6,5,4,3,2,1))]))
#print(search4e.report([search4e.greedy_bfs],[problema((8,1,9,5,2,3,4,6,7))]))


#print("astar_search")
#print(search4e.report([search4e.astar_search],[problema((3,1,8,4,6,5,7,9,2))]))
#print(search4e.report([search4e.astar_search],[problema((9,8,7,6,5,4,3,2,1))]))
#print(search4e.report([search4e.astar_search],[problema((8,1,9,5,2,3,4,6,7))]))
