import requests

def start_game(cookie,map):
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
        'Referer': 'https://pokemon-arena.co.il/?page=attack/attack_map',
        # 'Cookie': 'theme=-1; PHPSESSID=b3dc1b38c5c0c7776d3ac4b8b5b0fdcb',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = {
        'gebied': map,
    }

    response = requests.post(
        'https://pokemon-arena.co.il/?page=attack/attack_map#GameBox',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return response.text