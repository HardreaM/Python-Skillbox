def main():
    s = input()
    ans = ""
    for i in range(0, len(s)):
        if s[i] == ' ': ans += s[i-1]
    ans += s[-1]
    print(ans)

if __name__ == "__main__":
    main()