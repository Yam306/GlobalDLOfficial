import requests
import random

#rotating header list
#these help to keep requests module from getting detected easily and blocked
#if you are getting error 403 often you can try to insert more browser headers from online
headers_list = [
# Firefox 77 Mac
{
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Referer": "https://www.google.com/",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"
},
# Firefox 77 Windows
{
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://www.google.com/",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"
},
# Chrome 83 Mac
{
"Connection": "keep-alive",
"DNT": "1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Dest": "document",
"Referer": "https://www.google.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
},
# Chrome 83 Windows 
{
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Referer": "https://www.google.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9"
}
]

def urlformattask(url):
    url = str(url).strip()
    return url

def urlchecktask(url):
    headers = random.choice(headers_list) 
    try:
        request_obj = requests.get(url, headers=headers) 
        request_obj.encoding = 'utf-8'
        request_obj.raise_for_status()
        return('Success',request_obj)
    except requests.exceptions.ConnectionError as request_error_obj:
        return('ConnectionError',request_error_obj)
    except requests.exceptions.HTTPError as request_error_obj:
        return('HTTPError',request_error_obj)
    except requests.exceptions.Timeout as request_error_obj:
        return('Timeout',request_error_obj)
    except requests.exceptions.TooManyRedirects as request_error_obj:
        return('TooManyRedirects',request_error_obj)
    except requests.exceptions.RequestException as request_error_obj:
        return('RequestException',request_error_obj)

def errorchecktask(status,request_obj): 
    if status != 'Success':
        return(status,request_obj)
    request_status_code = int(request_obj.status_code)
    request_obj_content = request_obj.content 

    if request_status_code >= 100 and request_status_code <= 299:
        return('Success',request_status_code,request_obj_content) 
    elif request_status_code >= 300 and request_status_code <= 399:
        return('Redirected',request_status_code)
    elif request_status_code >= 400 and request_status_code <= 499:
        return('Client Error',request_status_code)
    elif request_status_code >= 500 and request_status_code <= 599:
        return('Server Error',request_status_code)
