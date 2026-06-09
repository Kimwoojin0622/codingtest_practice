def solution(arr, delete_list):
    result = [data for data in arr if data not in delete_list]
    return result
            