#!-*-coding:utf-8-*-
from __future__ import print_function
import requests

def lambda_handler(event, hoge):
    print("check status_code")
    response = requests.get("https://gunosy.com")
    return response.status_code
