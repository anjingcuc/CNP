import requests
from bs4 import BeautifulSoup
import os

header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, '
    'like Gecko) Chrome/67.0.3396.99 '
    'Safari/537.36',
    'Host':
    "www.zhihu.com",
    'Referer':
    "https://www.zhihu.com/question/299205851"
}

s = requests.session()

r = s.get('https://www.zhihu.com/question/299205851', headers=header)
bs = BeautifulSoup(r.text, "html.parser")

images = bs.select(
    "div.List-item > div > div.RichContent.RichContent--unescapable > div > span > figure > noscript > img"
)

for image in images:
  file_name = os.path.basename(image['src'])
  r = requests.get(image['src'], stream=True)
  with open(file_name, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
      if chunk:
        f.write(chunk)
