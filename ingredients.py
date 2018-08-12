import xml.etree.ElementTree as ET
import re
from collections import Counter
import matplotlib.pyplot as plt

def root_from_xml_filename(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return root

def lists_all_ingredients_from_root(root):

    all_ingredients = []

    for text in root.findall('*/*/*'):
        if text.text: m = re.search('Ingredients.*Directions',text.text, re.DOTALL)
        if m: x = m.group()
        if m: y = re.findall(r'\[\[.*\]\]',x)
        if m and y: 
            for ingredient in y:
                all_ingredients.append(ingredient)
    return all_ingredients

def plot_count_over(x_ingredients):
    root = root_from_xml_filename('cookbook_import_pages_current.xml')
    all_ingredients = lists_all_ingredients_from_root(root)
    ingredients_count = Counter(all_ingredients)
    over_x = {key: value for (key, value) in ingredients_count.items() if value > x_ingredients}
    x = [i for i in range(len(over_x))]
    y = [i for i in over_x.values()]
    #y.sort(reverse=True)
    plt.barh(x, y)
    labels = [label for label in over_x.keys()]
    plt.yticks(x, labels)
    if x_ingredients >= 1000:
        plt.tick_params(axis='y', labelsize=8)
    elif x_ingredients >= 500:
        plt.tick_params(axis='y', labelsize=5)
    plt.show()

plot_count_over(500)