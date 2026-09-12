#!/usr/bin/env python3

class Book:
    """Represents a book that can be read online, tracking its title and page count."""

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        # Guard against non-integer page counts so downstream reading
        # logic can always assume page_count is a whole number.
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
