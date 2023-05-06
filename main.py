import modules.log_id as id
import modules.sid as sid
import modules.start_game as game
import modules.attack as attack
import modules.finish as finish
import modules.bypass as bypass
import requests
import time
import sys
start_time = time.time()
Area = {
	0: {"id": 3, "name": "Grass","x":"141","y":"218"},
	1: {"id": 5, "name": "Cave"},
	2: {"id": 2, "name": "Fighting school"},
	3: {"id": 1, "name": "Lava cave"},
}

cookie = "Account-Cookie"
total_xp = 0
x = 0
while 1:
	try:
		game_text = game.start_game(cookie,3)
		log_id = id.generate(game_text)
		if "אנא השלם את משימת האבטחה על מנת להמשיך להלחם" in game_text:
			bypass.solve()
		else:
			attack.fight(cookie,"Close Combat",sid.generate(),log_id)
			finish.finish_game(cookie,sid.generate(),log_id)
			print(f"[+] {x} Battle(s)")
			x += 1
	except:
		bypass.solve(cookie)