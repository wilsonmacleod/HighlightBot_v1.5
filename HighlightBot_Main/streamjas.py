import re
import os
import requests as request
from tqdm import tqdm

def finder(subreddit):
    """get our highlight with streamable links"""

    list_of_links = [] #list of our post links
    posts_scanned = [] # list of ids to avoid getting duplicate list_of_links in hot and top
    post_names = [] #list of names for vid titles

    with open("posts_scanned.txt", "r") as f: #text file to keep history of downloads, so we never download same post twice
        posts_scanned = f.read()
        posts_scanned = posts_scanned.split("\n")
        posts_scanned = list(filter(None, posts_scanned))
    
    for submission in subreddit.top(time_filter='day',limit=40,):
        if re.search('streamja', submission.url) != None:
            if submission.id not in posts_scanned:
                posts_scanned.append(submission.id)#IDs for .txt
                list_of_links.append(submission.url)#streamable link from reddit post
                post_names.append(submission.title)#post titles for video files
                
    for submission in subreddit.hot(limit = 30):
        if re.search('streamja', submission.url) != None:
            if submission.id not in posts_scanned:
                    list_of_links.append(submission.url)
                    post_names.append(submission.title)

    with open("posts_scanned.txt", "w") as f: #write posts ids to our .txt
        for post_id in posts_scanned:
            f.write(post_id + "\n")

    sub_link_list = [i.split('m/')[1] for i in list_of_links]
    content = tuple(zip(post_names,sub_link_list))
    return content

def get_vids(sub_folder, content):
    """download highlights into daily folder per our reddit findings"""
    
    for title, link in tqdm(content): #go through tuple each sublink, download and save to our new directory under reddit title
        try:
            
            url = (f'https://streamja.com/{link}')
            r= request.get(url, stream = True)
        
            with open(os.path.join(sub_folder, f'{title[0:250]}.mp4'), 'wb') as f:
                print(f'{title}\nDownloading and writing')
                for chunk in r.iter_content(chunk_size=1024*10):#download in chunks
                    f.write(chunk)
                    f.flush()

        except FileNotFoundError: #video source has been taken down but reddit post still exists
            print('FileNotFoundError-Video has been taken down')