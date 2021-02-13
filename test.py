import requests

a = requests.post(
    "http://127.0.0.1:5000/api/contact",
    json={"token": "teste"},
    headers={
        "authorization_token": """ya29.a0AfH6SMAT2LtREYZIRBUgoaWyzOmLbcmu-v76OeR6odfU22uow-sOo2bBrjwT1db9vu9yF4XvAQUJG5pOr8phPdXf_yiLM2zQrpUZITcAJQe6CFVnseaevtfb9oKaTEtQb6fnK28qjJpX-QUAF9h6zR8sElPrnkU2gSTkAPS5XMgu"""
    },
)

print(a)
