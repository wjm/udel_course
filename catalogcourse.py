import requests
from lxml import html

url="https://catalog.udel.edu/preview_program.php?catoid=29&poid=20816"

re=requests.get(url)
tree=html.fromstring(re.content)
class_desp_list=tree.xpath('//li[@class="acalog-course"]/span/a/text()')
title=tree.xpath('//h1/text()')
class_name=class_desp_list[:]

for i in range(len(class_name)):
    class_name[i]=class_name[i].split('-')[0].strip()

print(class_name)