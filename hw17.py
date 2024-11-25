def check_and_add_10(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            result += 10
        return result
    return wrapper