import requests
import threading
headers = {'Cookie': 'D',
            'User-Agent': '',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'}
user = input('Who to bot? : ')
def Analytics_Bot():
    while True:
        r = requests.get(f'https://solo.to/{user}', headers=headers)
try:
      print('Sending views...')
      threads = []
      for i in range(20):
                t = threading.Thread(target=Analytics_Bot)
                t.daemon = True
                t.start()
                threads.append(t)
      for thread in threads:
                thread.join()
except:
  print('Error starting threads or some shit idfk')
