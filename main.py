from random import random
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import time

class justGetTen:
    
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__board = self.newBoard()
        self.__tailleCarre = 50
        self.__score = 0
        
        self.__root = Tk()
        self.__root.title("Just Get Ten")
        self.__root.config(bg="deepskyblue")
        self.__font1 = tkFont.Font(family="Helvetica", size=24, weight="bold")
        self.__font2 = tkFont.Font(family="Helvetica", size=16, weight="bold")
        
        ###############################################################################################
        
        self.__frame1 = Frame(self.__root, background="deepskyblue")
        self.__frame1.grid(row=0, column=0)
        
        self.__button4x4 = Button(self.__frame1, text='4x4', command=lambda: self.boardGrid(4, 100), highlightbackground="deepskyblue")
        self.__button4x4.pack(pady=self.__tailleCarre/2, padx=self.__tailleCarre/2)
        
        ################################################################################################
        
        self.__frame2 = Frame(self.__root, background="deepskyblue")
        self.__frame2.grid(row=0, column=1)
        
        self.__button5x5 = Button(self.__frame2, text='5x5', command=lambda: self.boardGrid(5, 80), highlightbackground="deepskyblue")
        self.__button5x5.pack(pady=self.__tailleCarre/2, padx=self.__tailleCarre/2)
        
        ##################################################################################################
        
        self.__frame3 = Frame(self.__root, background="deepskyblue")
        self.__frame3.grid(row=0, column=2)
        
        self.__button6x6 = Button(self.__frame3, text='6x6', command=lambda: self.boardGrid(6, 66), highlightbackground="deepskyblue")
        self.__button6x6.pack(pady=self.__tailleCarre/2, padx=self.__tailleCarre/2)
        
        ##################################################################################################
        
        self.__frame4 = Frame(self.__root, background="deepskyblue")
        self.__frame4.grid(row=0, column=3)
        
        self.__button7x7 = Button(self.__frame4, text='7x7', command=lambda: self.boardGrid(7, 57), highlightbackground="deepskyblue")
        self.__button7x7.pack(pady=self.__tailleCarre/2, padx=self.__tailleCarre/2)
        
        ###################################################################################################
        
        self.__frame5 = Frame(self.__root, background="deepskyblue")
        self.__frame5.grid(row=0, column=4)
        
        self.__button8x8 = Button(self.__frame5, text='8x8', command=lambda: self.boardGrid(8, 50), highlightbackground="deepskyblue")
        self.__button8x8.pack(pady=self.__tailleCarre/2, padx=self.__tailleCarre/2)
        
        ######################################################################################################
        
        self.__frame6 = Frame(self.__root, background="deepskyblue")
        self.__frame6.grid(row=1, column=0, columnspan=4)
        
        self.__canvas = Canvas(self.__frame6)
        self.__canvas.config(width = self.__columns*self.__tailleCarre+1, height = self.__rows*self.__tailleCarre+1, highlightthickness=0, bd=0, bg="deepskyblue")
        self.__canvas.pack(pady=self.__tailleCarre/2, padx=self.__tailleCarre/2)
        self.__canvas.bind('<Button-1>', self.gameTurn)
        
        #######################################################################################################
        
        self.__frame7 = Frame(self.__root, background="deepskyblue")
        self.__frame7.grid(row=1, column=4)
        
        self.__totalText = StringVar()
        self.__total = Label(self.__frame7, textvariable=self.__totalText, background="deepskyblue", font=self.__font2, fg="white")
        self.__total.pack(pady=self.__tailleCarre/2)
        self.__totalText.set("Total: "+str(self.__score))
        
        self.__maximumText = StringVar()
        self.__maximum = Label(self.__frame7, textvariable=self.__maximumText, background="deepskyblue", font=self.__font2, fg="white")
        self.__maximum.pack(pady=self.__tailleCarre/2, padx=self.__tailleCarre/2)
        self.__maximumText.set("Maximum: 0")
        
    # Déroulement du jeu ---------------------------------------------------------------------------
        
    def gameTurn(self, event):
        if self.possible(event.y//self.__tailleCarre, event.x//self.__tailleCarre):
            self.put(event.y//self.__tailleCarre, event.x//self.__tailleCarre)
            self.display()
            time.sleep(0.1)
            self.gravity()
            self.update()
            self.__maximumText.set("Maximum: "+str(self.max()))
            self.__totalText.set("Total: "+str(self.__score))
            self.display()
        if self.again() == False:
            messagebox.showinfo(title="Fin de partie", message="Total: "+str(self.__score)+"   Max: "+str(self.max()))
            retry = messagebox.askyesno(title="Restart ?", message="Voulez-vous rejouer ?")
            if retry == True:
                self.__board = self.newBoard()
                self.__score = 0
                self.max()
                self.__maximumText.set("Maximum: "+str(self.max()))
                self.__totalText.set("Total: "+str(self.__score))
                self.display()
            else:
                self.__root.destroy()
                
    # Grilles ----------------------------------------------------------------------------------
       
    def boardGrid(self, grille, tailleCarre):
        self.__columns, self.__rows, self.__score, self.__tailleCarre = grille, grille, 0, tailleCarre
        self.__board = self.newBoard()
        self.max()
        self.__maximumText.set("Maximum: "+str(self.max()))
        self.__totalText.set("Total: "+str(self.__score))
        self.play()
        
    # Fonctions du jeu --------------------------------------------------------------------------
    
    def newBoard(self):
        return [[self.randomNumber() for _ in range(self.__columns)] for _ in range(self.__rows)]
    
    def randomNumber(self):
        x = random()
        if x <= 0.4:
            return 1
        elif x <= 0.7:
            return 2
        elif x <= 0.95:
            return 3
        else:
            return 4
        
    def possible(self, i, j):
        if 0<=i-1<self.__rows and self.__board[i][j] == self.__board[i-1][j]:
            return True
        if 0<=j+1<self.__columns and self.__board[i][j] == self.__board[i][j+1]:
            return True
        if 0<=i+1<self.__rows and self.__board[i][j] == self.__board[i+1][j]:
            return True
        if 0<=j-1<self.__columns and self.__board[i][j] == self.__board[i][j-1]:
            return True
        return False
    
    def again(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                if self.possible(i, j) == True:
                    return True
        return False
                    
    def play(self):
        self.display()
        self.__root.mainloop()
                    
    def max(self):
        x=0
        for i in range(self.__rows):
            for j in range(self.__columns):
                if x<self.__board[i][j]:
                    x=self.__board[i][j]
        return x
    
    # Mise à jour de la grille ----------------------------------------------------------
    
    def put(self, i, j):
        self.__score += self.__board[i][j]
        x=self.__board[i][j]
        self.__board[i][j]+=1
        self.top(i, j, x)
        self.right(i, j, x)
        self.bottom(i, j, x)
        self.left(i, j, x)
        
    def top(self, i, j, x):
        if 0<=i-1<self.__rows and x == self.__board[i-1][j]:
            self.__score += self.__board[i-1][j]
            self.__board[i-1][j]=0
            self.top(i-1, j, x)
            self.right(i-1, j, x)
            self.left(i-1, j, x)
    
    def right(self, i, j, x):
        if 0<=j+1<self.__rows and x == self.__board[i][j+1]:
            self.__score += self.__board[i][j+1]
            self.__board[i][j+1]=0
            self.top(i, j+1, x)
            self.right(i, j+1, x)
            self.bottom(i, j+1, x)
            
    def bottom(self, i, j, x):
        if 0<=i+1<self.__rows and x == self.__board[i+1][j]:
            self.__score += self.__board[i+1][j]
            self.__board[i+1][j]=0
            self.right(i+1, j, x)
            self.bottom(i+1, j, x)
            self.left(i+1, j, x)
            
    def left(self, i, j, x):
        if 0<=j-1<self.__rows and x == self.__board[i][j-1]:
            self.__score += self.__board[i][j-1]
            self.__board[i][j-1]=0
            self.top(i, j-1, x)
            self.bottom(i, j-1, x)
            self.left(i, j-1, x)
    
    def gravity(self):
        grav = True
        while grav == True:
            grav = False
            for i in range(self.__rows):
                for j in range(self.__columns):
                    if 0<=i-1<self.__rows and self.__board[i][j] == 0 and self.__board[i-1][j] != 0:
                        self.__board[i][j], self.__board[i-1][j] = self.__board[i-1][j], self.__board[i][j]
                        self.display()
                        time.sleep(0.000000001)
                        grav = True
                        
    def update(self):
        for j in range(self.__rows):
            for i in range(self.__columns):
                if self.__board[i][j] == 0:
                    self.__board[i][j] = self.randomNumber()
                    self.display()
                    time.sleep(0.01)
                    
    # Affichage du jeu ---------------------------------------------------------------------    
    
    def display(self):
        self.__canvas.delete(ALL)
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__canvas.create_rectangle(j*self.__tailleCarre, i*self.__tailleCarre, j*self.__tailleCarre+self.__tailleCarre, i*self.__tailleCarre+self.__tailleCarre, fill=self.color(i, j), outline="white")
                if self.__board[i][j] != 0:
                    self.__canvas.create_text(j*self.__tailleCarre+self.__tailleCarre/2, i*self.__tailleCarre+self.__tailleCarre/2, text=str(self.__board[i][j]), font=self.__font1, fill="white")
        self.__canvas.update() 
    
    def color(self, i ,j):
        if self.__board[i][j] == 1:
            return "green"
        if self.__board[i][j] == 2:
            return "blue"
        if self.__board[i][j] == 3:
            return "orange"
        if self.__board[i][j] == 4:
            return "red"
        if self.__board[i][j] == 5:
            return "gold"
        if self.__board[i][j] == 6:
            return "brown"
        if self.__board[i][j] == 7:
            return "purple"
        if self.__board[i][j] == 8:
            return "pink"
        if self.__board[i][j] == 9:
            return "grey"
        if self.__board[i][j] >= 10:
            return "black"
    
test = justGetTen(8,8)
test.play()