"""Taks 1"""


# person = {
#           'Name': 'Bart Simpson',
#           'Address': '742 Evergreen Terrace'
#           }

# print(f"{person['Name']}, {person['Address']}")


"""Task 2"""


# bart = {"Name": 'Bart Simpson'}

# homer = {"Name": 'Homer Simpson'}

# address = {"address": '742 Evergreen Terrace'}

# bart.update(address)

# homer.update(address)

# print(bart['address'])

# print(type(bart['address']))


"""Task 3"""


# ages = {"Peter": "36",
#         "Robin": "29",
#         "Michael": "33",
#         }

# for person, age in ages.items():
    
#     print(f'{person} is {age} years old')
    


"""Task 4"""


# animals = {
#         "Alligator": 4,
#         "Tiger": 6, 
#         "Parrot": 9,
#         "Hamster": 2, 
#         "Dolphin": 5,
#         }


# key_list = sorted(animals.keys())

# for key in key_list:
    
#     if key.endswith('r'):
        
#         del animals[key]
        
# print(animals)

animals = {
    "Alligator": 4,
    "Tiger": 6, 
    "Parrot": 9,
    "Hamster": 2, 
    "Dolphin": 5,
}



def rearrange(dict):
    
    listing = sorted(dict.keys())
    
    for i in listing:
        
        if i.endswith('r'):
            
            del dict[i]
            
    return dict

print(rearrange(animals))


