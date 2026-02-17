def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def find_max(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def user_info(username, **details):
    print("Username:", username)
    for key, value in details.items():
        print(key, ":", value)


def show_data(title, *args, **kwargs):
    print("Title:", title)
    print("Args:", args)
    print("Kwargs:", kwargs)


print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))

print(find_max(3, 7, 2, 9, 1))

user_info("emil123", age=25, city="Oslo", hobby="coding")

show_data("User Info", "Emil", "Tobias", age=30, country="Norway")