import PySimpleGUI as sg

from gui.const import ActionKey

output_frame = sg.Frame(
    "出力方法",
    [
        [
            sg.Radio(
                "csv",
                key=ActionKey.SELECT_CSV,
                group_id="0",
                default=True,
                enable_events=True,
            ),
            sg.Radio(
                "json",
                key=ActionKey.SELECT_JSON,
                group_id="0",
                default=False,
                enable_events=True,
            ),
            sg.Radio(
                "txt",
                key=ActionKey.SELECT_TXT,
                group_id="0",
                default=False,
                enable_events=True,
            )
        ],
    ],
    size=(170, 50),
)
