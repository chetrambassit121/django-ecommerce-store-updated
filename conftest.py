import pytest
from pytest_factoryboy import register

from tests.factories import CategoryFactory

register(CategoryFactory)


@pytest.fixture
def product_category(db, category_factory):
    category = category_factory.create()
    return category


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
