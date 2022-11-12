with open ('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ing = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ing
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure})
        cook_book[dish_name] = ingredients
        file.readline()
        
print(cook_book)
print()

def get_shop_list_by_dishes(some_list, persons):
    cook_list = {}
    for dish in some_list:
        for ingredient in cook_book[dish]:
            cook_buy = dict(ingredient)
            #cook_list = dict(ingredients)
            cook_buy['quantity'] *= persons 
            cook_list[cook_buy['quantity']] = cook_buy
            #cook_list.update()
    return cook_list

by_dishes = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)
print(by_dishes)



                                   
            
      
            

 
