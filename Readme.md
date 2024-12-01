
<p align="center">
  <img src="./.github/assets/banner.png" height="200" alt="Price Parser Banner" />
</p>

<h3 align="center">💰 Price Parser: Extract Prices with Ease 💰</h3>

# Price Parser

Price Parser is a Python library that makes it simple to extract prices from text. With built-in support for **Pydantic** data types, it returns prices as structured data, including numeric values, currency names, and symbols.

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
pip install price-parser
```

---

## Features

- Extract numeric price values from strings.
- Detect currency symbols and convert them into readable currency names.
- Built on **Pydantic** for easy integration with modern Python projects.
- Lightweight and production-ready.

---

## Usage

### ParserTypePrice
Extract the numeric price value from a string as a **float**.

\`\`\`python
from price_parser import ParserTypePrice

price = ParserTypePrice(price_string="$19.99")
print(price.value)  # Output: 19.99
\`\`\`

---

### ParserTypeCurrency
Extract both the numeric price value and the currency details (symbol and name).

\`\`\`python
from price_parser import ParserTypeCurrency

price_info = ParserTypeCurrency(price_string="$19.99")
print(price_info.value)      # Output: 19.99
print(price_info.currency)   # Output: "USD"
print(price_info.symbol)     # Output: "$"
\`\`\`

---

## Example Use Cases

### Single Price Extraction
Parse a single price from a string:
\`\`\`python
from price_parser import ParserTypePrice

price = ParserTypePrice(price_string="€49,99")
print(price.value)  # Output: 49.99
\`\`\`

### Full Price Details
Extract both the price value and currency details:
\`\`\`python
from price_parser import ParserTypeCurrency

price_info = ParserTypeCurrency(price_string="₹1,500")
print(price_info.value)      # Output: 1500.0
print(price_info.currency)   # Output: "INR"
print(price_info.symbol)     # Output: "₹"
\`\`\`

### E-Commerce Data Processing
Ideal for processing pricing data from product listings.

\`\`\`python
from price_parser import ParserTypeCurrency

products = ["$19.99", "€15.50", "₹1200"]
for product in products:
    info = ParserTypeCurrency(price_string=product)
    print(f"Price: {info.value}, Currency: {info.currency}, Symbol: {info.symbol}")
\`\`\`

---

## Tests

Run unit tests to verify functionality:
\`\`\`bash
pytest
\`\`\`

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the package.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Running the Package

You can use the library directly in your Python projects. For development, clone the repository and use Poetry to manage dependencies:
\`\`\`bash
git clone https://github.com/yourusername/price-parser.git
cd price-parser
poetry install
\`\`\`

Happy Parsing! 💰
