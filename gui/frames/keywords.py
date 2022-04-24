from gui.const import ActionKey
from typing import List
import PySimpleGUI as sg


def build_keywords_frame(keywords: List[str]) -> sg.Frame:
    keywords_frame = sg.Frame(
        "対象キーワード",
        [
            [
                sg.Input("ここにキーワードを入力...", key='input', size=(25, 1)),
                sg.Listbox(keywords, size=(25, 3), key='keywords'),
            ],
            [
                sg.Button(
                    "入力を追加",
                    key=ActionKey.ADD_KEYWORD,
                    size=(20, 1),
                ),
                sg.Button(
                    "選択を削除",
                    key=ActionKey.DELETE_KEYWORD,
                    size=(20, 1),
                )
            ]
        ],
        size=(380, 110)
    )
    return keywords_frame
