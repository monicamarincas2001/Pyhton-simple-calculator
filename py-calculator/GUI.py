import tkinter as tk
import calculations

window = tk.Tk()  # create the object
window.minsize(518, 740)
window.maxsize(518, 740)
window.configure(bg='black')
result = tk.Text(window, height=2.5, width=29, font=("Arial", 24))
result.grid(columnspan=5)
result.configure(bg='black', fg='white')

# Buttons for numbers

B1 = tk.Button(window, text='1', command=lambda: calculations.add_to_calculation(1), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B1.grid(row=2, column=0)
B2 = tk.Button(window, text='2', command=lambda: calculations.add_to_calculation(2), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B2.grid(row=2, column=1)
B3 = tk.Button(window, text='3', command=lambda: calculations.add_to_calculation(3), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B3.grid(row=2, column=2)
B4 = tk.Button(window, text='4', command=lambda: calculations.add_to_calculation(4), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B4.grid(row=3, column=0)
B5 = tk.Button(window, text='5', command=lambda: calculations.add_to_calculation(5), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B5.grid(row=3, column=1)
B6 = tk.Button(window, text='6', command=lambda: calculations.add_to_calculation(6), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B6.grid(row=3, column=2)
B7 = tk.Button(window, text='7', command=lambda: calculations.add_to_calculation(7), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B7.grid(row=4, column=0)
B8 = tk.Button(window, text='8', command=lambda: calculations.add_to_calculation(8), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B8.grid(row=4, column=1)
B9 = tk.Button(window, text='9', command=lambda: calculations.add_to_calculation(9), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B9.grid(row=4, column=2)
B0 = tk.Button(window, text='0', command=lambda: calculations.add_to_calculation(0), bg='#A6A6A6', fg='white',
               font=('Arial', 30), width=5, height=2)
B0.grid(row=5, column=1)

# Buttons for operations

B_plus = tk.Button(window, text='+', command=lambda: calculations.add_to_calculation('+'), bg="#FE9500", fg='white',
                   font=('Arial', 30), width=5, height=2)
B_plus.grid(row=2, column=3)
B_min = tk.Button(window, text='-', command=lambda: calculations.add_to_calculation('-'), bg="#FE9500", fg='white',
                  font=('Arial', 30), width=5, height=2)
B_min.grid(row=3, column=3)
B_mul = tk.Button(window, text='x', command=lambda: calculations.add_to_calculation('*'), bg="#FE9500", fg='white',
                  font=('Arial', 30), width=5, height=2)
B_mul.grid(row=4, column=3)
B_div = tk.Button(window, text='/', command=lambda: calculations.add_to_calculation('/'), bg="#FE9500", fg='white',
                  font=('Arial', 30), width=5, height=2)
B_div.grid(row=5, column=3)
B_eq = tk.Button(window, text='=', command=lambda: calculations.evaluate_calculation(), bg="#333333", fg='white',
                 font=('Arial', 30), width=5, height=2)
B_eq.grid(row=6, column=1)
B_eq = tk.Button(window, text='Hello!', command=lambda: calculations.sayHello(), bg="#FE9500", fg='white',
                 font=('Arial', 30), width=5, height=2)
B_eq.grid(row=6, column=3)

# Buttons for order of calculations

B_par_open = tk.Button(window, text='(', command=lambda: calculations.add_to_calculation('('), bg="#333333", fg='white',
                       font=('Arial', 30), width=5, height=2)
B_par_open.grid(row=5, column=0)
B_par_close = tk.Button(window, text=')', command=lambda: calculations.add_to_calculation(')'), bg="#333333",
                        fg='white',
                        font=('Arial', 30), width=5, height=2)
B_par_close.grid(row=5, column=2)

# Button for clearing the text bar
B_clear = tk.Button(window, text='C', command=lambda: calculations.clear_field(), bg="#333333", fg='white',
                    font=('Arial', 30), width=5, height=2)
B_clear.grid(row=6, column=0)

# Button for admitting floats
B_clear = tk.Button(window, text=',', command=lambda: calculations.add_to_calculation('.'), bg="#333333", fg='white',
                    font=('Arial', 30), width=5, height=2)
B_clear.grid(row=6, column=2)

window.mainloop()  # run the mainloop
