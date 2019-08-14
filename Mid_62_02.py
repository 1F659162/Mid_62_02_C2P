num = input("Enter binary : ")
lnum = len(num)
total = 0
show = 's'
n = 1
count = -1
if lnum != 5 :
    if lnum > 5 :
        print("binary great than 5.")
    else :
        print("binary lower than 5.")
else :
    for i in range(lnum) :
        if num[i] == '1' or num[i] == '0' :
            print(num[i])
        else :
            print(num[i] , " <-- this isn't binary.")
            show = 'n'
        if num[count] == '1' :
            total += n
        count -= 1
        n *= 2
if show == 's'  :
    print("Decimal number : " , total)
            
