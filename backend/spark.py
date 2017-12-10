import json
import requests

accessToken = "YTMzYWNiYjAtZDNjMi00MzU3LTg0ZmMtYWQyZmU5NzRmOTZjZGVjOThmMWQtMDdk"

accessToken_hdr = 'Bearer ' + accessToken
spark_header = {'Authorization': accessToken_hdr}


def send_event(text):

    uri = 'https://api.ciscospark.com/v1/messages'

    mensagem = {
        "roomId":
        "Y2lzY29zcGFyazovL3VzL1JPT00vZmM3NzRkNjAtZGQ2Mi0xMWU3LTk3MTUtNDU5MTk4YmYxOTFl",
        "text":
        text
    }

    resp = requests.post(uri, headers=spark_header, json=mensagem)
    print(json.dumps(resp.json(), indent=4, separators=(',', ': ')))


def deleta_tuto():
    uri = 'https://api.ciscospark.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vZmM3NzRkNjAtZGQ2Mi0xMWU3LTk3MTUtNDU5MTk4YmYxOTFl'

    resp = requests.get(uri, headers=spark_header)
    messages = resp.json()

    uri_deleta = 'https://api.ciscospark.com/v1/messages/'

    for message in messages['items']:
        requests.delete(uri_deleta+message['id'], headers=spark_header)


deleta_tuto()