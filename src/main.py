from who_is_on_my_wifi import *
from socket import *
from _thread import *
import os

wiomw_list = who() # who(n)
ip_list = []

def list_connections(wiomw_list):
    for j in range(0, len(wiomw_list)):
        comm = f"\n{wiomw_list[j][0]} {wiomw_list[j][1]}\n{wiomw_list[j][2]} {wiomw_list[j][3]}\n{wiomw_list[j][4]} {wiomw_list[j][5]}\n"
        print(comm)

def ip_connected(wiowm_list, ip_list):
    for j in range(0, len(wiowm_list)):
        ip_temp = f"{wiomw_list[j][1]}"
        if(len(ip_temp) > 15):
            ip_temp_list = ip_temp.split(", ")
            ip_temp = ip_temp_list[0]
            ip_list.append(ip_temp)
        else:
            ip_list.append(ip_temp)
        print(ip_list)

list_connections(wiomw_list)
ip_connected(wiomw_list, ip_list)
