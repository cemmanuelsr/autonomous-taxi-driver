from Graph import Node

def sortFunction(val):
    return val[1]

class SearchAlgorithm:
    def search(self):
        pass

class BuscaGananciosa (SearchAlgorithm):

    def search (self, initialState):
        open = []
        new_n = Node(initialState, None)
        open.append((new_n, new_n.h()))
        while (len(open) > 0):
            open.sort(key = sortFunction, reverse = True)
            n = open.pop()[0]
            print('-----------------------')
            print(n.state.taxi.row, n.state.taxi.col, n.state.operator, n.state.passenger_on_taxi, n.state.h())
            if (n.state.is_goal()):
                return n
            for i in n.state.sucessors():
                new_n = Node(i,n)
                open.append((new_n, new_n.h()))
        return None

class AEstrela (SearchAlgorithm):

    def search (self, initialState):
        states = []
        open = []
        new_n = Node(initialState, None)
        open.append((new_n, new_n.f()))
        while (len(open) > 0):
            open.sort(key = sortFunction, reverse = True)
            n = open.pop()[0]

            if (n.state.is_goal()):
                return n
            for i in n.state.sucessors():
                new_n = Node(i,n)
                if (new_n.state.env() not in states):
                    open.append((new_n,new_n.f()))
                    states.append(new_n.state.env())
        return None
