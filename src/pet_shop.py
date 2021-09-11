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

