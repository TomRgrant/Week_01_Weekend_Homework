# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    shop_total = pet_shop['admin']['total_cash']
    return shop_total

def add_or_remove_cash(pet_shop, cash_add):
    old_total = pet_shop['admin']['total_cash']
    new_total = old_total + cash_add
    pet_shop['admin']['total_cash'] = new_total
    
def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, num):
    pet_shop['admin']['pets_sold'] = pet_shop['admin']['pets_sold'] + num

def get_stock_count(pet_shop):
    counter = 0
    for pet in pet_shop['pets']:
        counter += 1
    return counter

def get_pets_by_breed(pet_shop, breed):
    found_breed = []
    for pet in pet_shop['pets']:
        if pet['breed'] == breed:
            found_breed.append(pet)
    return found_breed

def find_pet_by_name(pet_shop, name):
    found_name = None
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            found_name = pet
    return found_name

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            pet_shop['pets'].remove(pet)

def add_pet_to_stock(petshop, new_pet):
    petshop['pets'].append(new_pet)

def get_customer_cash(customer):
    customer_cash = customer['cash']
    return customer_cash

def remove_customer_cash(customer, cash):
    customer['cash'] -= cash

def get_customer_pet_count(customer):
    total_pets = len(customer['pets'])
    return total_pets

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    can_buy_new_pet = False
    if customer['cash'] >= new_pet['price']:
        can_buy_new_pet = True
    return can_buy_new_pet

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet == None:
        pass
    else:
        customer_can_afford = customer_can_afford_pet(customer, pet)
        if customer_can_afford == True:
            remove_customer_cash(customer, pet['price'])
            remove_pet_by_name(pet_shop, pet)
            add_pet_to_customer(customer, pet)
            add_or_remove_cash(pet_shop, pet['price'])
            pet_shop['admin']['pets_sold'] += 1
            get_customer_pet_count(customer)
            get_pets_sold(pet_shop)
            get_customer_cash(customer)
            get_total_cash(pet_shop)
            get_customer_pet_count(customer)
