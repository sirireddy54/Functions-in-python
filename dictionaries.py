def save_user(**user):
    print(user)
    print(user["name"])

save_user(id=1, name="siri", age=25)

#output is   {'id': 1, 'name': 'siri', 'age': 25}
# dictionary holds {key: value} pairs