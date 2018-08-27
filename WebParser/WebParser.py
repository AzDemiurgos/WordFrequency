import os
import requests 
for seas in range(1, 9):
    n = 20
    if seas == 1 or seas == 2:
        n = 22
    else:
        if seas != 3:
            n = 24
    for ep in range (1, n):
        epi = ep
        if ep < 10:
            epi = "0{0}".format(ep)
        url = 'https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=how-i-met-your-mother&episode=s0{season}e{episod}'.format(season=seas, episod=epi)
        r = requests.get(url)
        value = r.text.encode('utf-8', 'ignore')
        if type(value) == str:
            value = str(value, 'utf-8', errors='ignore')
        else:
            value = str(value)
        with open ('test_request_s_{0}_e_{1}.text'.format(seas, epi), 'w') as output_file:
            #output_file.write(value.text.encode('utf-8', 'ignore'))
            output_file.write(value)
