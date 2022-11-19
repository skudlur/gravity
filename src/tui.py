import pytermgui as ptg
import gravity_modules as gm

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

    window2 = (
            ptg.Window(
                "",
                ptg.InputField("Not", prompt="Name: "),
                "",
                ptg.Container(
                    "Hello",
                    box = "EMPTY_HORIZONTAL",
                ),
                "",
                width = 60,
                box = "DOUBLE",
            )
            .set_title("[210 bold]gravity2")
            .center()
    )

    window.select(0)
    window2.select(1)

    manager.add(window)
    manager.add(window2)
