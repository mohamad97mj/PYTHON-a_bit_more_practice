import requests
from json import JSONDecodeError

number = input("Enter a number")

try:
    print(int(number) * 2)
except ValueError:
    print("you did not enter a base 10 number! try again!")

r = requests.post("http://someexampleurl.com/users", data={'text': "hello world"})
try:
    label = r.json()['label']
except JSONDecoderError:
    print("we could not decode the json response")
except KeyError:
    print("we get json back from server but it did not hva a key 'label'")
