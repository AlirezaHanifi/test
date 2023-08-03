import pytest


@pytest.mark.parametrize(
    "test_input, expected_output", [("2+2", 4), ("2-2", 0), ("2*2", 4), ("2/2", 1.0)]
)
def test_eval(test_input, expected_output) -> None:
    assert eval(test_input) == expected_output
