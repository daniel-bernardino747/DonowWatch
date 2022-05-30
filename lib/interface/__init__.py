class fg:
    black = '\033[90m'
    red = '\033[91m'
    green = '\033[92m'
    yell = '\033[93m'
    blue = '\033[94m'
    mag = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    reset = '\033[39m'


class bg:
    black = '\033[40m'
    red = '\033[101m'
    green = '\033[102m'
    burnyell = '\033[43m'
    yell = '\033[103m'
    blue = '\033[44m'
    mag = '\033[45m'
    pink = '\033[105m'
    cyan = '\033[106m'
    white = '\033[107m'
    grey = '\033[47m'
    reset = '\033[49m'


class stl:
    bright = '\033[1m'
    italic = '\033[3m'
    underline = '\033[4m'
    inverse = '\033[7m'
    scrat = '\033[9m'
    reset_all = '\033[0m'


def c():
    print('\n' * 30)


def options(*msg, crack='Exit'):
    menus = list()
    for a in msg:
        menus.append(a)
    for i, v in enumerate(menus):
        print(f'|{fg.mag}{f"[{i + 1}]":>14}{fg.white} {v:43}|')
    print(f'|{fg.red}{f"[0]":>14} {crack.title():43}{fg.white}|')
    print('=' * 60)
    n = int(input(f'{stl.inverse}{stl.bright}{" >>> DIGITE SUA OPÇÃO AQUI:":}{stl.reset_all}{fg.white} '))
    return n


def optionsList(*msg, crack='Exit'):
    menus = list()
    for a in msg:
        menus.append(a)
    breakline = 1
    for i, v in enumerate(menus):
        if breakline % 2 == 0:
            print(f'{fg.mag}{f"[{i + 1}]":>3}{fg.white} {v:24}|')
        else:
            print(f'|{fg.mag}{f"[{i + 1}]":>5}{fg.white} {v:23}', end=' ')
        breakline += 1
    n = int(input(f'\n{stl.inverse}{stl.bright}{" >>> DIGITE SUA OPÇÃO AQUI:":}{stl.reset_all}{fg.white} '))
    return n


def MainMenu(msg='MENU PRINCIPAL', nexit='EXIT', aexit=False):
    print(fg.white, end='')
    print('=' * 60)
    if aexit:
        print(f'{fg.mag}{stl.inverse}{stl.bright}{nexit:^60}{stl.reset_all}{fg.white}')
    else:
        print(f'{stl.inverse}{stl.bright}{msg:^60}{stl.reset_all}{fg.white}')
    print('=' * 60)


def SegundaryMenu(msg='MENU SEGUNDÁRIO'):
    print(fg.white, end='')
    print('=' * 60)
    print(f'{stl.bright}{msg:^60}{stl.reset_all}{fg.white}')
    print('=' * 60)


if __name__ == "__main__":
    MainMenu("DON'T KNOW WHAT TO WATCH?")
    resp = optionsList('genre 1', 'genre 2', 'genre 3', 'genre 3', 'genre 3', 'genre 3', 'genre 3', 'genre 3')
    if resp == 0:
        MainMenu(nexit='LOG OUT', aexit=True)
