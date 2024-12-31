def countValidClockTimes(time: str) -> int:
    # Assume necessary imports and helper functions are already defined
    valid_times = 0
    # Your code here
    valid_times += sum(1 for h in range(24) for m in range(60) if matchTime(f"{h:02}:{m:02}", time))
    return valid_times

def matchTime(time1: str, time2: str) -> bool:
    for t1, t2 in zip(time1, time2):
        if t2 != '?' and t1 != t2:
            return False
    return True

print(countValidClockTimes("2?:??")) # 3
print(countValidClockTimes("3?:2?")) # 9
print(countValidClockTimes("?4:?9")) # 10
print(countValidClockTimes("?8:7?")) # 10