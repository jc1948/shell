import tkinter as tk

class MenuBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, 
                          master, 
                          width=1000,
                          height=200)
        self.master.title('5 Games Arcade')
        self.pack_propagate(0)
        self.pack()
        self.greeting_var = tk.StringVar()
        self.greeting_var.set('1')

        # Question for user input
        self.question_var = tk.StringVar()
        self.question_var.set('What game would you like to play')
        self.question = tk.Label(self, textvariable=self.question_var)
        
         # The nextaction for where to go
        self.nextaction_var = tk.StringVar()
        self.nextaction = tk.Entry(self,
                                  textvariable=self.nextaction_var)
        self.nextaction_var.set('1')

        # Status of last action
        self.status_var = tk.StringVar()
        self.status_var.set('Choose game 1,2,3,4,5')
        self.status = tk.Label(self, textvariable=self.status_var)

        # The go button
        self.go_button = tk.Button(self,
                                   text='1 Dice Roller',
                                   command=self.game_action)
        self.anotherbutton= tk.Button(self,
                                      text='2 Mad Libs')
        self.anotherbutton2= tk.Button(self,
                                      text='3 Guess the Number')
        self.anotherbutton3= tk.Button(self,
                                       text='4 Text-Based Adventure Game')
        self.anotherbutton4=tk.Button(self,
                                      text='5 Hangman')

        # Put the controls on the form
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.anotherbutton.pack(fill=tk.X, side=tk.BOTTOM)
        self.anotherbutton2.pack(fill=tk.X, side=tk.BOTTOM)
        self.anotherbutton3.pack(fill=tk.X, side=tk.BOTTOM)
        self.anotherbutton4.pack(fill=tk.X, side=tk.BOTTOM)
        self.question.pack(fill=tk.X, side=tk.TOP)
        self.nextaction.pack(fill=tk.X, side=tk.TOP)
        self.status.pack(fill=tk.X, side=tk.TOP)
                
        self.init_game()
                   
    def print_status(self, text):
        self.status_var.set(text)
        print('%s' % text)
    def get_choice(self, dir):
        if dir=='1':
            choice = 0
        elif dir=='2':
            choice = 1
        elif dir=='3':
            choice = 2
        elif dir=='4':
            choice = 3
        elif dir=='5':
            choice = 4
        else:
            return -1
    def init_game(self):
        self.dirs = (0,0,0,0)
    def game_action(self):
        #self.stuck = True
        #while stuck:
        #if self.stuck:            
        dir = self.nextaction_var.get()
        print('%s' % dir)
        #input("Which direction do you want to go: N,E,S, or W? ")
        choice = self.get_choice(self.room, dir)
        if choice == -1:
            self.print_status("Please enter 1,2,3,4 or 5? ")
            return;
        elif choice == 5:
            self.print_status('You cannot go in that direction.')
            self.print_question("What game would you like to play: 1,2,3,4, or 5? ")
            return;
        else:
            self.room = self.room['directions'][choice]
        self.game_status()

    def run(self):
            self.mainloop()

# Launch the game GUI
app = MenuBar(tk.Tk())
app.run()