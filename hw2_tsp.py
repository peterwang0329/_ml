import numpy as np

citys = [
    [0,0],
    [0,1],
    [1,1],
    [1,0],
    [0.5,0.5],
    [0.5,1],
    [1,0.5],
    [0,0.5]
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

    best_path = path.copy()
    best_distance = total_distance(best_path, citys)
    print('frist_path=', best_path, 'frist_distance=', best_distance)

    for _ in range(10):
        for i in range(num_cities - 1):
            new_path = path.copy()
            new_path[i], new_path[i+1] = new_path[i+1], new_path[i] # 交換兩個城市的順序,微調路徑
            new_distance = total_distance(new_path, citys)

            if new_distance < best_distance:
                best_path = new_path
                best_distance = new_distance
                print('best_path=', best_path, 'best_distance=', best_distance)

        np.random.shuffle(path)  # 隨機改變路徑順序

    return best_path

for i in travel_salesman(citys):
    print(i,'.',citys[i])