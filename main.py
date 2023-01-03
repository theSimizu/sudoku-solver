import os
from time import sleep
from datetime import datetime



class Sudoku:
    def __init__(self) -> None:
        self.cells = []
        self._new_cells()
        self.matrix = [[0 for _ in range(9)] for _ in range(9)]
    
    def _new_cells(self):
        for x in range(9):
            for y in range(9):
                cell = {'value': 0, 
                        'x_axis': x,
                        'y_axis': y,
                        'block': 3*(x//3) + y//3,
                        'possible_values': set(x for x in range(1, 10))}
                self.cells.append(cell)
                # print(cell)
    
    def matrix_map(self):
        last = None
        for cell in self.cells:
            if cell['x_axis'] == last:
                print(f'{cell["value"]}', end='|')
            else:
                print('\n+-+-+-+-+-+-+-+-+-+')
                print(f'|{cell["value"]}', end='|')
            last = cell['x_axis']
        print('\n+-+-+-+-+-+-+-+-+-+')

    def is_valid(self, cell):
        if cell['value'] == 0 or cell['value'] > 9: return False
        x_axis, y_axis, block, value = cell['x_axis'], cell['y_axis'], cell['block'], cell['value']
        for item in self.cells:
            if item == cell: continue
            if (item['x_axis'] == x_axis or item['y_axis'] == y_axis or item['block'] == block) and item['value'] == value:
                return False
        return True

            

    def back_track(self):
        x_axis = 0
        y_axis = 0
        while True:
            for index, cell in enumerate(self.cells):
                if cell['x_axis'] == x_axis and cell['y_axis'] == y_axis:
                    while True:
                        self.cells[index]['value'] += 1
                        if self.is_valid(self.cells[index]): break

                        if self.cells[index]['value'] > 9:
                            self.cells[index]['value'] = 0
                            if x_axis > 0:
                                x_axis -= 1
                            else:
                                x_axis = 8
                                y_axis -= 1
                            break
                        

                    if self.cells[index]['value'] == 0:
                        break

                    if x_axis < 8:
                        x_axis += 1
                    else:
                        x_axis = 0
                        y_axis += 1
                    break
            os.system('clear')
            

            self.matrix_map()
            if self.is_valid(self.cells[-1]):
                break



                        

                        




if __name__ == '__main__':
    # start = datetime.utcnow().second
    sudoku = Sudoku()
    sudoku.back_track()
    # print(datetime.utcnow().second - start)
    # sudoku._new_cells()

    # print(sudoku.matrix)









# quit()
# for x in range(9):
#     for y in range(9):
#         if matrix[x][y] == 0:
#             for i in range(1, 10):
#                 if verify_conditions(matrix, f'{x}{y}', i):
#                     matrix[x][y] = i
#                     break
            
                
            



# for line in matrix:
#     print(line)

