import requests
from bs4 import BeautifulSoup

# 1. Parsing di una Pagina Web

# Ottenere il contenuto della pagina
response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')
print("Page Parsed Successfully.")

# 2. Trovare un Elemento

# Trovare il tag <title>
title = soup.find('title')
print("Title of the page:", title.text)

# 3. Trovare Tutti gli Elementi di un Tipo

# Trovare tutti i link <a>
all_links = soup.find_all('a')
print("All links on the page:")
for link in all_links:
    print(link.get('href'))

# 4. Filtrare per Attributi

# Trovare un link con una classe specifica
specific_link = soup.find('a', class_='specific-class')
if specific_link:
    print("Specific link:", specific_link.get('href'))
else:
    print("Specific link not found.")

# 5. Navigazione dell'albero

# Trovare il primo <p> e il suo genitore
first_paragraph = soup.find('p')
if first_paragraph:
    parent = first_paragraph.parent
    print("Parent tag of the first paragraph:", parent.name)

# 6. Modificare il Contenuto

# Modificare il contenuto del tag <title>
title.string = "New Title"
print("Modified Title:", title.text)

# 7. Aggiungere un Nuovo Elemento

# Aggiungere un nuovo tag <p> alla fine del body
new_paragraph = soup.new_tag('p')
new_paragraph.string = "This is a new paragraph."
soup.body.append(new_paragraph)
print("New paragraph added.")

# 8. Scrivere il Documento Modificato in un File

# Scrivere il documento modificato in un file HTML
with open('modified_page.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))
print("Modified page saved as 'modified_page.html'.")

# 9. Gestione degli Errori

# Gestione di errori durante il parsing
try:
    bad_response = requests.get('https://badurl.com')
    bad_soup = BeautifulSoup(bad_response.text, 'html.parser')
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
