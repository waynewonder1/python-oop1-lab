# Object Oriented Programming Lab - Bookstore

A small Python OOP exercise modeling two objects sold by an online bookstore:
a `Book` you can read and flip pages in, and a `Coffee` you can order and tip
for.

## Description

This project defines two classes:

- **`Book`** (`lib/book.py`) — has a `title` and a `page_count`. `page_count`
  is validated to always be an integer; assigning a non-integer prints
  `page_count must be an integer` instead of setting it. Calling
  `turn_page()` prints `Flipping the page...wow, you read fast!`.
- **`Coffee`** (`lib/coffee.py`) — has a `size` and a `price`. `size` is
  validated to be one of `Small`, `Medium`, or `Large`; any other value
  prints `size must be Small, Medium, or Large` instead of setting it.
  Calling `tip()` prints `This coffee is great, here's a tip!` and
  increases `price` by 1.

## Installation

1. Clone this repository.
2. Install dependencies:

   ```console
   pipenv install
   ```

3. Enter the virtual environment:

   ```console
   pipenv shell
   ```

## Usage

```python
from lib.book import Book
from lib.coffee import Coffee

book = Book("And Then There Were None", 272)
book.turn_page()  # "Flipping the page...wow, you read fast!"

coffee = Coffee(size="Large", price=3.50)
coffee.tip()  # "This coffee is great, here's a tip!" and price becomes 4.50
```

## Running Tests

This project is test-driven. Run all tests with:

```console
pytest
```

Or run the suites separately:

```console
pytest -x lib/testing/book_test.py
pytest -x lib/testing/coffee_test.py
```

The `-x` flag stops the run at the first failure, which is convenient while
developing.

## Screenshot

![All tests passing](images/tests-passing.png)

## Contributing

Issues and pull requests are welcome.

## License

See [LICENSE.md](LICENSE.md).
