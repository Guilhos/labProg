import random
import sys
sys.setrecursionlimit(10000)
MOD = 10**9 + 7

def parseRegex(expr):
    idx = 0

    def parse():
        nonlocal idx
        if expr[idx] in 'ab':
            c = expr[idx]
            idx += 1
            return ('lit', c)
        elif expr[idx] == '(':
            idx += 1
            left = parse()
            if expr[idx] == '|':
                idx += 1
                right = parse()
                idx += 1  # skip ')'
                return ('or', left, right)
            elif expr[idx] == '*':
                idx += 1  # skip '*'
                idx += 1  # skip ')'
                return ('star', left)
            else:
                right = parse()
                idx += 1  # skip ')'
                return ('concat', left, right)
        else:
            raise ValueError("Invalid expression")

    return parse()

def countRecognizedStrings(R, L):
    tree = parseRegex(R)
    memo = {}

    def count(node):
        if (id(node), L) in memo:
            return memo[(id(node), L)]

        res = [0] * (L + 1)

        if node[0] == 'lit':
            if L >= 1:
                res[1] = 1
        elif node[0] == 'or':
            left = count(node[1])
            right = count(node[2])
            for i in range(L + 1):
                res[i] = (left[i] + right[i]) % MOD
        elif node[0] == 'concat':
            left = count(node[1])
            right = count(node[2])
            for i in range(L + 1):
                for j in range(i + 1):
                    res[i] = (res[i] + left[j] * right[i - j]) % MOD
        elif node[0] == 'star':
            sub = count(node[1])
            res[0] = 1  # ε está sempre presente
            for i in range(1, L + 1):
                for j in range(1, i + 1):
                    res[i] = (res[i] + sub[j] * res[i - j]) % MOD

        memo[(id(node), L)] = res
        return res

    return count(tree)[L]

# Teste com gerador simples
def gerar_expressao():
    bases = ["a", "b"]
    exp = random.choice(bases)
    for _ in range(random.randint(1, 3)):
        op = random.choice(["|", "", "*"])
        if op == "":
            exp = f"({exp}{random.choice(bases)})"
        elif op == "|":
            exp = f"({exp}|{random.choice(bases)})"
        elif op == "*":
            exp = f"({exp}*)"
    return exp

def main():
    T = 3
    casos = []

    for _ in range(T):
        R, L = map(str.strip, input().split())
        L = int(L)
        casos.append((R, L))

    for R, L in casos:
        print(f"Expressão: {R}, Tamanho: {L}")
        resultado = countRecognizedStrings(R, L)
        print("Reconhecidas:", resultado)

if __name__ == '__main__':
    main()
