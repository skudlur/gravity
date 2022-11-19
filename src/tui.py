import pytermgui as ptg
import gravity_modules as gm
from pytermgui.window_manager.layouts import Slot, ROW_BREAK

gm.ip_connected(gm.wiomw_list, gm.ip_list)
stat_ip_list = gm.router_ip(gm.wiomw_list, gm.ip_list)
dict_ip = gm.zip_ip_dict(stat_ip_list, gm.ip_list)
router_ip = gm.router_ip_set(gm.wiomw_list, dict_ip)
host_ip = gm.host_ip_set(gm.wiomw_list, dict_ip)

CONFIG = """
config:
    InputField:
        styles:
            prompt: dim italic
            cursor: '@72'
        Label:
            styles:
                value: dim bold
        Window:
            styles:
                border: '60'
                corner: '60'
        Container:
            styles:
                border: '96'
                corner: '96'
"""

with ptg.YamlLoader() as loader:
    loader.load(CONFIG)

with ptg.WindowManager() as manager:
    layout = manager.layout

    layout.add_slot(Slot("Header", width=ptg.terminal.width - 30, height=7))
    layout.add_slot(Slot("Header Right"))

    layout.add_break()

    layout.add_slot(Slot("Body Left"))
    layout.add_slot(Slot("Body Right"))

    layout.add_break()

    layout.add_slot(Slot("Footer", height=5))

    for slot in layout.slots:
        if slot is ROW_BREAK:
            continue
        
        manager.add(ptg.Window(f"[bold] {slot.label}", box="DOUBLE"), animate=False)

    window = (
            ptg.Window(
                "",
                ptg.InputField("", prompt="IP Info:"),
                "",
                ptg.Container(
                    f'Router IP: {router_ip}',
                    f'Host IP: {host_ip}',
                    box = "EMPTY_VERTICAL",
                ),
                "",
                width = 60,
                box = "DOUBLE",
            )
            .set_title("[210 bold]gravity", position=0)
            .center()
    )
    window.select(0)

    manager.add(window)
