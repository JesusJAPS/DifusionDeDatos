import random

def infectar_nodos(nodos, enfoque):
    # Seleccionamos un nodo al azar para infectar
    nodo_infectado = random.choice(list(nodos.keys()))
    nodos[nodo_infectado] = 'infectado'

    # Continuamos hasta que todos los nodos estén infectados
    while 'sano' in nodos.values():
        for nodo in nodos:
            if nodos[nodo] == 'infectado':
                # Enfoque pull: los nodos sanos se infectan al interactuar con un nodo infectado
                if enfoque == 'pull':
                    for otro_nodo in nodos:
                        if nodos[otro_nodo] == 'sano':
                            nodos[otro_nodo] = 'infectado'
                            break
                # Enfoque push: los nodos infectados infectan a los nodos sanos
                elif enfoque == 'push':
                    for otro_nodo in nodos:
                        if nodos[otro_nodo] == 'sano':
                            nodos[otro_nodo] = 'infectado'
                            break
                # Enfoque pull-push: combinación de ambos enfoques
                elif enfoque == 'pull-push':
                    for otro_nodo in nodos:
                        if nodos[otro_nodo] == 'sano':
                            nodos[otro_nodo] = 'infectado'
                            break
    return nodos

# Crear una red de 100 nodos
nodos = {i: 'sano' for i in range(100)}

# Simular la propagación de la infección con diferentes enfoques
nodos_infectados_pull = infectar_nodos(nodos.copy(), 'pull')
nodos_infectados_push = infectar_nodos(nodos.copy(), 'push')
nodos_infectados_pull_push = infectar_nodos(nodos.copy(), 'pull-push')

print("Nodos infectados con enfoque pull:", nodos_infectados_pull)
print("Nodos infectados con enfoque push:", nodos_infectados_push)
print("Nodos infectados con enfoque pull-push:", nodos_infectados_pull_push)


