import firebase_admin
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

    for vaquinha in vaquinhas:
        ref_cows.append(db.reference('/Cows/' + vaquinha))

    for cow in ref_cows:
        for id_data, data in cow.order_by_key().limit_to_last(3).get().items():
            print(data)

    while True:
        
