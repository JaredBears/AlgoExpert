#Write a function that takes in a non-empty array of distinct integers
#and an integer representing a target sum.  If any two numers in the
#input array sum up to the target sum, the function should return
#them  in an array, in any order.  If no two numbers sum up to the target
#sum, the function should return an empty array.

def twoNumberSum(array, targetSum):
    i = 0;
    while i < len(array):
        j = i + 1;
        while j < len(array):
            if(array[i] + array[j] == targetSum):
                return [array[i], array[j]]
            j += 1;
        i += 1;
    return [];

array = [3, 5, -4, 8, 11, 1, -1, 6]

print(twoNumberSum(array, 10)); # [11, -1]
