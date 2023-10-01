def main():
    n = int(input())
    if n < 1:   print("Неверный ввод")
    else:   print(bin(n)[2::], oct(n)[2::], hex(n)[2::], sep=", ")

if __name__ == "__main__":
    main()