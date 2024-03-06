import requests

query = """
        {
            hello
            goodbye
        }
"""

# definir la url
url = "http://localhost:8000/graphql"

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)