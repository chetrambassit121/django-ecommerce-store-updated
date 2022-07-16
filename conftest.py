import pytest
from pytest_factoryboy import register

from tests.factories import CategoryFactory, ProductTypeFactory

register(CategoryFactory)
register(ProductTypeFactory)


@pytest.fixture
def product_category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture
def product_type(db, product_type_factory):
    product_type = product_type_factory.create()
    return product_type


# import pytest


# @pytest.fixture(scope="session")
# def test_fixture1():
#     print("Run once")
#     return 1


# @pytest.fixture(scope="session")
# def test_fixture1():
#     print("Run once")
#     return 1


# @pytest.fixture(scope="session")
# def test_fixture1():
#     print("Run once")
#     return 1
