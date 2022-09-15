# **CSAW CTF 2022**
## **Word Wide Web** 
___
### **Description:**

Isn't the Word Wide Web a fascinating place to be in? Words.. so many words.. all linked... NOTE: The flag doesn't have a wrapper. It needs to be wrapped with curly brackets and please put CTF in front of the curly brackets.
```
http://web.chal.csaw.io:5010
```
___
### **Recon:**

![1.png](https://github.com/L4P1Nz/CSAW-2022/blob/main/Word%20Wide%20Web/1.png)

Redirect đến /stuff và nhận được cookie:

![6.png](https://github.com/L4P1Nz/CSAW-2022/blob/main/Word%20Wide%20Web/6.png)

View Source của /stuff và nó tiếp tục dẫn ta đến /mistake

![3.png](https://github.com/L4P1Nz/CSAW-2022/blob/main/Word%20Wide%20Web/3.png)

Tiếp tục view source và bị dắt đi tùm lum. Kết hợp với Description của đề.

Như vậy bài này muốn ta viết script để redirect theo ý nó muốn, phía cuối con đường là flag ta đang tìm :( 

>Lưu ý: phải truy cập vào /stuff trước để set cookie, nếu không có cookie thì ta sẽ nhận mớ shit này :(

![7.png](https://github.com/L4P1Nz/CSAW-2022/blob/main/Word%20Wide%20Web/7.png) 


### **Exploit:**

```python
from bs4 import BeautifulSoup
import requests

def visit(new_url, cookie):
        print("try: " + new_url)
        response = requests.get(new_url,cookies=cookie)
        source = response.text
        soup = BeautifulSoup(source,'html.parser')
        if ('{' in response.text):
                print(response.text)
                exit(1)
        for s in soup.findAll('a') :
                href = s.get('href')
                if(href != None):
                        new_url = url + href
                        visit(new_url,response.cookies)


url = 'http://web.chal.csaw.io:5010'
cookie = {'solChain':'stuff'}
visit(url + '/stuff',cookie)

```

![8.png](https://github.com/L4P1Nz/CSAW-2022/blob/main/Word%20Wide%20Web/8.png)

P/s: Cú lừa cục mạnh từ Description :((


### **Update:**

Một simple write up từ discord: 

```
wget -r -l inf http://web.chal.csaw.io:5010/
```
