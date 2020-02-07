import numpy as np

from app.iterator.Iterator import Iterator


class BrowseHistory:

    def __init__(self):
        self.urls = np.array([])

    def push(self, url):
        self.urls = np.append(self.urls, url)

    def pop(self):
        removed = self.urls[-1]
        self.urls = np.delete(self.urls, -1)
        return removed

    def create_iterator(self):
        return NumpyIterator(self)


class ListIterator(Iterator):

    def __init__(self, history):
        self.history = history
        self.index = 0

    def has_next(self):
        return self.index < len(self.history.urls)

    def current(self):
        return self.history.urls[self.index]

    def next(self):
        self.index += 1


class NumpyIterator(Iterator):

    def __init__(self, history):
        self.history = history
        self.index = 0

    def has_next(self):
        return self.index < self.history.urls.size

    def current(self):
        return self.history.urls[self.index]

    def next(self):
        self.index += 1

