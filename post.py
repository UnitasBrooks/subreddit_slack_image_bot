from slacker import Slacker
from imgurpython import ImgurClient
import time
import pprint
import json
from random import randint

# Robots C0PE2U1R6
# Main C0HA24604

pp = pprint.PrettyPrinter(indent=4)

# Open credentials file
with open('credentials.json') as json_data:
    # Load credentials as a dict, close the file, print the credentials
    credentials = json.load(json_data)
    json_data.close()
    pp.pprint(credentials)

# Pull out credentifals from dictionary
imgur_client_id = credentials['imgur_client_id']
imgur_client_secret = credentials['imgur_client_secret']
slack_api_key = credentials['slack_api_key']

# Instatiate the imgur object
imgur = ImgurClient(imgur_client_id, imgur_client_secret)
# Instatiate the slack object
slack = Slacker(slack_api_key)

#channels = slack.channels.list()
#pp.pprint(channels.body)

def main():
    last_message = {'ts' : ''}
    while 1:
        messages = slack.channels.history('C0PE2U1R6')
        cur_message = messages.body['messages'][0]
        #pp.pprint(cur_message)
        if last_message['ts'] != cur_message['ts']:
            
            words = cur_message['text'].split(' ')
            pp.pprint(words)
            if len(words) >= 3 and words[0] == 'bot' and words[2] == "me":
                print 'Getting image from subreddit: ' +  words[1]
                url = get_image(imgur,words[1])
                slack.chat.post_message('#robots', url)
        last_message = cur_message
        time.sleep(1)

def get_image(imgur,sub_name):
    subreddit = imgur.subreddit_gallery(sub_name)
    image_id = ""
    url = ""
    try:
        random_image = subreddit[randint(0,len(subreddit)-1)]
        image_id = random_image.id
        url = "http://imgur.com/" + image_id + '.jpg'
    except:
        print "Could not find subreddit"
        url = "Could not find that, try venturebros, games, eve, or some other subreddit"
    
    
    return url  

main()