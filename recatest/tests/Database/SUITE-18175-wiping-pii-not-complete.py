from helpers.testHelpers import *
# person_code_v = '1617'
person_code_v = '1617'
_username = '7076333'
_SAFE = 'SAFE'

oracle[0].value_exists('safe_user', person_code=person_code_v)
oracle[0].value_exists('ca_booked_person', person_code=person_code_v)
oracle[0].value_exists('ca_kiosk_pin', person_code=person_code_v)
oracle[0].value_exists('suite_log', person_code=person_code_v)
oracle[0].value_exists('ca_person_access_level', person_code=person_code_v)
oracle[0].value_exists('ca_person_access_override', person_code=person_code_v)
oracle[0].value_exists('ca_person_induction', person_code=person_code_v)
oracle[0].value_exists('ca_person_sponsor', person_code=person_code_v)
oracle[0].value_exists('ca_person_access_profile', person_code=person_code_v)
oracle[0].value_exists('ca_person_comments', person_code=person_code_v)
oracle[0].value_exists('ca_driving_license', person_code=person_code_v)
oracle[0].value_exists('safe_watched_person', person_code=person_code_v)
oracle[0].value_exists('ca_person_sec_clea_ba', person_code=person_code_v)
oracle[0].value_exists('ca_person_evetting', person_code=person_code_v)
oracle[0].value_exists('CA_BADGE', person_code=person_code_v)
oracle[0].value_exists('CA_LOG', person_code=person_code_v)
oracle[0].value_exists('ca_person_special_driving', person_code=person_code_v)
oracle[0].value_exists('ca_person_badge_charge', person_code=person_code_v)

# NUMBER
oracle[0].value_not_exists('ca_person_detail', last_changed_username = _username)
oracle[0].value_not_exists('safe_user', username = _username)
oracle[0].value_not_exists('ca_booked_person', booker_username = _username)
oracle[0].value_not_exists('ca_kiosk_pin', username = _username)
oracle[0].value_not_exists('suite_log', log_username = _username)
oracle[0].value_not_exists('ca_person_access_level', username = _username)
oracle[0].value_not_exists('ca_person_access_override', username = _username)
oracle[0].value_not_exists('ca_person_induction', username = _username)
oracle[0].value_not_exists('ca_person_sponsor', last_changed_username = _username)
oracle[0].value_not_exists('ca_person_sponsor', assigned_by = _username)
oracle[0].value_not_exists('ca_person_access_profile', username = _username)
oracle[0].value_not_exists('ca_person_comments', username = _username)
oracle[0].value_not_exists('ca_driving_license', username = _username)
oracle[0].value_not_exists('safe_watched_person', email_address = _username)
oracle[0].value_not_exists('ca_person_sec_clea_ba', last_changed_username = _username)
oracle[0].value_not_exists('ca_person_evetting', last_changed_username = _username)
oracle[0].value_not_exists('ca_log', log_username = _username)
oracle[0].value_not_exists('ca_person_special_driving', username = _username)
oracle[0].value_not_exists('ca_person_badge_charge', last_changed_username = _username)

# SAFE
oracle[0].value_not_exists('ca_person_detail', last_changed_username = _SAFE)
oracle[0].value_not_exists('safe_user', username = _SAFE)
oracle[0].value_not_exists('ca_booked_person', booker_username = _SAFE)
oracle[0].value_not_exists('ca_kiosk_pin', username = _SAFE)
oracle[0].value_not_exists('suite_log', log_username = _SAFE)
oracle[0].value_not_exists('ca_person_access_level', username = _SAFE)
oracle[0].value_not_exists('ca_person_access_override', username = _SAFE)
oracle[0].value_not_exists('ca_person_induction', username = _SAFE)
oracle[0].value_not_exists('ca_person_sponsor', last_changed_username = _SAFE)
oracle[0].value_not_exists('ca_person_sponsor', assigned_by = _SAFE)
oracle[0].value_not_exists('ca_person_access_profile', username = _SAFE)
oracle[0].value_not_exists('ca_person_comments', username = _SAFE)
oracle[0].value_not_exists('ca_driving_license', username = _SAFE)
oracle[0].value_not_exists('safe_watched_person', email_address = _SAFE)
oracle[0].value_not_exists('ca_person_sec_clea_ba', last_changed_username = _SAFE)
oracle[0].value_not_exists('ca_person_evetting', last_changed_username = _SAFE)
oracle[0].value_not_exists('ca_log', log_username = _SAFE)
oracle[0].value_not_exists('ca_person_special_driving', username = _SAFE)
oracle[0].value_not_exists('ca_person_badge_charge', last_changed_username = _SAFE)
