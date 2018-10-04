import requests
import string

API_KEY='1889e61e8a976267ae3713aa45edd1c4'
site_encrypt='http://api.trytodecrypt.com/encrypt'
page_id='2'
crypttext='131017171A48221A1D170F'
text='a'

letters=list(string.printable)

url=site_encrypt + '?key=' + API_KEY + '&id=' + page_id +'&text='



for char in letters:
	url1=url+char
	response=requests.get(url1)
	print(char, response.content.decode("utf-8"))
