from tkinter import*

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.inst_Ibl = Label(self, text = "Enter your name: ")
        self.inst_Ibl.grid(row = 0, column = 0, columnspan = 1, sticky = S)

        self.name_ent = Entry(self)
        self.name_ent.grid(row = 0, column = 1, columnspan = 1, sticky = W )

        self.inst_Ibl = Label(self, text = "Enter password  for longevity:")
        self.inst_Ibl.grid(row = 1, column = 0, columnspan = 2, sticky = W)

        self.pw_Ibl = Label(self, text = "Password: ")
        self.pw_Ibl.grid(row = 2, column = 0, sticky = W)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 2, column = 1, sticky = W)

        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 3, column = 0, sticky = W)

        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 4, column = 0, columnspan = 2, sticky = W)


    
    def reveal(self):
       contents = self.pw_ent.get()
       name = self.name_ent.get()
       if contents == "Love":
            message = ", here's the secret to living to 100: " \
                        " be very KIND to others, one LOVE."
            
       elif contents == "clear":
            message = ", Here's the secret to living to 100: live to 99 " \
                        " be very KIND to others, one LOVE."
            
       else:
            message = ", That's not the correct answer, so I can't share " \
                        "the secret with you."
       self.secret_txt.delete(0.0, END)
       self.secret_txt.insert(0.0, name + message)

root = Tk()
root.title("Lonegevity")
root.geometry("300x150")

app = Application(root)

root.mainloop()