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

comodos = {'Suite Master':    {'Closet Master': 3.2, 'Media': 3.5},
           'Closet Master':   {'Closet Quarto 3': 3.2, 'Quarto 3': 2.5, 'Quarto 2': 3.4, 'Media': 2.2, 'Suite Master': 4},
           'Closet Quarto 3': {'Quarto 3': 2.5, 'Quarto 2': 2.6, 'Closet Master': 3.6},
           'Quarto 3':        {'Quarto 2': 3.4, 'Closet Master': 2.6, 'Closet Quarto 3': 2.7},
           'Quarto 2':        {'Quarto 3': 2.2, 'Closet Master': 3.6, 'Closet Quarto 3': 2.7},
           'Media':           {'Suite Master': 4, 'Escritório': 2.7},
           'Escritório':      {'Media': 2.7, 'Cozinha': 2.6, 'Sala': 3.1},
           'Cozinha':         {'Sala de Jantar': 3.5, 'Escritório': 2.6, 'Sala': 2.2},
           'Sala de Jantar':  {'Cozinha': 3.5},
           'Sala':            {'Escritório': 3.1, 'Cozinha': 2.2}
           }


localDeAcesso = {}
pos_rot = ''
pos_rep1 = ''
pos_rep2 = ''
pos_rep3 = ''


def atualiza_pos_rot(value):
    global pos_rot
    pos_rot = value
    imgPath = "imagens/Individual/" + value + ".png"
    img2 = ImageTk.PhotoImage(Image.open(imgPath))
    imgLabel.configure(image=img2)
    imgLabel.image = img2


def atualiza_pos_rep1(value):
    global pos_rot
    global pos_rep1
    pos_rep1 = value
    try:
        imgPath = "imagens/Duplas/" + pos_rot + "-" + pos_rep1 + ".png"
        img2 = ImageTk.PhotoImage(Image.open(imgPath))
    except:
        imgPath = "imagens/Duplas/" + pos_rep1 + "-" + pos_rot + ".png"
        img2 = ImageTk.PhotoImage(Image.open(imgPath))
    imgLabel.configure(image=img2)
    imgLabel.image = img2


def atualiza_pos_rep2(value):
    global pos_rot
    global pos_rep1
    global pos_rep2
    pos_rep2 = value
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


def Prim(G, start):
    mst = defaultdict(set)
    visited = set([start])
    edges = [
        (cost, start, to)
        for to, cost in G[start].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in G[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst


print(Prim(comodos, 'Sala'))

label = Label(
    text="_________________________________________________________________")
label.pack()

label = Label(text="\nSelecione o cômodo em será instalado o roteador:")
label.pack()


router_options = []
for item in comodostxt:
    router_options.append(item)
clicked = StringVar()
# clicked.set(router_options[0])

OptionMenu(root, clicked, *router_options,
           command=atualiza_pos_rot).pack(padx=100)


label = Label(
    text="\nSelecione os cômodos onde serão posicionados os repetidores:")
label.pack()

rep1_options = []
for item in comodostxt:
    rep1_options.append(item)
clicked = StringVar()
# clicked.set(rep1_options[0])
OptionMenu(root, clicked, *rep1_options,
           command=atualiza_pos_rep1).pack(padx=0)

rep2_options = []
for item in comodostxt:
    rep2_options.append(item)
clicked = StringVar()
# clicked.set(rep2_options[0])
OptionMenu(root, clicked, *rep2_options,
           command=atualiza_pos_rep2).pack(padx=100)

rep3_options = []
for item in comodostxt:
    rep3_options.append(item)
clicked = StringVar()
# clicked.set(rep3_options[0])
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
clicked.set(device_options[0])

OptionMenu(root, clicked, *device_options).pack(padx=100)


routeLabel = Label(
    root, text="\nA rota percorrida do roteador até o dispositivo foi:", pady=5)
routeLabel.pack()

melhorCaminho = Label(root, text="", wraplength=200, pady=5, padx=20).pack()

resultLabel = Label(
    root, text="\nEstá satisfeito com o resultado? Se não, reposicione os dispositivos de internet\n", pady=5)
resultLabel.pack()


root.mainloop()
