import os 
import random
import csv
import time

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []
programa = 0

def menu():
    print("Programa para sueldo de trabajadores\nSeleccione una de las siguientes opciones\n1. Asignar Sueldos Aleatorios\n2. Clasificar Sueldos\n3. Ver Estadisticas\n4. Reporte de Sueldos\n5. Salir del Programa")
    

def asignar_sueldos ():
    sueldos =[]
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo) 
    
    return(sueldos)

def clasificar_sueldo():
    
    menor_sueldo = []
    entre_sueldo = []
    superior_sueldo = []
    
    trabajador_menor = []
    trabajador_entre = []
    trabajador_superior = []
    
    for sueldo in sueldos:
        
        if sueldo < 800000:
            menor_sueldo.append(sueldo)
            
            posicion = sueldos.index(sueldo)
                        
            trabajador_menor.append(trabajadores[posicion])
            
        elif sueldo == 800000 and sueldo <= 2000000:
            entre_sueldo.append(sueldo)
            
            posicion = sueldos.index(sueldo)
            
            trabajador_entre.append(trabajadores[posicion])
            
        elif sueldo > 2000000:
            superior_sueldo.append(sueldo)
            
            posicion = sueldos.index(sueldo)
            
            trabajador_superior.append(trabajadores[posicion])
     
    cantidad_menor = len(menor_sueldo)
    
    cantidad_entre = len(entre_sueldo)
    
    cantidad_superior = len(superior_sueldo)       
    
    print("Lista de sueldos clasificados\n")
    
    print(f"Sueldos menor a $800.000 | TOTAL: {cantidad_menor}\n")
    
    print("Nombre Trabador   Sueldo")
    
    for i in trabajador_menor:
        
        print(f"{trabajador_menor[trabajador_menor.index(i)]}   $ {menor_sueldo[trabajador_menor.index(i)]}")
    
    print ("\n")
        
    print(f"Sueldos entre $800.000 y $2.000.000 | TOTAL: {cantidad_entre}\n")
    
    print("Nombre Trabador   Sueldo")
    
    for i in trabajador_entre:
        
        print(f"{trabajador_entre[trabajador_entre.index(i)]}   $ {entre_sueldo[trabajador_entre.index(i)]}")
    
    print ("\n")
    
    print(f"Sueldos superior a $2.000.000 | TOTAL: {cantidad_entre}\n")
    
    print("Nombre Trabador   Sueldo")
    
    for i in trabajador_superior:
        
        print(f"{trabajador_superior[trabajador_superior.index(i)]}   $ {superior_sueldo[trabajador_superior.index(i)]}")
        
    print("\n")
    
    total_sueldos = sum(sueldos)
    
    print(f"TOTAL SUELDOS: $ {total_sueldos}\n")
    
    

def media_geometrica(data):
    producto = 1
    for valor in data:
        producto *= valor
    
    return producto**(1/len(data))

def estadistica():
    
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    media_geometrica_estadistica = media_geometrica(sueldos)
    
    
    print(f"Mayor Sueldo: $ {max_sueldo}")
    print(f"Menor Sueldo: $ {min_sueldo}")
    print(f"Promedio Sueldos: $ {promedio_sueldos}")
    print(f"Media Geometrica: $ {media_geometrica_estadistica}")
    


def reporte_sueldos():
    
    with open("Reporte_Sueldos.csv", mode = "w") as hoja_trabajadores: 
        print("Nombre Trabajador   Sueldo Base   Descuento Salud   Descuento AFP   Sueldo Liquido")
    
        for i in trabajadores:
            nombre_trabajador = trabajadores[trabajadores.index(i)]
            sueldo_base = sueldos[trabajadores.index(i)]
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud -descuento_afp
            
            print(f"{nombre_trabajador}   {sueldo_base}  {descuento_salud}   {descuento_afp}   {sueldo_liquido}")
            
            escribir = csv.writer(hoja_trabajadores)
            escribir.writerow([nombre_trabajador, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])

def salir_programa ():
    print("Saliendo del Programa...")
    print("Desarollador por Yanira Gonzalez\n Rut: 19.439.498-5")


while programa==0:
    menu()
    
    try:
        opcion = input("Ingrese una opción del menu: ")
    except ValueError:
        print("Ingrese una opcion valida")
    
    if opcion =="1":
        sueldos = asignar_sueldos()
        
    elif opcion == "2":
        clasificar_sueldo()
    
    elif opcion == "3":
        estadistica()
        
    elif opcion == "4":
        reporte_sueldos()
        
    elif opcion == "5":
        salir_programa()
        break
    else:
        print("Ingrese una opcion valida")
      
        
        
        