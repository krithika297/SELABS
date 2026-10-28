
import pytest

from daycare_fees import (
    extra_hours_fee,
    enrolment_allowed,
    pickup_status,
)


def test_unknown_age_group():
    with pytest.raises(ValueError, match="unknown age group"):
        extra_hours_fee("school", 30, False)


def test_negative_hours():
    with pytest.raises(ValueError, match="invalid hours"):
        extra_hours_fee("toddler", -1, False)


def test_hours_within_included_limit():
    assert extra_hours_fee("toddler", 20, False) == 0


def test_extra_hours_without_sibling():
    assert extra_hours_fee("toddler", 26, False) == 9


def test_sibling_allowance_for_toddler():
    assert extra_hours_fee("toddler", 31, True) == 9


def test_sibling_allowance_not_applied_to_infant():
    assert extra_hours_fee("infant", 21, True) == 14


def test_infant_high_extra_hours_fee():
    assert extra_hours_fee("infant", 41, False) == 462


def test_toddler_high_extra_hours_fee():
    assert extra_hours_fee("toddler", 51, True) == 294


def test_enrolment_allowed_with_pending_immunisation():
    assert enrolment_allowed(12, 0, True) is True


def test_enrolment_denied_with_pending_immunisation():
    assert enrolment_allowed(11, 5, True) is False


def test_enrolment_denied_for_age_below_six_months():
    assert enrolment_allowed(5, 2, False) is False


def test_enrolment_denied_when_no_vacancies():
    assert enrolment_allowed(12, 0, False) is False


def test_enrolment_allowed_when_vacancy_exists():
    assert enrolment_allowed(12, 1, False) is True


def test_pickup_on_time_with_aftercare_and_friday():
    assert pickup_status(30, True, True) == "on_time"


def test_pickup_on_time_without_aftercare_or_friday():
    assert pickup_status(10, False, False) == "on_time"


def test_pickup_late_without_aftercare_or_friday():
    assert pickup_status(7, False, False) == "late"


def test_pickup_overdue_without_aftercare_or_friday():
    assert pickup_status(-6, False, False) == "overdue"


def test_pickup_late_with_aftercare_not_friday():
    assert pickup_status(10, True, False) == "late"


def test_pickup_overdue_on_friday():
    assert pickup_status(4, False, True) == "overdue"
