def solution(arr, queries):
    answer = arr
    for i in range(len(queries)):
        temp = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = temp
    return arr