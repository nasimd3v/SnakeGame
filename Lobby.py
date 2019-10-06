from tkinter import Tk, Label, Button, OptionMenu, StringVar
from Play import *


class Lobby_Loader:
    def __init__(self, master):
        pygame.init()

        self.master = master
        master.title('Game')
        master.resizable(0, 0)
        self.pw = 350
        self.ph = 100
        self.w = 600
        self.h = 350
        self.ws = master.winfo_screenwidth()
        self.hs = master.winfo_screenheight()
        self.x = (self.ws / 2) - (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)
        self.px = (self.ws / 2) - (self.pw / 2)
        self.py = (self.hs / 2) - (self.ph / 2)
        master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

        self.level = StringVar(master)
        self.level.set("Easy")
        self.option = OptionMenu(master, self.level, "Easy", "Medium", "Hard", "Harder", "Impossible")
        self.option.pack()

        self.greet_button = Button(master, text="Start Game", command=self.start_game)
        self.greet_button.pack()

    def start_game(self):
        global level
        if self.level.get() == "Easy":
            level = 10
        elif self.level.get() == "Medium":
            level = 20
        elif self.level.get() == "Hard":
            level = 40
        elif self.level.get() == "Harder":
            level = 60
        elif self.level.get() == "Impossible":
            level = 120

        Play(level)


if __name__ == '__main__':
    window = Tk()
    my_gui = Lobby_Loader(window)
    window.mainloop()
