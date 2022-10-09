#Write a function that takes in a non-empty array of
#sorted integers and returns a new array with the square
#of the original integers also sorted

def sortedSquaredArray(array):
    i = 0
    j = len(array) - 1
    results = []
    while i <= j:
        if(abs(array[i]) > abs(array[j])):
            results.insert(0,array[i] * array[i])
            i += 1
        else:
            results.insert(0, array[j] * array[j])
            j -= 1
    return results

testArrayOne = [-5, 1, 4, 8, 10]
resultArrayOne = [1, 16, 25, 64, 100]

print(sortedSquaredArray(testArrayOne) == resultArrayOne)
