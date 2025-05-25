from collections import defaultdict

def similar_pair(n, k, edges):
    arvr = defaultdict(list)
    temPai = [False] * (n + 1)

    # Construir a árvore e identificar a raiz
    for i, j in edges:
        arvr[i].append(j)
        temPai[j] = True

    raiz = next(i for i in range(1, n + 1) if not temPai[i])

    contador = 0
    caminho = []

    def contadorSimilar(no):
        contador
        # Verifica quantos ancestrais no caminho atual são similares
        for ancestral in caminho:
            if abs(ancestral - no) <= k:
                contador += 1

        caminho.append(no)
        for filho in arvr[no]:
            contadorSimilar(filho)
        caminho.pop()

    contadorSimilar(raiz)
    return contador

def generateTestCases():
    return [
        (5, 2, [(3, 2), (3, 1), (1, 4), (1, 5)]),
        (6, 3, [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)]),
        (4, 1, [(1, 2), (2, 3), (3, 4)]),
        (7, 4, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)]),
        (3, 0, [(1, 2), (2, 3)])
    ]

def main():
    testCases = generateTestCases()
    for idx, (n, k, edges) in enumerate(testCases, 1):
        print(f"🧪 Teste {idx}")
        print(f"n = {n}, k = {k}, edges = {edges}")
        resultado = similar_pair(n, k, edges)
        print(f"➡ Resultado: {resultado}\n")

if __name__ == "__main__":
    main()
