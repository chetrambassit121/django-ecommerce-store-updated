import pytest


def test_customer_str(customer):
    assert customer.__str__() == "user1"


def test_admin_user_str(adminuser):
    assert adminuser.__str__() == "admin_user"


def test_customer_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="")
    assert str(e.value) == "Customer Account: You must provide an email address"


def test_customer_email_incorrect(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="a.com")
    assert str(e.value) == "You must provide a valid email address"


def test_adminuser_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="", is_superuser=True, is_staff=True)
    assert str(e.value) == "Superuser Account: You must provide an email address"


def test_adminuser_email_incorrect(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="a.com", is_superuser=True, is_staff=True)
    assert str(e.value) == "You must provide a valid email address"
