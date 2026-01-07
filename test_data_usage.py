from data_usage import process_data_usage


def test_default_values():
    result = process_data_usage(["data_usage.py"])

    assert result["user_name"] == "Joel"
    assert result["plan_type"] == "Unlimited"
    assert result["total"] == 328
    assert result["average"] == (328 / 3)
    assert result["category"] == "Heavy User"


def test_command_line_arguments():
    args = [
        "data_usage.py",
        "Rahul",
        "Prepaid",
        "60",
        "70",
        "80"
    ]

    result = process_data_usage(args)

    assert result["user_name"] == "Rahul"
    assert result["plan_type"] == "Prepaid"
    assert result["total"] == 210
    assert result["average"] == 70
    assert result["category"] == "Moderate User"


def test_light_user_category():
    args = [
        "data_usage.py",
        "Anita",
        "Postpaid",
        "45",
        "50",
        "55"
    ]

    result = process_data_usage(args)

    assert result["category"] == "Light User"


def test_very_light_user_category():
    args = [
        "data_usage.py",
        "Ravi",
        "Basic",
        "20",
        "30",
        "25"
    ]

    result = process_data_usage(args)

    assert result["category"] == "Very Light User"
