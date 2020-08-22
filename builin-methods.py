class Currency:

    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd = exchange_to_usd

    def set_amount(self, amount):
        self.amount = amount

    def in_currency(self, amount):
        return amount / self.exchange_to_usd

    def to_usd(self, amount=None):
        to_convert = amount or self.amount
        return to_convert * self.exchange_to_usd

    def __eq__(self, other):
        return self.to_usd() == other.to_usd()

    def __gt__(self, other):
        return self.to_usd() > other.to_usd()

    def __lt__(self, other):
        return self.to_usd() < other.to_usd()

    def __le__(self, other):
        return self.to_usd() <= other.to_usd()

    def __ge__(self, other):
        return self.to_usd() >= other.to_usd()


def _get_currency_resource(resource, transform=(lambda x: x)):
    data = {
        'items': [
            {'code': 'usd', 'amount_to_usd': 1.00},
            {'code': 'usd', 'amount_to_usd': 1.21},
            {'code': 'usd', 'amount_to_usd': 1.07},
            {'code': 'usd', 'amount_to_usd': 0.14},
        ]
    }
    my_resource = data[resource]
    return [transform(x) for x in my_resource]


def get_currency_codes():
    return _get_currency_resource("items", lambda x: x['code'].upper)


def get_currencies():
    return _get_currency_resource("items", lambda x: Currency(x['code'], x['amount_to_usd']))


print(get_currency_codes())
print(get_currencies())