#Given two non-empty arrays of integers, write a function that determines
#whether the second array is a subsequnece of the first one.
#A subsequence of an array is a set of numbers that aren't necessarily adjacent
#in the array but that are in the same order as they appear in the array.
#For instance, the numbers [1, 3, 4] form a subsequence of the array
#[1, 2, 3, 4], and so do the numbers [2, 4].  Note that a single number in
#an array and the array itself are both valid subsequences of the array.

def isValidSubsequence(array, sequence):
    dummyArray = array;
    for i in sequence:
        if i not in dummyArray:
            return False
        else:
            dummyArray = dummyArray[dummyArray.index(i)+1:]
    return True

array = [5,1,22,25,6,-1,8,10]
sequence1= [1,6,-1,10]
sequence2 = [5,1, 25,22,6,-1,8,10]

print(isValidSubsequence(array, sequence1) == True)
print(isValidSubsequence(array, sequence2) == False)
