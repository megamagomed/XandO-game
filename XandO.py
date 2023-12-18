from tkinter import Canvas, Tk
from time import sleep

root =Tk()
canv_size = 600
canvas = Canvas(root, width=canv_size, height=canv_size)
canvas.pack()


class Field:
    def __init__(self, field_size, numbers_of_rows):
        self.field_size = field_size
        self.numbers_of_rows = numbers_of_rows
        self.cell_size = self.field_size // self.numbers_of_rows
        self.count = 0
        self.list_of_occupied_cells = []
        self.list_of_x = []
        self.list_of_0 = []
        self.list_of_figures = []
        self.current_player = 'x'
        self.count_of_figures = 0

    def made_field(self):
        for i in range(self.numbers_of_rows-1):
            canvas.create_line(0, self.cell_size*(i+1), self.field_size,self.cell_size*(i+1), fill='blue')
            canvas.create_line(self.cell_size*(i+1), 0, self.cell_size*(i+1), self.field_size, fill='blue')

    def made_cross(self, x, y):
        canvas.create_line(x, y, x+self.cell_size, y+self.cell_size, fill='red', width=3)
        canvas.create_line(x, y+self.cell_size, x+self.cell_size, y, fill='red', width=3)
        self.count +=1

    def made_zero(self, x, y):
        canvas.create_oval(x+10, y+10, x+self.cell_size-10, y+self.cell_size-10, outline = 'green', width = 3)
        self.count +=1
    
    def click_event(self, event):
        self.count_of_figures +=1
        cell_coordinates = self.change_coords(event.x, event.y)
        if cell_coordinates not in self.list_of_occupied_cells:
            self.list_of_occupied_cells.append(cell_coordinates)
            if self.current_player == 'x':
                self.made_cross(int(cell_coordinates[1])*self.cell_size, int(cell_coordinates[0])*self.cell_size )
                self.list_of_x.append(cell_coordinates)
                self.list_of_figures = self.list_of_x
        
            else :
                self.made_zero(int(cell_coordinates[1])*self.cell_size, int(cell_coordinates[0])*self.cell_size )
                self.list_of_0.append(cell_coordinates) 
                self.list_of_figures = self.list_of_0
               
            self.check_winner(self.list_of_figures)    
            self.change_player()

    def change_player(self):
        if self.current_player =='x':
            self.current_player = 'o'
        else:
            self.current_player = 'x'


    def change_coords(self,x,y):
        row = y//self.cell_size
        column = x//self.cell_size
        return row,column
    
    def check_winner(self, list_of_cells):
        count_row = 0
        count_column = 0
        count_diagonal1 = 0
        count_diagonal2 = 0
        win = False
        list_of_win_coordinates = []
        if len(list_of_cells)>=self.numbers_of_rows:
            for i in range(self.numbers_of_rows):
                for j in list_of_cells:
                    if  j[0] ==i:
                        count_row +=1
                        if count_row == self.numbers_of_rows:
                            list_of_win_coordinates.append('row')
                            list_of_win_coordinates.append(j[0])
                            print(list_of_win_coordinates)
                            win = True
                    if j[1] ==i:
                        count_column +=1
                        if count_column == self.numbers_of_rows:
                            list_of_win_coordinates.append('column')
                            list_of_win_coordinates.append(j[1])
                            print(list_of_win_coordinates)
                            win = True
                count_row = 0
                count_column = 0

            for j in list_of_cells:    
                if j[0]==j[1]:
                    count_diagonal1 +=1
                    if count_diagonal1 == self.numbers_of_rows:
                        win = True
                        list_of_win_coordinates.append('LRdiag')   
                        print(list_of_win_coordinates)
            count_diagonal1 = 0 
        
            for i in range(self.numbers_of_rows):
                if (i,self.numbers_of_rows-1-i) in list_of_cells:
                    count_diagonal2 +=1
                if count_diagonal2 == self.numbers_of_rows:
                    list_of_win_coordinates.append('RLdiag')
                    print(list_of_win_coordinates)
                    win = True
            count_diagonal2 = 0
        if win:
            self.finish_game(win, list_of_win_coordinates)
        if self.count_of_figures == self.numbers_of_rows*self.numbers_of_rows:
            self.finish_game(False)
        
    def finish_game(self, win_or_draw, win_coordinates = None):
        if win_or_draw == True:
            if win_coordinates[0] == "LRdiag":
                canvas.create_line(0,0, canv_size, canv_size, fill='yellow', width=5)
            if win_coordinates[0] == "RLdiag":
                canvas.create_line(0,canv_size, canv_size, 0, fill='yellow', width=5)
            if win_coordinates[0] == "row":
                canvas.create_line(0,self.cell_size/2+self.cell_size*win_coordinates[1], canv_size, self.cell_size/2+self.cell_size*win_coordinates[1], fill='yellow', width=5)
            if win_coordinates[0] == "column":
                canvas.create_line(self.cell_size/2+self.cell_size*win_coordinates[1],0, self.cell_size/2+self.cell_size*win_coordinates[1], canv_size, fill='yellow', width=5)
        if win_or_draw == False:
            print('НИЧЬЯ')
        canvas.unbind('<Button-1>')

       
                    

number_of_rows = 3
field = Field(canv_size, number_of_rows)
field.made_field()
canvas.bind('<Button-1>', field.click_event)



root.mainloop()