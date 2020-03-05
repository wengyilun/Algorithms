#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
	min_count = []
	for key in recipe.keys():
		if key not in ingredients.keys():
			print(f'{key} not in ingredients')
			return 0

		count = ingredients[key] // recipe[key]
		min_count.append(count)

	return min(min_count)


if __name__ == '__main__':
	# Change the entries of these dictionaries to test
	# your implementation with different inputs
	recipe = { 'milk': 2, 'sugar': 40, 'butter': 20}
	ingredients = { 'milk': 5, 'sugar': 120, 'butter': 500 }
	print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
		batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
