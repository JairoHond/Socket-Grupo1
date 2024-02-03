import socket

def server_program():
    # obtener el nombre del host
    host = socket.gethostname()
    # iniciar el número de puerto por encima de 1024
    port = 5000

    server_socket = socket.socket() # obtener la instancia

    # observa de cerca. La función bind() toma una tupla como argumento
    server_socket.bind((host, port)) # enlazar la dirección del host y el puerto juntos

    # configurar cuántos clientes puede escuchar el servidor simultáneamente
    server_socket.listen(2)
    conn, address = server_socket.accept()# aceptar nueva conexión
    print("Conexión desde: " + str(address))

    message_count = 0
    max_messages = 5  # Número máximo de mensajes antes de terminar
    #Validamos la condicion que no se pase del numero maximo de mensajes permitidos
    while message_count < max_messages:
        # recibir flujo de datos. no aceptará paquetes de datos mayores de 1024 bytes
        data = conn.recv(1024).decode()
        if not data: # si no se recibe ningún dato, romper
            break
        print("Del usuario conectado: " + str(data))

        if data.lower().strip() == 'bye':
            break

        message = input(' -> ')
        conn.send(message.encode())# enviar datos al cliente
        message_count += 1

    conn.close()#cerrar la conexion

if __name__ == '__main__':
    server_program()