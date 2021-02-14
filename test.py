import requests
import json

a = requests.put(
    "http://127.0.0.1:5000/api/user/",
    headers={
        "authorization-code": """ya29.A0AfH6SMDqtWQvFED6jDVVPR0cEJQ72FifVlpCrvKIg2ybNtku5r88YbG9OwiLmCYP4Uftd2ls_6Hxv_WG6JgukvUxFdGtnEyml0LVJ9XnJb7gyoZg3sOn_qagocaUCmCvGU2-yIaeYooMDgamiSJn9g9ZUiomHQ"""
    },
    data=json.dumps({
        'user_id': "ID TESTE",
        'user_email': "EMAIL",
        'user_name': "NOMEEE" 
        
    })
)

print(a.text)
