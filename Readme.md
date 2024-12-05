<p align="center">
  <img src="https://raw.githubusercontent.com/mohamedmamdouh22/price-parser/main/logos/logo-modified.png" alt="Price Parser Logo" width="400"/>
</p>

<h3 align="center">💰 Price Parser Reworkd: Extract Prices with Ease 💰</h3>

# Price Parser Reworkd

`Price Parser` is a Python library created by reworkd team that provides Pydantic-compatible data types for parsing and extracting price-related information from strings. It allows you to effortlessly handle numeric values, currency symbols, and currency names in a structured and validated way using Pydantic models.

---

- [Setup and Installation](#setup-and-installation)
- [Features](#features)
- [Usage](#usage)
  - [ParserTypePrice](#parsertypeprice)
  - [ParserTypeCurrency](#parsertypecurrency)
- [Example Use Cases](#example-use-cases)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)

---

## Setup and Installation

Install the library via pip:

```bash
pip install price-parser-reworkd
```

---

## Features

- Extract numeric price values from strings.
- Support for more than 60 currencies
- Detect currency symbols and convert them into readable currency names.
- Built on **Pydantic** for easy integration with modern Python projects.
- Lightweight and production-ready.
- Can handle price unavailable phrases

---

## Usage

### ParserTypeCurrency

Extract both the numeric price value and the currency details (symbol and name).

```python
from pydantic import BaseModel
from price_parser import ParserTypeCurrency

class PriceModel(BaseModel):
    price: ParserTypeCurrency

# Example 1: Valid input with currency symbol
price_info = PriceModel(price="$19.99")
print(price_info.price)
# Output: {'currency': 'USD', 'currency_symbol': '$', 'amount': 19.99}

# Example 2: Valid input without a currency
price_info = PriceModel(price=1500.75)
print(price_info.price)
# Output: {'currency': None, 'currency_symbol': None, 'amount': 1500.75}

# Example 3: String with known currency name
price_info = PriceModel(price="EUR 49.99")
print(price_info.price)
# Output: {'currency': 'EUR', 'currency_symbol': '€', 'amount': 49.99}

```

---

## Example Use Cases

### Full Price Details

Extract both the price value and currency details:

```python
from pydantic import BaseModel
from price_parser import ParserTypeCurrency

class CombinedModel(BaseModel):
    full_price_details_USD: ParserTypeCurrency
    full_price_details_EUR: ParserTypeCurrency

# Input data
data = {
    "full_price_details_USD": "USD 19.99",
    "full_price_details_EUR": "€1.234",
}

# Parse the data
price_info = CombinedModel(**data)
print(price_info.full_price_details_USD)   # Output: {'currency': 'USD', 'currency_symbol': '$', 'amount': 19.99}
print(price_info.full_price_details_EUR)  # Output: {'currency': 'EUR', 'currency_symbol': '€', 'amount': 1234.0}
```

### E-Commerce Data Processing

Ideal for processing pricing data from product listings.

```python
from pydantic import BaseModel
from price_parser import ParserTypeCurrency


class ProductModel(BaseModel):
    price: ParserTypeCurrency

def parse_and_display_products(products):
    """
    Parses a list of product prices using a Pydantic model and displays the extracted information.

    Args:
        products (list): A list of price strings to be parsed.
    """
    for product in products:
        try:
            product_data = ProductModel(price=product)
            info = product_data.price
            print(
                f"Price: {info['amount']}, Currency: {info['currency']}, Symbol: {info['currency_symbol']}"
            )
        except ValueError as e:
            print(f"Error parsing product price '{product}': {e}")


products = ["$19.99", "€15.50", "₹1200"]
parse_and_display_products(products)
```

---

## Tests

Run unit tests to verify functionality:

```bash
pytest
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the package.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Running the Package

You can use the library directly in your Python projects. For development, clone the repository and use Poetry to manage dependencies:

```bash
git clone https://github.com/mohamedmamdouh22/price-parser.git
cd price-parser
poetry install
```

Happy Parsing! 💰
