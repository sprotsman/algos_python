# Write a function with an input of list of ints like [1,1,1,3,3,3,3,4,5,6,6,9,9,]
# Return an array that looks like this.
# 3-1, 4-3, 1-4, 1-5, 2-6, 2-9

def occurrences(l):
    counter = {}
    for item in l:
        if item not in counter:
            counter[item] = 0
        counter[item] += 1

    result = ", ".join(f"{v}-{k}" for k, v in counter.items())

    return result


items = [1, 1, 1, 3, 3, 3, 3, 4, 5, 6, 6, 9, 9]
print(occurrences(items))
