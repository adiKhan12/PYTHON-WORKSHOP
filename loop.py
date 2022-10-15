num_dict = {1:"one", 2:"two", 3:"three"}


# 1st method
for num_key in num_dict:
    print(f"number key is : {num_key}, and Value is: {num_dict.get(num_key)}")


print("\nNow 2nd method \n")

#2nd method
for num_key, num_value in num_dict.items():
    print(f"number key is : {num_key}, and Value is: {num_value}")