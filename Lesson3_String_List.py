
if __name__ == '__main__':
    # # tar2 class
    # str="python.com"
    # str=str[len(str)-1]+str[:len(str)-1:1]
    # print(str)
    # # tar3 class
    # print("Enter String")
    # str1=input()
    # print(str1[1:len(str1)-1:2])
    # # tar4 class
    # print("Enter String")
    # str2=input()
    # print(str2.upper())
    # print(str2[:3:1].upper()+str2[3:len(str)-3:1].lower()+str2[len(str)-3::].upper())

    #tar4 HM
    number=list(range(1,17))
    print(number)

    count=  number.pop(-1)
    count+= number.pop(0)
    count+= number.pop(12)
    count += number.pop(7)

    print(number)
    print(count)

    

