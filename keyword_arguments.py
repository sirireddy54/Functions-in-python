def player(firstname, lastname):
    print(f"hello {firstname} {lastname}, how are you?")


player("virat","kohli")   #normal arguments i.e positional arguments
print("finished")

player(lastname="smith",firstname="John")  #keyword arguments
print("finished again")