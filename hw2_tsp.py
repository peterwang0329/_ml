import numpy as np
citys = [
    [0, 0],   # 城市 0
    [2, 4],   # 城市 1
    [3, 1],   # 城市 2
    [5, 3],   # 城市 3
    [1, 5],   # 城市 4
    [4, 0],   # 城市 5
    [2, 2],   # 城市 6
    [0, 3],   # 城市 7
    [5, 5],   # 城市 8
    [3, 4]    # 城市 9
]

def calculate_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def total_distance(path, citys):
    distance = 0
    for i in range(len(path) - 1):
        distance += calculate_distance(citys[path[i]], citys[path[i+1]])
    distance += calculate_distance(citys[path[-1]], citys[path[0]]) # 回到起點形成一個迴圈
    return distance

def travel_salesman(citys):
    num_cities = len(citys)
    path = [(i+1)%num_cities for i in range(num_cities)] # path = [1,2,3,4,5,6,7,8,0]
    distance = total_distance(path, citys)

    best_path = path.copy()
    best_distance = distance
    print('frist_path=', path, 'frist_distance=', distance)

    max = 10000
    limit = 1000
    count = 0

    for _ in range(max):
        neighbor_path = path.copy()
        i, j = np.random.randint(0, num_cities, 2)  # 隨機交換兩個城市的順序,微調路徑
        neighbor_path[i], neighbor_path[j] = neighbor_path[j], neighbor_path[i]
        neighbor_distance = total_distance(neighbor_path, citys)

        if neighbor_distance < best_distance:
            best_path = neighbor_path
            best_distance = neighbor_distance
            count = 0
            print('path=', best_path, 'distance=', best_distance)
        else:
            count += 1
        
        if count >= limit:
            break

    print('best_path=', best_path, 'best_distance=', best_distance)
    return best_path

for i in travel_salesman(citys):
    print(i,'.',citys[i])