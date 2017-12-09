from geopy.distance import great_circle

def analizer (data, dist):
    n_vaquinhas = len(data)
    matrix_adj = [[0 for x in range(n_vaquinhas)] for y in range(n_vaquinhas)] 

    for i in range(n_vaquinhas):
        for j in range(n_vaquinhas):
            if i != j:
                matrix_adj[i][j] = great_circle(data[i]['cord'], data[j]['cord']).meters
                matrix_adj[j][i] = great_circle(data[j]['cord'], data[i]['cord']).meters
    
    for i in range(n_vaquinhas):
        for j in range(n_vaquinhas):
            if i != j:
                if matrix_adj[i][j] < dist:
                    data[i]['status'] = 1
                    data[i]['adj'].append(data[j]['id'])

    for var in data:
        print(var)
            
            


