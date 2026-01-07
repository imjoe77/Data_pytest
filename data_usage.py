import sys

def process_data_usage(argv=None):
    if argv is None:
        argv = sys.argv

    # Command-line arguments check
    if len(argv) == 6:
        script_name = argv[0]
        user_name = argv[1]
        plan_type = argv[2]
        d1 = float(argv[3])
        d2 = float(argv[4])
        d3 = float(argv[5])
    else:
        script_name = argv[0]
        user_name = "Joel"
        plan_type = "Unlimited"
        d1 = 120
        d2 = 98
        d3 = 110

    total = d1 + d2 + d3
    average = total / 3

    # Usage classification
    if average >= 100:
        category = "Heavy User"
    elif average >= 70:
        category = "Moderate User"
    elif average >= 40:
        category = "Light User"
    else:
        category = "Very Light User"

    return {
        "script_name": script_name,
        "user_name": user_name,
        "plan_type": plan_type,
        "usage": (d1, d2, d3),
        "total": total,
        "average": average,
        "category": category
    }


if __name__ == "__main__":
    result = process_data_usage()

    print("Script Name:", result["script_name"])
    print("User Name:", result["user_name"])
    print("Plan Type:", result["plan_type"])
    print("Data Usage (GB):", *result["usage"])
    print("Total Usage:", result["total"])
    print("Average Usage:", result["average"])
    print("Usage Category:", result["category"])
