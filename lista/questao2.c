#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int insertionSort(int arr_count, int *arr)
{
    int i, j, key;
    int deslocamentos = 0;
    for (i = 1; i < arr_count; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            deslocamentos++;
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
    return deslocamentos;
}
void generateRandomArray(int *arr, int size, int min, int max)
{
    for (int i = 0; i < size; i++)
    {
        arr[i] = min + rand() % (max - min + 1);
    }
}
void printArray(int *arr, int size)
{
    printf("Array de entrada: [");
    for (int i = 0; i < size; i++)
    {
        printf("%d", arr[i]);
        if (i < size - 1)
            printf(", ");
    }
    printf("]\n");
}
int main()
{
    srand(time(NULL));
    int t;
    scanf("%d", &t);
    if (t < 1 || t > 15)
    {
        printf("Entrada inválida.\n");
        return 1;
    }
    for (int i = 0; i < t; i++)
    {
        int n;
        scanf("%d", &n);
        if (n < 1 || n > 100000)
        {
            printf("Entrada inválida.\n");
            return 1;
        }
        int arr[n];
        for (int j = 0; j < n; j++) {
            scanf("%d", &arr[j]);
            if (arr[j] < 0 || arr[j] > 1000000) {
                printf("Entrada inválida.\n");
                return 1;
            }
        }
        
        int result = insertionSort(n, arr);
        printf("Deslocamentos realizados: %d\n", result);
    }
    return 0;
}