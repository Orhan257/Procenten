def procentmenu():
    while True:
        print("\n--- PROCENTSOMMEN MENU ---")
        print("1. Hoeveel is p% van a?")
        print("2. Hoeveel % is a van b?")
        print("3. A neemt toe met p% → nieuwe waarde?")
        print("4. A neemt af met p% → nieuwe waarde?")
        print("5. A neemt toe naar nieuwe waarde → met hoeveel %?")
        print("6. A neemt af naar nieuwe waarde → met hoeveel %?")
        print("0. Stoppen")

        keuze = input("Kies een somtype (0-6): ")

        match keuze:
            case "1":
                a = float(input("Voer de grondwaarde (a) in: "))
                p = float(input("Voer het percentage (p) in: "))
                resultaat = a * (p/100)
                print(f"\nBerekening: {p/100} × {a} = {resultaat}")
                print(f"Antwoord: {p}% van {a} is {resultaat}")

            case "2":
                a = float(input("Voer getal a in: "))
                b = float(input("Voer getal b in: "))
                resultaat = (a / b) * 100
                print(f"\nBerekening: {a} ÷ {b} × 100 = {resultaat}%")
                print(f"Antwoord: {a} is {resultaat:.2f}% van {b}")

            case "3":
                a = float(input("Oude waarde: "))
                p = float(input("Percentage toename: "))
                factor = 1 + p/100
                resultaat = a * factor
                print(f"\nJe moet vermenigvuldigen met {factor} (want 100% + {p}% = {100+p}%)")
                print(f"Berekening: {a} × {factor} = {resultaat}")
                print(f"Antwoord: nieuwe waarde = {resultaat}")

            case "4":
                a = float(input("Oude waarde: "))
                p = float(input("Percentage afname: "))
                factor = 1 - p/100
                resultaat = a * factor
                print(f"\nJe moet vermenigvuldigen met {factor} (want {100-p}% van de waarde blijft over)")
                print(f"Berekening: {a} × {factor} = {resultaat}")
                print(f"Antwoord: nieuwe waarde = {resultaat}")

            case "5":
                oud = float(input("Oude waarde: "))
                nieuw = float(input("Nieuwe waarde: "))
                factor = nieuw / oud
                p = (factor - 1) * 100
                print(f"\nBerekening: {nieuw} ÷ {oud} = {factor} → toename van {p}%")
                print(f"Antwoord: toename = {p}%")

            case "6":
                oud = float(input("Oude waarde: "))
                nieuw = float(input("Nieuwe waarde: "))
                factor = nieuw / oud
                p = (1 - factor) * 100
                print(f"\nBerekening: {nieuw} ÷ {oud} = {factor} → afname van {p}%")
                print(f"Antwoord: afname = {p}%")

            case "0":
                print("Programma stopt. Tot ziens!")
                break

            case _:
                print("Ongeldige keuze, probeer opnieuw.")

# Start het programma
procentmenu()
