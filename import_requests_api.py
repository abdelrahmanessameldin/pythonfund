import requests
import json

GITLAB_URL = "https://gitlab.com/api/v4"
USERNAME = "Abdelrahmanessameldin-Barq"

Endpoint = (f"{GITLAB_URL}/users/{USERNAME}/projects")

response = requests.get(Endpoint)

my_projects = response.json()

for project in my_projects :
    print(f"project name is : {project['name']}")


#print (response.text)

data = json.loads(response.text)

'''for project in data:
    print('Project Name: ', project['name'])
    print('Project Description: ', project['description'])
    print('Project URL: ', project['web_url'])
    print('Created At: ', project['created_at'])
    print('Last Activity At: ', project['last_activity_at'])
    print('The readme URL is: ', project['readme_url'])
    print('-----------------------------------------')

print (response.json)
'''