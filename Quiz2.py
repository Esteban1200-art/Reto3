meses = int(input("¿Cuántos meses desea analizar? "))

# solicitar las variables antes del cliclo
gasto = float(input("Gasto del mes 1: "))
total = gasto #el acumulado que inicia en el primer mes
mayor = gasto #va a comparar los valores para definir el maSyor
menor = gasto #va a comparar los valores para definir el menor

# Usamos el for para se cumpla elfuncionamiento segun lo que requiere el usuario
for i in range(2, meses + 1): #inicia en 2 porque el primer mes ya se ingreso
    gasto = float(input(f"Gasto del mes {i}: "))#ingresa el gasto del mes de la variable i
    total = total+gasto # la suma de los meses ingresados 
    if gasto > mayor: #compara el gasto del mes con el mayor registrado
        mayor = gasto 
    if gasto < menor:#compara el gasto del mes con el menor registrado
        menor = gasto

print("\n RESULTADOS ")
print("Gasto total:", total)
print("Promedio:", total/meses)#IMPRIME EL PROMEDIO DE GASTOS dependiendo de los meses que se ingresaron
print("Mayor gasto:", mayor)#IMPRIME EL VALOR MAS GRANDE DENTRO DEL LOS GASTOS 
print("Menor gasto:", menor)#IMPRIME EL VALOR MAS PEQUEÑO DENTRO DEL LOS GASTOS
print("Diferencia:", mayor-menor)#IMPRIME LA DIFERENCIA ENTRE EL MAYOR Y EL MENOR
