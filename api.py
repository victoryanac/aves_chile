import requests
import json
from string import Template


html_template = Template('''<!DOCTYPE html>
<html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="ISO-8859-1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>aves_chile</title>
</head>
<body>
<h1> Aves de Chile </h1>
    $body

</body>
</html>
</html>
''')


elemento_template = Template( ''' <h2> $espanol </h2>
                                    <h3> $ingles </h3>
                                    <img src="$url">
                                        ''')


def request_get(url):
    return requests.get(url).json()


def buil_html(url):
    response = request_get(url)
    texto = ""

    for ave in response:
        nombre_espanol = ave['name']['spanish']
        nombre_ingles = ave['name']['english']
        imagen = ave['images']['main']
        texto += elemento_template.substitute(espanol=nombre_espanol, ingles=nombre_ingles, url=imagen)    
    return html_template.substitute(body=texto)

html = buil_html("https://aves.ninjas.cl/api/birds")
with open("aves.html", "w") as f:
    f.write(html)




