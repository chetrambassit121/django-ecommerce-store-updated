import pytest


@pytest.fixture(scope="session")
def test_fixture1():
    print("Run once")
    return 1


@pytest.fixture(scope="session")
def test_fixture1():
    print("Run once")
    return 1


@pytest.fixture(scope="session")
def test_fixture1():
    print("Run once")
    return 1
