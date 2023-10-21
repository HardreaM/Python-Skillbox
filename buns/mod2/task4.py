def convert(n, base):
    if n == 0:
        return "0"
    alphabet = "0123456789abcdef"
    ans = ""
    while n > 0:
        ans += alphabet[n % base]
        n //= base
    return ans[::-1]

def main():
    n = int(input())
    if n < 1:   print("Неверный ввод")
    else:   print(convert(n, 2), convert(n, 8), convert(n, 16), sep=", ")

if __name__ == "__main__":
    main()