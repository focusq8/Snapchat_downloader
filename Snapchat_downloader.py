import requests
import random
import os

RED = '\033[91m'
GREEN  = '\33[32m'

username = input("""






Username : """)


url = f'https://search.snapchat.com/lookupStory?id={username}'

path_folder = username

try:
	os.mkdir(path_folder)

except FileExistsError:
	
	print("This user has a folder in your System.")

os.chdir(path_folder)
json = requests.get(url)

if json:
    json = json.json()
else:
    print(f'{RED}{username} ➝ Not Found ✘ ')
    exit()
storyTitle = json['storyTitle']

snapList = json['snapList']

snapLength = len(snapList)

print('---------------------')

print(f'\n{GREEN}User: {username}')
print(f'\n{GREEN}Title: {storyTitle}')
print(f'\n{GREEN}Count: ',len(snapList))

print('---------------------')

for snap_loop in snapList:
    get_random = random.random()

    print (snap_loop['snapUrls']['mediaUrl'])
    if snap_loop['snapUrls']['mediaUrl'].endswith(".mp4"):
      down_videos = format(snap_loop['snapUrls']["mediaUrl"])

      requesttry = requests.get(f'{down_videos}').content
      with open(f'{get_random}''.mp4','wb') as video:
        video.write(requesttry)

    else:
        down_photos = format(snap_loop['snapUrls']['mediaUrl'])
        requesttry1 = requests.get(f'{down_photos}').content
        with open(f'{get_random}''.jpg', 'wb') as image:
            image.write(requesttry1)
        
if snap_loop ['snapIndex']+1 == snapLength:
    print("\n")
    print(f"{GREEN}Successfully Downloaded ... ( ✔ )" )
