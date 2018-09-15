import xml.etree.ElementTree as ET
tree = ET.parse('../cookbook_import_pages_current.xml')
root = tree.getroot()

web_pages = [web_page for web_page in root.findall('{http://www.mediawiki.org/xml/export-0.10/}page') if web_page.find('{http://www.mediawiki.org/xml/export-0.10/}ns').text=='0']

names = []
recipes = []
for web_page in web_pages:
    names.append(web_page.find('{http://www.mediawiki.org/xml/export-0.10/}title').text)
    recipes.append(web_page.find('{http://www.mediawiki.org/xml/export-0.10/}revision').find('{http://www.mediawiki.org/xml/export-0.10/}text').text)

import pandas as pd
d = {'Names': names, 'Recipes': recipes}
df = pd.DataFrame(data=d)
df.to_csv(path_or_buf=r'recipes.csv')
