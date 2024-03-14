numeroProcurado = 10
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

listaSequencia = []
for x in range(numeroProcurado):
    listaSequencia.append(fibonacci(x))

print(listaSequencia)

if numeroProcurado in listaSequencia:
    print("O número pertence a sequência")
else:
    print("O número não pertence a sequência")
