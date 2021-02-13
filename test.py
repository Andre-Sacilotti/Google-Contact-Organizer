import requests

a = requests.get(
    "http://127.0.0.1:5000/api/contact/",
    headers={
        "authorization-code": """ya29.A0AfH6SMBYT3F93H8gDRwG39XsrCu0hLt3tWHv-wZpGuvSgGwt88fRrK1MneOQF-HbzGxoyTG9qzkU8538nipfWnwPHedAS4VEosWRTJKLHJHuz1oVKeM4Rf-e-sVteCjQySLsOmSToNyQttMOgfRFbH5X8LE9UQ"""
    },
)

print(a.text)
