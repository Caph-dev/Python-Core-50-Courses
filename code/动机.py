def get_full_name(first_name: str, last_name: str) -> str: 
    full_name = first_name.upper() + " " + last_name.upper()
    return full_name

def get_name_with_age(name: str, age: int) -> str:
    name_with_age = name.capitalize() + " is " + str(age) + " years old" 
    return name_with_age

print(get_full_name("john", "doe"))
print(get_name_with_age("john", 20))