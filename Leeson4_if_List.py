from sys import maxsize


def func5(*argm):
    if len(argm)==0:
       return "invalid parameter"
    max=0
    for x in argm:
        if max<int(x):
            max=x
    return max
if __name__ == '__main__':
#     print("Enter a day")
#     day=input()
#     match day:
#         case "ראשון" | "שני" | "שלישי" | "רביעי" | "חמישי":
#             print("Weekday")
#         case "שישי | שבת":
#             print("Weekend")
#         case _:
#             print("invalid input")
#
#     #tar 5
#     arr=[14,18,16,36]
#     for x in arr:
#         print(x) if x>20 else ""
#
#      #tar4
#     print("Enter 5 numbers")
#     sum=0
#     for x in range(1,5):
#         sum+=int(input())
#     print("avg: ",sum/5)

    #tar5

    print("the max is:" ,func5(1,2,3,4,5,6,7,8,9,10))


