def main():
    s = input()
    c = 0
    for i in range(len(s)): 
        if s[i] == ',':  c = i
    a = int(s[:c])
    b = int(s[c+2::])
    print(a % b)

if __name__ == "__main__":
    main()