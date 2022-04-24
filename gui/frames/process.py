import PySimpleGUI as sg

from gui.const import ActionKey

process_frame = sg.Frame(
    "動作方法",
    [
        [
            sg.Radio(
                "待機する",
                key=ActionKey.SELECT_WAIT,
                group_id="1",
                default=True,
                enable_events=True,
            ),
            sg.Radio(
                "待機しない",
                key=ActionKey.SELECT_NO_WAIT,
                group_id="1",
                default=False,
                enable_events=True,
            )
        ],
    ],
    size=(200, 50),
)
