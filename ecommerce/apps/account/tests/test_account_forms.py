import pytest
from ecommerce.apps.account.forms import RegistrationForm, UserAddressForm


@pytest.mark.parametrize(
    "full_name, phone, address_line, address_line2, town_city, postcode, validity",
    [
        ("mike", "02343343434", "add1", "add2", "town", "postcode", True),
        ("", "02343343434", "add1", "add2", "town", "postcode", False),
    ],
)
def test_customer_add(full_name, phone, address_line, address_line2, town_city, postcode, validity):
    form = UserAddressForm(
        data={
            "full_name": full_name,
            "phone": phone,
            "address_line": address_line,
            "address_line2": address_line2,
            "town_city": town_city,
            "postcode": postcode,
        }
    )
    assert form.is_valid() is validity


def test_customer_create_address(client, customer):
    user = customer
    client.force_login(user)
    response = client.post(
        "/account/add_address/",
        data={
            "full_name": "test",
            "phone": "test",
            "address_line": "test",
            "address_line2": "test",
            "town_city": "test",
            "postcode": "test",
        },
    )
    assert response.status_code == 302
