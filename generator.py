import pytest
users = ["test1@magento.com", "test2@magento.com", "test3@magento.com"]
password = ["pass123", "pass345", "pass678"]


def generate_pairs():
    pairs = []
    for user in users:
        for passw in password:
            pairs.append(pytest.param((user, passw), id=f"{user}, {passw}"))
    return pairs

# @pytest.mark.parametrize(
#     "creds",
#     [
#         pytest.param(("test1@magento.com", "pass123"),
#                      id="test1@magento.com, pass123"),
#         pytest.param(("test2@magento.com", "pass345"),
#                      id="test2@magento.com, pass345"),
#         pytest.param(("test3@magento.com", "pass678"),
#                      id="test3@magento.com, pass678"),
#     ]
# )
