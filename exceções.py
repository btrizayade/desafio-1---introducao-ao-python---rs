print("Exemplo de captura de exceções")
while True:
    try:
        numero = int(input("Insira um número inteiro: "))
        resultado = 10/numero
        print(f"Resultado {resultado}")
    except ValueError as e:
        print(f"Erro de value error: {e}")
        raise ValueError("Tipo de variáveis incompatíveis")
    except Exception as e:
        print(f"Erro: {e}")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operação finalizada com sucesso.")
