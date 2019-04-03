import os
import datetime
import praw
import streamables
import streamjas

def create_subfolder(subreddit):
    
    try:
        os.makedirs(r'C:\Users\wilso\Desktop\highlight_bot_{}\{}'.format(today,subreddit), exist_ok=False)  #make daily folder if it already exists continue
        sub_folder = os.path.realpath(r'C:\Users\wilso\Desktop\highlight_bot_{}\{}'.format(today,subreddit))
    except OSError:
        sub_folder = os.path.realpath(r'C:\Users\wilso\Desktop\highlight_bot_{}\{}'.format(today,subreddit))
    return sub_folder #edit also x3 if used on another machine: 'C:\Users\wilso\'

def main():

    os.makedirs(r'C:\Users\wilso\Desktop\highlight_bot_{}'.format(today), exist_ok=True) #create daily foler
    subreddit_dict = {
        'nba_subreddit': reddit.subreddit("nba"), 
        'soccer_subreddit': reddit.subreddit("soccer"), 
        'collegebball_subreddit': reddit.subreddit("CollegeBasketball")}
    
    for subreddit in subreddit_dict.values():
        sub_folder = create_subfolder(subreddit) #create sub-folder in our daily folder per subreddit
        print(subreddit)
        content = streamables.finder(subreddit) #search for our highlights (streamables)
        streamables.get_vids(sub_folder, content) #download and save highlights as mp4s
        content = streamjas.finder(subreddit) #search for our highlights (streamjas)
        streamjas.get_vids(sub_folder, content) #download and save highlights as mp4s

if __name__ == "__main__":

    reddit = praw.Reddit('bot1')
    today = datetime.datetime.today().strftime('%m-%d-%Y')
    main()