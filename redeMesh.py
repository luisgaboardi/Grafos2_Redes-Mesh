from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import heapq
from collections import defaultdict

root = Tk()
root.title("Redes Mesh e seu trajeto até os dispositivos")
root.geometry("675x900")

intro = Label(root, text="\nFoi delegada a você a missão de instalar uma soluçao de internet de uma casa.\nLhe foi informado que à sua disposição há:\nUm roteador e mais três repetidores Mesh, sendo o posicionamento deles arbitrário por você.\nObs: Quanto menor o número de repetidores percorridos, melhor é a qualidade do sinal.\n")
intro.pack()

imagem = PhotoImage(file="imagens/Individual/planta.png")
imgLabel = Label(root, image=imagem)
imgLabel.pack()

comodostxt = ['Suite Master', 'Closet Master', 'Closet Quarto 3', 'Quarto 3',
              'Quarto 2', 'Media', 'Escritorio', 'Cozinha', 'Sala de Jantar', 'Sala']

comodosdict = {'Suite Master': {'Closet Master':   3.2, 'Media':         3.5},
               'Closet Master':   {'Closet Quarto 3': 3.2, 'Quarto 3':      2.5, 'Quarto 2':        3.4, 'Media': 2.2, 'Suite Master': 4},
               'Closet Quarto 3': {'Quarto 3':        2.5, 'Quarto 2':      2.6, 'Closet Master':   3.6},
               'Quarto 3':        {'Quarto 2':        3.4, 'Closet Master': 2.6, 'Closet Quarto 3': 2.7},
               'Quarto 2':        {'Quarto 3':        2.2, 'Closet Master': 3.4, 'Closet Quarto 3': 2.7},
               'Media':           {'Suite Master':    4.0, 'Escritório':    2.7, 'Closet Master':   3.5},
               'Escritorio':      {'Media':           2.7, 'Cozinha':       2.6, 'Sala':            3.1},
               'Cozinha':         {'Sala de Jantar':  3.5, 'Escritório':    2.6, 'Sala':            2.2},
               'Sala de Jantar':  {'Cozinha':         3.5},
               'Sala':            {'Escritório':      3.1, 'Cozinha':       2.2}
               }

comodos = []
for i in range(10):
    comodos = comodos + [[0]*10]

# Definindo o alcance de cada cômodo (arestas) utlizando matriz de arestas
# Suite Master
comodos[0][1] = 3.2
comodos[0][5] = 3.5

# Closet Master
comodos[1][0] = 4.0
comodos[1][2] = 3.2
comodos[1][3] = 2.5
comodos[1][4] = 3.4
comodos[1][5] = 2.2

# Closet Quarto 3
comodos[2][1] = 3.6
comodos[2][3] = 2.5
comodos[2][4] = 2.6

# Quarto 3
comodos[3][1] = 2.6
comodos[3][2] = 2.7
comodos[3][4] = 3.4

# Quarto 2
comodos[4][1] = 3.4
comodos[4][2] = 2.7
comodos[4][3] = 2.2

# Media
comodos[5][0] = 4
comodos[5][1] = 3.5
comodos[5][6] = 2.7

# Escritório
comodos[6][5] = 2.7
comodos[6][7] = 2.6
comodos[6][9] = 3.1

# Cozinha
comodos[7][6] = 2.6
comodos[7][8] = 3.5
comodos[7][9] = 2.2

# Sala de Jantar
comodos[8][7] = 3.5

# Sala
comodos[9][6] = 3.1
comodos[9][7] = 2.2

comodosAcess = {}
comodosAcessMat = []
pos_rot = ''
flagR = 0
pos_rep1 = ''
flag1 = 0
pos_rep2 = ''
flag2 = 0
pos_rep3 = ''
flag3 = 0
pos_cel = ''
flagCel = 0

solution = StringVar()


def atualiza_pos_rot(value):
    global pos_rot
    global comodosAcess
    comodosAcess = {}

    aux = 0
    for c in comodosdict:
        if(c == value):
            comodosAcess[value] = comodosdict[value]
            comodosAcessMat.append(comodos[aux])

        aux += 1

    pos_rot = value
    imgPath = "imagens/Individual/" + value + ".png"
    img2 = ImageTk.PhotoImage(Image.open(imgPath))
    imgLabel.configure(image=img2)
    imgLabel.image = img2


def atualiza_pos_rep1(value):
    global pos_rot
    global pos_rep1
    pos_rep1 = value

    global comodosAcess
    global flag1
    if(flag1 == 1 and len(comodosAcess) > 1):
        comodosAcess.popitem()
        flag1 = 0
    global flag2
    if(flag2 == 1 and len(comodosAcess) > 1):
        comodosAcess.popitem()
        flag2 = 0
    global flag3
    if(flag3 == 1 and len(comodosAcess) > 1):
        comodosAcess.popitem()
        flag3 = 0

    aux = 0
    for c in comodosdict:
        if(c == value):
            flag1 = 1
            comodosAcess[value] = comodosdict[value]
            comodosAcessMat.append(comodos[aux])

        aux += 1

    try:
        imgPath = "imagens/Duplas/" + pos_rot + "-" + pos_rep1 + ".png"
        img2 = ImageTk.PhotoImage(Image.open(imgPath))
    except:
        imgPath = "imagens/Duplas/" + pos_rep1 + "-" + pos_rot + ".png"
        img2 = ImageTk.PhotoImage(Image.open(imgPath))
    try:
        imgLabel.configure(image=img2)
        imgLabel.image = img2
    except:
        pass


