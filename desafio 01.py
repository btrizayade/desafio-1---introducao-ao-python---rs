def adicionar_contato(contatos, telefone, email, nome_contato="contato padrão", favoritado=False):
    contato = {"contato": nome_contato, "telefone": telefone, "email": email, "favoritado": favoritado}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✅" if contato["favoritado"] else " "
        nome_contato = contato["contato"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} - {telefone} - {email}")
    return

def editar_contato(contatos, indice_contato, nome_atualizado, telefone_atualizado, email_atualizado):
    indice_contato_atualizado = int(indice_contato) - 1
    if 0 <= indice_contato_atualizado < len(contatos):
        # Editando o contato
        if nome_atualizado:
            contatos[indice_contato_atualizado]["contato"] = nome_atualizado
        if telefone_atualizado:
            contatos[indice_contato_atualizado]["telefone"] = telefone_atualizado
        if email_atualizado:
            contatos[indice_contato_atualizado]["email"] = email_atualizado
        print(f"Contato {indice_contato} atualizado com sucesso!")
    else:
        print("Índice de contato inválido.")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        # Marcar/desmarcar como favorito
        contatos[indice_contato_ajustado]["favoritado"] = not contatos[indice_contato_ajustado]["favoritado"]
        status = "favoritado" if contatos[indice_contato_ajustado]["favoritado"] else "desfavoritado"
        print(f"Contato {indice_contato} foi {status} com sucesso!")
    else:
        print("Índice de contato inválido.")
    return

def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        del contatos[indice_contato_ajustado]
        print(f"Contato {indice_contato} deletado com sucesso!")
    else:
        print("Índice de contato inválido.")
    return

def ver_contatos_favoritos(contatos):
    print("\nLista de contatos favoritos:")
    favoritos = [contato for contato in contatos if contato["favoritado"]]
    if favoritos:
        for indice, contato in enumerate(favoritos, start=1):
            print(f"{indice}. {contato['contato']} - {contato['telefone']} - {contato['email']}")
    else:
        print("Nenhum contato favorito.")
    return

contatos = []
while True:
    print("\nMenu")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Favoritar contato")
    print("5. Deletar contato")
    print("6. Ver lista de contatos favoritos")
    print("7. Sair")

    escolha = input("Insira o número do que deseja fazer: ")

    if escolha == "1":
        nome_contato = input("Insira o nome do contato que deseja adicionar: ")
        telefone = input("Insira o telefone do contato: ")
        email = input("Insira o e-mail do contato: ")
        adicionar_contato(contatos, nome_contato, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Insira o número do contato que deseja editar: ")
        nome_atualizado = input("Novo nome (deixe vazio para não alterar): ")
        telefone_atualizado = input("Novo telefone (deixe vazio para não alterar): ")
        email_atualizado = input("Novo e-mail (deixe vazio para não alterar): ")
        editar_contato(contatos, indice_contato, nome_atualizado, telefone_atualizado, email_atualizado)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Insira o número do contato que deseja favoritar/desfavoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input("Insira o número do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)

    elif escolha == "6":
        ver_contatos_favoritos(contatos)

    elif escolha == "7":
        print("Programa finalizado")
        break

    else:
        print("Opção inválida. Tente novamente.")
