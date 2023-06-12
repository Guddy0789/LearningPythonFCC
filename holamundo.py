print("hola, mundo!")
num = 15
num

dictionario={"a":1,"b":2,"c":3,"d":4}

print(dictionario)
#imprimir clave, nota: el valor q se le asigne no necesariamente es VALOR/VALUE
for loqsea in dictionario:
    print(loqsea)
    
#imprimir solo el valor
for valooor in dictionario.values():
    print(valooor)
#imprimir clave y valor
print("Imprimir dictionary")
for clave,valor in dictionario.items():
    print(clave,"-",valor)
print("EJEMPLO WHILE")
#While

x=10
while x <= 20:
    print(x)
    x+=1

print("aprendiendo funciones")
def suma(a,b):
    return a+b

result = suma(2,3)
print("resultado:",result)

#FIBOONACCI PYTHON
print("fibo fibo fibonacci")
def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print("resultado fibo: ",fibo(2))
n_terms = 2
for i in range(1, n_terms + 1):
    print(fibo(i), end=" ")

print("--------factorial------")
#Funcion factorial
print("--------factorial------")
def facto(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * facto(n-1)        

f_terms = 5
for i in range(1, f_terms + 1):
    print("-",facto(i), end=" ")
