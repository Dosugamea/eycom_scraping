from typing import Any, Dict
from gui.const import ActionKey
from lib.eycom_scraper import EyComScraper, Article  # noqa
from gui.window import build_window
from gui.settings import Settings

"""
メインスクリプト
"""

# EyComScraperのインスタンス作成
client = EyComScraper()
# PySimpleGUIのWindow作成
window = build_window()
# 設定管理オブジェクト作成
settings = Settings()


# TODO: イベントに対応するスクリプトを割当
event_dict = {
    ActionKey.SELECT_CSV: settings.change_output_type,
    ActionKey.SELECT_JSON: settings.change_output_type,
    ActionKey.SELECT_TXT: settings.change_output_type,
    ActionKey.SELECT_WAIT: settings.change_wait,
    ActionKey.SELECT_NO_WAIT: settings.change_wait,
}
event_window_dict = {
    ActionKey.CHANGE_PATH: settings.change_output_path,
    ActionKey.SELECT_PATH: settings.change_output_path,
    ActionKey.ADD_KEYWORD: settings.add_keyword,
    ActionKey.DELETE_KEYWORD: settings.remove_keyword,
}


def start_process(settings: Settings):
    print(settings.output_type)
    print(settings.output_path)
    print(settings.keywords)
    print(settings.wait)


if __name__ == "__main__":
    # イベントループ
    while True:
        a, b = window.read()
        event: str = a
        values: Dict[str, Any] = b
        # print(event, values)
        if event in event_dict.keys():
            event_dict[event](values)
        if event in event_window_dict.keys():
            event_window_dict[event](window, values)
        if event == ActionKey.START:
            start_process(settings)
        if event in (None, "Exit"):
            break
    window.close()
