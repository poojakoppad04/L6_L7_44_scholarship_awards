
import pytest

from scholarship_awards import (
    award_amount,
    is_eligible,
    application_status,
)


@pytest.mark.parametrize(
    "category, marks, income, renewal, expected",
    [
        ("merit", 80, "low", False, 500),
        ("merit", 100, "low", True, 4800),
        ("sports", 80, "high", False, 2000),
        ("sports", 80, "low", True, 3200),
        ("arts", 65, "low", False, 0),
        ("arts", 66, "high", False, 60),
        ("merit", 70, "low", False, 0),
        ("merit", 90, "high", False, 900),
        ("merit", 90, "low", False, 1500),
    ],
)
def test_award_amount_branches(category, marks, income, renewal, expected):
    assert award_amount(category, marks, income, renewal) == expected


@pytest.mark.parametrize(
    "category, marks, income, renewal, message",
    [
        ("science", 90, "low", False, "unknown category"),
        ("merit", -1, "low", False, "invalid marks"),
    ],
)
def test_award_amount_errors(category, marks, income, renewal, message):
    with pytest.raises(ValueError, match=message):
        award_amount(category, marks, income, renewal)


@pytest.mark.parametrize(
    "attendance, backlogs, special, expected",
    [
        (60, 2, True, True),
        (60, 3, True, False),
        (74, 0, False, False),
        (75, 0, False, True),
        (90, 1, False, True),
        (90, 2, False, False),
    ],
)
def test_eligibility_branches(attendance, backlogs, special, expected):
    assert is_eligible(attendance, backlogs, special) is expected


@pytest.mark.parametrize(
    "days_left, renewal, paper, expected",
    [
        (40, True, True, "open"),
        (30, False, False, "open"),
        (25, False, True, "closing"),
        (15, False, True, "closing"),
        (14, False, True, "closed"),
        (10, True, False, "closed"),
    ],
)
def test_application_status_branches(days_left, renewal, paper, expected):
    assert application_status(days_left, renewal, paper) == expected
