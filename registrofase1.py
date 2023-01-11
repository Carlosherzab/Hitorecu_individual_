# Datos de entrada
nombre = input("Ingrese el nombre del cliente: ")
apellido = input("Ingrese el apellido del cliente: ")
direccion = input("Ingrese la dirección del cliente: ")
telefono = input("Ingrese el teléfono del cliente: ")
email = input("Ingrese el correo electrónico del cliente: ")
tarjeta = input("Ingrese el número de tarjeta")
 
# Guardando los datos en un diccionario
cliente = {
    "nombre": nombre,
    "apellido":apellido,
    "direccion": direccion,
    "telefono": telefono,
    "email": email,
    "tarjeta": tarjeta
}
 
# Guardando el diccionario en una lista
clientes_registrados = []
clientes_registrados.append(cliente)
 
# Mostrando el mensaje de confirmación
print("El cliente ha sido registrado exitosamente.")
