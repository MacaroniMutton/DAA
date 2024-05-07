class Item:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.cost = value / weight
        self.index = index

def knapsack_branch_bound(capacity, items):
    # Sort items by cost
    items.sort(key=lambda x: x.cost, reverse=True)

    def bound(i, current_weight, current_value):
        total_weight = current_weight
        total_value = current_value

        while i < len(items) and total_weight + items[i].weight <= capacity:
            total_weight += items[i].weight
            total_value += items[i].value
            i += 1

        if i < len(items):
            total_value += (capacity - total_weight) * items[i].cost

        return total_value

    def knapsack_recursive(i, current_weight, current_value, included):
        nonlocal max_value, max_included
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            max_included = included[:]

        if bound(i, current_weight, current_value) > max_value:
            if i < len(items):
                knapsack_recursive(i + 1, current_weight + items[i].weight, current_value + items[i].value, included + [1])
                knapsack_recursive(i + 1, current_weight, current_value, included + [0])

    max_value = 0
    max_included = []
    knapsack_recursive(0, 0, 0, [])
    return max_value, max_included

# Example usage:
if __name__ == "__main__":
    items = [Item(2, 10, 1), Item(4, 10, 2), Item(6, 12, 3), Item(9, 18, 4)]
    capacity = 15
    max_value, max_included = knapsack_branch_bound(capacity, items)
    print("Maximum value:", max_value)
    print("Items included:", max_included)
