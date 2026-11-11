import math
from hypothesis import given, strategies as st

from processor import parse_applicant, marks_average, payable_award


@given(st.one_of(st.text(), st.none()))
def test_parse_applicant_no_crash(s):
    result = parse_applicant(s)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and isinstance(result[0], str)
        and isinstance(result[1], float)
    )


@given(st.one_of(st.text(), st.none()))
def test_marks_average_no_crash(s):
    result = marks_average(s)
    assert result is None or isinstance(result, int)


@given(st.one_of(st.text(), st.none()))
def test_payable_award_no_crash(s):
    result = payable_award(s)
    assert result is None or (
        isinstance(result, (int, float))
        and math.isfinite(result)
        and result >= 0
    )
