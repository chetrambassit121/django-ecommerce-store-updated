import pytest


def test_customer_str(customer):
    assert customer.__str__() == "user1"



