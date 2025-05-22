import mysql.connector
 
conection = mysql.connector.connect(
    #host, user, password, database
    host = "localhost",
    user = "root",
    password = "@Drumstick28",
    database = "ecommerce"
 
)
#crear cursor#
cursor = conection.cursor()


 #tabla productos
cursor.execute("SELECT nombre, descripcion, precio FROM productos;")
products = cursor.fetchall()
for aux in products:
    print(f"Nombre: {aux[0]}, Descripción: {aux[1]}, Precio: {aux[2]} ")
    

#tabla categoria
cursor.execute(f"SELECT categoria_id, nombre FROM categoria;")
category = cursor.fetchall()
for aux in category:
    print(f"Categoria id: {aux[0]}, Nombre: {aux[1]} ")


#tabla usuario
cursor.execute(f"SELECT nombre, email, direccion, telefono FROM usuario;")
user = cursor.fetchall()
for au in user:
    print(f" Nombreuser: {au[0]}, mail: {au[1]}, name: {au[2]}, telefono: {au[3]} ")



#tabla factura
cursor.execute(f"SELECT factura_id, usuario_id, fecha_factura, total_factura FROM factura;")
factura = cursor.fetchall()
for aux in factura:
    print(f"Factura id: {aux[0]}, usuario id: {aux[1]}, fecha: {aux[2]}, total: {aux[3]} ")




#tabla ticket de entrega
cursor.execute(f"SELECT ticket_id, factura_id, direccion_entrega, estado, fecha_entrega FROM ticket_de_entrega;")
ticket_de_entrega = cursor.fetchall()
for aux in ticket_de_entrega:
    print(f"Ticket id: {aux[0]}, factura id: {aux[1]}, direccion: {aux[2]}, estado: {aux[3]}, fecha: {aux[4]} ")



#tabla pago
cursor.execute(f"SELECT pago_id, factura_id, metodo_pago, estado_pago FROM pago;")
pago = cursor.fetchall()
for aux in pago:
    print(f"Pago id: {aux[0]}, factura id: {aux[1]}, metodo de pago: {aux[2]}, estado: {aux[3]} ")


#tabla detalle_factura
cursor.execute(f"SELECT detalle_id, factura_id, producto_id, cantidad_producto, precio_unitario, subtotal_factura FROM detalle_factura;")   
detalle_factura = cursor.fetchall()
for aux in detalle_factura:
    print(f"Detalle id: {aux[0]}, factura id: {aux[1]}, producto id: {aux[2]}, cantidad: {aux[3]}, precio unitario: {aux[4]}, subtotal: {aux[5]} ") 


 
 
cursor.close()
conection.close()
    

