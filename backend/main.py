import json
import math

import firebase_admin
from distance_analyzer import analizer
from firebase_admin import credentials, db
from acelerometro import accelerometer
import requests

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


if __name__ == '__main__':

    refencia_tenda = (-43.371226, -21.782599)

    cred = credentials.Certificate(
        'sendgpsthdata-firebase-adminsdk-6xw6f-87cc03533f.json')

    firebase_admin.initialize_app(
        cred, {
            'databaseURL': 'https://sendgpsthdata.firebaseio.com'
        })

    ref_cows = []
    ref = db.reference('/Cows')
    vaquinhas = ref.get()
    id_vaquinhas = []
    for vaquinha in vaquinhas:
        ref_cows.append(db.reference('/Cows/' + vaquinha))
        id_vaquinhas.append(vaquinha)

    while True:
        data = []

        for i in range(len(ref_cows)):
            aux = ref_cows[i].order_by_key().limit_to_last(1).get()

            for indice in aux:
                vaquinha = {
                    'id': id_vaquinhas[i][4:],
                    'cord': (aux[indice]['longitude'],
                             aux[indice]['latitude']),
                    'date': aux[indice]['date'],
                    'ac': {
                        'x': aux[indice]['ac_X'],
                        'y': aux[indice]['ac_Y'],
                        'z': aux[indice]['ac_Z']
                    },
                    'status': {
                        'adj': [],
                        'head': 0
                    }
                }

                vaquinha['cord'] = (
                    abs(vaquinha['cord'][0] - refencia_tenda[0]),
                    abs(vaquinha['cord'][1] - refencia_tenda[1]))

                vaquinha['cordenada'] = {
                    'longitude': vaquinha['cord'][0],
                    'latitude': vaquinha['cord'][1]
                }

                data.append(vaquinha)

        data = analizer(data, 15)
        data = accelerometer(data)

        print(requests.post(
            "https://realtime-firebase-arlen.firebaseio.com/vacas.json",
            json=data))
