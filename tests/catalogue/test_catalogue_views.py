import pytest


@pytest.mark.core
def test_hello_world3(test_fixture1):
    print("function_fixture3")
    assert test_fixture1 == 1


# # use this decorator if you know test will fail
# @pytest.mark.xfail
# def test_hello_world3(test_fixture1):
#     print("function_fixture3")
#     assert test_fixture1 == 1

# # use this decorator if you want to skip text
# @pytest.mark.skip
# def test_hello_world3(test_fixture1):
#     print("function_fixture3")
#     assert test_fixture1 == 1
