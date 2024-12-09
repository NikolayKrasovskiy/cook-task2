def readrecipes(filename):
    cookbook = {}  # Dictionary to store the recipes
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # Read all lines from the file
    i = 0  # Index to iterate through lines

    while i < len(lines):
        dish_name = lines[i].strip()  # Dish name
        i += 1

        if lines[i].strip().isdigit():  # Check if the next line contains the ingredient count
            ingredient_count = int(lines[i].strip())  # Get the ingredient count
            i += 1
        else:
            continue  # Skip if it's not a valid recipe format

        ingredients = []  # List to store ingredients for the dish
        for j in range(i, i + ingredient_count):  # Loop through ingredients
            ingredient_info = lines[j].strip().split(' | ')  # Split ingredient info
            ingredient = {
                'ingredient_name': ingredient_info[0],  # Ingredient name
                'quantity': int(ingredient_info[1]),  # Quantity of ingredient
                'measure': ingredient_info[2]  # Measure unit (e.g., grams, liters)
            }
            ingredients.append(ingredient)  # Add ingredient to the list
        cookbook[dish_name] = ingredients  # Add dish with ingredients to cookbook

        i += ingredient_count  # Move index forward

    return cookbook  # Return the complete cookbook


def printcookbook(cookbook):
    for dishname, ingredients in cookbook.items():  # Iterate through dishes
        print(dishname)  # Print dish name
        print(len(ingredients))  # Print number of ingredients
        for ingredient in ingredients:  # Loop through each ingredient
            print(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}")  # Print ingredient details
        print()


def getshoplistbydishes(dishes, person_count, cookbook):
    shopping_list = {}  # Dictionary to store shopping list
    for dish in dishes:  # Iterate through the selected dishes
        if dish in cookbook:  # Check if dish exists in the cookbook
            for ingredient in cookbook[dish]:  # Loop through the ingredients of the dish
                ingredient_name = ingredient['ingredient_name']  # Get the ingredient name
                quantity = ingredient['quantity'] * person_count  # Calculate total quantity for person_count

                measure = ingredient['measure']  # Measure unit (e.g., grams, liters)

                # Update the shopping list
                if ingredient_name in shopping_list:
                    shopping_list[ingredient_name]['quantity'] += quantity  # Add to existing quantity
                else:
                    shopping_list[ingredient_name] = {
                        'quantity': quantity,  # Set initial quantity
                        'measure': measure  # Set measure unit
                    }

    return shopping_list  # Return the final shopping list


# Example usage
filename = 'cook.txt'  # File with recipes
cookbook = readrecipes(filename)  # Read the cookbook from file
printcookbook(cookbook)  # Print the cookbook


# Selected dishes and the number of people
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shoppinglist = getshoplistbydishes(dishes, person_count, cookbook)  # Get shopping list
print(shoppinglist)  # Print the shopping list