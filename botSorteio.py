from instagrapi import Client
import random
import time

user = "SEU USERNAME AQUI"
password = "SUA SENHA AQUI"
client = Client()
client.login(user, password)

print("To dentro")

usersMarcados = []
alvos = []

hashtags = ["cinema", "mubi", "cinefilo", "cinefila", "filmes", "movies", "hollywood", "filme", "Atores", "Cult", "Gaspar", "Scorsese"]

while True:
    alvos = []
    print("Entrei no loop")
    hashtag = random.choice(hashtags)
    posts = client.hashtag_medias_top(hashtag, 20)
    print(hashtag)
    for i, media in enumerate(posts):
        name = media.user.username
        id = media.id
        lks = client.media_likers(id)
        print(len(lks))
        time.sleep(2)
        for lk in lks:
            if lk.username not in usersMarcados:
                time.sleep(2)
                usersMarcados.append(lk.username)
                alvos.append(lk.username)
                print(lk.username)
        for i in range(0,len(alvos),2):
            time.sleep(2)
            client.media_comment("3315971012594756360_24774699945", f"@{alvos[i]} @{alvos[i+1]}")
            print("Comentei!")
            usersMarcados.append(alvos[i])
            usersMarcados.append(alvos[i+1])
            print("Terminei")
            time.sleep(10)
