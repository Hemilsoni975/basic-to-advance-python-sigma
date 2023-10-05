# Dictionary is depend on key and value
# Dictionary is collection of ordered data

# myDict = { "key" : "value"}

# myDict = {}  # this represent an empty dictionary
# myDict = {1}   # this represent set not the dictionary

# simple dictionary
myDict = {
    "hemil": "soni",
    "umang": "nayak",
    "aman": "talaviya",
    "marks": [12,35],
    "AnotherDict": {975: "hemil", 906: "kesar", 961: "smit", 808 : "sanju"}
}
print(myDict)
print(type(myDict))

# print(myDict["patel"])  # this will return error
print(myDict.get("patel"))  # it will return none
print(myDict.keys())  # display all the keys
print(myDict.values())  # display all the values

# dictionary can be change
myDict["Marks"] = [45, 90]  # changing value of key of dictionary
print(myDict['Marks'])

# nested dictionary can be written as :
print(myDict['AnotherDict'])
print(myDict['AnotherDict'][975])

print("-----DICTIONARY-METHODS-----")

wow = {12: "hemil", 3: "umang", 808: "sanju", 961: "smit"}
wow1 = {16: "mit", 11: "kesar", 904: "hem"}

print(wow.items())  # it display all the key and value of dictionary using loop

for key, value in wow.items():
    print(f"the value corresponding to {key} is {value}")  # this is "f" string here variable is displayed in {} brackets

wow.update(wow1)  # it helps to update the dictionary by adding new key-values
print(wow)

wow2 = wow1.copy()  # helps to copy key-values of dictionary
print(wow2)
del wow2[904]
print(wow2)

wow.pop(808)  # helps to remove specific pair
print(wow)

wow.popitem()  # removes the last pair
print(wow)

wow.clear()  # clears whole dictionary
print(wow)

del wow  # delete the dictionary
# print(wow)
