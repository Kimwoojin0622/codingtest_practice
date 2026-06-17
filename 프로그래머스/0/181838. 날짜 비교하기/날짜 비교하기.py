def solution(date1, date2):
    for date1_ymd, date2_ymd in zip(date1, date2):
        if date1_ymd < date2_ymd:
            return 1
        elif date1_ymd > date2_ymd:
            return 0
        else:
            continue
    return 0

## zip 사용 전
# def solution(date1, date2):
#     if date1[0] <= date2[0]:
#         if date1[0] < date2[0]:
#             return 1
#         else:
#             if date1[1] <= date2[1]:
#                 if date1[1] < date2[1]:
#                     return 1
#                 else:
#                     if date1[2] < date2[2]:
#                         return 1
#     return 0
