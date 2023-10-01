def main():
    s = input()
    even = 0
    notEven = 0
    for i in range(0, len(s)):
        if i % 2 == 0:  notEven += int(s[i])
        else:   even += int(s[i])
    
    if (notEven + even * 3) % 10 == 0:  print("yes")
    else:   print("no")

if __name__ == "__main__":
    main()