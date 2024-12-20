import pytest
from pydantic import BaseModel, ValidationError
from price_parser.parser import ParserTypeCurrency


class _TestModel(BaseModel):
    value: ParserTypeCurrency


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("$1,000.00", {"currency": "USD", "currency_symbol": "$", "amount": 1000.00}),
        ("€1.00", {"currency": "EUR", "currency_symbol": "€", "amount": 1.0}),
        (
            "£1,000,000.00",
            {"currency": "GBP", "currency_symbol": "£", "amount": 1000000.00},
        ),
        ("¥1000.00", {"currency": "JPY", "currency_symbol": "¥", "amount": 1000.00}),
        ("₹1000", {"currency": "INR", "currency_symbol": "₹", "amount": 1000.00}),
        (1000, {"currency": None, "currency_symbol": None, "amount": 1000.00}),
        (1000.00, {"currency": None, "currency_symbol": None, "amount": 1000.00}),
        ("-¥1,234.56", {"currency": "JPY", "currency_symbol": "¥", "amount": -1234.56}),
        ("$0.1", {"currency": "USD", "currency_symbol": "$", "amount": 0.1}),
        ("€.1", {"currency": "EUR", "currency_symbol": "€", "amount": 0.1}),
        ("1000", {"currency": None, "currency_symbol": None, "amount": 1000.00}),
        (1000, {"currency": None, "currency_symbol": None, "amount": 1000.00}),
        (
            "$1,234.5678",
            {"currency": "USD", "currency_symbol": "$", "amount": 1234.5678},
        ),
        ("   $1,234  ", {"currency": "USD", "currency_symbol": "$", "amount": 1234.0}),
        ("   $ 1,234  ", {"currency": "USD", "currency_symbol": "$", "amount": 1234.0}),
        ("1.234 €", {"currency": "EUR", "currency_symbol": "€", "amount": 1234.0}),
        ("1.234€", {"currency": "EUR", "currency_symbol": "€", "amount": 1234.0}),
        ("€1.234", {"currency": "EUR", "currency_symbol": "€", "amount": 1234.0}),
        ("1,234$", {"currency": "USD", "currency_symbol": "$", "amount": 1234.0}),
        ("1,234 $", {"currency": "USD", "currency_symbol": "$", "amount": 1234.0}),
        ("1,234 USD", {"currency": "USD", "currency_symbol": "$", "amount": 1234.0}),
        ("1.234 EUR", {"currency": "EUR", "currency_symbol": "€", "amount": 1234.0}),
        ("1000.00 JPY", {"currency": "JPY", "currency_symbol": "¥", "amount": 1000.00}),
        ("1000 INR", {"currency": "INR", "currency_symbol": "₹", "amount": 1000.00}),
        ("1.234,45", {"currency": None, "currency_symbol": None, "amount": 1234.45}),
        (
            "1.234.456,00",
            {"currency": None, "currency_symbol": None, "amount": 1234456.00},
        ),
        (
            "1.000.000",
            {"currency": None, "currency_symbol": None, "amount": 1000000.00},
        ),
        (
            "Starting At 12.99",
            {"currency": None, "currency_symbol": None, "amount": 12.99},
        ),
        ("From 399.99", {"currency": None, "currency_symbol": None, "amount": 399.99}),
        ("0.0004 $", {"currency": "USD", "currency_symbol": "$", "amount": 0.0004}),
        ("د.إ 1000", {"currency": "AED", "currency_symbol": "د.إ", "amount": 1000.0}),
        ("₦500", {"currency": "NGN", "currency_symbol": "₦", "amount": 500.0}),
        (
            "Kč 1,234.56",
            {"currency": "CZK", "currency_symbol": "Kč", "amount": 1234.56},
        ),
        ("₪123.45", {"currency": "ILS", "currency_symbol": "₪", "amount": 123.45}),
        ("₫1000000", {"currency": "VND", "currency_symbol": "₫", "amount": 1000000.0}),
        ("S/.500", {"currency": "PEN", "currency_symbol": "S/.", "amount": 500.0}),
        ("₽123456", {"currency": "RUB", "currency_symbol": "₽", "amount": 123456.0}),
        ("kr1.234,50", {"currency": "NOK", "currency_symbol": "kr", "amount": 1234.5}),
        (
            "100.000 KZT",
            {"currency": "KZT", "currency_symbol": "T", "amount": 100000.0},
        ),
        ("L1,000.00", {"currency": "RON", "currency_symbol": "L", "amount": 1000.0}),
        ("৳123.45", {"currency": "BDT", "currency_symbol": "৳", "amount": 123.45}),
        (
            "zł12,345.67",
            {"currency": "PLN", "currency_symbol": "zł", "amount": 12345.67},
        ),
        ("₮1234", {"currency": "MNT", "currency_symbol": "₮", "amount": 1234.0}),
        ("10000 Ft", {"currency": "HUF", "currency_symbol": "Ft", "amount": 10000.0}),
        ("B/. 123.45", {"currency": "PAB", "currency_symbol": "B/.", "amount": 123.45}),
        (
            "Price Not Available",
            None,
        ),
        (
            "Unavailable Price",
            None,
        ),
        (
            "Price Upon Request",
            None,
        ),
        (
            "Contact for Price",
            None,
        ),
        (
            "Request a Quote",
            None,
        ),
        ("TDB", None),
        ("N/A", None),
        (
            "Price Not Disclosed",
            None,
        ),
        ("Out of Stock", None),
        ("Sold Out", None),
        (
            "Pricing Not Provided",
            None,
        ),
        ("Not Priced", None),
        (
            "Currently Unavailable",
            None,
        ),
        (
            "Ask for Pricing",
            None,
        ),
        (None, None),
    ],
)
def test_currency_success(input_value, expected_output):
    model = _TestModel(value=input_value)
    assert model.value == expected_output


# Failure cases: these should raise a ValidationError
@pytest.mark.parametrize(
    "input_value",
    [
        "abc",
        "one hundred",
        "1.00.00",
        "1.2.3",
        "Begin 12.00 End 23.00",
        "Between 12.00 And 23.00",
        "From 12.00 To 23.00",
        "12.00 - 23.00",
        "Not a number",
        "1.234.56",
        "1,234,56",
        "$",
        "1,234.56.78",
        "123,456,12",
        "$$",
        "1,2,3",
        "abc$",
        "Twelve Dollars",
        "1 000,00",
        "NaN",
        "INF",
        "-INF",
        "OnlySymbol$",
        "",
        {},
        [],
    ],
)
def test_currency_failure(input_value):
    with pytest.raises(ValidationError):
        _TestModel(value=input_value)
