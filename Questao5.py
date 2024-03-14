stringX = "Target"
print("String Normal:", stringX)


inverte = []
for n in stringX: #Transforma a string em uma lista
    inverte += n

size = len(inverte) #Tamanho da lista: Quantas letras tem?
stringInvertida = ""

for l in range(size): #Percorre a lista da frente para traz. Do final para o começo
    stringInvertida += inverte[size - 1]
    size -= 1

print("String Normal:", stringInvertida)