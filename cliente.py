import socket

def client_program():
    host = socket.gethostname() # ya que ambos códigos se están ejecutando en la misma PC
    port = 5000 # número de puerto del servidor de sockets
    #Instanciar
    client_socket = socket.socket()
    #Conectar al servidor
    client_socket.connect((host, port))

    message_count = 0
    max_messages = 5  # Número máximo de mensajes antes de terminar

    while message_count < max_messages:
        message = input(" -> ") # tomar la entrada
        client_socket.send(message.encode()) # enviar mensaje

        if message.lower().strip() == 'bye':
            break

        data = client_socket.recv(1024).decode() # recibir respuesta
        print('Recibido del servidor: ' + data) # mostrar en la terminal

        message_count += 1 #conteo de mensajes

    client_socket.close() # cerrar la conexión

if __name__ == '__main__':
    client_program()