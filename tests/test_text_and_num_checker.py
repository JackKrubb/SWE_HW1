from routes import product_routes, stock_routes, vending_machine_routes


def test_text_is_invalid():
    test_text = "hello"
    test_text2 = "1235"

    assert vending_machine_routes.text_is_invalid(test_text2) is True
    assert vending_machine_routes.text_is_invalid(test_text) is False
    assert product_routes.text_is_invalid(test_text2) is True
    assert product_routes.text_is_invalid(test_text) is False


def test_num_is_invalid():
    test_num = "123"
    test_num2 = "12.50"
    test_num3 = "-10"
    test_num4 = "chips"

    assert product_routes.num_is_invalid(test_num2) is True
    assert product_routes.num_is_invalid(test_num) is False
    assert product_routes.num_is_invalid(test_num3) is True
    assert product_routes.num_is_invalid(test_num4) is True
    assert stock_routes.num_is_invalid(test_num2) is True
    assert stock_routes.num_is_invalid(test_num) is False
    assert stock_routes.num_is_invalid(test_num3) is True
    assert stock_routes.num_is_invalid(test_num4) is True
