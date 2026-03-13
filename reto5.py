# Una empresa en crecimiento ha perdido el control de su
#  base de datos de clientes y contactos, ya que
#  la información se encuentra dispersa y sin
#  organización. Se requiere diseñar un sistema en consola que permita:
# Agregar nuevos contactos (nombre, teléfono, email).
# Buscar contactos por nombre.
# Actualizar o eliminar información existente.
# Guardar y cargar los datos desde un archivo para mantener la persistencia de la información.
import csv
import uuid
import os
nombre_archivo = "contactos.csv"

if not os.path.exists(nombre_archivo):
    with open(nombre_archivo, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["id", "nombre", "telefono", "email"])

def generar_id():
    return str(uuid.uuid4())

def obtener_contactos(nombre):
    contactos = []
    with open(nombre_archivo,"r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for contacto in csv_reader:
            if nombre.lower() in contacto["nombre"].lower():
                contactos.append(contacto)
    return contactos


def agregar_contacto(nombre,telefono,email):
    id = generar_id()
    with open(nombre_archivo,"a",newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([id,nombre,telefono,email])

def actualizar_contacto(id,nombre,telefono,email):
    contactos = []
    with open(nombre_archivo,"r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for contacto in csv_reader:
            if contacto["id"] == str(id):
                contacto["nombre"] = nombre
                contacto["telefono"] = telefono
                contacto["email"] = email
            contactos.append(contacto)
    with open(nombre_archivo,"w",newline="") as new_file:
        campos = ["id","nombre","telefono","email"]
        csv_writer = csv.DictWriter(new_file,fieldnames=campos)
        csv_writer.writeheader()
        csv_writer.writerows(contactos)

def borrar_contacto(id):
    contactos = []
    with open(nombre_archivo,"r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for contacto in csv_reader:
            if contacto["id"] != str(id):
                contactos.append(contacto)
    with open(nombre_archivo,"w",newline="") as new_file:
        campos = ["id","nombre","telefono","email"]
        csv_writer = csv.DictWriter(new_file,fieldnames=campos)
        csv_writer.writeheader()
        csv_writer.writerows(contactos)


ejecutar = True
while ejecutar:
    print("1.Agregar contacto")
    print("2.Buscar contacto")
    print("3.Actualizar contacto")
    print("4.Eliminar contacto")
    print("5.Salir")
    eleccion = input("Elige una opcion:")
    if eleccion == '1':
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        agregar_contacto(nombre, telefono, email)
        print("Contacto agregado")
    
    if eleccion == '2':
        nombre_buscar = input("Nombre a buscar: ")
        contactos = obtener_contactos(nombre_buscar)
        if contactos:
            for contacto in contactos:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
        else:
            print("No se encontraron contactos.")

    if eleccion == '3':
        nombre_buscar = input("Nombre del contacto a actualizar: ")
        contactos = obtener_contactos(nombre_buscar)
        if contactos:
            for indice, contacto in enumerate(contactos):
                print(f"{indice+1}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
            opcion = int(input("Elige el número del contacto a actualizar: ")) - 1
            contacto = contactos[opcion]
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nuevo_email = input("Nuevo email: ")
            actualizar_contacto(contacto["id"], nuevo_nombre, nuevo_telefono, nuevo_email)
            print("Contacto actualizado")
        else:
            print("No se encontraron contactos.")
    if eleccion == '4':
        nombre_buscar = input("Nombre del contacto a eliminar: ")
        contactos = obtener_contactos(nombre_buscar)
        if contactos:
            for indice, contacto in enumerate(contactos):
                print(f"{indice+1}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
            opcion = int(input("Elige el número del contacto a eliminar: ")) - 1
            contacto = contactos[opcion]
            borrar_contacto(contacto["id"])
            print("Contacto borrado")
        else:
            print("No se encontraron contactos.")
    if eleccion == '5':
        ejecutar = False
    