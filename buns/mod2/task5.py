def main():
    s = input()
    c = 0
    for i in range(len(s)): 
        if s[i] == ',':  c = i
    a = s[:c]
    b = s[c+1::]
    print(chr(ord('a') + (ord(a) - ord('a') + int(b)) % 26))

if __name__ == "__main__":
    main()