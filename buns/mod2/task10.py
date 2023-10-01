def main():
    s = input()
    ans = ""
    for i in range(0, len(s)):
        if s[i] == ' ': ans += s[i-1]
    ans += s[-1]
    print(ans)

    """
    Можно через split:
        ans = ""
        for word in s.split():
            ans += word[-1]
    """

if __name__ == "__main__":
    main()