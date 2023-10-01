def main():
    s = input()
    vov = 0
    cons = 0
    for i in range(0, len(s)):
        if s[i] == ' ': continue
        elif s[i] in "аиеёоуыэюя":
            vov += 1
        else:
            cons += 1
    print(vov, cons)

if __name__ == "__main__":
    main()