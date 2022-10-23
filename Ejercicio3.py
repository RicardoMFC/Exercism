import sys

def pastilla():
    try:
        valor_pastilla=int (input("Escriba 1 si tiene la pastilla activa sino, escriba 0\n"))
        while valor_pastilla!=1 and valor_pastilla!=0:
            valor_pastilla=int (input("Escriba 1 si tiene la pastilla activa sino, escriba 0\n"))
    except:
        pass
    else:
        return valor_pastilla

def fantasma():
    try:
        valor_fantasma=int (input("Escriba 1 si está sobre un fantasma sino, escriba 0\n"))
        while valor_fantasma!=1 and valor_fantasma!=0:
            valor_fantasma=int (input("Escriba 1 si está sobre un fantasma sino, escriba 0\n"))
    except:
        pass
    else:
        return valor_fantasma

def posicion():
    try:
        valor_punto=int (input("Escriba 1 si está sobre un punto sino escriba un 0\n"))
        while valor_punto!=1 and valor_punto!=0:
            valor_punto=int (input("Escriba 1 si está sobre un punto sino escriba un 0\n"))
    except:
        pass
    else:
        return valor_punto

def puntos():
    try:
        valor_puntos=int (input("Escriba 1 si se ha comido todos los puntos, sino escriba 0\n"))
        while valor_puntos!=1 and valor_puntos!=0:
            valor_puntos=int (input("Escriba 1 si se ha comidos todos los puntos, sino escriba 0\n"))
    except:
        pass
    else:
        return valor_puntos

def eat_ghost(pastilla, fantasma):
    if pastilla==1 and fantasma==1:
        return 1
    else:
        return 0

def score(tocando_pastila, tocando_punto):
    if tocando_pastila==1 or tocando_punto==1:
        return 1
    else:
        return 0


#si una de las dos se cumple devuelve True


def lose(pastilla, fantasma):
    if pastilla==0 and fantasma==1:
        return 1
    else:
        return 0
    
def win (puntos, pastilla, fantasma):
    if puntos==1 and pastilla==1 and fantasma==1:
        return 1
    else:
        return 0

def main():
    valor_pastilla = pastilla()
    valor_fantasma = fantasma()
    valor_posicion = posicion()
    fantasmas_comidos = eat_ghost(valor_pastilla, valor_fantasma)
    puntuacion=score(valor_pastilla, valor_posicion )
    perder=lose(valor_pastilla, valor_fantasma)

    if perder==1:
        print ("Le ha comido un fantasma\n")

    todos_puntos=puntos()
    valor_victoria=win(todos_puntos, valor_pastilla, valor_fantasma)
    if valor_victoria==1:
        print("Ha ganado\n")
    else:
        print("Ha perdido\n")
    if fantasmas_comidos==1:
        print ("Ha comido un fantasma\n")
    else:
        print ("No ha comido ningún fantasma\n")
    if puntuacion==1:
        print("Puntúa!\n")
    else:
        print("no puntúa\n")
    
main()