# two sum is where you need to find two numbers
# that add up to the target number from the list

def solution():

    nums = [2,7,11,15]
    target = 17
    a = {}   # dictionary created to store all attempts

    for i, n in enumerate(nums):   # i is for index of the enumerate and n is the number e.g 0:2, 1:7, 2:11 etc.
        if target - n in a:      
            print(a[target - n], i)
        elif target - n not in a:
            a[n] = i

# if target - n is in a then it will return the index of the number which is target - n and the index of the current number(i)
# if it is not then it will add that number to the dictionary to try the next combinations
#solution() 



def practice():
    target = 12
    arr = [5, 7, 3, 2, 3, 4]
    a = {}

    for i, n in enumerate(arr):
        if target - n in a:
            print(a[target - n], i)
        elif target - n not in a:
            a[n] = i

practice()