import sys
import math

MAX_ITER = 1000
EPSILON = 1e-6

def resolver_labirinto(n, m, k, si, sj, maze, tunnels):
    prob = [[1.0 if maze[i][j] == '%' else 0.0 for j in range(m)] for i in range(n)]
    temp = [[0.0 for _ in range(m)] for _ in range(n)]

    tun_map_i = [[-1 for _ in range(m)] for _ in range(n)]
    tun_map_j = [[-1 for _ in range(m)] for _ in range(n)]

    for t in tunnels:
        x1, y1, x2, y2 = t
        tun_map_i[x1][y1], tun_map_j[x1][y1] = x2, y2
        tun_map_i[x2][y2], tun_map_j[x2][y2] = x1, y1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(MAX_ITER):
        max_delta = 0.0

        for i in range(n):
            for j in range(m):
                if maze[i][j] in ['#', '*', '%']:
                    continue

                x, y = i, j
                if tun_map_i[i][j] != -1:
                    x, y = tun_map_i[i][j], tun_map_j[i][j]

                soma = 0.0
                count = 0

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#':
                        soma += prob[nx][ny]
                        count += 1

                temp[i][j] = soma / count if count > 0 else 0.0
                delta = abs(temp[i][j] - prob[i][j])
                max_delta = max(max_delta, delta)

        for i in range(n):
            for j in range(m):
                if maze[i][j] != '%' and maze[i][j] != '*':
                    prob[i][j] = temp[i][j]

        if max_delta < EPSILON:
            break

    return prob[si][sj]

def main():
    n, m, k = map(int, input().split())
    if n < 1 or n > 20 or m < 1 or m > 20 or k < 0 or k > m * n:
        print("Entrada inválida.")
        return

    maze = [list(input().strip()) for _ in range(n)]

    si = sj = -1
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'A':
                si, sj = i, j
                break
        if si != -1:
            break

    tunnels = []
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        tunnels.append((a - 1, b - 1, c - 1, d - 1))

    print("Maze:")
    for row in maze:
        print(''.join(row))

    print("Tunnels:")
    for t in tunnels:
        print(*t)

    resultado = resolver_labirinto(n, m, k, si, sj, maze, tunnels)
    print(f"Probabilidade de fuga: {resultado:.6f}")

if __name__ == "__main__":
    main()
