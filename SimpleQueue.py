from json import dumps, loads
import json

class SimpleQueue():
    def __init__(self):
        self.__queue = list()
        self.__tail = 0
        self.__head = 0
        return
    
    # Properties
    @property
    def IsEmpty(self) -> bool:
        return self.__head == self.__tail

    @property
    def Head(self) -> int:
        return self.__head

    @property
    def Tail(self) -> int:
        return self.__tail

    @property
    def ActiveIndexes(self) -> list:
        return range(self.__head, self.__tail)

    @property
    def ActiveItems(self) -> list:
        return [self.__queue[i] for i in self.ActiveIndexes]

    @property
    def ActiveCount(self) -> int:
        return self.__tail - self.__head

    @property
    def History(self) -> list:
        return self.__queue

    @property
    def Last(self):
        return self.History[self.Head - 1]
    
    @property
    def AsDict(self) -> dict:
        queueDict = {
            "head": self.__head,
            "tail": self.__tail,
            "queue": self.__queue
        }
        return queueDict
    
    @property
    def AsString(self) -> str:
        return json.dumps(self.AsDict, ensure_ascii = False, indent = 4)

    # Methods
    def Add(self, item):
        self.__queue.append(item)
        self.__tail += 1
        return

    def Pop(self):
        self.__head += 1
        return self.__queue[self.__head - 1]

    def AddItems(self, items: list):
        for item in items:
            self.Add(item)
        return

    def Compress(self):
        """Compress queue. This will drop all deactive items."""
        self.__queue = self.ActiveItems
        self.__tail = self.ActiveCount
        self.__head = 0
        return

    def PopAll(self):
        """Pop up all item."""
        pops = list()
        while not self.is_empty:
            pops.append(self.pop())
        return pops

    def Clean(self):
        self.__head = self.__tail
        return

    def Reinitialize(self):
        """Reinitialize queue. But why don't you create a new empty queue?"""
        self.__queue = list()
        self.__head = 0
        self.__tail = 0
        return
    
    # Construct
    @classmethod
    def FromString(cls, string: str):
        queueDict = loads(string)
        return cls.FromDict(queueDict)

    @classmethod
    def FromDict(cls, dic: dict):
        queue = SimpleQueue()
        queue.__head = dic["head"]
        queue.__tail = dic["tail"]
        queue.__queue = dic["queue"]
        return queue

    # Magic Methods
    def __repr__(self):
        """For directly typing in command line."""
        abstract = "Head: {}, Tail: {}\n".format(self.Head, self.Tail)
        abstract += "Active: {}\n".format(self.ActiveItems)
        abstract += "History:{}\n".format(self.History)
        return abstract

    def __str__(self):
        """For print()."""
        return self.__repr__()

    def __len__(self):
        """For len()."""
        return self.ActiveCount

    def __iter__(self):
        """For iterator"""
        for item in self.ActiveItems:
            yield item

    def __contains__(self, item):
        """For operator 'in'."""
        return item in self.ActiveItems

    def __bool__(self):
        """Convert to bool."""
        return not self.IsEmpty
