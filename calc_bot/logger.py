def save_log(some_str, res):
    with open('Logger.txt', "a", encoding="utf-8") as data:
        data.write(f'{some_str} = {res}\n')