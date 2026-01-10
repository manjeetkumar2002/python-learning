# consecutive ones not allowed

def solve(index,numbers,result,flag):
    if index>=len(numbers):
        result.append("".join(numbers))
        return
    numbers[index] = "0"
    solve(index+1,numbers,result,True)
    if flag:
        numbers[index] = "1"
        solve(index+1,numbers,result,False)
        numbers[index] = "0"


def generateBinaryString(n):
    numbers = ["0"]*n
    result = []
    solve(0,numbers,result,True)
    return result

print(generateBinaryString(3))