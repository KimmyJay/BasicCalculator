import tkinter as tk


window = tk.Tk()  #we want a calculator with buttons of 4x4 grid
window.title('Caculator')

disValue = 0
operators = {'+': 1, '-': 2, '/': 3, '*': 4, 'C': 5, '=': 6} #operator dictionary - returns number corresponding to operator button/key input
stoValue = 0
opPre = 0

def clear(): #resets all variables
    global disValue, stoValue, opPre #global keyword allows variable to be accessed outside the scope of the method
    stoValue = 0
    disValue = 0
    opPre = 0
    str_value.set(str(disValue)) #set display value as such

def number_click(value):
    global disValue
    disValue = disValue * 10 + value #takes into account that we are using the decimal system for our calculator ex) 23= 2 * 10 + 3
    str_value.set(str(disValue)) #set display value as such

def operator_click(value):
    global disValue, operators, stoValue, opPre
    #operators = {'+': 1, '-': 2, '/': 3, '*': 4, 'C': 5, '=': 6}
    op = operators[value]
    if op == 5:
        clear()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0: #if no operation has yet to have been chosen
        opPre = op #set new operation as our previous operator
        stoValue = disValue #store our current value
        disValue = 0 #reset the display value after we choose an operation
        str_value.set(str(disValue))
    elif op == 6: #we are setting the display value as the calculation at this point
        if opPre == 1:
            disValue = stoValue + disValue
        if opPre == 2:
            disValue = stoValue - disValue
        if opPre == 3:
            disValue = stoValue / disValue
        if opPre == 4:
            disValue = stoValue * disValue
        str_value.set(str(disValue))
        stoValue = disValue
        opPre = 0
    else:
        clear()


def button_click(value):
    # if the value is an integer, we invoke number_click() .. if value is not an integer, we invoke operator_click()
    try:
        value = int(value)
        number_click(value)
    except:
        operator_click(value)

str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(window, textvariable=str_value, justify='right')
dis.grid(column=0, row=0, columnspan=40, ipadx=80, ipady=30)

calItem = [['1', '2', '3', '4'],
           ['5', '6', '7', '8'],
           ['9', '0', '+', '-'],
           ['/', '*', 'C', '=']]

#nested for loop that iterates through each calItem element
for i, items in enumerate(calItem): #((0, ['1', '2', '3', '4']), (1, ['5', '6', '7', '8']) .... )
    for k, item in enumerate(items):
        # for each item create a button in grid with given text, width and height and assign it a location on the grid
        bt = tk.Button(window,
                       text=item,
                       width=10,
                       height=5,
                       command = lambda cmd = item: button_click(cmd) # assigns functionality to button using anonymous function?
                       )
        bt.grid(column=k, row=i + 1)

window.mainloop()
