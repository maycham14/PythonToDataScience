def display_message():
    print("I am learning something new")


display_message()


def favorite_book(title):
    print(f"my favorite book is {title.title()}")


favorite_book("amadu")


def make_shirt(text, size="large"):
    print(f"size of the shirt is {size} and message printed is  {text}")


make_shirt(text="i love python")


def describe_city(country, city="paris"):
    print(f"{city} is in {country} ")


describe_city("france")
describe_city("gambia", "banjul")
describe_city("senegal", "dakar")


def city_country(city, country):
    print(f"{city} is in {country}")


city_country("santiago", "chile")
city_country("santiago", "chile")
city_country("santiago", "gambia")


def make_album():
    album = {}

    while True:
        artist_name = input("artist_name: ")
        album_title = input("artist_title: ")
        if artist_name.lower() == "q" or album_title.lower() == "q":
            break
        else:
            album["artist_name"] = artist_name
            album["album_title"] = album_title
            print(f"artist is {artist_name} and album is {album_title}")
            continue


make_album()


def sand_witches(*available):
    print(f"the available sand_witches are {available}")
    return available


sand_witches("chicken", "beef", "sardine")


def my_profile(first, last, **user_info):
    user_info["first"] = first
    user_info["last"] = last
    return user_info


user_profile = my_profile("may", "cham", age=30)
print(user_profile)


def make_car(name, type, color, tow_pakage=True, **info):
    info["name"] = name
    info["type"] = type
    info["color"] = color

    if tow_pakage:
        info["tow_pakage"] = tow_pakage
        return info


car = make_car("subaru", "outback", color="blue", tow_pakage=True)
print(car)
