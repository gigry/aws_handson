import json
import urllib.request
import boto3
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # ※ここは自分のバケット名に書き換えてくれな！たのむぜーーーーーー
    BUCKET_NAME = "my-weather-log-20260102"
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            weather = data[0]['timeSeries'][0]['areas'][0]['weathers'][0]
            result_message = f"東京の今日の天気は「{weather}」だぜ。"
            file_name = datetime.now().strftime('%Y-%m-%d') + ".txt"
            
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=file_name,
                Body=result_message
            )
            return {'statusCode': 200, 'body': json.dumps(f"S3に保存成功！: {file_name}")}
    except Exception as e:
        print(e)
        return {'statusCode': 500, 'body': '失敗したぜ...'}
if __name__ == "__main__":
    lambda_handler(None, None)
