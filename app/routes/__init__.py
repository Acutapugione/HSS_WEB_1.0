AUTH_CONTEXT = {
    "auth_endpoints": [
        ("logout", "Вийти",), 
    ],
"profile_endpoints": [
    ("profile", "Профіль",), 
    ],
"appeals_endpoints": [
    ("appeals", "Перелік звернень"),
    ("create_appeal", "Створити звернення"),
]
}

ANONYMOUS_CONTEXT = {
    "auth_endpoints": [
        ("sign_up", "Зареєструватись",), 
        ("sign_in", "Авторизуватись",), 
    ]
}


from . auth import sign_in, sign_up
from . landing import landing
from . appeal import appeals, create_appeal, appeal
from . error import page_not_found
from . home import home
from . profile import profile