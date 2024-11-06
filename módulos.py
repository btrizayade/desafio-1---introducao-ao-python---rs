# exemplo de importação de módulo padrão
import math

raiz_quadrada = math.sqrt(25)
print(f"a raiz quadrada de 25 é {raiz_quadrada}")

from math import sqrt

raiz_quadrada = sqrt(25)
print(f"a raiz quadrada de 25 é {raiz_quadrada}")

# exemplo de criação e utilização de módulo personalizado
import meu_módulo

mensagem = meu_módulo.saudacao("Bia")
resultado_dobro = meu_módulo.dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")

from meu_módulo import saudacao, dobro
mensagem = saudacao("Bia")
resultado_dobro = dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")