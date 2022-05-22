import requests, re

#target web
tar_url = 'https://www.hifini.com'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'
    }
#request domin web
respond = requests.get(url=tar_url, headers=headers)

#regular expression
obj_re_domin = re.compile(r'<div class="subject break-all">.*?<a href="(?P<song_url>.*?)">(?P<song_name>.*?)[[]', re.S)

#apply regular expression
content_domin = obj_re_domin.finditer(respond.text)

for ele in content_domin:
    #splicing the child web
    child_url = tar_url + '/' + ele.group('song_url')
    #request child web
    respond_child = requests.get(child_url, headers=headers)

    print(ele.group('song_url', 'song_name'))
