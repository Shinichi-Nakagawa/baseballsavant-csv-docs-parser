import csv
from requests_html import HTMLSession

session = HTMLSession()

response = session.get('https://baseballsavant.mlb.com/csv-docs')
response.html.render(timeout=120)

article_template = response.html.find('.article-template', first=True)
columns = []
for b in article_template.find('b'):
    columns.append(b.text)

descriptions = []
for ul in article_template.find('ul'):
    descriptions.append(ul.text)

values = dict(zip(columns, descriptions))

CSV_COLUMNS = ['column', 'description']

with open('baseball-savant_csv-docs_description.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
    writer.writeheader()
    for (c, d) in zip(columns, descriptions):
        writer.writerow({'column': c, 'description': d})
