import requests
from bs4 import BeautifulSoup
import pprint

if __name__ == '__main__':

    links1 = []
    subtext1 = []

    def requester(para):
        res = requests.get(f'https://news.ycombinator.com/news?p={para}')
        # print(res.text)
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(soup.body)
        # print(soup.body.content)
        # print(soup.find_all('div'))
        # print(soup.find_all('a'))
        links = soup.select('.storylink')

        subtext = soup.select('.subtext')

        return links, subtext
    # print(votes[0].get('id'))

    def sorting(hn_list):
        return sorted(hn_list, key=lambda k: k['3.points'], reverse=True)


    def create_custom_hn(links, subtext):
        hn = []
        # print(subtext)
        for idx, item in enumerate(links):

            title = links[idx].getText()
            href = links[idx].get('href', None)
            vote = subtext[idx].select('.score')
            # print(vote)
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'1.title': title, '2.href': href, '3.points': points})

        return hn

    for item in range(10):
        a, b = requester(item)
        links1 = links1 + a
        subtext1 = subtext1 + b

    list_hn = create_custom_hn(links1, subtext1)
    hacker_news = sorting(list_hn)

    # pprint.pprint(list_hn)
    # pprint.pprint(hacker_news)
    count = 0
    for item in hacker_news:
        count += 1
        pprint.pprint(item)
    print(count)
