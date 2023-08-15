import math

# Definindo os comprimentos dos catetos
cateto_a = 4
cateto_b = 3

# Calculando o quadrado da hipotenusa
quadrado_hipotenusa = cateto_a ** 2 + cateto_b ** 2

# Calculando a hipotenusa usando a raiz quadrada
hipotenusa = math.sqrt(quadrado_hipotenusa)

# Imprimindo o resultado
print(f"A hipotenusa é: {hipotenusa}")
