"""
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он
дополнительно возвращал список вершин, которые необходимо обойти.
"""


# на вход подаётся граф в виде таблицы смежности
def dijkstra(graph, start):
    def get_parents(i, parents):
        if parents[i] == -1:
            return []
        else:
            return get_parents(parents[i], parents) + [parents[i]]

    inf = float('inf')
    length = len(graph)
    is_visited = [False] * length
    cost = [inf] * length
    parent = [-1] * length
    ww = []
    cost[start] = 0
    min_cost = 0

    while min_cost < inf:
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = inf
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    ways = {i: get_parents(i, parent) + [i] if cost[i] != inf else None for i in range(length)}

    return cost, ways


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

s = int(input('От какой вершины идти: '))
c, w = dijkstra(g, s)

print(f'Путь от вершины {s}:')
for i in range(len(g)):
    if i != s:
        print(f' - до вершины {i}: стоимость {c[i]}, маршрут: {w[i]}')
