def main():
    s = input()
    for i in range(0, len(s)):
        if s[i] == ' ': continue
        elif s.count(s[i]) > 1:
            print(True)
            return
    print(False)

if __name__ == "__main__":
    main()