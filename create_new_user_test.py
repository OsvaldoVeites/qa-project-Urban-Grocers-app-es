import sender_stand_request
import data

response = sender_stand_request.post_new_user(data.user_body)

def get_user_body(first_name,phone_number,user_address):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    current_body["phone"] = phone_number
    current_body["address"] = user_address
    return current_body

def positive_assert(first_name,  phone_number,  user_address):
    user_body=get_user_body(first_name,phone_number,user_address)
    user_response=sender_stand_request.post_new_user(user_body)
    print (user_response)
    print (user_response.json())
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user =(user_body["firstName"] + ',' + user_body["phone"] + ',' + user_body["address"]
                + ",,," + user_response.json()["authToken"])
    assert users_table_response.text.count (str_user) == 1


def test_create_new_user_get_success_response():
    positive_assert (first_name="Osvaldo",
                phone_number='+55568994701',
                user_address= "Martires Irlandeses 45")

