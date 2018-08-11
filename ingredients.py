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

def plot_from_ingredient_count(ingredient_count):
    x = [i for i in range(len(ingredient_count))]
    y = [i for i in ingredient_count.values()]
    y.sort(reverse=True)
    plt.bar(x, y)
    plt.show()

root = root_from_xml_filename('cookbook_import_pages_current.xml')
all_ingredients = lists_all_ingredients_from_root(root)
count_ingredients = Counter(all_ingredients)
over_100 = {key: value for (key, value) in count_ingredients.items() if value > 100}
plot_from_ingredient_count(over_100)