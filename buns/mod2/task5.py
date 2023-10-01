def main():
    a, b = input().split(',')
    print(chr(ord('a') + (ord(a) - ord('a') + int(b)) % 26))

if __name__ == "__main__":
    main()