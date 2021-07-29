# PiePieSpider

## Demo

An demo to use PiePieSpider is at https://github.com/Hedaozi/Spider/tree/main/CnkiSpider/QueryResult. To see how PiePieSpider works, you may focus on CnkiSpider/CnkiNetWalker.py at https://github.com/Hedaozi/Spider/blob/main/CnkiSpider/QueryResult/CnkiSpider/CnkiNetWalker.py.

## Usage

Copy the whole folder to root directory of your Python project. Then

```python
from PiePieSpider.Frame import *
from PiePieSpider.Content import *
```

## References

### PiePieSpider.SimpleQueue

This module provides `SimpleQueue` class. 

#### SimpleQueue

A very simple queue class. Multithreading is not supported. 

##### Properties

###### SimpleQueue.IsEmpty

A boolean property about whether the queue is empty.

###### SimpleQueue.Head

A int property about the index of head item.

###### SimpleQueue.Tail

A int property about the index of tail item.

###### SimpleQueue.ActiveIndexes

###### SimpleQueue.ActiveItems

###### SimpleQueue.ActiveCount

###### SimpleQueue.History

###### SimpleQueue.Last

###### SimpleQueue.AsDict

###### SimpleQueue.AsString

##### Methods

##### SimpleQueue.Add(self, item: any)

##### SimpleQueue.Pop(self)

##### SimpleQueue.AddItems(self, items: list)

##### SimpleQueue.Compress(self)

##### SimpleQueue.PopAll(self)

##### SimpleQueue.Clean(self)

##### SimpleQueue.Reinitialize(self)

##### Class Methods

##### SimpleQueue.FromString(cls, string: str)

##### SimpleQueue.FromDict(cls, dic: dict)

### PiePieSpider.Content

#### RequestGetter

##### Properties

###### RequestGetter.IsRequestsGet

###### RequestGetter.Text

###### RequestGetter.Bytes

##### Methods

###### RequestGetter.Get(self)

###### RequestGetter.Post(self, formData, verify = False)

#### HtmlTextTools

##### Class Methods

###### HtmlTextTools.DropLineMark(cls, string: str)

###### HtmlTextTools.DropReturnMark(cls, string: str)

###### HtmlTextTools.DropTabMark(cls, string: str)

###### HtmlTextTools.DropSpace(cls, string: str)

###### HtmlTextTools.DropAllSpacing(cls, string: str)

#### XmlParser

##### Class Methods

###### ElementTree(cls, html: str)

###### TryCatchXpath(cls, xml: lxml.etree.\_ElementTree, xpaths: list, index: int = 0)

#### ReParser

##### Class Methods

###### ReParser.QuickMatch(cls, regExp: str, string: str, index = 0)

#### BaseExtender

#### BaseNetWalker

##### Properties

###### BaseNetWalker.Result

###### BaseNetWalker.ErrorInfo

### PiePieSpider.Frame



