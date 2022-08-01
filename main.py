from tkinter import *
from resolver import solver

window = Tk()
window.title("Sudoku Solver")
window.geometry("324x550")

label = Label(window, text="Entrez les valeurs et appuyez sur 'Resoudre'")
label.grid(row=0, column=1, columnspan=10)

errLabel = Label(window, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel = Label(window, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

cells = {}


def validateNumber(P):
    out = (P.isdigit() or P == "") and len(P) < 2
    return out


reg = window.register(validateNumber)


def make3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(window, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row + i + 1, column=column + j + 1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row + i + 1, column + j + 1)] = e


def make9x9Grid():
    color = "#D0ffff"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            make3x3Grid(rowNo, colNo, color)
            if color == "#D0ffff":
                color = "#ffffD0"
            else:
                color = "#D0ffff"


def clearValues():
    errLabel.config(text="")
    solvedLabel.config(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")


def getValues():
    board = []
    errLabel.config(text="")
    solvedLabel.config(text="")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)


btn = Button(window, command=getValues, text="Resoudre", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

btn2 = Button(window, command=clearValues, text="Reinitialiser", width=10)
btn2.grid(row=20, column=6, columnspan=5, pady=20)


def updateValues(s):
    sol = solver(s)
    if sol != "no":
        for row in range(2, 11):
            for col in range(1, 10):
                if s[row-2][col-1] == 0:
                    cells[(row, col)].config(fg="red")
                cells[(row, col)].delete(0, "end")
                cells[(row, col)].insert(0, sol[row - 2][col - 1])
        solvedLabel.config(text="Sudoku resolu")
    else:
        errLabel.config(text="Pas de solution possible")


make9x9Grid()
window.mainloop()
