'''
CALLING YOUR API
First you need to import requests library, otherwise you can't call your API.
All imports and requests should be at the top of your code
Adding datetime
'''
from datetime import datetime

import requests
#You then need to specify your endpoint, i.e., the https for your API
#Note, you can first call your API on Insomnia and analyse the data structure there
endpoint = "https://api.artic.edu/api/v1/artworks?fields=id,title,artist_display,date_display,main_reference_number,description,alt_text,short_description"

'''
ENDPOINTS
Figuring out what endpoint I want to use based on the info I need
I looked at both in Insomnia 
https://api.artic.edu/api/v1/artworks?fields=id,title,artist_display,date_display,main_reference_number,description,alt_text,short_description
https://api.artic.edu/api/v1/artworks
'''
#Call requests library, to use a special get method to get data from endpoint. Save to response
response = requests.get(endpoint).json()
'''
For the actual data, which will come from the internet as a JSON file
For Python to understand this, you need to use inbuilt JSON function to import JSON package in Python script

The code below is more of me figuring out if I am retrieving the data I need using print 
data = response.json()
print(response)
'''

'''
TESTING!! 

Figuring out what data from JSON data I want and testing to see if I can retrieve that

total_artworks = response['pagination']['total'] #total no of artworks
title = response['data'][0]['title'] #title of the first artwork - data is a list, [0] for first item in list, 'title' is key
description = response['data'][0]['description'] #description of first artwork, too long
short_description = response['data'][0]['short_description'] #short description of first artwork which I prefer to use
artist_display = response['data'][0]['artist_display'] #Artist name, and info
# print(artist_display)

'''
#FUNCTIONS!!
#get short description of artwork based number user gives
#Not sure if this is a necessary function -- some artworks don't have a short description
#I will instead add it to my get_artist_info function
# def get_description(response:str, i:int):
#     short_description = response['data'][i]['short_description']
#     return short_description


#returns list of titles and artist display info from API
def get_artist_info(response:str):
    art_list = []
    for item in response['data']:
        artworks = {
            'title':item['title'],
            'artist_display': item['artist_display'],
            'short_description': item['short_description']
        }
        art_list.append(artworks)
    return art_list

# print(get_artist_info(response))

def get_total_art(reponse): #No of artworks
    return response['pagination']['total']
'''
MORE TESTING AND THINKING

print(get_total_art(response))
This showed me there were 126079 pieces of artwork I could work with!
That is a lot so I will limit it to 30? 
Can use a for loop to limit it's range??

#for x in range(0,get_total_art(response)-126048):#prints artworks 1-30 (or 0-29 in Python speak)
    #Think there should be an easier way to do this but I'm not sure how
    #print(x)
'''

'''GETTING USER INPUT'''

file = open("outputs.txt","a")

print("You're going to an art gallery! But what should you go and see? \n Enter a number from 1-10")

user_input = input("There will be a bonus if you guess my lucky number. \n Either way, I'll tell you what will be worth your time: ")

# if int(user_input) == False or int(user_input) > 10:
#     print("That's not right try again!")

while user_input.isdigit() == False or int(user_input) > 10:
    print("That's not right try again!")
    user_input = input("Enter a number from 1-30 and I'll tell you what will be worth your time:  ")
    if user_input.isdigit() == True and int(user_input) < 10:
        break


int_input = int(user_input)
bonus = 'Henri Matisse'
bonus_test = bonus[2:9]

if int_input == 7:
    test = input(f"Wow you guessed my lucky number! \n Here is a bonus question. Can you guess who this famous artist is? {bonus_test}")
    if test.lower() ==  "henri matisse":
        print("Wow you're so smart! \n")
    else:
        print("Not quite! Better luck next time \n")


#when I try to get info from my list I get a Type error unless I convert user input to integer
#my while loop checks it is an int using .isdigit but does not convert the string input to an int
reccomendation = get_artist_info(response)

output = reccomendation[int(user_input)-1]

file.write("Here is all the useful information for you! \n" )
for keys, value in output.items():
    print(value)
    file.write(str(value))


now = datetime.now().strftime("%Y-%m-%d")

print(f"I would day the best time to visit would be {now}!!")

file.write(f"I would day the best time to visit would be {now}!!")

file.close()