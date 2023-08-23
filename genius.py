import asyncio
import requests
from pystyle import *
from bs4 import BeautifulSoup

import aiohttp

GENIUS = Write.Input("Genius Song Link > ", Colors.blue, interval=0)

SCRAPED_PAGE = requests.get(GENIUS)

LOOPED = False

PAGE_ID = ""

SOUP = BeautifulSoup(SCRAPED_PAGE.content, "html.parser")

if SOUP.find("meta", attrs={"property": "twitter:app:url:iphone"}):
    content = SOUP.find("meta", attrs={"property": "twitter:app:url:iphone"})["content"]
    for x in content:
        if x.isdigit():
            PAGE_ID = PAGE_ID + x


print(" ")

AMOUNT = Write.Input("Views Amount > ", Colors.blue, interval=0)

views_sent = 0


async def fetch(s, url):
    global views_sent
    async with s.get(f"https://genius.com/api/songs/{PAGE_ID}/count_view") as r:
        if r.status == 404:
            Write.Print(f"[{views_sent}] Failed!\n", Colors.red, interval=0)
        else:
            views_sent = views_sent + 1
            Write.Print(f"[{views_sent}] Sent!\n", Colors.blue, interval=0)
        if LOOPED == True:
            await fetch_all(s, str(url))


async def fetch_all(s, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res


async def main():
    urls = range(1, int(AMOUNT))
    async with aiohttp.ClientSession() as session:
        global LOOPED
        htmls = await fetch_all(session, urls)
        if LOOPED == True:
            urls = range(1, 9999999)
            await fetch_all(session, urls)
        else:
            end = Write.Input("All views sent > ", Colors.blue, interval=0)
            if end == "return":
              await fetch_all(session, urls)
            if end == "loop":
                print("Loop has been turned on.")
                LOOPED = True
                await fetch_all(session, urls)

if __name__ == '__main__':
    asyncio.run(main())