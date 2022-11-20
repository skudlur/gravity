from rich.console import Console
from rich import print
from rich import box
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
import gravity_modules as gm
import tui_modules as tm
import os

stat_ip_list = gm.router_ip(gm.wiomw_list, gm.ip_list)
dict_ip = gm.zip_ip_dict(stat_ip_list, gm.ip_list)
router_ip = gm.router_ip_set(gm.wiomw_list, dict_ip)
host_ip = gm.host_ip_set(gm.wiomw_list, dict_ip)
table = tm.table_gen()

os.system("clear")

text = Text("gravity", justify="center")
text.stylize("bold magenta", 0, 3)
panel = Panel(text)
print(panel)

text2 = Text(f"Router IP: {router_ip}" + f"\nHost IP: {host_ip}", justify = "center")
text2.stylize("pink")
panel2 = Panel(text2)

sys_info = Text("System Information", justify="center")
sys_panel = Panel(sys_info)

layout = Layout()
layout.split_row(
        Layout(name="Available devices"),
        Layout(name="left")
)
layout["Available devices"].update(
        table
)
layout["left"].ratio = 2
layout["left"].split_column(
        Layout(name="System Info")
)
layout["System Info"].update(
        panel2
)

print(layout)
