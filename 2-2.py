##幅優先探索

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

a = np.loadtxt("maze.txt")
print(a)

open_list = []
close_list =[]

aisle_list = [] ##ノードを格納するリスト

i=0
j=0

for i in range (15): ##通し番号を振ってリストに格納
    for j in range (15):
        if a[i,j] == 0:
            aisle_list.append((i, j))

print(aisle_list)


for i in range (0,15): ##探索開始
    for j in range(0,15):
        if a[i,j] == 0:

            open_list.append((i,j))


##pop処理

            if close_list != None:
                close_list.append(open_list.pop(0))

##周辺ノードのオープンリストへのアペンド
##迷路の数値が0、かつ未探索のものをopリストに追加

            if a[i,j-1] == 0 and (i,j-1) not in open_list and (i,j-1) not in close_list:
                open_list.append((i,j-1))

            elif [i+1,j] == 0 and (i+1,j) not in open_list and (i+1,j) not in close_list:
                open_list.append((i+1,j))

            elif a[i,j+1] == 0 and (i,j+1) not in open_list and (i,j+1) not in close_list:
                open_list.append((i,j+1))

            elif a[i+1,j] == 0 and (i+1,j) not in open_list and (i+1,j) not in close_list:
                open_list.append((i+1,j))

print(close_list)
