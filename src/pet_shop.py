# WRITE YOUR FUNCTIONS HERE
import pdb

#test 1 
def get_pet_shop_name(pet_list):
    shop_name = pet_list["name"]
    return shop_name

#test 2 
def get_total_cash(pet_list):
    return pet_list["admin"]["total_cash"]

# does this call the amount rather than access the point in the actual list??
# def add_or_remove_cash(pet_list, cash_amount):
#     new_total = get_total_cash(pet_list) 
#     new_total += cash_amount

#tests 3 and 4     
def add_or_remove_cash(pet_list, cash_amount):
    pet_list["admin"]["total_cash"] += cash_amount

#test 5   
def get_pets_sold(pet_list):
    return pet_list["admin"]["pets_sold"]

#test 6
def increase_pets_sold(pet_list, amount_sold):
    pet_list["admin"]["pets_sold"] += amount_sold


#test 7 
def get_stock_count(pet_list):
    animals_in_stock = len(pet_list["pets"])
    return animals_in_stock

#test 8 and 9
def get_pets_by_breed(pet_list, breed):
    count = []
    for num_of_breed_found in pet_list["pets"]:
        if num_of_breed_found["breed"]== breed:
            count.append(breed) 
    return count 

#test 10 and 11
def find_pet_by_name(pet_list, animal_name):
    for animal in pet_list["pets"]:
        if animal["name"] == animal_name:
            return animal

#test 12
def remove_pet_by_name(pet_list, animal_name):
    for animal in pet_list["pets"]:
        if animal["name"] == animal_name:
            pet_list["pets"].remove(animal)


#test 13 
def add_pet_to_stock(pet_list, new_pet):
    pet_list["pets"].append(new_pet)


#test 14
def get_customer_cash(customer_list):
    return customer_list["cash"]


#test 15 
def remove_customer_cash(customer, cash_amount):
    customer["cash"] -= cash_amount

#test 16 
def get_customer_pet_count(customers):
    return len(customers["pets"])
