# Redes Mesh

**Número da Lista**: 2 <br>
**Conteúdo da Disciplina**: Grafos 2 <br>

## Alunos

| Matrícula  | Aluno                  |
| ---------- | ---------------------- |
| 16/0144132 | Rodrigo Fernandes      |
| 18/0022962 | Luís Guilherme G. Lins |

## Link para vídeo explicativo:

https://www.loom.com/share/f8ec74d0bc02428699eb569b6a93df7e

## Sobre

&nbsp;&nbsp;&nbsp;&nbsp; Uma rede mesh é uma alternativa ao protocolo LAN (Local Area Network) padrão. Ela é composta de vários nós (roteadores) que, juntos, exercem a função de uma grande e única rede, possibilitando a conexão do usuário com qualquer um dos nós. Os nós fazem a função de repetidores e cada nó está ligado a um ou mais outros nós. Desta maneira é possível transmitir mensagens de um nó a outro por diferentes caminhos. Este aplicativo tem como objetivo simular uma conexão de um celular com um roteador, por intermédio de repetidores. Implementaremos o algoritmo de Prim para descobrir a menor rota entre os dois.

## Screenshots

![](Main.png) ![](End.png)

## Requisitos

Para a execução do programa, se faz necessária a instalação dos seguintes componentes via terminal:

- python3-pil
- python3-pil.imagetk

A instalação pode ser realizada com o seguinte comando: <br>
`sudo apt-get install python3-pil python3-pil.imagetk`

## Instalação

**Linguagem**: Python 3.X
Para a instalação serão necessários:

- Git
- Ambiente capaz de interpretar Python 3.X

### Linux

No terminal, escolha o local no qual a pasta será instalada e execute:

1. `git clone https://github.com/projeto-de-algoritmos/Grafos2_Redes-Mesh.git`
2. `cd Grafos2_Redes-Mesh`

Ou

1. Faça o download do projeto zipado a partir do GitHub
2. Descompacte a pasta no destino _path_ escolhido
3. Utilizado o terminal, acesse o local onde a pasta foi descompactada
4. `cd path/Grafos2_Redes-Mesh`

## Uso

1. No diretório do projeto, execute, com Python 3.X, o arquivo de extensão .py com o comando: <br><br>
   `python3 redeMesh.py` <br><br>
2. Se a instalação foi bem sucedida, a seguinte janela foi aberta: <br><br>
   ![](Main.png) <br><br>
3. Tendo a imagem da planta da casa como referência visual, escolha os cômodos nos quais estão: o roteador, três repetidores e o celular. <br><br>
   ![](Select.png) <br><br>
4. O aplicativo irá calcular a distância percorrida do sinal. <br><br>
   ![](End.png) <br><br>
5. O passo 4 deve ser repetido caso a estação inicial seja alterada. <br><br>
