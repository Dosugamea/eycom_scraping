import PySimpleGUI as sg
from gui.const import ActionKey
from gui.frames.keywords import build_keywords_frame
from gui.frames.output import output_frame
from gui.frames.process import process_frame
from gui.frames.save import save_frame

"""
PySimpleGUIのWindow作成
"""

keywords = [
    "気候変動",
    "脱炭素",
    "サステナ",
    "CO",
    "排出量",
    "TCFD",
    "TNFD",
    "銀行",
    "金融",
]

layout = [
    [
        [build_keywords_frame(keywords)],
        [output_frame, process_frame],
        [save_frame],
    ],
    [sg.Submit("取得開始", key=ActionKey.START, size=(47, 2), disabled=False)],
    [sg.Text("処理ログ")],
    [sg.Output(size=(52, 10), key="log")],
]

sg.theme("DarkGrey9")


def build_window():
    window = sg.Window("EyComScraping", layout)
    return window
