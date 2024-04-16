import socket

# Crear un socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a una dirección y un puerto
sock.bind(('0.0.0.0', 12345))  # Escucha en todas las interfaces de red, puerto 12345

# Escuchar conexiones entrantes
sock.listen()

while True:
    # Aceptar una conexión entrante
    conn, addr = sock.accept()
    print(f'Conexión establecida desde {addr}')

    # Recibir un mensaje del cliente
    data = conn.recv(1024)
    print(f'Mensaje recibido: {data}')

    # Enviar una respuesta al cliente
    conn.sendall(b'Mensaje recibido!')

    # Cerrar la conexión
    conn.close()
