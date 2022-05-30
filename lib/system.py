import lib.interface as inter
import lib.index as index
from pandas import read_csv

indexo = read_csv(r'C:\Users\Daniel.DESKTOPDAN\principal_tools\Documents\For_Datas\Dont-Know-Watch\movies.csv')

while True:
    inter.MainMenu("DON'T KNOW WHAT TO WATCH?")
    resp = inter.options('Giveaway a Movie Aleatory', 'Select a Genre')
    if resp == 1:
        ans = index.randomMovie(indexo)
        print('=' * 60)
        print(' >>> Our recommendation is:', inter.fg.mag, ans, inter.fg.white)
    if resp == 2:
        inter.SegundaryMenu('GENRES')
        genres = index.listGenres(indexo)
        inter.optionsList(genres)
    if resp == 0:
        inter.MainMenu(nexit='LOG OUT', aexit=True)
