def main():
    a = input()
    c = 0
    for i in range(len(a)): 
        if a[i] == ',':  c = i

    s = a[:c]
    x = a[c+1::]

    c = 0
    for i in range(0, len(s)):
        if s[i] != x:
            print(c)
            exit()
        c += 1
    print(c)

if __name__ == "__main__":
    main()