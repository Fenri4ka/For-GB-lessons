import random


def creating_base_csv():
    f = "Base.csv"
    with open(f, "w", encoding="utf-8") as data:
        data.write(f'Артикул,Наименование,Код номенклатуры,Номенклатурная группа,Цена(руб),Наличие(шт),Продажи январь,Продажи февраль,Продажи март,Продажи апрель,Продажи май, Продажи июнь,Продажи июль\n')


def getting_fill_base():
    f = "Base.csv"
    for _ in range(50):
        art = str(random.randint(100, 110)) + str(random.randint(100, 999)) + str(random.randint(100, 999))
        num_gr = "0" + str(random.randint(10, 15))
        sell_jun = random.randint(100, 500)
        sell_feb = random.randint(100, 500)
        sell_mar = random.randint(100, 500)
        sell_apr = random.randint(100, 500)
        sell_may = random.randint(100, 500)
        sell_jn = random.randint(100, 500)
        sell_jul = random.randint(100, 500)
        price = random.randint(100, 1000)
        with open(f, "a", encoding="utf-8") as data:
            data.write(f'{art},"Наименование",{num_gr},"группа",{price},{sell_jun},{sell_feb},{sell_mar},{sell_apr},{sell_may},{sell_jn},{sell_jul}\n')


