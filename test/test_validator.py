# tests/test_validator.py
def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False

def test_validate_phone():
    assert validate_phone("+79161234567") is True
    assert validate_phone("8-916-123-45-67") is True
    assert validate_phone("123") is False