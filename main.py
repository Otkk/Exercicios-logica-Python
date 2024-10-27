#1
realCliente = float(input('Quantos reais você quer cambiar para dolar?'))
print (realCliente/3.12)


#2
DolarCliente = float(input('Quantos dolares você quer cambiar para real?'))
print (DolarCliente*3.12)


#3
altParede = float(input('Qual a altura(em metros) da parede?'))
largParede = float(input('Qual a largura(em metros) da parede?'))
altAzuleijo = float(input('Qual a altura(em metros) do azuleijo?'))
largAzuleijo = float(input('Qual a largura(em metros) do azuleijo?'))
area = altParede * largParede
areaAzuleijo = altAzuleijo * largAzuleijo
print (area / areaAzuleijo) 


#4
ladoA = float(input("Digite o tamanho (em metros) do lado A do retangulo: "))
ladoB = float(input('Digite o tamanho (em metros) do lado B do retangulo: '))
area = ladoA * ladoB
perimetro = (2 * ladoA) + (2 * ladoB)
print (f'A area do retangulo é {area} metros, enquanto seu perimetro é {perimetro} metros')


#5
m = float(input('Digite o peso da pessoa em kg: '))
h = float(input('Digite a altura da pessoa em m: '))
imc = m / (h**2)
print (f'O IMC da pessoa é {imc}')
#6
import numpy as np
pi = np.pi
raio = float(input('digite o valor do raio: '))
volume = (4/3)*pi*raio*3
area = 4*pi*raio*2
print(f'O volume da esfera é {volume} e a area é de {area} ')


#8
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))
nota4 = int(input("Digite a nota 4: "))
print (nota1 + nota2 + nota3 + nota4 / 4)

#9
p1 = int(input('Digite a nota da prova do primeiro semestre'))
p2 = int(input('Digite a nota da prova do segundo semestre'))
ativ = int(input('Digite a nota das atividades do semestre:'))
media = (4*p1 + 4*p2 + 2 * ativ)/10
print(f'A média do semestral é {media}')

#10
s0 = 2
v0 = 3
a = 10
t = int (input('digite o valor de tempo: '))
print (s0 + v0*t + 1/2 * a * t**2)