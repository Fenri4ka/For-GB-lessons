from write_resoults import field


def build_field():
    print("*" * 13)
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print('*'* 13)
