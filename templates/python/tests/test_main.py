from src.main import handler


def test_handler_returns_message():
    assert handler()["message"].startswith("Hello")
