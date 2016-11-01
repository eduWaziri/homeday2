def find_max_min(l):
    if min(l) == max(l):
        return [len(l)]
    else:
        return [min(l), max(l)]

l = [4,4]
print find_max_min(l)