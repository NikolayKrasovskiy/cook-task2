def read_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            i += 1
            if lines[i].strip().isdigit():
                ingredient_count = int(lines[i].strip())
                i += 1
            else:
                continue
            ingredients = []
            for j in range(i, i + ingredient_count):
                ingredient_info = lines[j].strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            i += ingredient_count
    return cook_book

def print_cook_book(cook_book):
    for dish_name, ingredients in cook_book.items():
        print(dish_name)
        print(len(ingredients))
        for ingredient in ingredients:
            print(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}")
        print()  # Печатаем пустую строку после каждого блюда

file_name = 'cook.txt'
cook_book = read_recipes(file_name)
print_cook_book(cook_book)