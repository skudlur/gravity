from who_is_on_my_wifi import *
from socket import *
from _thread import *
import os

wiomw_list = who() # who(n)

for j in range(0, len(wiomw_list)):
    comm = f"\n{wiomw_list[j][0]} {wiomw_list[j][1]}\n{wiomw_list[j][2]} {wiomw_list[j][3]}\n{wiomw_list[j][4]} {wiomw_list[j][5]}\n"
    print(comm)


