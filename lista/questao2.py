def insertionSort(arr):
    deslocamentos = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            deslocamentos += 1
        arr[j + 1] = key
    return deslocamentos

def printArray(arr):
    print("Array de entrada: [", end="")
    print(", ".join(map(str, arr)), end="")
    print("]")

def main():
    try:
        t = int(input())
        if t < 1 or t > 15:
            print("Entrada inválida.")
            return
        for _ in range(t):
            n = int(input())
            if n < 1 or n > 100000:
                print("Entrada inválida.")
                return
            arr = list(map(int, input().split()))
            if len(arr) != n or any(x < 0 or x > 1000000 for x in arr):
                print("Entrada inválida.")
                return

            printArray(arr)
            result = insertionSort(arr)
            print(f"Deslocamentos realizados: {result}")
    except Exception:
        print("Entrada inválida.")

if __name__ == "__main__":
    main()
