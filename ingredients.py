import xml.etree.ElementTree as ET
import re
from collections import Counter
import matplotlib.pyplot as plt

tree = ET.parse(r'C:\Users\ANDRE\Downloads\cookbook_import_pages_current.xml\cookbook_import_pages_current.xml')
root = tree.getroot()

all_ingredients = []

for text in root.findall('*/*/*'):
 if text.text: m = re.search('Ingredients.*Directions',text.text, re.DOTALL)
 if m: x = m.group()
 if m: y = re.findall(r'\[\[.*\]\]',x)
 if m and y: 
  for ingredient in y:
   all_ingredients.append(ingredient)

top_ingredients = Counter(all_ingredients)
over_100 = {key: value for (key, value) in top_ingredients.items() if value > 100}
x = [i for i in range(1, len(over_100)+1)]
y = [x for x in over_100.values()]
y.sort()
plt.bar(x, y)
plt.show()