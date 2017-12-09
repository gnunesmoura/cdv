
def accelerometer(data):
    for firstData in data:
        acValue = firstData["ac"]
        #Abaixando a cabeca fica -6, Levantando a cabeca fica 6
        yValue = str(acValue["y"]).split('.')[0]
        yValue = int(yValue)
        if(yValue <= -6 and yValue >= 6):
            if(yValue <= -6):
                firstData["status"]["head"] = -1
            else:
                firstData["status"]["head"] = 1
    print(data)
    return "hi"