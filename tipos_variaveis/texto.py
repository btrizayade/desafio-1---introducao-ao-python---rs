# declaração
nome_completo = "Beatriz Ayade á ! / _"
# três aspas pulam linha
nome_completo_aspas = """Beatriz
Ayade""" ''''''
nome_completo_quebra = "Beatriz \
Ayade"
nome = "Beatriz"
sobrenome = "Ayade"

# formatação
print("Nome completo (1a forma):", nome_completo)
# concatenação (+) não tem espaço automático
print("Nome completo (2a forma): " + nome_completo)
print("Nome completo (3a forma):" + " Beatriz" + " " + " Ayade")
print("Nome completo (4a forma):" + " Beatriz", "Ayade")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
# forma mais segura:
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
# forma mais visualmente agradável:
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))
