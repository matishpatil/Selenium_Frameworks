# coding=utf-8
"""Cucumber Basket feature tests."""

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers,
)
from cucumbers import CucumberBasket
from functools import partial


scenarios('../features/cucumbers.feature')
#@scenario('features\cucumbers.feature', 'Add cucumbers to the basket')
#def test_add_cucumbers_to_the_basket():
#    pass


EXTRA_TYPES = {
    'Number': int,
}


# parse_num = partial(parser.cfparse(, extra_types=EXTRA_TYPES)
@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers'), extra_types=EXTRA_TYPES)
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket'), extra_types=EXTRA_TYPES)
def cucumbers_are_added_to_the_basket(basket, some):
    basket.add(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers'), extra_types=EXTRA_TYPES)
def the_basket_contains_6_cucumbers(basket, total):
    assert basket.count() == total
