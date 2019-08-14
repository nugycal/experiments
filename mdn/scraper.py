from bs4 import BeautifulSoup
import requests
import json
import re
import os

API_URL = "https://developer.mozilla.org/en-US/docs/feeds/json/tag/Javascript"
REFERENCE_URL = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference"
BASE_URL = "https://developer.mozilla.org"

data = requests.get(REFERENCE_URL)
soup = BeautifulSoup(data.text, 'html.parser')
parent = soup.find("article", { "id": "wikiArticle" })
matches = []
links = []
for match in parent.find_all("a", href=True):
    if re.sub(r'#.*', '', match["href"]) not in matches:
        links.append(re.sub(r'#.*', '', match["href"]))
        matches.append(re.sub(r'#.*', '', match["href"]))

try:
    os.mkdir("output")
except:
    print("Couldn't create output directory")
    exit(1)

try:
    os.mkdir("output/res")
except:
    print("Couldn't create resources directory")
    exit(1)

linked_res = []
extra_links = []

for link in links:
    data = requests.get(BASE_URL + link)
    data = data.text
    soup = BeautifulSoup(data, 'html.parser')

    quick_links = soup.find("div", {'class':'quick-links'})
    for a in quick_links.find_all("a", href=True):
        if a['href'] not in links:
            extra_links.append(a['href'])

    for a in soup.find_all("a", href=True):
        if '/en-US/docs/' in a['href']:
            a['href'] = a['href'].replace('/en-US/docs/', '/') + ".html"
        elif '/en-US/' == a['href']:
            a['href'] = '/'

    for example in soup.find_all("pre", {'class':'brush:'}):
        example.decompose()

    for example in soup.find_all("iframe", {'class':'interactive'}):
        example.decompose()

    for stylesheet in soup.find_all("link", href=True):
        if "http" in stylesheet['href'] and stylesheet['href'] not in linked_res and stylesheet['href'] not in links:
            linked_res.append(stylesheet['href'])
            sheet = requests.get(stylesheet['href'])
            sheet = sheet.text
            with open("output/res/" + re.sub(r'.*/', '', stylesheet['href']), "w") as f:
                f.write(sheet)
        if "http" in stylesheet['href']:
            stylesheet['href'] = "/res/" + re.sub(r'.*/', '', stylesheet['href'])

    for script in soup.find_all("script", src=True):
        if "http" in script['src'] and script['src'] not in linked_res:
            linked_res.append(script['src'])
            sheet = requests.get(script['src'])
            sheet = sheet.text
            with open("output/res/" + re.sub(r'.*/', '', script['src']), "w") as f:
                f.write(sheet)
        if "http" in script['src']:
            script['src'] = "/res/" + re.sub(r'.*/', '', script['src'])

    for image in soup.find_all("img", src=True):
        if "http" in image['src'] and image['src'] not in linked_res:
            linked_res.append(image['src'])
            sheet = requests.get(image['src'])
            with open("output/res/" + re.sub(r'.*/', '', image['src']), "wb") as f:
                f.write(sheet.content)
        if "http" in stylesheet['href']:
            image['src'] = "/res/" + re.sub(r'.*/', '', image['src'])

    try:
        os.makedirs("output/" + re.sub(r'/[A-Za-z\._]+$', '', link).replace('/en-US/docs/', ''))
    except:
        print("Failed to construct directory tree: " + "output/" + re.sub(r'/[A-Za-z\._]+$', '', link).replace('/en-US/docs/', ''))
    with open("output/" + re.sub(r'/[A-Za-z\._]+$', '', link).replace('/en-US/docs/', '') + "/" + re.sub(r'.*/', '', link) + ".html", "w") as f:
        f.write(str(soup))
    with open("output/index.html", "a") as f:
        f.write('<a href="' + re.sub(r'/[A-Za-z\._]+$', '', link).replace('/en-US/docs/', '') + "/" + re.sub(r'.*/', '', link) + ".html" + '">' + re.sub(r'.*/', '', link) + "</a><br>")

for link in extra_links:
    data = requests.get(BASE_URL + link)
    data = data.text
    soup = BeautifulSoup(data, 'html.parser')

    for a in soup.find_all("a", href=True):
        if '/en-US/docs/' in a['href']:
            a['href'] = a['href'].replace('/en-US/docs/', '/') + ".html"
        elif '/en-US/' == a['href']:
            a['href'] = '/index.html'

    for example in soup.find_all("pre", {'class':'brush:'}):
        example.decompose()

    for example in soup.find_all("iframe", {'class':'interactive'}):
        example.decompose()

    for stylesheet in soup.find_all("link", href=True):
        if "http" in stylesheet['href'] and stylesheet['href'] not in linked_res:
            linked_res.append(stylesheet['href'])
            sheet = requests.get(stylesheet['href'])
            sheet = sheet.text
            with open("output/res/" + re.sub(r'.*/', '', stylesheet['href']), "w") as f:
                f.write(sheet)
        if "http" in stylesheet['href']:
            stylesheet['href'] = "/res/" + re.sub(r'.*/', '', stylesheet['href'])

    for script in soup.find_all("script", src=True):
        if "http" in script['src'] and script['src'] not in linked_res:
            linked_res.append(script['src'])
            sheet = requests.get(script['src'])
            sheet = sheet.text
            with open("output/res/" + re.sub(r'.*/', '', script['src']), "w") as f:
                f.write(sheet)
        if "http" in script['src']:
            script['src'] = "/res/" + re.sub(r'.*/', '', script['src'])

    for image in soup.find_all("img", src=True):
        if "http" in image['src'] and image['src'] not in linked_res:
            linked_res.append(image['src'])
            sheet = requests.get(image['src'])
            with open("output/res/" + re.sub(r'.*/', '', image['src']), "wb") as f:
                f.write(sheet.content)
        if "http" in stylesheet['href']:
            image['src'] = "/res/" + re.sub(r'.*/', '', image['src'])

    try:
        os.makedirs("output/" + re.sub(r'/[A-Za-z\._]+$', '', link).replace('/en-US/docs/', ''))
    except:
        print("Failed to construct directory tree: " + "output/" + re.sub(r'/[A-Za-z\._]+$', '', link).replace('/en-US/docs/', ''))
    with open("output/" + re.sub(r'/[A-Za-z\._]+$', '', link).replace('/en-US/docs/', '') + "/" + re.sub(r'.*/', '', link) + ".html", "w") as f:
        f.write(str(soup))
    with open("output/index.html", "a") as f:
        f.write('<a href="' + re.sub(r'/[A-Za-z\._]+$', '', link).replace('/en-US/docs/', '') + "/" + re.sub(r'.*/', '', link) + ".html" + '">' + re.sub(r'.*/', '', link) + "</a><br>")
