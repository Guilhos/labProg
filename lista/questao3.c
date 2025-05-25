#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int compare_ints(const void *a, const void *b) {
    int ia = *(const int*)a;
    int ib = *(const int*)b;
    return ia - ib;
}

int activityNotifications(int *expenditure, int n, int d)
{   
    int notific = 0;
    for(int i = 0; i < n; i++)
    {
        if (i > d){
            int start = i - d;
            int end = i;
            int size = end - start;

            int *sublista = malloc(size * sizeof(int));

            for (int i = 0; i < size; i++) {
                sublista[i] = expenditure[start + i];
            }

            qsort(sublista, size, sizeof(int), compare_ints);

            double mediana_val;

            if (size % 2 == 1) {
                mediana_val = sublista[size / 2];
            } else {
                int mid1 = sublista[(size / 2) - 1];
                int mid2 = sublista[size / 2];
                mediana_val = (mid1 + mid2) / 2.0;
            }

            if (expenditure[i] >= 2 * mediana_val) {
                notific += 1;
            }
            
        }
    }
    
    return notific;
}

int main()
{
    srand(time(NULL));
    int n, d;
    scanf("%d %d", &n, &d);
    if (n < 1 || n > 200000 || d < 1 || d > n)
    {
        printf("Entrada inválida.\n");
        return 1;
    }
    int gastos[n];
    for (int i = 1; i < n; i++)
    {
        scanf("%d", &gastos[i]);
        if (gastos[i] < 0 || gastos[i] > 200)
        {
            printf("Entrada inválida.\n");
            return 1;
        }
    }
    int resultado = activityNotifications(gastos, n, d);
    printf("%d\n", resultado);
    return 0;
}