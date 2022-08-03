from tkinter import *
import ast


# intacias de la app o raiz
root = Tk()
root.title("Calculator")
# cuadro de texto
display = Entry(root, font="Console 19")
display.grid(row=1, columnspan=6, padx=12, pady=6, sticky=W + E)
indexI = 0


def get_numbers(n):
    global indexI
    display.insert(indexI, n)
    indexI += 1


def get_operation(operador):
    global indexI
    operator_lent = len(operador)
    display.insert(indexI, operador)
    indexI += operator_lent


def clear_display():
    display.delete(0, END)


def undo():
    display_state = display.get()
    if len(display_state):
        # elimina el ultimo numero de la pantalla
        display_new_state = display_state[:-1]
        # renderizo el estado nuevo
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "Error")


def calculate():
    display_state = display.get()
    try:
        math_expression = ast.expr(display_state)
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0, "Error")


# creacion de los butones
Button(root, text="1", command=lambda: get_numbers(1)).grid(
    row=2, column=0, sticky=W + E
)
Button(root, text="2", command=lambda: get_numbers(2)).grid(
    row=2, column=1, sticky=W + E
)
Button(root, text="3", command=lambda: get_numbers(3)).grid(
    row=2, column=2, sticky=W + E
)

Button(root, text="4", command=lambda: get_numbers(4)).grid(
    row=3, column=0, sticky=W + E
)
Button(root, text="5", command=lambda: get_numbers(5)).grid(
    row=3, column=1, sticky=W + E
)
Button(root, text="6", command=lambda: get_numbers(6)).grid(
    row=3, column=2, sticky=W + E
)

Button(root, text="7", command=lambda: get_numbers(7)).grid(
    row=4, column=0, sticky=W + E
)
Button(root, text="8", command=lambda: get_numbers(8)).grid(
    row=4, column=1, sticky=W + E
)
Button(root, text="9", command=lambda: get_numbers(9)).grid(
    row=4, column=2, sticky=W + E
)
# botnes de limpieaza
Button(root, text="AC", command=lambda: clear_display()).grid(
    row=5, column=0, sticky=W + E
)
Button(root, text="0", command=lambda: get_numbers(0)).grid(
    row=5, column=1, sticky=W + E
)
Button(root, text="%", command=lambda: get_operation("%")).grid(
    row=5, column=2, sticky=W + E
)
# botones arimeticos
Button(root, text="+", command=lambda: get_operation("+")).grid(
    row=2, column=4, sticky=W + E
)
Button(root, text="-", command=lambda: get_operation("-")).grid(
    row=3, column=4, sticky=W + E
)
Button(root, text="*", command=lambda: get_operation("*")).grid(
    row=4, column=4, sticky=W + E
)
Button(root, text="/", command=lambda: get_operation("/")).grid(
    row=5, column=4, sticky=W + E
)
# extra
Button(root, text="🠔", command=lambda: undo()).grid(
    row=2, column=5, sticky=W + E, columnspan=2
)
Button(root, text="exp", command=lambda: get_operation("**")).grid(
    row=3, column=5, sticky=W + E
)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(
    row=3, column=6, sticky=W + E
)
Button(root, text="(", command=lambda: get_operation("(")).grid(
    row=4, column=5, sticky=W + E
)
Button(root, text=")", command=lambda: get_operation(")")).grid(
    row=4, column=6, sticky=W + E
)
Button(root, text="=", command=lambda: calculate()).grid(
    row=5, column=5, sticky=W + E, columnspan=2
)

# registro de los succesos en este caso la raiz
root.mainloop()
