from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Redes Mesh e seu trajeto até os dispositivos")

intro = Label(root, text="\nFoi delegada a você a missão de instalar uma soluçao de internet de uma casa.\nLhe foi informado que à sua disposição há:\nUm roteador e mais dois repetidores Mesh, sendo o posicionamento deles arbitrário por você.\nObs: Quanto menor o número de repetidores percorridos, melhor é a qualidade do sinal.\n")
intro.pack()

imagem = Image.open("planta.png").resize((650, 350), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)
imgLabel = Label(image=imagem)
imgLabel.pack()

# A partir da esquerda, sentido horário
comodos = {'Suite Master':    ['Closet Master', 'Media', 'Varanda'],
           'Closet Master':   ['Closet Quarto 3', 'Quarto 3', 'Quarto 2', 'Media', 'Suite Master'],
           'Closet Quarto 3': ['Quarto 3', 'Quarto 2', 'Closet Master'],
           'Quarto 3':        ['Quarto 2', 'Closet Master', 'Closet Quarto 3'],
           'Quarto 2':        ['Quarto 3', 'Media', 'Closet Master', 'Closet Quarto 3'],
           'Media':           ['Closet Master', 'Quarto 2', 'Escritório', 'Varanda'],
           'Escritório':      ['Media', 'Cozinha', 'Varanda'],
           'Cozinha':         ['Sala de Jantar', 'Escritório', 'Sala'],
           'Sala de Jantar':  ['Cozinha', 'Sala'],
           'Sala':            ['Varanda', 'Escritório', 'Cozinha', 'Sala de Jantar'],
           'Varanda':         []
          }


def atualiza_imagem(*args):
  #print('Detectei mudança de valor')


label = Label(text="_________________________________________________________________")
label.pack()

label = Label(text="\nSelecione o cômodo em será instalado o roteador:")
label.pack()


router_options = []
for item in comodos:
    router_options.append(item)
clicked = StringVar()
clicked.set(router_options[0])
clicked.trace("w", atualiza_imagem)

OptionMenu(root, clicked, *router_options).pack(padx=100)



label = Label(text="\nSelecione o cômodo onde será posicionado o primeiro repetidor:")
label.pack()

rep1_options = []
for item in comodos:
    rep1_options.append(item)
clicked = StringVar()
clicked.set(rep1_options[0])
clicked.trace("w", atualiza_imagem)

OptionMenu(root, clicked, *rep1_options).pack(padx=100)


label = Label(text="\nSelecione o cômodo do segundo repetidor:")
label.pack()

rep2_options = []
for item in comodos:
    rep2_options.append(item)
clicked = StringVar()
clicked.set(rep2_options[0])
clicked.trace("w", atualiza_imagem)

OptionMenu(root, clicked, *rep2_options).pack(padx=100)


label = Label(text="_________________________________________________________________")
label.pack()
label = Label(text="\nDado um celular acessando a internet no cômodo:")
label.pack()

device_options = []
for item in comodos:
    device_options.append(item)
clicked = StringVar()
clicked.set(device_options[0])
clicked.trace("w", atualiza_imagem)

OptionMenu(root, clicked, *device_options).pack(padx=100)



routeLabel = Label(root, text="\nA rota percorrida do roteador até o dispositivo foi:", pady=5)
routeLabel.pack()

melhorCaminho = Label(root, text="", wraplength=200, pady=5, padx=20).pack()

resultLabel = Label(root, text="\nEstá satisfeito com o resultado? Se não, reposicione os dispositivos de internet\n", pady=5)
resultLabel.pack()


root.mainloop()
