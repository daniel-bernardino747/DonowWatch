from random import randint
from pandas import read_csv

indexo = read_csv(r'C:\Users\Daniel.DESKTOPDAN\principal_tools\Documents\For_Datas\Dont-Know-Watch\movies.csv')


def randomMovie(arq):
    title_release = arq['title']
    random_choice = title_release.loc[randint(0, int(title_release.shape[0]))]
    return f'{random_choice}'


def listGenres(arq):
    t = list()
    for line in arq.index:
        for word in arq.loc[line, 'genres'].split('|'):
            if word in t:
                pass
            else:
                t.append(word)
    return t


if __name__ == "__main__":
    t = listGenres(indexo)
    print(t)