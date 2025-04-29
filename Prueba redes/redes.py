import os
import json

# Inicialización de variables 
x = 0
y = 0
os.system("clear")


archivo_datos = "dispositivos.txt"


if os.path.exists(archivo_datos):
    with open(archivo_datos, "r") as archivo:
        dispositivos_por_campus = json.load(archivo)
else:
    # Base de datos 
    dispositivos_por_campus = {
        "zona core": [],
        "campus uno": [],
        "campus matriz": [],
        "dual stack": [],
        "sector outsourcing": []
    }

# Función para guardar archivos por zona
def guardar_zonas_separadas():
    if not os.path.exists('zonas'):
        os.makedirs('zonas')
        
    for zona, dispositivos in dispositivos_por_campus.items():
        nombre_archivo = f"zonas/{zona.replace(' ', '_')}.txt"
        with open(nombre_archivo, 'w') as f:
            json.dump(dispositivos, f, indent=4)
        print(f"Archivo de zona creado/actualizado: {nombre_archivo}")

print("¿Qué quieres hacer?")
print("1. Ver los dispositivos.\n2. Ver los campus.\n3. Añadir dispositivo.\n4. Añadir campus.\n5. Generar archivos por zona")
selector = input("Elegir una opción: ")

# Opción 1: Ver dispositivos
if selector == "1":
    os.system("clear")
    y = 1
    print("Elegir un campus\n")
    for campus_nombre in dispositivos_por_campus.keys():
        print(f"{y}. {campus_nombre}")
        y += 1
    
    selector = input("\nElija una opción: ")
    x = int(selector) - 1
    campus_seleccionado = list(dispositivos_por_campus.keys())[x]
    
    os.system("clear")
    print(f"\n--- Dispositivos en {campus_seleccionado} ---")
    for dispositivo in dispositivos_por_campus[campus_seleccionado]:
        print(f"{dispositivo['tipo']}: {dispositivo['nombre']} | VLAN: {dispositivo['vlan']} | IP: {dispositivo['ip']} | Jerarquía: {dispositivo.get('jerarquia','')} | Servicios: {', '.join(dispositivo.get('servicios', []))}")

# Opción 2: Ver campus 
elif selector == "2":
    os.system("clear")
    y = 1
    for campus_nombre in dispositivos_por_campus.keys():
        print(f"{y}. {campus_nombre}")
        y += 1

# Opción 3: Añadir dispositivo 
elif selector == "3":
    os.system("clear")
    y = 1
    print("¿Dónde agregar nuevo dispositivo?\n")
    for campus_nombre in dispositivos_por_campus.keys():
        print(f"{y}. {campus_nombre}")
        y += 1
    
    selector = input("\nElija una opción: ")
    x = int(selector) - 1
    campus_seleccionado = list(dispositivos_por_campus.keys())[x]
    
    os.system("clear")
    print("Elija un dispositivo:\n\n1. Router.\n2. Switch.\n3. Switch multicapa.\n4. PC.\n5. Servidor.\n6. Impresora.")
    variable1 = input("Elija su opción: ")
    
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
    nombre = input("Nombre: ")
    
    print("Agregue la dirección IP del dispositivo:")
    ip = input("IP: ")
    
    print("Agregue el número de VLAN (deje en blanco si no aplica):")
    vlan = input("VLAN: ")

    print("Elija una jerarquía:\n1. Núcleo\n2. Distribución\n3. Acceso")
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
            print("Servicios para Router:\n1. Enrutamiento\n2. Salir")
            serv = input("Opción: ")
            if serv == "1":
                servicios.append("Enrutamiento")
            elif serv == "2":
                break

    elif variable1 == "2":  # Switch
        while True:
            print("Servicios para Switch:\n1. Datos\n2. VLAN\n3. Trunking\n4. Salir")
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

    # Guardar el nuevo estado en el archivo
    with open(archivo_datos, "w") as archivo:
        json.dump(dispositivos_por_campus, archivo, indent=4)

    print("\n¡Dispositivo agregado con éxito!")

# Opción 4: Añadir campus 
elif selector == "4":
    os.system("clear")
    print("Ingrese el nombre del nuevo campus:")
    nuevo_campus = input("Nombre: ")
    dispositivos_por_campus[nuevo_campus] = []

    # Guardar después de añadir el campus
    with open(archivo_datos, "w") as archivo:
        json.dump(dispositivos_por_campus, archivo, indent=4)

    print(f"\n¡Campus {nuevo_campus} creado!")

# Opción 5: Generar archivos por zona
elif selector == "5":
    guardar_zonas_separadas()
    print("\n¡Archivos por zona generados con éxito!")
