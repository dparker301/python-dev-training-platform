def handler(event, context):
    name = (event.get('queryStringParameters') or {}).get('name', 'World')
    return {"statusCode":200,"headers":{"Content-Type":"application/json"},"body":f'{{"message":"Hello, {name}!"}}'}
