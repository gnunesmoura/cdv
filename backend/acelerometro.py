
def accelerometer(data):
    for firstData in data:
        acValue = firstData["ac"]
        #Abaixando a cabeca fica -6, Levantando a cabeca fica 6
        yValue = str(acValue["y"]).split('.')[0]
        yValue = int(yValue)
        #Transformando as cabeças de acordo com o acelerômetro
        if(yValue <= -6 and yValue >= 6):
            if(yValue <= -6):
                firstData["status"]["head"] = -1
            else:
                firstData["status"]["head"] = 1
    for subData in data:
        head = subData["status"]["head"]
        if(head == 0):
            adj = subData["status"]["adj"]
            if(len(adj) != 0):
                for row in data:
                    if(row["id"] == adj[0]):
                        if(row["status"]["head"] == 1):
                            subData["status"]["mounted"]="true"
    return data