def main():
    a = input()
    s = ""
    for i in range(len(a)-1, -1, -1):
        if a[i] == ".":
            print(s[::-1])
            s = ""
        else:
            s += a[i]
    print(s[::-1])

if __name__ == "__main__":
    main()