import os
import datetime
import praw
import streamables
import streamjas

def create_folder():

    try: #make daily folder if it already exists continue
        os.makedirs(r'C:\Users\wilso\Desktop\highlight_bot_{}'.format(today), exist_ok=False) 
    except OSError:   #edit if used on another machine: 'C:\Users\wilso\'
        pass

def create_subfolder(subreddit):

    try: #make daily folder if it already exists continue
        os.makedirs(r'C:\Users\wilso\Desktop\highlight_bot_{}\{}'.format(today,subreddit), exist_ok=False) 
        sub_folder = os.path.realpath(r'C:\Users\wilso\Desktop\highlight_bot_{}\{}'.format(today,subreddit))
    except OSError:
        sub_folder = os.path.realpath(r'C:\Users\wilso\Desktop\highlight_bot_{}\{}'.format(today,subreddit))
    return sub_folder #edit also x3 if used on another machine: 'C:\Users\wilso\'

def main():

    subreddit_dict = {'nba_subreddit': reddit.subreddit("nba"), 'soccer_subreddit': reddit.subreddit("soccer"), 'collegebball_subreddit': reddit.subreddit("CollegeBasketball")}
    create_folder() #create daily folder on Desktop
    for subreddit in subreddit_dict.values():
        sub_folder = create_subfolder(subreddit) #create s a sub-folder in our daily folder per subreddit
        sublinks = streamables.finder(subreddit) #search for our highlights
        streamables.get_vids(sub_folder, sublinks) #download and save highlights as mp4s
    subreddit = subreddit_dict['soccer_subreddit'] #only r/soccer uses streamja, save processing time
    sublinks = streamjas.finder(subreddit) #search for our highlights
    streamjas.get_vids(sub_folder, sublinks) #download and save highlights as mp4s

if __name__ == "__main__":

    reddit = praw.Reddit('bot1')
    today = datetime.datetime.today().strftime('%m-%d-%Y')
    main()