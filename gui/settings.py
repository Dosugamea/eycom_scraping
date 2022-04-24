from typing import Any, Dict, List

from gui.const import ActionKey

"""
PySimpleGUIのアクション発生時に変更される設定インスタンス
"""


class Settings():
    output_type: str = 'csv'
    output_path: str = '/tmp'
    keyword: List[str] = ['']
    wait: bool = False

    def __init__(self) -> None:
        self.output_type: str = 'csv'
        self.output_path: str = '/tmp'
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

    def change_output_path(self, params: Dict[str, Any]) -> None:
        pass

    def add_keyword(self, params: Dict[str, Any]) -> None:
        pass

    def remove_keyword(self, params: Dict[str, Any]) -> None:
        pass
