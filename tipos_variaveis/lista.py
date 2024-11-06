# declaração de uma lista
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# exibindo uma lista
print("minha lista de exemplo", minha_lista)

# exibindo os elementos de uma lista
minha_lista[0] = "python"
print("minha lista de exemplo", minha_lista)
print("minha_lista[0]: ", minha_lista[0])
print("minha_lista[1:7]", minha_lista[1:7])
print("minha_lista[:6]", minha_lista[:6])
print("minha_lista[2:]", minha_lista[2:])

# métodos de lista
# método append() = adiciona um elemento ao final da lista
minha_lista.append(6)
print("após append(6):", minha_lista)

# método index = retorna o índice do primeiro elemento como o valor especificado
indice = minha_lista.index(6)
print("índice do elemento 6 é:", indice)

# método insert = insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("após o insert(2,10):", minha_lista)

# método pop
elemento_removido = minha_lista.pop(3)
print("elemento removido:", elemento_removido)
print("após pop(3):", minha_lista)

# método remove
minha_lista.remove(True)
print("após remove(True):", minha_lista)

# método sort = organiza em ordem crescente (só funciona com um tipo único dentro da lista)
minha_lista.sort()
print("após sort()", minha_lista)

