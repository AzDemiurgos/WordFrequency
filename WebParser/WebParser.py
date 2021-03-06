import os
import requests   
from lxml import html
import re

def write_to_file(first_idx, second_idx, value):
    #with open ('HIMYM_s_{0}_e_{1}.text'.format(first_idx, second_idx), 'w') as output_file:
    with open ('Got\\GoT_s_{0}_e_{1}.text'.format(first_idx, second_idx), 'w') as output_file:
            output_file.write(value)

def parse_html(value):  
     tree = html.fromstring(value)
     value = tree.xpath('//div[@class = "scrolling-script-container"]/text()')[0]
     br_items = tree.xpath('//div[@class = "scrolling-script-container"]')[0]
     for br_item in br_items:
        #list_br = br_item.xpath('//br')[0].tail
        value += '\t'
        value += br_item.tail
        value += '\n'
     return value

def crawling(seas, ep):
    epi = ep
    if ep < 10:
        epi = "0{0}".format(ep)
    #url = 'https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=how-i-met-your-mother&episode=s0{season}e{episod}'.format(season=seas, episod=epi)
    url = 'https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=game-of-thrones&episode=s0{season}e{episod}'.format(season=seas, episod=epi)
    r = requests.get(url)
    return r

def decoding(r):
    #value = r.encode('utf-8', 'ignore')
    value = r.encode('ascii', errors='xmlcharrefreplace')
    #value = r.text.encode('utf-8', 'ignore')
    #value = r.encode('utf-8', 'ignore')
    if type(value) == str:
        value = str(value, 'utf-8', errors='ignore')
    else:
        value = str(value)
    return value

def define_episod_count(seas):
    #n = 21
    #if seas == 1 or seas == 2:
    #    n = 23
    #else:
    #    if seas != 3:
    #        n = 25
    n = 8
    if seas < 7:
        n = 11
    return n

def main():
    result = ""
    for seas in range(1, 8):
        n = define_episod_count(seas)
        s = 1
        if seas == 7:
            s = 0
        for ep in range (s, n):
            if seas == 7 and ep == 1:
                continue;
            rq = crawling(seas, ep)
            #value = decoding(rq)
            value = rq.text.encode('ascii', 'ignore')
            value = parse_html(value)
            #value = re.sub('\\\\.', value, '\\$')
            #value.replace('\\n','')
            #value.replace('\\r','')
            #value.replace('\\t','')
            #value.strip()
            #value = decoding(value)
            write_to_file(seas, ep, value)
            result += value
    write_to_file("","", result)

if __name__ == "__main__":
    main() 
