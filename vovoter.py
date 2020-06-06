from torrequest import TorRequest
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## BEGINNING OF CONFIGURATION

url = 'URL'

cookies = {
}

headers = {
}

data = ''

## END OF CONFIGURATION

no_of_requests = 50

for x in range(no_of_requests):
    with TorRequest() as tr:
        response1 = tr.get('http://ipecho.net/plain')
        response2 = tr.post(url, headers=headers, cookies=cookies, data=data, verify=False)
        print(str(x)+" "+response1.text+" "+response2.text)
        tr.close()
    time.sleep(3)


