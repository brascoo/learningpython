theBoard = {'1' : '1', '2' : '2', '3' : '3',
            '4' : '4', 'x' : '', '6' : '6',
            '7' : '7', '8' : '8', '9' : '9'}
boardKeys = []

for key in theBoard:
    boardKeys.append(key)

def DisplayBoard(board):
    print("+-------+-------+-------+")
    print ("|       |       |       |")
    print("|   " + board['1'] + "   |   " + board ['2']+'   |   ' + board ['3'] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board["4"] + "   |   " + "X" + "   |   " + board["6"] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board["7"] + "   |   " + board["8"] + "   |   " + board["9"] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#

def EnterMove(board):
    
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
#def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#

#def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#

#def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#

DisplayBoard(theBoard)