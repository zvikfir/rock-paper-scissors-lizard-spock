import tkinter
import random


class Game(tkinter.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._frame = Menu(master=self, controller=self)

        self.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)

    def switch_frame(self, new_frame, show_back_button=True):
        self._frame.destroy()
        self._frame = tkinter.Frame(self)
        if show_back_button:
            tkinter.Button(self._frame, text='back', image=BACK_IMAGE,
                           command=lambda: self.switch_frame(Menu, False)).pack(anchor='nw')
        new_frame(master=self._frame, controller=self).pack()
        self._frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)


class Menu(tkinter.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        def pack_function(widget):
            widget.pack(side=tkinter.TOP, fill=tkinter.BOTH, pady=20)

        pack_function(tkinter.Label(self, text='Rock Paper Scissors\n Lizard Spock!', font=(None, 24)))
        pack_function(tkinter.Button(self, text='Play!', font=(None, 18),
                                     command=lambda: controller.switch_frame(Play)))
        pack_function(tkinter.Button(self, text='Instructions', font=(None, 18),
                                     command=lambda: controller.switch_frame(Instructions)))
        pack_function(tkinter.Button(self, text='Exit', font=(None, 18), command=lambda: exit()))

        self.pack()


class Instructions(tkinter.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        tkinter.Label(self, image=INSTRUCTIONS_IMAGE).pack(fill=tkinter.BOTH, expand=tkinter.TRUE)

        self.pack()


class Play(tkinter.Frame):

    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.__prompt = tkinter.StringVar(self, value='Choose an option!')

        tkinter.Label(self, textvariable=self.__prompt, font=(None, 16), pady=20).pack(side=tkinter.TOP, fill=tkinter.X,
                                                                                       expand=tkinter.TRUE)

        self.__buttons_frame = tkinter.Frame(self)

        self.__my_button(text='Rock', image=ROCK_IMAGE)
        self.__my_button(text='Paper', image=PAPER_IMAGE)
        self.__my_button(text='Scissors', image=SCISSORS_IMAGE)
        self.__my_button(text='Lizard', image=LIZARD_IMAGE)
        self.__my_button(text='Spock', image=SPOCK_IMAGE)

        self.__buttons_frame.pack(side=tkinter.TOP)

        self.pack()

    def __my_button(self, *args, **kwargs):
        tkinter.Button(self.__buttons_frame, command=lambda action=kwargs['text']: self.__on_button_click(action),
                       *args, **kwargs).pack(side=tkinter.LEFT, fill=tkinter.X,
                                             expand=tkinter.TRUE, padx=5)

    def __on_button_click(self, action):
        action = action.lower()

        ROCK = 'rock'
        PAPER = 'paper'
        SCISSORS = 'scissors'
        LIZARD = 'lizard'
        SPOCK = 'spock'

        dispatch = {
            ROCK: {'win': [SCISSORS, LIZARD], 'lose': [PAPER, SPOCK]},
            PAPER: {'win': [ROCK, SPOCK], 'lose': [SCISSORS, LIZARD]},
            SCISSORS: {'win': [PAPER, LIZARD], 'lose': [ROCK, SPOCK]},
            LIZARD: {'win': [SPOCK, PAPER], 'lose': [SCISSORS, ROCK]},
            SPOCK: {'win': [SCISSORS, ROCK], 'lose': [LIZARD, PAPER]}
        }

        computer_choice = random.choice((ROCK, PAPER, SCISSORS, LIZARD, SPOCK))
        result = f'Computer chose {computer_choice}\n'
        if computer_choice in dispatch[action]['win']:
            result += 'You WIN! :)'
        elif computer_choice in dispatch[action]['lose']:
            result += 'You LOSE :('
        else:
            result += 'It\'s a TIE'

        self.__prompt.set(result)


if __name__ == '__main__':
    app = tkinter.Tk()
    app.title('Rock Paper Scissors Lizard Spock!')
    app.geometry('600x400')
    app.resizable(False, False)

    INSTRUCTIONS_IMAGE = tkinter.PhotoImage(file='assets/instructions.png').subsample(3, 3)
    ROCK_IMAGE = tkinter.PhotoImage(file='assets/rock.png')
    PAPER_IMAGE = tkinter.PhotoImage(file="assets/paper.png")
    SCISSORS_IMAGE = tkinter.PhotoImage(file="assets/scissors.png")
    SPOCK_IMAGE = tkinter.PhotoImage(file="assets/spock.png").subsample(2, 2)
    LIZARD_IMAGE = tkinter.PhotoImage(file="assets/lizard.png").subsample(11, 11)
    BACK_IMAGE = tkinter.PhotoImage(file="assets/back.png").subsample(2, 2)

    Game(app)

    app.mainloop()
