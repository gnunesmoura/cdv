import firebase_admin
from cow import analizer
from acelerometro import accelerometer
from firebase_admin import credentials, db

if __name__ == '__main__':
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
            
            for ind in aux:
                data.append({
                    'id': id_vaquinhas[i][4:],
                    'cord': (aux[ind]['latitude'], aux[ind]['longitude']),
                    'date': aux[ind]['date'],
                    'ac': {
                        'x': aux[ind]['ac_X'],
                        'y': aux[ind]['ac_Y'],
                        'z': aux[ind]['ac_Z']
                    },
                    'status': {
                        'adj': [],
                        'head': 0
                    }
                })

        data = analizer(data, 15)
        data = accelerometer(data)
