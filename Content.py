import requests
from lxml import etree
import re
from traceback import format_exc

class RequestGetter():
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        return

    def Get(self):
        self.response = requests.get(self.url, headers = self.headers)
        return

    def Post(self, formData, verify = False):
        self.response = requests.post(self.url, data = formData, headers = self.headers, verify = verify)
        return

    @property
    def IsRequestsGet(self):
        return self.response.status_code == 200

    @property
    def Text(self):
        return self.response.text

    @property
    def Bytes(self):
        return self.response.content

class HtmlTextTools():
    @classmethod
    def DropLineMark(cls, string):
        return string.replace("\n", "")

    @classmethod
    def DropReturnMark(cls, string):
        return string.replace("\r", "")

    @classmethod
    def DropTabMark(cls, string):
        return string.replace("\t", "")

    @classmethod
    def DropSpace(cls, string):
        return string.replace(" ", "")

    @classmethod
    def DropAllSpacing(cls, string: str):
        string = cls.DropLineMark(string)
        string = cls.DropReturnMark(string)
        string = cls.DropTabMark(string)
        string = cls.DropSpace(string)
        return string

class XmlParser(HtmlTextTools):
    Utf8Parser = etree.HTMLParser(encoding = "utf-8")

    @classmethod
    def ElementTree(cls, html):
        return etree.fromstring(html, parser = cls.Utf8Parser)

    @classmethod
    def TryCatchXpath(cls, xml: etree._ElementTree, xpaths: list, index: int = 0):
        if index >= len(xpaths):
            return None
        try:
            result = xml.xpath(xpaths[index])
            return (
                result if result != []
                else cls.TryCatchXpath(xml, xpaths, index + 1)
            )
        except:
            print(format_exc())
            return cls.TryCatchXpath(xml, xpaths, index + 1)

class ReParser(HtmlTextTools):
    @classmethod
    def QuickMatch(cls, regExp: str, string: str, index = 0) -> str:
        """Match a regular expression and a string. Return the certain item of results.
        regExp: Regular expression.
        string: String to be matched.
        index: The index of item returned. Default as 0.
        """
        pattern = re.compile(regExp)
        results = re.findall(pattern, string)
        return results[index]

class BaseExtender():
    def __init__(self, spiderControl, spiderItems):
        spiderControl.AddItems(spiderItems)
        return

class BaseNetWalker():
    @property
    def Result(self):
        pass

    @property
    def ErrorInfo(self):
        pass
    