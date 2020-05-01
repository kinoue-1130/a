# -*- coding: utf-8

import sys

def asobi(a,b):

    nokori = a-b

    if 0 <= nokori:
        nokori = nokori
    else:
        nokori = -1

    return nokori

if __name__ == "__main__":

    i = list(map(int,input().split()))#N,M取得

    if 1 <= i[0] and i[0] <= 1000000 and 1 <= i[1] and i[1] <+ 1000:

        i_2 = list(map(int,input().split()))#A1-AM取得

        for x in range(len(i_2)):
            if i_2[x] <= 1 or 10000 <= i_2[x]:
                print('Aiは1から10000で入力してください')
                sys.exit()

        max_asobi = asobi(i[0],sum(i_2))
        print(max_asobi)

    else:
        print('Nは1から1000000、またはMは1から10000で入力してください')