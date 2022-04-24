import PySimpleGUI as sg

from gui.const import ActionKey

save_frame = sg.Frame(
    "保存先",
    [
        [
            sg.InputText(
                key=ActionKey.CHANGE_PATH,
                default_text='保存先',
                enable_events=True
            ),
            sg.InputText(
                key=ActionKey.SELECT_PATH,
                do_not_clear=False,
                enable_events=True,
                visible=False
            ),
            sg.FileSaveAs(
                "開く",
                initial_folder='/tmp'
            ),
        ],
    ],
    size=(380, 50),
)
