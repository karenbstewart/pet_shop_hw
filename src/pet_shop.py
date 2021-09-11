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

#test 10 



