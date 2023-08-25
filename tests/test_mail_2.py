import pytest


@pytest.fixture()
def set_up():
    print("Вход в систему выполнен")


def test_sending_mail_1():
    print("Письмо 1 отправлено")


def test_sending_mail_2():
    print("Письмо 2 отправлено")
