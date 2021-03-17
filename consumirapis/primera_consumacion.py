import requests
import json
if __name__=='__main__':
    url = 'https://api.tutiempo.net/json/?lan=es&apid=zsGqXqX4qqXeA2W&lid=54635'
    response = requests.get(url)

    texto=(response.json())
    
    with open('datos.json','w') as file:
        json.dump(texto,file)

    with open('datos.json','r') as file:
        data = json.load(file)

temperatura = (data["hour_hour"]["hour1"]['temperature'])
