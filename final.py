import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import StringVar, messagebox, ttk

window = tk.Tk()
window.geometry('500x600')
window.title('Unit Converter')
window.configure(bg='peach puff2')

font1 = font.Font(family='helvetica', size=30)
font2 = font.Font(family='helvetica', size=10)
font3 = font.Font(family='helvetica', size=20)

number_from = StringVar()

def fromfunc(event):
    global result_from
    result_from = event.widget.get()

def tofunc(event):
    global result_to
    result_to = event.widget.get()

def answer(n1):
    num1 = n1.get()
    try:
        number1 = float(num1)
    except ValueError:
        messagebox.showerror('Error', 'Term not recognized')
        return

    calculate = 0.0

    conversion_factors = {
       # Volume conversions
        'Cubic meters to Cubic meters': 1,
        'Cubic meters to Cubic foot': 35.3147,
        'Cubic meters to Liters': 1000,
        'Cubic meters to Gallons': 264.172,
        'Cubic meters to Cubic centimeters': 1e6,
        'Cubic meters to Barrels': 6.28981,
        'Cubic foot to Cubic meters': 0.0283168,
        'Cubic foot to Cubic foot': 1,
        'Cubic foot to Liters': 30,
        'Cubic foot to Gallons': 7.48052,
        'Cubic foot to Cubic centimeters': 28316.8,
        'Liters to Cubic meters': 0.001,
        'Liters to Cubic foot': 0.0353147,
        'Liters to Liters': 1,
        'Liters to Gallons': 0.264172,
        'Liters to Cubic centimeters': 1000,
        'Gallons to Cubic meters': 0.00378541,
        'Gallons to Cubic foot': 0.133681,
        'Gallons to Liters': 3.78541,
        'Gallons to Gallons': 1,
        'Gallons to Cubic centimeters': 3785.41,
        'Cubic centimeters to Cubic meters': 1e-6,
        'Cubic centimeters to Cubic foot': 3.53147e-5,
        'Cubic centimeters to Liters': 0.001,
        'Cubic centimeters to Gallons': 0.000264172,
        'Cubic centimeters to Cubic centimeters': 1,
        
        # Length conversions
        'Millimeters to Centimeters': 0.1,
        'Millimeters to Meters': 0.001,
        'Millimeters to Kilometers': 1e-6,
        'Centimeters to Millimeters': 10,
        'Centimeters to Meters': 0.01,
        'Centimeters to Kilometers': 1e-5,
        'Meters to Millimeters': 1000,
        'Meters to Centimeters': 100,
        'Meters to Kilometers': 0.001,
        'Kilometers to Millimeters': 1e6,
        'Kilometers to Centimeters': 1e5,
        'Kilometers to Meters': 1000,
        
        # Mass conversions
        'Milligrams to Centigrams': 0.1,
        'Milligrams to Grams': 0.001,
        'Milligrams to Kilograms': 1e-6,
        'Centigrams to Milligrams': 10,
        'Centigrams to Grams': 0.01,
        'Centigrams to Kilograms': 1e-5,
        'Grams to Milligrams': 1000,
        'Grams to Centigrams': 100,
        'Grams to Kilograms': 0.001,
        'Kilograms to Milligrams': 1e6,
        'Kilograms to Centigrams': 1e5,
        'Kilograms to Grams': 1000
    }

    conversion_key = f"{result_from} to {result_to}"
    if conversion_key in conversion_factors:
        calculate = number1 * conversion_factors[conversion_key]
    else:
        messagebox.showerror('Error', 'Conversion not supported')

    result.configure(text=f"{calculate} {result_to}")

def selected(event):
    unit = event.widget.get()
    if unit in ['Volume', 'Length', 'Mass']:
        units_list = {
            'Volume': ('Cubic meters', 'Cubic foot', 'Liters', 'Gallons', 'Cubic centimeters'),
            'Length': ('Millimeters', 'Centimeters', 'Meters', 'Kilometers'),
            'Mass': ('Milligrams', 'Centigrams', 'Grams', 'Kilograms')
        }
        fromdd['values'] = units_list[unit]
        todd['values'] = units_list[unit]

main = tk.Label(window, text='Unit Converter', bg='peach puff2', fg='blue')
main['font'] = font1
main.place(relx='0.48', rely='0.1', anchor='center')

unit = tk.Label(window, text='Unit -:', bg='peach puff2')
unit['font'] = font2
unit.place(relx='0.25', rely='0.28')

n = StringVar()
unitdd = ttk.Combobox(window, width='35', textvariable=n)
unitdd['values'] = ('Volume', 'Length', 'Mass')
unitdd.place(relx='0.57', rely='0.3', anchor='center')
unitdd.current()
unitdd.bind('<<ComboboxSelected>>', selected)

label_from = tk.Label(window, text='From -:', bg='peach puff2')
label_from['font'] = font2
label_from.place(relx='0.238', rely='0.37')

f = StringVar()
fromdd = ttk.Combobox(window, width='35', textvariable=f)
fromdd.place(relx='0.57', rely='0.39', anchor='center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>', fromfunc)

num_from = tk.Entry(window, width=10, textvariable=number_from)
num_from.place(relx='0.82', rely='0.37')

answer = partial(answer, num_from)

to = tk.Label(window, text='To -:', bg='peach puff2')
to['font'] = font2
to.place(relx='0.268', rely='0.45')

t = StringVar()
todd = ttk.Combobox(window, width=35, textvariable=t)
todd.place(relx='0.57', rely='0.47', anchor='center')
todd.current()
todd.bind('<<ComboboxSelected>>', tofunc)

result = tk.Label(window, text='', bg='white', width=20)
result['font'] = font3
result.place(relx='0.21', rely='0.6')

get_answer = tk.Button(window, text='Get Answer', bg='cyan2', command=answer)
get_answer['font'] = font2
get_answer.place(relx='0.46', rely='0.7')

art = tk.Label(window, text='', bg='peach puff2', fg='blue')
art['font'] = font3
art.place(relx='0.21', rely='0.9')

window.mainloop()
