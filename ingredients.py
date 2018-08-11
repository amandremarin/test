import xml.etree.ElementTree as ET
import re
from collections import Counter

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