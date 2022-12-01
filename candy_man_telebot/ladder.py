import pandas as pd
import csv


def write_ladder(player):
    df = pd.read_csv("candy_ladder.csv", encoding='utf-8', index_col='Игрок')
    df.loc[player, 'Победы'] += 1
    df.sort_values('Победы', ascending=False)
    df.to_csv("candy_ladder.csv", encoding='utf-8')
    
    
def see_ladder():
    ladder = ''
    with open("candy_ladder.csv", encoding="utf-8") as f:
        read_f = csv.reader(f, delimiter=",")
        for row in read_f:
            ladder += f'{row[0]} {row[1]}\n'
    return ladder