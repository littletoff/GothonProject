#testing how to use dictionaries

geography = {"France": "Paris", "Switzerland": "Bern", "Austria":"Vienna"}

print(geography["France"])
print(geography)

#cycle through the dictionary using for statement
for country, capital in geography.items():
    print(geography[country])


#get what you want from a dictionary
mycountry=geography.get(None, "Bern")
print(mycountry)

#get what you want from a dictionary, but an entry doesn't exist
mycountry=geography.get(None, "Warsaw")
if not mycountry:
    print("There is no entry")
print(mycountry)


#lists and such
ten_things = "Apples Oranges Crows Telephone Light Sugar"
stuff=ten_things.split(" ")
print(stuff)
stuff.pop()
print(stuff)

print(len(stuff))
intlength=len(stuff)

for i in range(0, intlength):
    print(stuff[i])

    
