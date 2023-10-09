import pprint

import requests
import re
import bs4

entry_point_url: str = 'https://fauux.neocities.org/Love'

fetched_links: list = []

next_link = entry_point_url
while True:
    if next_link in fetched_links:
        break

    fetched_links.append(next_link)
    res: requests.Response = requests.get(next_link)

    if res.ok:
        soup = bs4.BeautifulSoup(res.text)
        all_links_on_page = soup.find_all('a')
        for link in all_links_on_page:
            link: bs4.Tag
            if re.search('fauux.neocities.org', link.attrs['href']):
                next_link = link.attrs['href']
                print(f'{len(fetched_links)} links has been found!')
    else:
        break

with open('all_links.py', 'w') as file:
    file.write(f'all_links: list = {pprint.pformat(fetched_links)}')
