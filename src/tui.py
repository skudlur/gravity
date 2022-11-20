from rich.console import Console
from rich import print
from rich import box
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
import gravity_modules as gm

layout = Layout()
print(layout)

gm.ip_connected(gm.wiomw_list, gm.ip_list)
gm.name_connected(gm.wiomw_list, gm.name_list)

text = Text("gravity", justify="center")
text.stylize("bold magenta", 0, 3)
panel = Panel(text)
print(panel)

def table_gen() -> Table:
    table = Table(title="IP List", box=box.DOUBLE)

    table.add_column("No.", justify="center", style="cyan")
    table.add_column("Name", justify="center", style="magenta")
    table.add_column("IP Address", justify="center", style="green")
    
    for j in range(0, len(gm.ip_list)):
        table.add_row(f"{j+1}", f"{gm.name_list[j]}", f"{gm.ip_list[j]}")
    return table

print(table_gen())

