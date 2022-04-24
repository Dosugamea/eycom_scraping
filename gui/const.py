from enum import Enum

"""
PySimpleGUIのActionの定数を定義
"""


class ActionKey(Enum):
    ADD_KEYWORD = 1
    DELETE_KEYWORD = 2
    SELECT_CSV = 3
    SELECT_JSON = 4
    SELECT_TXT = 5
    SELECT_WAIT = 6
    SELECT_NO_WAIT = 7
    CHANGE_PATH = 8
    SELECT_PATH = 9
    START = 10

# class VariableKey(Enum):
#     INPUT_KEYWORD = 1
#     CHOICE_KEYWORD = 2
