def binary_search_comparisons(a, pos):
    pos = 0
    left, right = 0, len(a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        pos += 1
        
        if a[mid] == pos:
            return pos
        elif a[mid] < pos:
            left = mid + 1
        else:
            right = mid - 1
    return pos

if __name__ == "__main__":
    a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    x = 15

    print(binary_search_comparisons(a, x))