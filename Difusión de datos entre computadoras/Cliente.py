import socket
import select

# Lista de nodos (computadoras) a las que enviar el mensaje
nodos = ['192.168.1.1', '192.168.1.2', '192.168.1.3']

# Crear un socket para cada nodo
sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in nodos]

# Conectar cada socket a su nodo correspondiente
for nodo, sock in zip(nodos, sockets):
    sock.connect((nodo, 12345))  # Asumiendo que el puerto 12345 está abierto en cada nodo

# Enviar un mensaje a cada nodo
for sock in sockets:
    sock.sendall(b'Hola, nodo!')

# Esperar una respuesta de cada nodo
for sock in sockets:
    data = sock.recv(1024)
    print(f'Respuesta recibida: {data}')

# Cerrar todos los sockets
for sock in sockets:
    sock.close()
