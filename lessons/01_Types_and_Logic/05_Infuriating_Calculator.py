"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()     
window.withdraw()

# Ask the user for the first number   
e = simpledialog.askfloat('Very Infuriating Calculator', "Add your first number.")
# Ask the user for the second number
f = simpledialog.askfloat('Very Infuriating Calculator', "Add your second number.")
# Ask the user for the math operation
g = simpledialog.askstring('Very Infuriating Calculator', "Add your operation.")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if g == '+':
   messagebox.showinfo('Very Infuriating Calculator', e + f)
elif g == '/':
   messagebox.showinfo('Very Infuriating Calculator', e / f)
elif g == '-':
   messagebox.showinfo('Very Infuriating Calculator', e - f)
elif g == '*':
   messagebox.showinfo('Very Infuriating Calculator', e * f)

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
elif g == 'x':
   messagebox.showinfo('Very Infuriating Calculator', "ERROR, operation not found.")
# Keep the window open
