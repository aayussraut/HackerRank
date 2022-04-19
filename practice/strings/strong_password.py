def minimumNumber(n, password):
    length_pass=n
    count=0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    numbers=set(numbers)
    lower_case=set(lower_case)
    upper_case=set(upper_case)
    password=set(password)

    if len(password.intersection(numbers))==0:
        count+=1
    if len(password.intersection(lower_case))==0:
        count+=1
    if len(password.intersection(upper_case))==0:
        count+=1
    if len(password.intersection(special_characters))==0:
        count+=1
    if((n+count)<6):
        temp=6-(n+count)
        count+=temp

    print(count)


n=3
password="Ab1"

minimumNumber(n, password)