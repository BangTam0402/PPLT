def find_max(lst):
    m = lst[0]
    for x in lst:
        if x > m:
            m = x
    return m
def find_min(lst):
    m = lst[0]
    for x in lst:
        if x < m:
            m = x
    return m
scores = [6.5, 8.0, 4.5, 9.5, 7.0]
print("Max:", find_max(scores))
print("Min:", find_min(scores))
