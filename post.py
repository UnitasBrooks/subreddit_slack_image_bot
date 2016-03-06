from slacker import Slacker
from imgurpython import ImgurClient
import time
import pprint
import json
from random import randint

# Robots C0PE2U1R6
# Main C0HA24604

pp = pprint.PrettyPrinter(indent=4)

with open('credentials.json') as json_data:
    credentials = json.load(json_data)
    json_data.close()
    pp.pprint(credentials)

imgur_client_id = credentials['slack_client_id']
imgur_client_secret = credentials['slack_client_secret']
slack_api_key = credentials['slack_api_key']

imgur = ImgurClient(imgur_client_id, client_secret)

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
            if cur_message['text'] == 'bot vbros me':
                print 'hello'
                url = get_image(imgur)
                slack.chat.post_message('#robots', url)
        last_message = cur_message
        time.sleep(1)

def get_image(imgur):
    subreddit = imgur.subreddit_gallery('venturebros')
    random_image = subreddit[randint(0,len(subreddit)-1)]
    image_id = random_image.id
    url = "http://imgur.com/" + image_id + '.jpg'
    return url  
main()
