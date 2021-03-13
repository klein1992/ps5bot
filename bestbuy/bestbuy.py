import os

import boto3
import requests
from requests_html import HTMLSession

awsDefaultRegion = os.getenv('AWS_DEFAULT_REGION')
awsTopicARN = os.getenv('AWS_TOPIC_ARN')
searchUrl = os.getenv('SEARCH_URL')

textMessage='PS5 Is Ready to Order Hurry!'
textMessageSubject='From AWS PS5 Bot'

try:
    session = HTMLSession()
    isOrderable = session.get(searchUrl).html.find("button", containing="Add to Cart")
    if isOrderable:
        print("Ready to Order")
        client = boto3.client('sns', awsDefaultRegion)
        response = client.publish(
        TopicArn=awsTopicARN,
        Message=textMessage,
        Subject=textMessageSubject
        )
    else:
        print("The ps5 is sold out right now")

except requests.exceptions.RequestException as e:
    print(e)
