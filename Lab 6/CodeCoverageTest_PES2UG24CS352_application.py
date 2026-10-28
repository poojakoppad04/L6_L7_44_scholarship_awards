
import pytest

from scholarship_awards import (
    award_amount,
    is_eligible,
    application_status,
)


def test_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        award_amount("science", 90, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError, match="invalid marks"):
        award_amount("merit", -1, "low", False)


def test_renewal_merit_low_income_high_marks():
    assert award_amount("merit", 100, "low", True) == 4800


def test_sports_high_income_high_marks():
    assert award_amount("sports", 80, "high", False) == 2000


def test_marks_just_above_cutoff():
    assert award_amount("merit", 80, "low", False) == 500


def test_below_cutoff():
    assert award_amount("merit", 70, "low", False) == 0


def test_special_quota_eligible():
    assert is_eligible(60, 2, True) is True


def test_regular_applicant_eligible():
    assert is_eligible(90, 1, False) is True


def test_low_attendance_ineligible():
    assert is_eligible(70, 0, False) is False


def test_application_open():
    assert application_status(40, True, True) == "open"


def test_application_closing():
    assert application_status(25, False, True) == "closing"


def test_application_closed():
    assert application_status(10, True, False) == "closed"
