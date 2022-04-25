from typing import Any, Dict, List
import PySimpleGUI as sg
from gui.const import ActionKey

"""
PySimpleGUIのアクション発生時に変更される設定インスタンス
"""


class Settings():
    output_type: str = 'csv'
    output_path: str = '保存先'
    keyword: List[str] = ['']
    wait: bool = False

    def __init__(self) -> None:
        self.output_type: str = 'csv'
        self.output_path: str = '保存先'
        self.keywords: List[str] = ['']
        self.wait: bool = False

    def change_output_type(self, params: Dict[str, int]) -> None:
        if params[ActionKey.SELECT_CSV]:
            self.output_type = 'csv'
        elif params[ActionKey.SELECT_JSON]:
            self.output_type = 'json'
        elif params[ActionKey.SELECT_TXT]:
            self.output_type = 'txt'
        print("output_type", self.output_type)

    def change_wait(self, params: Dict[str, Any]) -> None:
        if params[ActionKey.SELECT_WAIT]:
            self.wait = True
        elif params[ActionKey.SELECT_NO_WAIT]:
            self.wait = False
        print("wait", self.wait)

    def change_output_path(self, window: sg.Window, params: Dict[str, Any]) -> None:
        # 開くから変更された場合
        if params[ActionKey.SELECT_PATH] != self.output_path:
            self.output_path = params[ActionKey.SELECT_PATH]
            window[ActionKey.CHANGE_PATH].update(self.output_path)

    def add_keyword(self, window: sg.Window, params: Dict[str, Any]) -> None:
        new_kw = params["input"]
        self.keywords.append(new_kw)

    def remove_keyword(self, window: sg.Window, params: Dict[str, Any]) -> None:
        remove_kw = params["keywords"][0]
        self.keywords = [k for k in self.keywords if k != remove_kw]
