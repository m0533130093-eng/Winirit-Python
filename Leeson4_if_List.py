if __name__ == '__main__':
    print("Enter a day")
    day=input()
    match day:
        case "ראשון" | "שני" | "שלישי" | "רביעי" | "חמישי":
            print("Weekday")
        case "שישי | שבת":
            print("Weekend")
        case _:
            print("invalid input")

    #tar 5
    arr=[14,18,16,36]
    for x in arr:
        print(x) if x>20 else ""

     #tar
    print("Enter 5 numbers")
    sum=0
    for x in range(1,5):
        sum+=int(input())
    print("avg: ",sum/5)



