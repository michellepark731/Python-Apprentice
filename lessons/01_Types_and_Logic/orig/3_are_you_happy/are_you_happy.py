from tkinter import Tk, simpledialog, messagebox



# TODO: Look at the AreYouHappy.png image
#       Use pop-ups to recreate the chart using if and elif statements


def onclick(args):
    # TODO 1) Run the program and play many rounds of Rock Paper Scissors. Does the computer always choose the same thing?

    # TODO 2) Change the value of opponent_selection to be a random number between 1 and 3
    def reply():
        if selection:2
        messagebox.showinfo("Do you want to be happy?")
        if selection:3
        messagebox.showinfo("Keep on doing whatever you're doing!")

   

    selection = 1

    if args == "Not happy":
        selection = 2
    elif args == "Yes":
        selection = 3

    messagebox.showinfo(None, "You are: " + str(args) + ".\n"
                        + "You should:" + reply + ".\n")

