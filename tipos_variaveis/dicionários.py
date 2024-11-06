# criando um dicionário de exemplo
pessoa = {"nome": "Maria", "idade": 25, "cidade": "Salvador"}

# exibindo o dicionário
print("meu dicionário de exemplo", pessoa)

# acessando valores por chave
print("nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("cidade:", pessoa["cidade"])
pessoa["sobrenome"] = "Silva"
print("sobrenome:", pessoa["sobrenome"])

# removendo um par chave-valor
del pessoa["sobrenome"]

# métodos: keys(), values(), items()
# keys()
chaves = list(pessoa.keys())
print("chaves do dicionário: ", chaves)
print("chaves do dicionário: ", chaves[0])

# values()
valores = list(pessoa.values())
print("valores do dicionário: ", valores)

#items
itens = list(pessoa.items())
print("pares chave-valor do dicionário: ", itens)
print("primeira chave-valor: %s = %s" (itens[0][0],itens[0][1]))