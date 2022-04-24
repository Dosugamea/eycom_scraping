from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import time
import requests
from lxml import html as htmlParser
# https://github.com/lxml/lxml-stubs


@dataclass
class Article():
    title: str
    url: str


class EyComScraper():
    """https://www.ey.com/ja_jp/newsroom からニュースをスクレイピングするスクリプト"""

    ENDPOINT = "https://www.ey.com/ja_jp/index-pages/newsroom/" \
        "_j/main-content/tabs/item1/tabContent/" \
        "content/contentlistnews_copy.content"
    WAIT_TIME = 3

    def __init__(
        self, endpoint: Optional[str] = None, wait_time: Optional[int] = 3
    ) -> None:
        self.WAIT_TIME = wait_time
        if endpoint:
            self.ENDPOINT = endpoint

    def download_page(
        self, url: str,
        params: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, Any]] = None
    ):
        """ページを取得してlxml.htmlでパースしたElementを返します"""
        resp = requests.get(url, params=params, cookies=cookies)
        with open("out.html", "w", encoding="utf8") as f:
            f.write(resp.text)
        elem = htmlParser.fromstring(resp.text)
        return elem

    def get_total_pages(self, with_wait=False) -> int:
        """ニュースのページ数を取得します"""
        if with_wait:
            time.sleep(self.WAIT_TIME)
        elem = self.download_page(
            self.ENDPOINT,
            params={
                "p": 1,
                "arguments": "[]"
            }
        )
        count: str = elem.xpath(
            '//div[@class="page page-1"]/@data-page-count'
        )[0]
        return int(count)

    def get_news(self, page: int, with_wait=False) -> List[Article]:
        """指定したページのニュース一覧を取得します"""
        if with_wait:
            time.sleep(self.WAIT_TIME)
        elem = self.download_page(
            self.ENDPOINT,
            params={
                "p": page,
                "arguments": "[]"
            }
        )
        links = [
            "https://www.ey.com" + path
            for path in elem.xpath('//div[@class="contentList-text"]/a/@href')
        ]
        titles = elem.xpath('//span[@class="hyperlink-text-link"]/text()')
        resp = [
            Article(title, link)
            for title, link in zip(titles, links)
        ]
        return resp

    def get_filtered_news(
        self, keywords: List[str], from_all=False, with_wait=True
    ) -> List[Article]:
        """
        指定したキーワードに一致するニュースを取得します

        Args:
            keywords: 検索したいキーワードのリスト
            from_all: Trueの場合、過去全てのニュースから探索します(デフォルトは1ページ目のみ)
            with_wait: Falseの場合、待機時間なしで取得します(デフォルトは待機する)
        """
        news: List[Article] = self.get_news(1)
        if from_all:
            total_pages = self.get_total_pages(with_wait)
            for i in range(2, total_pages + 1):
                print(f"{i}/{total_pages} ページ目を取得しています")
                news.extend(self.get_news(i, with_wait))
        filtered_news = [
            news
            for news in news
            if any([keyword in news.title for keyword in keywords])
        ]
        return filtered_news


def main() -> None:
    client = EyComScraper()
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
    print(client.get_filtered_news(keywords, from_all=True))


if __name__ == '__main__':
    main()
