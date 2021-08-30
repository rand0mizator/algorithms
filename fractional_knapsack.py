# Fractional Knapsack Problem (Greedy algorithm solution)

# general approach: sort items by (cost / weight) in descending order
# go one by one and add them to knapsack
# if some space left in knapsack, but whole item doesnt fit in
# put its fraction: weight * ((capacity - total_weight) / weight)
# and add cost proportionally: cost * ((capacity - total_weight) / weight)

def fill_knapsack(items, capacity):
    total_weight = 0
    total_cost = 0
    i = 0
    if capacity == 0 or not items or items[i][0] == 0 or items[i][1] == 0:
        return f"{total_cost:.3f}"
    while total_weight < capacity:
        try:
            cost, weight = items[i]
            if total_weight + weight <= capacity:
                total_cost += cost
                total_weight += weight
            elif total_weight + weight > capacity:
                total_cost += cost * ((capacity - total_weight) / weight)
                total_weight += weight * ((capacity - total_weight) / weight)
            i += 1
        except IndexError:
            break

    return f"{total_cost:.3f}"


def main():
    items = []
    items_count, capacity = map(int, input().split())
    for i in range(items_count):
        cost, weight = map(int, input().split())
        items.append((cost, weight))
    items.sort(key=lambda x: -(x[0] / x[1]))
    print(fill_knapsack(items, capacity))


if __name__ == '__main__':
    main()
