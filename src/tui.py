import pytermgui as ptg
from pytermgui.pretty import pprint
import yaml
import yamlloader

OUTPUT = {}

def submit(manager: ptf.WindowManager, window: ptg.Window) -> None:
    for widget in window:
        if isinstace(widget, ptg.InputField):
            OUTPUT[widget.prompt] = widget.value
            continue

        if isinstance(widget, ptg.Container):
            label, field = iter(widget)
            OUTPUT[label.value] = field.value

    manager.stop()

with ptg.YamlLoader() as loader:
    loader.load(CONFIG)

with ptg.WindowManager() as manager:
    window = {
        ptf.Window(
            "",

        )
    }


