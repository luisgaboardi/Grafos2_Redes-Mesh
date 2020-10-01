from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Redes Mesh e seu trajeto até os dispositivos")
root.geometry("675x900")

intro = Label(root, text="\nFoi delegada a você a missão de instalar uma soluçao de internet de uma casa.\nLhe foi informado que à sua disposição há:\nUm roteador e mais três repetidores Mesh, sendo o posicionamento deles arbitrário por você.\nObs: Quanto menor o número de repetidores percorridos, melhor é a qualidade do sinal.\n")
intro.pack()

imagem = PhotoImage(file="imagens/Individual/planta.png")
imgLabel = Label(root, image=imagem)
imgLabel.pack()

# A partir da esquerda, sentido horário
comodos = []
for i in range(10):
  comodos = comodos + [[0]*10]

# Definindo o alcance de cada cômodo (arestas) utlizando matriz de arestas
#Suite Master
comodos[0][0] = 1
comodos[0][1] = 1
comodos[0][5] = 1

#Closet Master
comodos[1][0] = 1
comodos[1][1] = 1
comodos[1][2] = 1
comodos[1][3] = 1
comodos[1][4] = 1
comodos[1][5] = 1

#Closet Quarto 3
comodos[2][1] = 1
comodos[2][2] = 1
comodos[2][3] = 1
comodos[2][4] = 1

#Quarto 3
comodos[3][1] = 1
comodos[3][2] = 1
comodos[3][3] = 1
comodos[3][4] = 1

#Quarto 2
comodos[4][1] = 1
comodos[4][2] = 1
comodos[4][3] = 1
comodos[4][4] = 1

#Media
comodos[5][0] = 1
comodos[5][1] = 1
comodos[5][5] = 1
comodos[5][6] = 1

#Escritório
comodos[6][5] = 1
comodos[6][6] = 1
comodos[6][7] = 1

#Cozinha
comodos[7][6] = 1
comodos[7][7] = 1
comodos[7][8] = 1
comodos[7][9] = 1

#Sala de Jantar
comodos[8][7] = 1
comodos[8][8] = 1
comodos[8][9] = 1

#Sala
comodos[9][6] = 1
comodos[9][7] = 1
comodos[9][8] = 1
comodos[9][9] = 1

comodostxt = ['Suite Master', 'Closet Master', 'Closet Quarto 3', 'Quarto 3', 'Quarto 2', 'Media', 'Escritorio', 'Cozinha', 'Sala de Jantar', 'Sala']

'''
comodos = {0 'Suite Master':    ['Closet Master', 'Media'],
           1 'Closet Master':   ['Closet Quarto 3', 'Quarto 3', 'Quarto 2', 'Media', 'Suite Master'],
           2 'Closet Quarto 3': ['Quarto 3', 'Quarto 2', 'Closet Master'],
           3 'Quarto 3':        ['Quarto 2', 'Closet Master', 'Closet Quarto 3'],
           4 'Quarto 2':        ['Quarto 3', 'Closet Master', 'Closet Quarto 3'],
           5 'Media':           ['Suite Master', Closet Master', 'Escritório'],
           6 'Escritório':      ['Media', 'Cozinha'],
           7 'Cozinha':         ['Sala de Jantar', 'Escritório', 'Sala'],
           8 'Sala de Jantar':  ['Cozinha', 'Sala'],
           9 'Sala':            ['Escritório', 'Cozinha', 'Sala de Jantar'],
          }
'''

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
    imgPath = "imagens/Trios/" + pos[0] + "-" + pos[1] + '-' + pos[2] + ".png"
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
  try:
    imgPath = "imagens/" + pos_rot + "-" + pos_rep1 + '-' + pos_rep2 + ".png"
    img2 = ImageTk.PhotoImage(Image.open(imgPath))
  except:
    imgPath = "imagens/" + pos_rot + "-" + pos_rep2 + '-' + pos_rep1 + ".png"
    img2 = ImageTk.PhotoImage(Image.open(imgPath))
  imgLabel.configure(image=img2)
  imgLabel.image = img2


label = Label(text="_________________________________________________________________")
label.pack()

label = Label(text="\nSelecione o cômodo em será instalado o roteador:")
label.pack()


router_options = []
for item in comodostxt:
    router_options.append(item)
clicked = StringVar()
#clicked.set(router_options[0])

OptionMenu(root, clicked, *router_options, command=atualiza_pos_rot).pack(padx=100)



label = Label(text="\nSelecione os cômodos onde serão posicionados os repetidores:")
label.pack()

rep1_options = []
for item in comodostxt:
    rep1_options.append(item)
clicked = StringVar()
#clicked.set(rep1_options[0])
OptionMenu(root, clicked, *rep1_options, command=atualiza_pos_rep1).pack(padx=0)

rep2_options = []
for item in comodostxt:
    rep2_options.append(item)
clicked = StringVar()
#clicked.set(rep2_options[0])
OptionMenu(root, clicked, *rep2_options, command=atualiza_pos_rep2).pack(padx=100)

rep3_options = []
for item in comodostxt:
    rep3_options.append(item)
clicked = StringVar()
#clicked.set(rep3_options[0])
OptionMenu(root, clicked, *rep3_options, command=atualiza_pos_rep3).pack(padx=100)


label = Label(text="_________________________________________________________________")
label.pack()
label = Label(text="\nDado um celular acessando a internet no cômodo:")
label.pack()

device_options = []
for item in comodostxt:
    device_options.append(item)
clicked = StringVar()
clicked.set(device_options[0])

OptionMenu(root, clicked, *device_options).pack(padx=100)



routeLabel = Label(root, text="\nA rota percorrida do roteador até o dispositivo foi:", pady=5)
routeLabel.pack()

melhorCaminho = Label(root, text="", wraplength=200, pady=5, padx=20).pack()

resultLabel = Label(root, text="\nEstá satisfeito com o resultado? Se não, reposicione os dispositivos de internet\n", pady=5)
resultLabel.pack()


root.mainloop()
