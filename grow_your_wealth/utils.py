from babel.numbers import format_decimal
def currencify(x):
    return format_decimal(x, locale="en_US")

