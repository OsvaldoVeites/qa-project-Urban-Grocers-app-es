import data
import sender_stand_request
from data import user_body


def get_kit_body(kit_name):
    kit_current_body = data.kit_body.copy()
    kit_current_body["name"] = kit_name
    return kit_current_body

def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]

def positive_assert(kit_name):
    auth_token = get_new_user_token()
    kit_body = get_kit_body(kit_name)
    kit_user_response =sender_stand_request.post_new_kit(kit_body,auth_token)
    assert kit_user_response.status_code == 201

def negative_assert(kit_name):
    auth_token = get_new_user_token()
    kit_body = get_kit_body(kit_name)
    kit_user_response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert kit_user_response.status_code == 400
    assert kit_user_response.json()["code"] == 400
    assert kit_user_response.json()["message"] == "El nombre debe contener sólo letras latino,\
                                                    un espacio y un guión. De 2 a 15 caracteres"

def test_crate_kit_name_kit_1_character_get_success_report():
    positive_assert(kit_name = "A")

def test_crate_kit_name_kit_511_characters_get_success_report():
    positive_assert(kit_name = "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                               abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                               abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                               dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                               dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                               abcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdab\
                               cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                               bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                               bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                               bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                               bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_name_kit_without_name_get_failure_report():
    negative_assert(kit_name = "")

def test_crate_kit_name_kit_with_512_characters_get_failure_report():
    negative_assert(kit_name = "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                                abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                                abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                                abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                                abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcd\
                                abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                                abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                                abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                                abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                                abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_name_kit_with_simbols_get_success_report():
    positive_assert(kit_name = "\"№%@\",")

def test_crate_kit_has_space_in_name_kit_get_success_report():
    positive_assert(kit_name = " A Aaa")

def test_crate_kit_has_numbers_in_name_kit_get_success_report ():
    positive_assert(kit_name = "123")

def negative_assert_no_body():
    auth_token = get_new_user_token()
    kit_body = {}
    kit_user_response = sender_stand_request.post_new_kit(kit_body,auth_token)
    assert kit_user_response.status_code == 400
    assert kit_user_response.json()["code"] == 400
    assert kit_user_response.json() ['message'] == 'No se han aprobado todos los parámetros requeridos'

def  test_crate_kit_without_body_in_name_kit_get_failure_report():
    negative_assert_no_body ()

def test_create_kit_number_type_in_kit_name_get_error_report():
    negative_assert(kit_name = 123)

