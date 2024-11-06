# coleção ordenada (lista) e imutável de elementos, usa parêntesis
# criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)

print("minha tupla", minha_tupla)
print("minha tupla [0]", minha_tupla[0])
print("minha tupla [2]", minha_tupla[2])
print("minha tupla [-1]", minha_tupla[-1])

# método count
contagem = minha_tupla.count(2)
print("quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(3)
print("índice da primeira ocorrÊncia do elemento 3:", indice)