def hackerrankInString(s):
    text="hackerrank"
    j=0
    for i in s:
        if i==text[j]:
            j+=1
            if j==len(text):
                print("yes")
                return("Yes")
    print("No")
    return("No")

# s="hhaacckkekraraannk"
s="rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"
hackerrankInString(s)