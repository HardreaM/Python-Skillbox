def main():
    c1 = -1
    c2 = 0
    s = input()
    for i in range(len(s)):
        if s[i] == ' ' and c1 == -1:  c1 = i
        elif s[i] == ' ' and c1 != -1:  c2 = i
    a, b, c = int(s[:c1]), int(s[c1+1:c2]), int(s[c2+1::])
    print((a + b + c) - max(a, b, c) - min(a, b, c))

if __name__ == "__main__":
    main()