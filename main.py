import mysql.connector
conection=  mysql.connector.connect (

host = "localhost",
user = "root",
password = "Sh01@2024",
database="ecommerce",

)

cursor = conection.cursor()
cursor.execute ("SELECT nombre, email, contrasena, direccion, telefono FROM usuario")

usuario = cursor.fetchall()

for ax in usuario:
    print(f"nombre:{ax[0]}, email:{ax[1]}, contraseña:{ax[2]}, direccion:{ax[3]}, telefono{ax[4]}")

    cursor.close()
    conection.close()