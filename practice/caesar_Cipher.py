def caesarCipher(s, k):
    output=""
    for i in s:
        if 65<=ord(i)<=90:
            temp=(ord(i)-65+k)%26
            output+=chr(temp+65)
        elif 97<=ord(i)<=122:
            temp=(ord(i)-97+k)%26
            output+=chr(temp+97)
        else:
            output+=i
    print(output)

s="middle-Outz"
k=2
caesarCipher(s, k)