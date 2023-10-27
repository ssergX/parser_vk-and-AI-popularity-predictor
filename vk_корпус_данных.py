import requests
import json
import time
import pandas as pd

token='vk1.a.qlKPp3-oxl5VWetUpdlYGxgkHcV1zXf3tec0nSj-vqInuZXJ3WWLAmkWh3_8-ItYeOIbgQSvkZxpd_8Uha82T1N1kfD0CYfQr6oxxTybhTXbiitzuGQb1zWvfT-HH6J5AC6ACFHdtBLTCc8pvZDwMd5r0chtuNg3OL5n_9Y1sVbBiR-67Ja-SEcKuLffrHaIOKhnjNtBimRIeRTD7FvQpg'

def get_wall_posts(token):



    params = {
        'access_token': token,
        'owner_id': "-31480508",
        'v' : 5.131,
        'offset': "100",
        'count': 30
    }

    response = requests.get(url, params = params)
    return response.json()

wall_posts = get_wall_posts(token)


data_posts = pd.DataFrame(columns= ['id_group','id_post','data','description','title','text','views','likes','reposts'])
j = len(data_posts)



for i in range(len(wall_posts['response']['items'])):
    try:
        link = wall_posts['response']['items'][i]['attachments'][0]['link']
        description = link['description']
        title = link['title']
    except:
        try:
            video = wall_posts['response']['items'][i]['attachments'][0]['video']
            description = video['description']
            title = video['title']
        except:
            try:
                photo = wall_posts['response']['items'][i]['attachments'][0]['photo']
                description = photo['description']
                title = photo['title']
            except:
                description,title = '',''

    if wall_posts['response']['items'][i]['id'] in list(data_posts['id_post']):
        index = data_posts[data_posts['id_post']] == wall_posts['response']['items'][i]['id'].index[0]
        data_posts.loc[index] = [wall_posts['response']['items'][i]['owner_id'],
                             wall_posts['response']['items'][i]['id'],
                             wall_posts['response']['items'][i]['date'],
                             description,
                             title,
                             wall_posts['response']['items'][i]['text'],
                             wall_posts['response']['items'][i]['views']['count'],
                             wall_posts['response']['items'][i]['likes']['count'],
                             wall_posts['response']['items'][i]['reposts']['count']
                             ]
        print("есть в датафрейме")
    else:
        data_posts.loc[j] = [wall_posts['response']['items'][i]['owner_id'],
                                 wall_posts['response']['items'][i]['id'],
                                 wall_posts['response']['items'][i]['date'],
                                 description,
                                 title,
                                 wall_posts['response']['items'][i]['text'],
                                 wall_posts['response']['items'][i]['views']['count'],
                                 wall_posts['response']['items'][i]['likes']['count'],
                                 wall_posts['response']['items'][i]['reposts']['count']
                            ]
    j += 1

print(f"data_posts:{data_posts}")
print(f"j:{j}")
count_post = wall_posts['response']['count']
print(f"count_post:{count_post}")
data_posts.to_excel (r'C:\Users\user\Desktop\Лист Microsoft Excel.xlsx')