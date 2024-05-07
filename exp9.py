import sys

MAX = 100

class Set:
    def __init__(self):
        self.elements = [0] * MAX
        self.cost = 0
        self.ratio = sys.float_info.max

def calc_ratio(m, sets, covered, result):
    for i in range(m):
        if result[i] == 1:
            continue
        eff_size = sets[i].elements[0]
        for j in range(1, sets[i].elements[0] + 1):
            if covered[sets[i].elements[j]] == 1:
                eff_size -= 1
        if eff_size == 0:
            sets[i].ratio = sys.float_info.max
        else:
            sets[i].ratio = sets[i].cost / eff_size

def findMin(sets, m):
    min_index = 0
    min_ratio = sys.float_info.max
    for i in range(m):
        if sets[i].ratio < min_ratio:
            min_ratio = sets[i].ratio
            min_index = i
    return min_index

def subsetCover(sets, m, size):
    covered = [0] * MAX
    total_cost = 0
    result = [0] * MAX
    itr = m
    while size > 0 and itr > 0:
        index = findMin(sets, m)
        result[index] = 1
        sets[index].ratio = sys.float_info.max
        total_cost += sets[index].cost
        for i in range(1, sets[index].elements[0] + 1):
            if covered[sets[index].elements[i]] != 1:
                covered[sets[index].elements[i]] = 1
                size -= 1
        calc_ratio(m, sets, covered, result)
        itr -= 1
    if size == 0:
        print("Selected sets are:")
        for i in range(m):
            if result[i]:
                print("Set {} (cost: {}): {}".format(i + 1, sets[i].cost, sets[i].elements[1:sets[i].elements[0] + 1]))
        print("Total cost:", total_cost)
    else:
        print("No solution.")

def main():
    n = int(input("Enter number of elements in the original set: "))
    m = int(input("Enter number of sets: "))
    sets = [Set() for _ in range(MAX)]
    for i in range(m):
        print("Enter number of elements in set {} and its cost: ".format(i + 1), end="")
        sets[i].elements[0], sets[i].cost = map(int, input().split())
        sets[i].ratio = sets[i].cost / sets[i].elements[0]
        print("Enter elements of set {}: ".format(i + 1), end="")
        sets[i].elements[1:sets[i].elements[0] + 1] = map(int, input().split())
    subsetCover(sets, m, n)

if __name__ == "__main__":
    main()