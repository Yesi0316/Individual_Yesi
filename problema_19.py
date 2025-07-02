print("Ejercicio #19") #Temperaturas

temperaturas= [float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")) ]

temp_mayor= [temperaturas[0],temperaturas[1],temperaturas[2],temperaturas[3],temperaturas[4],temperaturas[5],temperaturas[6],temperaturas[7],temperaturas[8],temperaturas[9]]
temp_menor= [temperaturas[0],temperaturas[1],temperaturas[2],temperaturas[3],temperaturas[4],temperaturas[5],temperaturas[6],temperaturas[7],temperaturas[8],temperaturas[9]]

temp_mayor.sort
im= (temperaturas[0]>30)+(temperaturas[1]>30)+(temperaturas[2]>30)+(temperaturas[3]>30)+(temperaturas[4]>30)+(temperaturas[5]>30)+(temperaturas[6]>30)+(temperaturas[7]>30)+(temperaturas[8]>30)+(temperaturas[9]>30)
temp_menor.sort
print(temp_menor)
im2=(temperaturas[0]<10)+(temperaturas[1]<10)+(temperaturas[2]<10)+(temperaturas[3]<10)+(temperaturas[4]<10)+(temperaturas[5]<10)+(temperaturas[6]<10)+(temperaturas[7]>30)+(temperaturas[8]<10)+(temperaturas[9]<10)
del temp_menor[(im2-1)+1:-1]

print(f"Las temperaturas mayores a 30 son: {temp_mayor}\n Las menores a 10 son: {temp_menor}")
