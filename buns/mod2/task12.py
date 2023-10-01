def main():
    s = input()
    ans = ""
    for i in range(0, len(s)):
        if s[i] in "+0123456789":   ans += s[i]
    print(ans)

if __name__ == "__main__":
    main()