def atualiza_pos_rep2(value):
    global pos_rot
    global pos_rep1
    global pos_rep2
    pos_rep2 = value

    global comodosAcess

    global flag2
    if(flag2 == 1 and len(comodosAcess) > 1):
        comodosAcess.popitem()
        flag2 = 0
    global flag3
    if(flag3 == 1 and len(comodosAcess) > 1):
        comodosAcess.popitem()
        flag3 = 0

    aux = 0
    for c in comodosdict:
        if(c == value):
            flag2 = 1
            comodosAcess[value] = comodosdict[value]
            comodosAcessMat.append(comodos[aux])

        aux += 1

    pos = []
    pos.append(pos_rot)
    pos.append(pos_rep1)
    pos.append(pos_rep2)
    pos.sort()
    try:
        imgPath = "imagens/Trios/" + pos[0] + \
            "-" + pos[1] + '-' + pos[2] + ".png"
        img2 = ImageTk.PhotoImage(Image.open(imgPath))
        imgLabel.configure(image=img2)
        imgLabel.image = img2
    except:
        pass


def atualiza_pos_rep3(value):
    global pos_rot
    global pos_rep1
    global pos_rep2
    global pos_rep3
    pos_rep3 = value

    global comodosAcess

    global flag3
    if(flag3 == 1 and len(comodosAcess) > 1):
        comodosAcess.popitem()
        flag3 = 0

    aux = 0
    for c in comodosdict:
        if(c == value):
            flag3 = 1
            comodosAcess[value] = comodosdict[value]
            comodosAcessMat.append(comodos[aux])

        aux += 1

    pos = []
    pos.append(pos_rot)
    pos.append(pos_rep1)
    pos.append(pos_rep2)
    pos.append(pos_rep3)
    pos.sort()
    try:
        imgPath = "imagens/Quatro/" + \
            pos[0] + "-" + pos[1] + '-' + pos[2] + '-' + pos[3] + ".png"
        img2 = ImageTk.PhotoImage(Image.open(imgPath))
        imgLabel.configure(image=img2)
        imgLabel.image = img2
    except:
        pass


def atualiza_pos_cel(value):

    global comodosAcess
    global flagCel
    global pos_cel
    pos_cel = value
    if(flagCel == 1 and len(comodosAcess) > 1):
        comodosAcess.popitem()
        flagCel = 0

    aux = 0
    for c in comodosdict:
        if(c == value):
            flagCel = 1
            comodosAcess[value] = comodosdict[value]
            comodosAcessMat.append(comodos[aux])

        aux += 1

    no_cel = 0
    for i in comodostxt:
        if(i == pos_cel):
            break
        no_cel += 1

    dijkstra(len(comodosAcessMat)-1)


dist = []

# A utility function to find the vertex with
# minimum distance value, from the set of vertices
# not yet included in shortest path tree


def minDistance(dist, sptSet):
    # Initilaize minimum distance for next node
    min = sys.maxsize
    min_index = -1
    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(len(comodosAcessMat)):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    if(min_index == -1):
        print('Não rolou')
        exit(-1)

    return min_index

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation


def dijkstra(src):
    global dist
    dist = [sys.maxsize] * (len(comodosAcessMat))
    dist[src] = 0
    sptSet = [False] * (len(comodosAcessMat))

    for cout in range(len(comodosAcessMat)):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minDistance(dist, sptSet)

        # Put the minimum distance vertex in the
        # shotest path tree
        sptSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shotest path tree
        for v in range(len(comodosAcessMat)):
            print(v)
            if comodosAcessMat[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + comodosAcessMat[u][v]:
                dist[v] = dist[u] + comodosAcessMat[u][v]

    global solution
    solution = str(dist[0]) + ' Metros através dos repetidores'
    print(solution)
    result = Label(root, text=solution, wraplength=200, pady=5, padx=20).pack()


label = Label(
    text="_________________________________________________________________")
label.pack()

label = Label(text="\nSelecione o cômodo em será instalado o roteador:")
label.pack()


router_options = []
for item in comodostxt:
    router_options.append(item)
clicked = StringVar()

OptionMenu(root, clicked, *router_options,
           command=atualiza_pos_rot).pack(padx=100)


label = Label(
    text="\nSelecione os cômodos onde serão posicionados os repetidores:")
label.pack()

rep1_options = []
for item in comodostxt:
    rep1_options.append(item)
clicked = StringVar()

OptionMenu(root, clicked, *rep1_options,
           command=atualiza_pos_rep1).pack(padx=0)


rep2_options = []
for item in comodostxt:
    rep2_options.append(item)
clicked = StringVar()

OptionMenu(root, clicked, *rep2_options,
           command=atualiza_pos_rep2).pack(padx=100)


rep3_options = []
for item in comodostxt:
    rep3_options.append(item)
clicked = StringVar()

OptionMenu(root, clicked, *rep3_options,
           command=atualiza_pos_rep3).pack(padx=100)


label = Label(
    text="_________________________________________________________________")
label.pack()
label = Label(text="\nDado um celular acessando a internet no cômodo:")
label.pack()

device_options = []
for item in comodostxt:
    device_options.append(item)
clicked = StringVar()

OptionMenu(root, clicked, *device_options,
           command=atualiza_pos_cel).pack(padx=100)

routeLabel = Label(
    root, text="\nA menor distância que o sinal do roteador percorre até o dispositivo é:", pady=5)
routeLabel.pack()

#solution = dijkstra(len(comodosAcessMat)-1)

global result


root.mainloop()
