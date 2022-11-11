import boto3
from flask import current_app as app

def dynamodb_put_item(item_data):
    session = boto3.Session(region_name="us-east-1")
    dynamodb = session.resource("dynamodb")
    table = dynamodb.Table(app.config["DYNAMODB_TABLE"])
    return table.put_item(Item=item_data)


def dynamodb_scan():
    session = boto3.Session(region_name="us-east-1")
    dynamodb = session.resource("dynamodb")
    table = dynamodb.Table(app.config["DYNAMODB_TABLE"])
    response = table.scan()
    return response.get('Items', [])
