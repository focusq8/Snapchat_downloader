import requests
import random
import os

CRED = '\033[91m'
CEND = '\033[0m'
CBLUEBG   = '\33[34'
CGREEN  = '\33[32m'

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
    print(CRED +f'{username}', ' ➝ Not Found ✘ ' + CRED)
    exit()
storyTitle = json['storyTitle']

snapList = json['snapList']

snapLength = len(snapList)

print('---------------------')

print(f'\nUser: {username}')
print(f'\nTitle : {storyTitle}')
print('\nCount: ',len(snapList))

print('---------------------')

for snap_loop in snapList:
    get_random = random.random()

    print (snap_loop['snapUrls']['mediaUrl'])
    if snap_loop['snapUrls']['mediaUrl'].endswith(".mp4"):
      tt = format(snap_loop['snapUrls']["mediaUrl"])

      requesttry = requests.get(f'{tt}').content
      with open(f'{get_random}''.mp4','wb') as video:
        video.write(requesttry)

    else:
        down_photos = format(snap_loop['snapUrls']['mediaUrl'])
        requesttry1 = requests.get(f'{tt}').content
        with open(f'{get_random}''.jpg', 'wb') as image:
            image.write(requesttry1)
        
if snap_loop ['snapIndex']+1 == snapLength:
    print("\n")
    print( CGREEN + "Successfully Downloaded ... ( ✔ )" + CGREEN )
