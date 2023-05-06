import requests

def finish_game(cookie,sid,log_id):
    cookies = {
        'theme': '-1',
        'PHPSESSID': cookie,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Alt-Used': 'pokemon-arena.co.il',
        'Connection': 'keep-alive',
        'Referer': 'https://pokemon-arena.co.il/?page=attack/wild/wild-attack',
        # 'Cookie': 'theme=-1; PHPSESSID=b3dc1b38c5c0c7776d3ac4b8b5b0fdcb',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'aanval_log_id': log_id,
        'sid': sid,
    }

    response = requests.get(
        'https://pokemon-arena.co.il/attack/wild/wild-finish.php',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response.text