from asyncpg import UniqueViolationError

import aiohttp

from bs4 import BeautifulSoup
from base.database import Logs

url = "https://citaty.info/random"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/96.0.4664.45 Safari/537.36"}


async def set_connection():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers, ssl=False) as response:
            connect = await response.text()
            soup = BeautifulSoup(connect, 'lxml')
            text = soup.find('div', class_='field-item even last').text.strip()
            author = soup.find('div', class_='field-item even').text
            try:
                await Logs.create(text=text, author=author)
            except UniqueViolationError:
                await set_connection()
            text_tags = ''
            try:
                hashtags = soup.find('div', class_='node__topics').find_all('div', class_='field-item even')
                tags = list()
                for tag in hashtags:
                    tags.append(f'{tag.text.strip()}')
                for info in tags:
                    if ' ' in info:
                        info = info.replace(' ', '_')
                    if ',' in info:
                        info = info.replace(',', '')
                    text_tags += f'#{info} '
            except AttributeError:
                pass
            try:
                odd_tagg = soup.find('div', class_='node__topics').find('div', class_='field-item odd')
                additional_tag = f'#{odd_tagg.text.strip()}'
            except AttributeError:
                additional_tag = ''
            msg = f'{text}\n\n{author}\n\n{additional_tag} {text_tags}'
            return msg


