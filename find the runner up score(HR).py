if __name__ == '__main__':
    n = int(input()) 
    #print (input().split())
    #arr = [int(x) for x in input().split()]
    #print (list(input()))
    arr = list(map(int, input().split()))
    #print (arr)
    #arr = sorted(arr)
    arr.sort()
    #print (arr)
    for i in range(n-1, -1, -1):
        if arr[i]<arr[n-1]:
            temp = arr[i]
            break
    print (temp)
    #sorted(arr)
    #print (arr[n-1])
           
