#!/usr/bin/env python3

class Book:
    def __init__(self, title, author=None, page_count=272, genre=None):
        self.title = title
        self._author = author
        self._page_count = page_count
        self._genre = genre

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    
        