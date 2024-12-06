# author: Svante Aretun
# date: March 17, 2023

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
import numpy as np

if __name__ == '__main__':

    def update_ui(tiles):
        board = np.reshape(tiles, (4, 4))
        row = 0
        for i in board:
            col = 0
            for j in i:
                text = StringVar()
                if str(j) == "0":
                    text.set(" ")
                else:
                    text.set(str(j))
                button = Button(gui, textvariable=text, name=str(j), bg='white', fg='black', font=font, height=2, width=5, command=lambda m=str(j): clickButton(m))
                button.grid(row=row, column=col)
                col += 1
            row += 1


    # clickButton method
    def clickButton(name):
        if name == 'shuffle':
            tiles.shuffle()
            update_ui(tiles.tiles)
        elif name == 'quit':
            print('Game Over!')
            gui.destroy()
        else:
            tiles.update(int(name))
            update_ui(tiles.tiles)
            if tiles.is_solved() == True:
                print('You Win!')
                gui.destroy()


    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons
    update_ui(tiles.tiles)
    text = StringVar()
    text.set("shuffle")
    shuffle = Button(gui, textvariable=text, name="shuffle", bg="white", fg='black', font=font, height=1, width=5, command = lambda  m="shuffle": clickButton(m))
    shuffle.grid(row=4, column=1)
    text = StringVar()
    text.set("quit")
    quit = Button(gui, textvariable=text, name="quit", bg="white", fg='black', font=font, height=1, width=5, command = lambda m="quit" : clickButton(m))
    quit.grid(row=4, column=2)

    # update the window
    gui.mainloop()