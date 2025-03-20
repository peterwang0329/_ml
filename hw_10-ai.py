import requests

qustion = "自我介紹一下"

response = requests.post(
    'http://localhost:11434/api/chat',
    json={
        'model': 'llama3.2:3b',
        'messages': [
            {
                'role': 'user',
                'content': qustion
            }
        ],
        'stream': False,
    }
)

print('我:'+qustion)
print('='*20)
print(response.json()['model']+':')
print(response.json()['message']['content'])