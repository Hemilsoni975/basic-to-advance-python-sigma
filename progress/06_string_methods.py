# strings methods

a = "!!!Hemil Y. Soni!!!"
b = "overview oF striNg methOds"
c = " welcome to my program !!! "
d = "HelloWorldIsBasicProgramOfAll"
e = "    "
f = "HEMIL"

print(a) 
print(len(a)) # length of the strings 
print(a.upper()) # converts whole string into uppercase
print(a.lower()) # converts whole string into lowercase
print(a.rstrip("!")) # deletes last element of string 
print(a.replace("Hemil" , "hemu")) # helps to replace the string 
print(a.split(" ")) # helps to split in list type 
print(b.capitalize()) # converts only first letter to uppercase and converts all other letters to lowercase
print(c.center(50)) # aligns string to center as per the parameter given by user 
print(a.count("!")) # count the letters how many time it is repeated 
print(b.endswith("!")) # here it checks that is string completed with "!" if no then false
print(c.endswith("!")) # here it checks that is string completed with "!" if yes then true 
print(c.endswith("my" , 1 , 13)) # here it checks value in between the string provided by start and end index position
print(b.startswith("overview")) # here it checks that is string completed with "!" if no then false
print(c.find("my")) # here it helps to find that the word is there in the string or not it not then return -1
print(c.index("my")) # it works same as find() but if word is not there in string it will throw error
print(d.isalnum()) # here it checks whether the string contains A-Z,a-z,0-9
print(d.isalpha()) # here it checks whether the string contact A-Z,a-z, if any numeric value is present then return false
print(f.isupper()) ## it checks whether the string is in upercase if yes then return true otherwise fasle
print(c.islower()) # it checks whether the string is in lowercase if yes then return true otherwise fasle
print(c.isprintable()) # it checks the string is printable and doesn't contain "\" symbol in between else retrun false
print(e.isspace()) # method return true only and only when string contains space otherwise return false 
print(a.istitle()) # it checks the first letter of the words in string is capital or not if capital return true else fasle
print(b.swapcase()) # it helps to swap uppercase letter to lowercase and lowercase to uppercase
print(b.title()) # it helps to convert all first letter of word to uppercase