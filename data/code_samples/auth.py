def login(token):
    if token is None:
        raise Exception("Token missing")
    return "Login successful"