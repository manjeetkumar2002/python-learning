n = 3

def solve(index,total,bracket,result):
    if index >= len(bracket):
        if total == 0:
            result.append("".join(bracket))
        return
    if total > len(bracket)//2:
        return
    if total < 0:
        return
    bracket[index] = "("
    solve(index+1,total+1,bracket,result)
    bracket[index] = ")"
    solve(index+1,total-1,bracket,result)
def generateValidParenthesis(n):
    brackets = [""]*(2*n)
    result = []
    solve(0, 0, brackets, result)
    return result

print(generateValidParenthesis(n))