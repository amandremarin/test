import xml.etree.ElementTree as ET
import re
from collections import Counter
import matplotlib.pyplot as plt

def plot_top(x_ingredients):
    top_x_ingredients = get_top_ingredients(x_ingredients)
    x = [i for i in range(len(top_x_ingredients))]
    y = [i for i in top_x_ingredients.values()]
    plt.barh(x, y, align='center')
    labels = [re.sub('[\[\]]','', label) for label in top_x_ingredients.keys()]
    plt.yticks(x, labels)
    plt.xlabel('How Many Recipes Used This Ingredient')
    plt.ylabel('Ingredient')
    plt.title('Top {0} Ingredients In Recipes'.format(x_ingredients))
    if x_ingredients <= 35:
        pass
    elif x_ingredients <= 50:
        plt.tick_params(axis='y', labelsize=8)
    else:
        plt.tick_params(axis='y', labelsize=5)
    plt.show()

def get_top_ingredients(x_ingredients):
    root = root_from_xml_filename('../cookbook_import_pages_current.xml')
    all_ingredients = list_all_ingredients_from_root(root)
    ingredients_count = Counter(all_ingredients)
    top_x_ingredients = {key: value for (key, value) in ingredients_count.most_common(x_ingredients)}
    return top_x_ingredients

def root_from_xml_filename(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return root

def list_all_ingredients_from_root(root):
    all_ingredients = []
    for text in root.findall('*/*/*'):
        if text.text: m = re.search('Ingredients.*Directions',text.text, re.DOTALL)
        if m: x = m.group()
        if m: y = re.findall(r'\[\[.*\]\]',x)
        if m and y: 
            for ingredient in y:
                all_ingredients.append(ingredient)
    return all_ingredients

user_input = int(input("How many ingredients do you want to show?: "))
plot_top(user_input)