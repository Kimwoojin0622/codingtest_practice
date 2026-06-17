def solution(date1, date2):
    for date1_ymd, date2_ymd in zip(date1, date2):
        if date1_ymd < date2_ymd:
            return 1
        elif date1_ymd > date2_ymd:
            return 0
        else:
            continue
    return 0