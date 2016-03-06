from slacker import Slacker
import time
import pprint
from random import randint
from imgurpython import ImgurClient

client_id = 'imgur_client_id_here'
client_secret = 'imgur_secret_here'

imgur = ImgurClient(client_id, client_secret)

# Robots C0PE2U1R6
# Main C0HA24604

slack = Slacker('slack_api_key_here')
pp = pprint.PrettyPrinter(indent=4)

def main():
	#channels = slack.channels.list()
	#pp.pprint(channels.body)
	last_message = {'ts' : ''}
	while 1:
		messages = slack.channels.history('C0HA24604')
		cur_message = messages.body['messages'][0]
		#pp.pprint(cur_message)
		if last_message['ts'] != cur_message['ts']:
			if cur_message['text'] == 'bot vbros me':
				print 'hello'
				url = get_image(imgur)
				slack.chat.post_message('#dadswithradnads', url)
		last_message = cur_message
		time.sleep(1)

def get_image(imgur):
	subreddit = imgur.subreddit_gallery('venturebros')
	random_image = subreddit[randint(0,len(subreddit)-1)]
	image_id = random_image.id
	url = "http://imgur.com/" + image_id + '.jpg'
	return url	
main()
