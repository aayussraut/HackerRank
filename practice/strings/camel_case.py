def camelcase(s):
    count=1
    for i in s:
        if 65<=ord(i)<=90:
            count+=1
    print(count)


s="saveChangesInTheEditor"
camelcase(s)