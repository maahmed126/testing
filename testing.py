def handler(event,context):

    kg=event['queryStringParameters']['kg']
    lb=float(kg)*2.20462
    ans = str(kg) + " Kgs is " + str(round(lb, 2)) + " lbs\n"

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': ans
    }
