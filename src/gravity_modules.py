from who_is_on_my_wifi import *
from socket import *
from _thread import *
import os

wiomw_list = who() # who(n)
conn_list = []
ip_list = []
#router_ip = ''
#host_ip = ''
text = 'no'

def list_connections(wiomw_list):
    for j in range(0, len(wiomw_list)):
        comm = f"\n{wiomw_list[j][0]} {wiomw_list[j][1]}\n{wiomw_list[j][2]} {wiomw_list[j][3]}\n{wiomw_list[j][4]} {wiomw_list[j][5]}\n"
        print(comm)

def ip_connected(wiowm_list, ip_list):
    for j in range(0, len(wiowm_list)):
        ip_temp = f"{wiomw_list[j][1]}"
        if(len(ip_temp) > 15):
            try:
                ip_temp_list = ip_temp.split(", ")
            except Exception:
                raise Exception("No IP found, check your network connection")
            ip_temp_list = ip_temp.split(" ")
            ip_temp = ip_temp_list[0]
            ip_list.append(ip_temp)
        else:
            ip_list.append(ip_temp)

def router_ip(wiowm_list, ip_list):
    stat_ip_list = []
    for j in range(0, len(wiowm_list)):
        stat_temp = f'{wiomw_list[j][5]}'
        stat_ip_list.append(stat_temp)
    return stat_ip_list

def zip_ip_dict(list1, list2):
    return dict(zip(list1, list2))

def router_ip_set(wiowm_list, dict_ip):
    for j in range(0, len(wiowm_list)):
        stat_temp = f'{wiomw_list[j][5]}'
        ip_temp = f'{wiomw_list[j][1]}'
        if("(router)" in stat_temp):
            router_ip = dict_ip.get(f'{stat_temp}')
            return router_ip

def host_ip_set(wiowm_list, dict_ip):
    for j in range(0, len(wiowm_list)):
        stat_temp = f'{wiomw_list[j][5]}'
        ip_temp = f'{wiomw_list[j][1]}'
        if("(Your device)" in stat_temp):
            host_ip = dict_ip.get(f'{stat_temp}')
            return host_ip

#list_connections(wiomw_list)
#ip_connected(wiomw_list, ip_list)
#print(ip_list)
#stat_ip_list = router_ip(wiomw_list, ip_list)
#print(stat_ip_list)
#dict_ip = zip_ip_dict(stat_ip_list, ip_list)
#print(dict_ip)
#router_host_ip_set(wiomw_list, dict_ip)

#list_connections(wiomw_list, conn_list)
#print(conn_list)
