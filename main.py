from calculator import calculate

def main():
    print("Einfacher CLI-Taschenrechner")
    print("Beenden mit 'exit'\n")

    while True:
        expr = input(">> ")
        if expr.lower() == "exit":
            break
        result = calculate(expr)
        print("=", result)

if __name__ == "__main__":
    main()