def main():
    s, x = input().split(',')
    c = 0
    for i in range(0, len(s)):
        if s[i] != x:
            print(c)
            break
        c += 1

if __name__ == "__main__":
    main()