import pandas as pd
import emoji

acervo = pd.read_csv("Acervo GG - Página1.csv",
                     delimiter=";",
                     encoding='utf-8-sig')

nome = ""
preco = ""
autor = ""
genero = ""
estado = ""
indice = 0
out = ""
outs = []

with open("Acervo GG - Página1.csv", encoding='utf-8-sig') as file:
  for line in file:
    elements = line.strip().split(",")
    nome = elements[0]  
    autor = elements[1] 
    genero = elements[2] 
    estado = elements[3]
    preco = elements[4]
    print (nome, autor, genero, estado, preco)
    out = "\n %s \n By: %s \n %s\N{money with wings} \n Se tiver interesse comenta 'Quero' aqui em baixo!\N{sparkling heart}\U0001F431 \n\n Especificações do livro\U0001F50D \n\n Estado: %s \n Genero: %s \n " % (nome, autor, preco, estado, genero)
    outs.append(out)

with open("output.txt", "w") as file:
  # Write some text to the file
  for string in outs:
    file.write((string.replace('//', ', ')).replace('"', ''))

print("Data has been written to the file.")
