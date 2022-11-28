import pandas as pd
field = list(range(1, 10))


def write_ladder(name):
    df = pd.read_csv("Ladder.csv", encoding='utf-8', index_col='Игрок')
    df.loc[name, 'Победы'] += 1
    df.to_csv("Ladder.csv", encoding='utf-8')


def see_ladder():
    df = pd.read_csv("Ladder.csv", encoding='utf-8')
    df.sort_values('Победы', ascending=False)
    print(df)
