def interweavingStrings(one, two, three):
    if len(three) is not len(one)+len(two):
        return False
    def helper(pointerOne=0, pointerTwo=0, pointerThree=0):
        if pointerThree >= len(three):
            return True
        conditionOne = pointerOne < len(one)
        conditionTwo = pointerTwo < len(two)
        if conditionOne and one[pointerOne] == three[pointerThree]:
            if conditionTwo and one[pointerOne] == two[pointerTwo]:
                return helper(pointerOne + 1, pointerTwo, pointerThree + 1) or helper(pointerOne, pointerTwo + 1, pointerThree + 1)
            return helper(pointerOne + 1, pointerTwo, pointerThree + 1)
        elif conditionTwo and two[pointerTwo] == three[pointerThree]:
            return helper(pointerOne, pointerTwo + 1, pointerThree + 1)
        else:
            return False
    return helper()

print(interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjob"))
