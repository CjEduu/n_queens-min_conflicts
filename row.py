"""We'll be choosing rows instead of columns as an arbitrary choice, they can be swapped in their roles of variables and domain"""

class Row():
    queen_in:int
    conflict_values:list[int] # rows of the table in which a queen could be placed
    def __init__(self,queen:int,size:int,*args, **kwargs):
        self.queen_in = queen
        self.conflict_values = [0 for i in range(size)]
    
    def new_queen_value(self,new_queen:int) -> None:
        self.queen_in = new_queen
        
    def __repr__(self) -> str:
        queen = f" QUEEN = {self.queen_in} "
        values = f" VALUES = {self.conflict_values} "
        return queen + values