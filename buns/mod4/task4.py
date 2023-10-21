def check(s):
    chars = dict()
    for i in s:
        if chars.get(i) == None:
            chars[i] = 0
        chars[i] += 1
    
    oddLetter = ""
    countOdd = 0

    for i in chars.keys():
        if chars[i] % 2 == 1:
            oddLetter = i
            countOdd += 1
            if countOdd > 1:
                return (None, None)
    
    return (chars, oddLetter)

def create_palindrom(chars, oddLetter):
    half = ""
    center = oddLetter * chars[oddLetter]
    for i in chars.keys():
        if i == oddLetter:
            continue
        half += i * (chars[i] // 2)
    
    return half + center + half[::-1]


s = input()
chars, oddLetter = check(s)
if chars != None or oddLetter != None:
    print(create_palindrom(chars, oddLetter))