import re
calendar = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month = ""
date = ""
year = ""
# index = 0

while len(date) != 2 and len(year) != 4:
    try:
        month, date, year = re.split(r"[,/]", input("Date: ").strip())
        # print("MM/DD/YYY")
        month = month.title()

    except ValueError:
        # print("Invalid Entry")
        continue


for months in calendar:
        if month == months:
            month = calendar.index(month)+1
        else:
             month = month
# print(index)
print(f"{year}-{month:02}-{date}",end="")
