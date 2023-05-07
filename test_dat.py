from dat import save_data, load_data
import logging

test_data_key = "test_data"


def test_save_data():
    data = "test stuff"
    ret = save_data(test_data_key, data)
    assert ret == "data saved"


def test_load_data():
    data = load_data(test_data_key)
    print(data)
    logging.warning(data)
    assert len(data) > 0


def test_load_non_existent():
    exception_happened = False
    try:
        data = load_data("stuff")
    except:
        exception_happened = True
    assert exception_happened
