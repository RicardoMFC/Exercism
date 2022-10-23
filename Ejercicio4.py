budget=127.5
exchange_rate=1.2
def exchange_money(budget, exchange_rate):
    return budget/exchange_rate
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    pass

exchanging_value=120
def get_change(budget, exchanging_value):
    return budget-exchanging_value
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    pass

denomination=5
number_of_bills=128

def get_value_of_bills(denomination, number_of_bills):
    return denomination*number_of_bills
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    pass


def get_number_of_bills(budget, denomination):
    return int (budget/denomination)
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    pass

denomination=20
def get_leftover_of_bills(budget, denomination):
    return budget - int(budget/denomination)*denomination
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    pass

spread=10
def exchangeable_value(budget, exchange_rate, spread, denomination):
    return int(budget/((exchange_rate*(1+spread/100))*denomination))*denomination
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    pass