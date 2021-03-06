import lib.interface as inter
import lib.index as index
from pandas import read_csv

indexo = read_csv(r'C:\Users\Daniel.DESKTOPDAN\principal_tools\Documents\For_Datas\Dont-Know-Watch\movies.csv')

while True:
    inter.MainMenu("DON'T KNOW WHAT TO WATCH?")
    resp = inter.options('Giveaway a Random Movie', 'Select a Random Movie According to Genre')
    try:
        if resp == 1:
            ans = index.randomMovie(indexo)
            print('=' * 60)
            print(' >>> Our recommendation is:', inter.fg.mag, ans, inter.fg.white)
        elif resp == 2:
            while True:
                inter.SegundaryMenu('GENRES')
                genres = index.listGenres(indexo)
                respo = inter.optionsList(genres)
                if respo == 0:
                    break
                elif respo > 20 or respo < 0:
                    print('=' * 60)
                    print('\033[93mThis genre is not listed. Try Again')
                    pass
                else:
                    ans = respo - 1
                    for i, v in enumerate(genres):
                        if ans == i:
                            movie = index.randomInGenre(indexo, v)
                            print('=' * 60)
                            print(' >>> Our recommendation is:', inter.fg.mag, movie, inter.fg.white)
                    break
        elif resp == 0:
            inter.MainMenu(nexit='LOG OUT', aexit=True)
            break
        elif resp < 0 or resp > 2:
            raise ValueError

    except ValueError:
        print('\n\033[91m<<<\033[97m O valor digitado não é aceito.\n'
              '\033[91m<<<\033[97m Digite um numeral entre as opções.\n')
        continue
