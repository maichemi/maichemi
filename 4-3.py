import math

from math import exp

def h(x):
    return x*exp(-x/2)-exp(-x)

def h_prime(x):
    return exp(-x/2)-1/2*x*exp(-x/2)+exp(-x)

def Newton(ini,err):
    x_n=ini
    x_n_scc=0
    count=0
    while True:
        count=count+1
        x_n_scc=x_n-h(x_n)/h_prime(x_n)
        if h(x_n_scc)<err:
            break
        x_n=x_n_scc
    print(\
        "数値解は",x_n_scc,\
        "\nその時の関数の値は",h(x_n_scc),\
        "\n計算回数は",count,"です")
