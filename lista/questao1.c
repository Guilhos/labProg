#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define MAX_ITER 1000
#define EPSILON 1e-6

float resolverLabirinto(int n, int m, int k, int si, int sj, char maze[n][m+1], int tunnels[k][4]) {
    double prob[n][m];
    double temp[n][m];

    // Inicializa a matriz de probabilidades
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            prob[i][j] = (maze[i][j] == '%') ? 1.0 : 0.0;

    // Mapeamento dos túneis: -1 significa "sem túnel"
    int tun_map_i[n][m], tun_map_j[n][m];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            tun_map_i[i][j] = -1;
            tun_map_j[i][j] = -1;
        }

    for (int i = 0; i < k; i++) {
        int x1 = tunnels[i][0], y1 = tunnels[i][1];
        int x2 = tunnels[i][2], y2 = tunnels[i][3];
        tun_map_i[x1][y1] = x2; tun_map_j[x1][y1] = y2;
        tun_map_i[x2][y2] = x1; tun_map_j[x2][y2] = y1;
    }

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    for (int iter = 0; iter < MAX_ITER; iter++) {
        double max_delta = 0.0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maze[i][j] == '#' || maze[i][j] == '*' || maze[i][j] == '%') continue;

                int x = i;
                int y = j;

                // Se tiver túnel, vai para a outra ponta
                if (tun_map_i[i][j] != -1) {
                    x = tun_map_i[i][j];
                    y = tun_map_j[i][j];
                }

                double soma = 0.0;
                int count = 0;

                for (int d = 0; d < 4; d++) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m && maze[nx][ny] != '#') {
                        soma += prob[nx][ny];
                        count++;
                    }
                }

                temp[i][j] = (count > 0) ? soma / count : 0.0;
    double delta = fabs(temp[i][j] - prob[i][j]);
                if (delta > max_delta)
                    max_delta = delta;
            }
        }

        // Atualiza a matriz de probabilidades
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (maze[i][j] != '%' && maze[i][j] != '*')
                    prob[i][j] = temp[i][j];

        if (max_delta < EPSILON)
            break;
    }

    return (float) prob[si][sj];
}


char gerarElemento() {
    char opcoes[] = {'O', 'O', 'O', 'O', 'O', '#', '*', '%'};
    return opcoes[rand() % 8];
}

int main() {
    srand(time(NULL));
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    if (n < 1 || n > 20 || m < 1 || m> 20 || k < 0 || k > m*n) {
        printf("Entrada inválida.\n");
        return 1;
    }

    char maze[n][m + 1];
    for (int i = 0; i < n; i++){
        scanf("%s", maze[i]);
    }

    int si = -1, sj = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (maze[i][j] == 'A') {
                si = i;
                sj = j;
                break;
            }
        }
        if (si != -1) break;
    }

    int tunnels[k][4];
    for (int i = 0; i < k; i++) {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        tunnels[i][0] = a - 1;
        tunnels[i][1] = b - 1;
        tunnels[i][2] = c - 1;
        tunnels[i][3] = d - 1;  
    }

    printf("Maze:\n");

    for (int i = 0; i < n; i++)
        printf("%s\n", maze[i]);

    printf("Tunnels:\n");

    for (int i = 0; i < k; i++)
        printf("%d %d %d %d\n", tunnels[i][0], tunnels[i][1],
               tunnels[i][2], tunnels[i][3]);

    float resultado = resolverLabirinto(n, m, k, si, sj, maze, tunnels);

    printf("Probabilidade de fuga: %.6f\n", resultado);

    return 0;
}