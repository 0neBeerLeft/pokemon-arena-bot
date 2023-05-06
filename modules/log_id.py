def generate(code):
    for i in code.split("\n"):
        if "aanval_log_id=" in i:
            return i.split("+")[1]