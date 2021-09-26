stuffdict = {'w1':(10, 1),
             'w2':(15, 3),
             'w3':(12, 2.3),
             'w4':(8, 0.7),
             'w5':(11, 1.5),
             'w6':(10,1),
             'w7':(7, 3)}
def get_volume_and_weights(stuffdict):
    capacity = [stuffdict[item][0] for item in stuffdict]
    weights = [stuffdict[item][1] for item in stuffdict]
    return capacity, weights

def get_memtable(stuffdict, C=30):
    capacity, weights = get_volume_and_weights(stuffdict)
    n = len(weights)
    V = [[0 for a in range(C + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for c in range(C + 1):
            # base case
            if i == 0 or c == 0:
                V[i][c] = 0
            elif capacity[i - 1] <= c:
                V[i][c] = max(weights[i - 1] + V[i - 1][c - capacity[i - 1]], V[i - 1][c])
            else:
                V[i][c] = V[i - 1][c]
    return V, capacity, weights

def get_selected_items_list(stuffdict, C = 30):
    V, capacity, weights = get_memtable(stuffdict)
    n = len(weights)
    res = V[n][C]
    c = C
    items_list = []
    Weights = 0
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][c]:
            continue
        else:
            items_list.append((capacity[i - 1], weights[i - 1]))
            res -= weights[i - 1]
            c -= capacity[i - 1]
            Weights += weights[i-1]

    selected_stuff = []
    for search in items_list:
        for key, weights in stuffdict.items():
            if weights == search:
                selected_stuff.append(key)

    return selected_stuff, Weights

stuff = get_selected_items_list(stuffdict)
print(stuff)