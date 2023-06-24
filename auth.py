"""User authentication for using the library."""


class AuthError(Exception):
    pass


__ALLOWED_USERS_MAP = {
    "admin": "737f2c06-4765-46f1-9a32-7adac6b6fbd1",
    "home_boy": "b3c5a609-31d7-4157-84ee-dec4a67446bd",
    "inspector": "aad9a972-2758-436b-b72b-2e14bd65c566",
}


def _check_token(token: str):
    if token not in set(__ALLOWED_USERS_MAP.values()):
        raise AuthError("Invalid token!")


def get_auth_token(user: str) -> str:
    token = __ALLOWED_USERS_MAP.get(user)
    if token is None:
        raise AuthError(f"User {user} is not authorized to access this API")
    else:
        return token
