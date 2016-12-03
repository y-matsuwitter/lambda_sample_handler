#!-*-coding:utf-8-*-
import requests

def lambda_handler(event, hoge):
    response = requests.get("https://gunosy.com")
    return response.status_code
