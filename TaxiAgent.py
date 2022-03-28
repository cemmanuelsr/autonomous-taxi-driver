from Graph import State
from algorithms import AEstrela, BuscaGananciosa
from utils import *

class TaxiAgent(State):

    def __init__(self, desc, decode, operator=-1):
        self.desc = desc
        self.operator = operator

        taxi_row, taxi_col, pass_idx, dest_idx = decode

        self.passenger_on_taxi = (pass_idx == 4)

        self.taxi = Taxi(row=taxi_row, col=taxi_col)

        if(pass_idx == 4):
            pass_row, pass_col = taxi_row, taxi_col
        else:
            pass_row, pass_col = find_row_col(desc, pass_idx)
        
        self.passenger = Passenger(row=pass_row, col=pass_col, idx=pass_idx)

        dest_row, dest_col = find_row_col(desc, dest_idx)
        self.destiny = Destiny(row=dest_row, col=dest_col, idx=dest_idx)
    
    def sucessors(self):
        sucessors = []

        if(self.passenger_on_taxi):
            if(self.taxi.row == self.destiny.row and self.taxi.col == self.destiny.col):
                decode = (self.taxi.row, self.taxi.col, self.destiny.idx, self.destiny.idx)
                sucessors.append( TaxiAgent(self.desc, decode, operator=5) )
                return sucessors
        else:
            if(self.taxi.row == self.passenger.row and self.taxi.col == self.passenger.col):
                decode = (self.taxi.row, self.taxi.col, 4, self.destiny.idx)
                sucessors.append( TaxiAgent(self.desc, decode, operator=4) )
                return sucessors

        for move, operator in MOVE_ACTION_MAP.items():
            if(operator != FORBIDDEN_OPERATION[self.operator]):
                row_offset, col_offset = move
                if (operator in [0, 1] and 0 <= self.taxi.row + row_offset <= 4):
                    decode = (self.taxi.row + row_offset, self.taxi.col, self.passenger.idx, self.destiny.idx)
                    sucessors.append( TaxiAgent(self.desc, decode, operator=operator) )
                if(operator in [2, 3] and 0 <= self.taxi.col + col_offset <= 4):
                    decode = (self.taxi.row, self.taxi.col + col_offset, self.passenger.idx, self.destiny.idx)
                    sucessors.append( TaxiAgent(self.desc, decode, operator=operator) )

        return sucessors
    
    def is_goal(self):
        return self.passenger.idx == self.destiny.idx
    
    def description(self):
        return "Implementar um taxi driver que é capaz de definir uma sequência de atividades para pegar um passageiro em um lugar e deixá-lo em outro lugar"
    
    def cost(self):
        return 1

    def h(self):
        if(self.passenger_on_taxi):
            return euclidian_distance(self.taxi, self.destiny)
        else:
            return euclidian_distance(self.taxi, self.passenger)

    def print(self):
        return self.desc
    
    def env(self):
        return (self.desc, self.taxi.row, self.taxi.col, self.passenger.idx, self.destiny.idx)


class TaxiSolver:

    def __init__(self, desc, decode):
        self.agent = TaxiAgent(desc, decode)

    def path(self, algorithm=AEstrela()):    
        result = algorithm.search(self.agent)
        return result.path()

