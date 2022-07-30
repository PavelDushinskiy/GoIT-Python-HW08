from datetime import datetime, timedelta

users = [
    {"name": "Bill", "birthday": "2022-08-01"},
    {"name": "Bob", "birthday": "2022-07-31"},
    {"name": "Julia", "birthday": "2022-08-03"},
    {"name": "Jan", "birthday": "2022-07-27"},
    {"name": "Nick", "birthday": "2022-07-28"},
    {"name": "Peter", "birthday": "2022-07-29"},
    {"name": "Richard", "birthday": "2022-07-30"},
    {"name": "Tom", "birthday": "2022-07-31"},
    {"name": "Yan", "birthday": "2022-07-29"}
]

birthdays_weekday = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
}


def print_list_users():
    for day, names in birthdays_weekday.items():
        if names:
            print(day, ": ", end="")
            print(*names, sep=", ")


def get_birthdays_per_week(list_users: list, date_for_congratulations: datetime) -> object:
    start_date = datetime.strptime(str(date_for_congratulations), "%Y-%m-%d")
    end_date = start_date + timedelta(days=6)
    if datetime.weekday(start_date) == 0:
        start_date = start_date - timedelta(days=2)
        end_date = end_date - timedelta(days=2)
    for user in list_users:
        user_name = user.get("name")
        datetime_birthday = datetime.strptime(user.get("birthday"), "%Y-%m-%d")
        if start_date <= datetime_birthday <= end_date:
            key_birthdays_weekday = datetime.strftime(
                datetime_birthday, "%A")
            if str(key_birthdays_weekday) in ["Saturday", "Sunday"]:
                key_birthdays_weekday = "Monday"
            birthdays_weekday.get(key_birthdays_weekday).append(user_name)
    if {i: j for i, j in birthdays_weekday.items() if j != []} == {}:
        print("Unfortunately, there are no users' birthdays this week")
        return
    print_list_users()


if __name__ == "__main__":
    get_birthdays_per_week(
        users, date_for_congratulations=datetime.now().date())
