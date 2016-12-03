from __future__ import print_function

def lambda_handler(event, hoge):
    print("Hello world")
    return event["key"]
