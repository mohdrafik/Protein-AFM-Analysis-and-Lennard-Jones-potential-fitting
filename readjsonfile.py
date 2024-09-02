
import json
with open('complex_data.json','r+') as file:
    complex_data= json.load(file)
    person_name  = complex_data['person']["name"]  # will give the name of the person.
    print(person_name)
    person_age = complex_data['person']['age']
    print(person_age)
    
# Access values in the complex data
# person_name = complex_data["person"]["name"]
# person_age = complex_data["person"]["age"]

# Access the list of contacts
contacts = complex_data["person"]["contacts"]

# Access values within the list of contacts
for contact in contacts:
    contact_type = contact["type"]
    contact_value = contact["value"]
    print(f"Contact Type: {contact_type}, Value: {contact_value}")

# Access books data within the JSON
books = complex_data["books"]

# Iterate over books and access values
for book in books:
    book_title = book["title"]
    book_authors = book["authors"]
    book_price = book["price"]
    print(f"Book Title: {book_title}, Authors: {', '.join(book_authors)}, Price: ${book_price:.2f}")