import numpy as np
import matplotlib.pyplot as plt

a = 0
b = -500
c = 0.0002
d = 0


#導関数dR/dt,dJ/dt
def func_Rom(t,R,J):
    return a * R + b * J  #dR/dt =aR+bJ

def func_Jur(t,R,J):
    return c * R + d * J #dJ/dt =cR+dJ


#Euler法（導関数、tの初期値、R,Jの初期値、刻み幅dt）
def euler(func_Rom, func_Jur, t, R, J, dt=1e-3):

    dR = func_Rom(t, R, J)*dt  #変化量を計算
    dJ = func_Jur(t, R, J)*dt  #変化量を計算
    t += dt  #変数を更新
    R += dR  #変化量を加えて更新
    J += dJ  #変化量を加えて更新

    return t, R, J


#常微分方程式を逐次計算（導関数、R,Jの初期値、tの開始点、tの終了点、刻み幅dt）
def ode_calc_(func_Rom, func_Jur, R_start, J_start, t_start, t_end, dt=1e-3):
    num_calc = 0  #計算回数
    t_div = np.abs((t_end-t_start)/dt)  #格子分割数
    if(t_end<t_start):  #負の方向に計算する時は刻み幅の符号を反転
        dt = -dt

    #初期値
    t = t_start  #独立変数t
    R = R_start  #従属変数R
    J = J_start  #従属変数J

    print("t = {:.7f},  R = {:.7f},  J = {:.7f}".format(t, R, J))

    #グラフ用データを追加
    t_list = [t]
    R_list = [R]
    J_list = [J]

    #ずっと繰り返す
    while(True):
        t, R, J = euler(func_Rom, func_Jur, t, R, J, dt)
        print("t = {:.7f},  R = {:.7f},  J = {:.7f}".format(t, R, J))

        #グラフ用データを追加
        t_list.append(t)
        R_list.append(R)
        J_list.append(J)

        num_calc += 1  #計算回数を数える

        #「計算回数が格子分割数以上」ならば終了
        if(t_div<=num_calc):
            print("Finished.")
            print()
            break

    return t_list, R_list, J_list

#可視化
def visualization(t_list, R_list, J_list):
    plt.xlabel("$t$")  #x軸の名前
    plt.ylabel("$LOVE(t)$")  #y軸の名前
    plt.grid()  #点線の目盛りを表示

    plt.plot(t_list,J_list, label="$Juliet(t)$", color='#ff0000')  #折線グラフで表示
    plt.plot(t_list,R_list, label="$Romio(t)$", color='#0000ff')  #折線グラフで表示



    plt.legend(loc='best') #凡例(グラフラベル)を表示
    plt.savefig('2_another.png')  #グラフを表示


#メイン実行部
if (__name__ == '__main__'):
    #Euler法でdt離れた点の値を取得
    t, R, J = euler(func_Rom, func_Jur, 0.0, 1.0, 1.0, 0.0)
    print("t = {:.7f},  R = {:.7f},  J = {:.7f}".format(t, R, J))


    #常微分方程式を逐次計算
    t_list, R_list, J_list = ode_calc_(func_Rom, func_Jur, 1.0, 1.0, -5.0, 5.0)


    #結果を可視化
    visualization(t_list, R_list, J_list)
