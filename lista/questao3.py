def activity_notifications(expenditure, d):
    notific = 0

    for i in range(d, len(expenditure)):
        window = sorted(expenditure[i - d:i])

        if d % 2 == 1:
            median = window[d // 2]
        else:
            median = (window[d // 2 - 1] + window[d // 2]) / 2

        if expenditure[i] >= 2 * median:
            notific += 1

    return notific

def main():
    try:
        n, d = map(int, input().split())
        if n < 1 or n > 200000 or d < 1 or d > n:
            print("Entrada inválida.")
            return

        gastos = list(map(int, input().split()))
        if len(gastos) != n or any(x < 0 or x > 200 for x in gastos):
            print("Entrada inválida.")
            return

        resultado = activity_notifications(gastos, d)
        print(resultado)
    except:
        print("Entrada inválida.")

if __name__ == "__main__":
    main()
