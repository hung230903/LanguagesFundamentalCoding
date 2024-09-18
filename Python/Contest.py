import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
        
    return n > 1

def binary_search(a, x):
    left = 0
    right = 8
    pos = 0
    while(left <= right):
        mid = (right - left) // 2
        pos+=1
        if(a[mid] == x):
            return pos
        elif(a[mid] > x):
            right = mid - 1
        else:
            left = mid + 1
    return pos

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = int(input())

    print(binary_search(a, x))