import requests
import json
import base64

#--------------------
#--------------------
#--------------------
read_config = True
#--------------------
#--------------------
#--------------------

emoji = None
emoji_id = None
text = None

if read_config == False:
    token = input('Token: ')
    text = input('Custom Status: ')
    emoji = input('Emoji Name: ')
    emoji_id = input('Emoji ID: ')
else:
    f = open('./config.json')
    json = json.load(f)
    accs = len(json['accs'])
    configs = len(json['configs'])

    i = 0

    while i <= accs:
        try:
            name = json['accs'][i]['name']
            print (f'[{i}] {name}')
            i += 1
        except:
            break
    
    acc_id = input('Account ID: ')
    try:
        acc_id = int(acc_id)
        token = json['accs'][acc_id]['token']
    except:
        print('Wrong ID')
        exit()
    
    i = 0
    while i <= configs:
        try:
            text = json['configs'][i]['text']
            emoji = json['configs'][i]['emoji_name']
            emoji_id = json['configs'][i]['emoji_id']
            print (f'[{i}] - ({emoji}) {text}')
            i += 1
        except:
            break
    con_id = input('Config ID: ')
    try:
        con_id = int(con_id)
        text = json['configs'][con_id]['text']
        emoji = json['configs'][con_id]['emoji_name']
        emoji_id = json['configs'][con_id]['emoji_id']
    except:
        print('Wrong ID')
        exit()



headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-US",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "discord.com",
    "Origin": "https://discord.com",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Authorization": token,
    "Content-Type": "application/json"
}
data = {}
if emoji != "":
    data["custom_status"] = {"text": text, 'emoji_name': emoji, 'emoji_id': emoji_id}
else:
    data["custom_status"] = {"text": text}

req = requests.patch('https://discord.com/api/v6/users/@me/settings', headers=headers, json=data)

a = input("Do you want to change your avatar?: (Yes / Everthing else): ")

if ((a == "Yes") or (a == "yes")):
    pic = json['configs'][con_id]['avatar']
    print(pic)
    try:
        with open(pic, "rb") as imageFile:
            str = base64.b64encode(imageFile.read()).decode()

        str = 'data:image/png;base64,{}'.format(str)
        data = {
            'avatar': str
        }
        req = requests.patch('https://discord.com/api/v6/users/@me', headers=headers, json=data)
        print(req)
    
    except Exception as e:
        print(e)
        print('No Avatar')
else:
    print('OK, no Avatar')
    exit()