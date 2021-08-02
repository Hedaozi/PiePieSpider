## Introduction to PiePieSpider

### Demo

An demo to use PiePieSpider is at [here](https://github.com/Hedaozi/Spider/tree/main/CnkiSpider/QueryResult). To see how PiePieSpider works, you may focus on [CnkiSpider/CnkiNetWalker.py](https://github.com/Hedaozi/Spider/blob/main/CnkiSpider/QueryResult/CnkiSpider/CnkiNetWalker.py).

### Usage

Copy the whole folder to root directory of your Python project. Then

```python
from PiePieSpider.Frame import *
from PiePieSpider.Content import *
```

## Simple API References

See API references at [here](https://hedaozi.github.io/Documentations/Reference-PiePieSpider).

### Dependencies:

- Python 3
- requests
- lxml
- json
- re
- time
- traceback

### PiePieSpider.SimpleQueue

#### SimpleQueue

A very simple queue class. Multithreading is not supported. 

A SimpleQueue has 3 fields, `head`, `tail` and `queue.` When pop, the queue set `head` to `head + 1` instead of remove the popped item from the `queue` (a `list` in fact). If you want to remove the popped item from the `queue`, use `self.Compress()` method or `self.Reinitialize()` method.

##### Properties

| Usage | Return | Description |
| ----- | ------ | ----------- |
| `SimpleQueue.IsEmpty` | `bool` | Whether the queue is empty. |
| `SimpleQueue.Head` | `int` | The index of head item. |
| `SimpleQueue.Tail` | `int` | The index of tail item. |
| `SimpleQueue.ActiveIndexes` | `list` | Indexes of items in the queue. |
| `SimpleQueue.ActiveItems` | `list` | Items in the queue. |
| `SimpleQueue.ActiveCount` | `int` | Length of the queue. |
| `SimpleQueue.History` | `list` | Items in the queue and popped items. |
| `SimpleQueue.Last` | `Any`| Last popped item. |
| `SimpleQueue.AsDict` | `dict` | Convert to `dict`. |
| `SimpleQueue.AsString` | `str` | Convert to `str`. |

##### Methods

| Usage | Return | Description |
| ----- | ------ | ----------- |
| `SimpleQueue.Add(self, item: Any)` | `None` | Add an item. |
| `SimpleQueue.Pop(self)` | `Any` | Pop an item. |
| `SimpleQueue.AddItems(self, items: list)` | `None` | Add items. |
| `SimpleQueue.Compress(self)` | `None` | Delete deactive (popped) items from history. |
| `SimpleQueue.PopAll(self)` | `list` | Pop all items. |
| `SimpleQueue.Clean(self)` | `None` | Pop all items without return value. |
| `SimpleQueue.Reinitialize(self)` | `None` | Set queue as new. |

##### Class Methods

| Usage | Return | Description |
| ----- | ------ | ----------- |
| `SimpleQueue.FromString(cls, string: str)` | `SimpleQueue` | Construct method. Create a `SimpleQueue` instance from **json** style string. |
| `SimpleQueue.FromDict(cls, dic: dict)` | `SimpleQueue` | Construct method. Create a `SimpleQueue` instance from `dict`. |

### PiePieSpider.Content

#### RequestGetter

##### Properties

| Usage | Description |
| ----- | ----------- |
| RequestGetter.IsRequestsGet | |
| RequestGetter.Text | |
| RequestGetter.Bytes | |

##### Methods

| Usage | Description |
| ----- | ----------- |
| RequestGetter.Get(self) | |
| RequestGetter.Post(self, formData, verify = False) | |

#### HtmlTextTools

##### Class Methods

| Usage | Description |
| ----- | ----------- |
| HtmlTextTools.DropLineMark(cls, string: str) | |
| HtmlTextTools.DropReturnMark(cls, string: str) | |
| HtmlTextTools.DropTabMark(cls, string: str) | |
| HtmlTextTools.DropSpace(cls, string: str) | |
| HtmlTextTools.DropAllSpacing(cls, string: str) | |

#### XmlParser

##### Class Methods

| Usage | Description |
| ----- | ----------- |
| XmlParser.ElementTree(cls, html: str) | |
| XmlParserTryCatchXpath(cls, xml: lxml.etree._ElementTree, xpaths: list, index: int = 0) | |

#### ReParser

##### Class Methods

| Usage | Description |
| ----- | ----------- |
| ReParser.QuickMatch(cls, regExp: str, string: str, index = 0) | |

#### BaseExtender

#### BaseNetWalker

##### Properties

| Usage | Description |
| ----- | ----------- |
| BaseNetWalker.Result | |
| BaseNetWalker.ErrorInfo | |

### PiePieSpider.Frame

#### WorkImage

##### Methods

| Usage | Description |
| ----- | ----------- |
| Save(self, path: str) | |
| SaveAsDir(self, path: str, storageLengthLimit: int) | Not support currently. |

##### Class Methods

| Usage | Description |
| ----- | ----------- |
| FromJson(cls, path: str) | |
| FromDir(cls, path: str, storageLengthLimit: int) | Not support currently. |
| New(cls, initialItems: list) | |

#### SimpleSpiderFrame

##### Methods

| Usage | Description |
| ----- | ----------- |
| LoadWorkImage(self, workImage: WorkImage) | |
| NewStart(self, initialItems: list, outputPath: str, groupSize: int) | |
| Continue(self, outputPath: str, groupSize: int, workImage: WorkImage = None, workImagePath: str = None, fixError: bool = True) | |
| FixError(self) | |
| StartSpider(self, outputPath: str, groupSize: int) | |
| ReportProcess(self) | |
| ReportResult(self, isError: bool, result: str = "") | |
| ReportCache(self) | |
| ReportCacheSavingDone(self) | |
| SpiderPause(self) | |

#### MultiThreadSpiderFrame

Not support currently.

