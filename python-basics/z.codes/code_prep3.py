from datetime import datetime, timedelta

a = datetime.strptime(input(), "%Y-%m-%d")
n = int(input())
new_date = a + timedelta(days=n)
print(new_date.strftime("%Y-%m-%d"))