import numpy as np

def criar_matriz_adjacencia(n_vertices, arestas):
    matriz = np.zeros((n_vertices, n_vertices), dtype=int)
    for (origem, destino) in arestas:
        matriz[origem-1][destino-1] += 1
        matriz[destino-1][origem-1] += 1
    return matriz

def eh_simples(matriz):
    n = len(matriz)
    for i in range(n):
        if matriz[i][i] > 0:
            return False
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] > 1:
                return False
    return True

def identificar_paralelos_lacos(matriz):
    paralelos = []
    lacos = []
    n = len(matriz)
    for i in range(n):
        if matriz[i][i] > 0:
            lacos.append(i + 1)
        for j in range(i + 1, n):
            if matriz[i][j] > 1:
                paralelos.append((i + 1, j + 1))
    return paralelos, lacos

def pendentes_isolados(matriz):
    pendentes = []
    isolados = []
    n = len(matriz)
    for i in range(n):
        grau = sum(matriz[i])
        if grau == 1:
            pendentes.append(i + 1)
        elif grau == 0:
            isolados.append(i + 1)
    return pendentes, isolados

def eh_regular(matriz):
    graus = [sum(linha) for linha in matriz]
    return all(grau == graus[0] for grau in graus)

def eh_completo(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] == 0:
                return False
    return True

n_vertices = int(input("Digite o número de vértices: "))
n_arestas = int(input("Digite o número de arestas: "))
arestas = []

for _ in range(n_arestas):
    origem = int(input("Digite o vértice de origem da aresta: "))
    destino = int(input("Digite o vértice de destino da aresta: "))
    arestas.append((origem, destino))

matriz = criar_matriz_adjacencia(n_vertices, arestas)

print("Matriz de Adjacência:")
print(matriz)

if eh_simples(matriz):
    print("O grafo é simples.")
else:
    print("O grafo não é simples.")

paralelos, lacos = identificar_paralelos_lacos(matriz)
if paralelos:
    print(f"Arestas paralelas: {paralelos}")
else:
    print("Não há arestas paralelas.")
if lacos:
    print(f"Laços: {lacos}")
else:
    print("Não há laços.")

pendentes, isolados = pendentes_isolados(matriz)
if pendentes:
    print(f"Vértices pendentes: {pendentes}")
else:
    print("Não há vértices pendentes.")
if isolados:
    print(f"Vértices isolados: {isolados}")
else:
    print("Não há vértices isolados.")

if eh_regular(matriz):
    print("O grafo é regular.")
else:
    print("O grafo não é regular.")

if eh_completo(matriz):
    print("O grafo é completo.")
else:
    print("O grafo não é completo.")











