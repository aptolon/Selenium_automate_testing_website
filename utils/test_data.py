reg_valid_user = {
    "email": "234256234@example.com",
    "mobile_phone": "+1234432893",
    "password": "valid1sword423",
    "dob": "20-01-2000",
    "gender": "male"
}

reg_invalid_user = {
    "email": "1alid@email.com",
    "mobile_phone": "+1231532893", # Пользователь с таким номером телефона уже зарегистрирован
    "password": "valid1sword123",
    "dob": "20-01-2000",
    "gender": "male"
}

log_valid_user = {
    "email": "fordallyy222@gmail.com",
    "password": "tuWVLhYWhW"
}

log_invalid_user = {
    "email": "tttjfjjjfj@example.com",
    "password": "valid1sword123"
}
cart_invalid_promo = {
    "code": "2222"
}


search_valid_query = {
    "query": "сумка unblock L"
}

search_invalid_query = {
    "query": "некорректный запрос"
}

search_partial_query = {
    "part_query": "PAK",
    "query": "PAKKU"
}
