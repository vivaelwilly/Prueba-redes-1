import os
from tkinter import Variable

# Inicialización de variables 
x = 0
y = 0
os.system("clear")

# Base de datos vacía
dispositivos_por_campus = {
    "zona core": [],
    "campus uno": [],
    "campus matriz": [],
    "dual stack": [],
    "sector outsourcing": []
}

print("que quieres hacer? ")
print("1. Ver los dispositivos. \n2. Ver los campus. \n3. Añadir dispositivo. \n4. Añadir campus.")
selector = input("elegir una opcion: ")

# Opción 1: Ver dispositivos
if int(selector) == 1:
    os.system("clear")
    y = 1
    print("elijir un campus \n")
    for campus_nombre in dispositivos_por_campus.keys():
        print(f"{y}. {campus_nombre}")
        y += 1
    
    selector = input("\n Elija una opcion: ")
    x = int(selector) - 1
    campus_seleccionado = list(dispositivos_por_campus.keys())[x]
    
    os.system("clear")
    print(f"\n--- Dispositivos en {campus_seleccionado} ---")
    for dispositivo in dispositivos_por_campus[campus_seleccionado]:
        print(f"{dispositivo['tipo']}: {dispositivo['nombre']} | VLAN: {dispositivo['vlan']} | IP: {dispositivo['ip']} | Jerarquía: {dispositivo.get('jerarquia','')} | Servicios: {', '.join(dispositivo.get('servicios', []))}")

# Opción 2: Ver campus 
elif int(selector) == 2:
    os.system("clear")
    y = 1
    for campus_nombre in dispositivos_por_campus.keys():
        print(f"{y}. {campus_nombre}")
        y += 1

# Opción 3: Añadir dispositivo 
elif int(selector) == 3:
    os.system("clear")
    y = 1
    print("¿Donde agregar nuevo dispositivo? \n")
    for campus_nombre in dispositivos_por_campus.keys():
        print(f"{y}. {campus_nombre}")
        y += 1
    
    selector = input("\n Elija una opcion: ")
    x = int(selector) - 1
    campus_seleccionado = list(dispositivos_por_campus.keys())[x]
    
    os.system("clear")
    print("elija un dispositivo: \n \n1. Router. \n2. Switch. \n3. Switch multicapa. \n4. PC. \n5. Servidor. \n6. Impresora.")
    variable1 = input("Elija su opcion: ")
    
    tipos = {
        "1": "ROUTER",
        "2": "SWITCH",
        "3": "SWITCH_MULTICAPA",
        "4": "PC",
        "5": "SERVIDOR",
        "6": "IMPRESORA"
    }
    
    os.system("clear")
    print("Agregue el nombre de su dispositivo")
    nombre = input("Agregue su nombre: ")
    
    print("Agregue la dirección IP del dispositivo:")
    ip = input("IP: ")
    
    print("Agregue el número de VLAN (deje en blanco si no aplica):")
    vlan = input("VLAN: ")

    print("Elija una jerarquía: \n1. Núcleo\n2. Distribución\n3. Acceso")
    jerarquia_opcion = input("Opción: ")
    jerarquias = {
        "1": "Núcleo",
        "2": "Distribución",
        "3": "Acceso"
    }
    jerarquia = jerarquias.get(jerarquia_opcion, "")

    servicios = []
    if variable1 == "1":  # Router
        while True:
            print("Servicios para Router: \n1. Enrutamiento\n2. Salir")
            serv = input("Opción: ")
            if serv == "1":
                servicios.append("Enrutamiento")
            elif serv == "2":
                break

    elif variable1 == "2":  # Switch
        while True:
            print("Servicios para Switch: \n1. Datos\n2. VLAN\n3. Trunking\n4. Salir")
            serv = input("Opción: ")
            if serv == "1":
                servicios.append("Datos")
            elif serv == "2":
                servicios.append("VLAN")
            elif serv == "3":
                servicios.append("Trunking")
            elif serv == "4":
                break

    elif variable1 == "3":  # Switch multicapa
        while True:
            print("Servicios para Switch Multicapa:\n1. Datos\n2. VLAN\n3. Trunking\n4. Enrutamiento\n5. Salir")
            serv = input("Opción: ")
            if serv == "1":
                servicios.append("Datos")
            elif serv == "2":
                servicios.append("VLAN")
            elif serv == "3":
                servicios.append("Trunking")
            elif serv == "4":
                servicios.append("Enrutamiento")
            elif serv == "5":
                break

    dispositivos_por_campus[campus_seleccionado].append({
        "tipo": tipos[variable1],
        "nombre": nombre,
        "ip": ip,
        "vlan": vlan,
        "jerarquia": jerarquia,
        "servicios": servicios
    })
    print("\n¡Dispositivo agregado con éxito!")

# Opción 4: Añadir campus 
elif int(selector) == 4:
    os.system("clear")
    print("Ingrese el nombre del nuevo campus:")
    nuevo_campus = input("Nombre: ")
    dispositivos_por_campus[nuevo_campus] = []
    print(f"\n¡Campus {nuevo_campus} creado!")
