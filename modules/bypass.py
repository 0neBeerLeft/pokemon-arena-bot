import sys
import os
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = "2Captcha-api-key"

solver = TwoCaptcha(api_key)
def solve(cookie):
    try:
        print("[?] Bypassing captcha... [This process can take up to 30 seconds]")
        result = solver.recaptcha(
            sitekey='6Lfm8uQkAAAAAMys-ODy8wclxhstAPrHFNujPibl',
            url='https://pokemon-arena.co.il/index.php?page=bot-check')

        cookies = {
            'theme': '-1',
            'PHPSESSID': cookie,
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://pokemon-arena.co.il',
            'Alt-Used': 'pokemon-arena.co.il',
            'Connection': 'keep-alive',
            'Referer': 'https://pokemon-arena.co.il/index.php?page=bot-check',
            # 'Cookie': 'theme=-1; PHPSESSID=b3dc1b38c5c0c7776d3ac4b8b5b0fdcb',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        params = {
            'page': 'bot-check',
        }

        data = {
            'g-recaptcha-response': result["code"],
            'battle': 'המשך להלחם!',
        }

        response = requests.post('https://pokemon-arena.co.il/index.php', params=params, cookies=cookies, headers=headers, data=data)
    except Exception as e:
        sys.exit(e)
