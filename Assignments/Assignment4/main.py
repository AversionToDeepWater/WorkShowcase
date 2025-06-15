import requests
import json

def get_all_kdramas_frontend():
    endpoint= "http://127.0.0.1:5000/kdramas"
    result = requests.get(endpoint).json()
    return result

def add_new_kdramas_front_end(new_kdrama_dict):
    endpoint = "http://127.0.0.1:5000/kdramas/add"
    result = requests.post(
        endpoint,
        headers={'content-type': 'application/json'},
        data=json.dumps(new_kdrama_dict)
    )#.json()
    return result

def add_new_ratings_front_end(new_rating_dict):
    endpoint = "http://127.0.0.1:5000/kdramas/addratings"
    result = requests.post(
        endpoint,
        headers={'content-type': 'application/json'},
        data=json.dumps(new_rating_dict)
    )
    return result#.json()

def delete_kdrama_by_id(id):
    endpoint = f"http://127.0.0.1:5000/kdramas/remove/{id}"
    result = requests.delete(endpoint).json()
    return result


def new_kdrama_input():
    title = input("Please enter the Kdrama title: ").strip()
    main_male_lead = input("Please enter the name of the main male lead: ").strip()
    main_female_lead = input("Please enter the name of the main female lead: ").strip()
    watched = input("Have you watched this yet? (Y/N): ").upper().strip()

    #checking user input
    while title is None:
        title = input("Please input a title: ")
    while main_male_lead is None:
        main_male_lead = input("Please enter the name of the main male lead: ")
    while main_female_lead is None:
        main_female_lead = input("Please enter the name of the main female lead: ")
    # while watched != 'Y' or watched != 'N':
    #     watched = input("Please enter in the format of Y/N: ")

    new_kdrama_dict = {
        "title": title,
        "main_male_lead": main_male_lead,
        "main_female_lead": main_female_lead,
        "watched" : watched
    }
    return new_kdrama_dict

def new_rating_input():
    kdrama_id = int(input("ID numerical of the Kdrama you would like to rate: "))
    rating = float(input("Please enter your rating out of 10: "))

    while rating > 10:
        rating = float(input("Please enter a rating out of 10: "))

    new_rating_dict = {
        "kdrama_id": kdrama_id,
        "rating": rating
    }

    return new_rating_dict

def run():
    print("\n Hello! Welcome to the Kdrama watchlist and rating tracker")
    print("~~~~~~~~~~~~~~~")
    print("Please select an option :D")
    print(" A: View your current Kdrama watchlist \n B: Add a Kdrama to your watchlist \n C: Add a rating \n D: Delete Kdrama from your watchlist ")

    ans = input("Please enter a letter: ").upper().strip()

    if ans == 'A':
        if get_all_kdramas_frontend() is None:
            print("Working on it...")
        print(get_all_kdramas_frontend())
    elif ans == 'B':
        new_kdrama_dict = new_kdrama_input()
        print("Here is the updated list: ")
        print(add_new_kdramas_front_end(new_kdrama_dict))
    elif ans == 'C':
        new_rating_dict = new_rating_input()
        print("Here is the updated ratings: ")
        print(add_new_ratings_front_end(new_rating_dict))
    elif ans == 'D':
        print("Here is your list")
        kdramas_all = get_all_kdramas_frontend()
        if kdramas_all is not None:
            remove_id = input("Please enter an id to remove: ").strip()
            print("The Kdrama has been removed")
            print(delete_kdrama_by_id(remove_id))
    else:
        print("You have not selected a valid option :((")


if __name__ == "__main__":
    run()








