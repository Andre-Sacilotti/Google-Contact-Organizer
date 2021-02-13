import requests

a = requests.post(
    "http://127.0.0.1:5000/api/teste",
    data={
        "token": """ya29.a0AfH6SMDSucEKk5abf33zutFiG354En6-ojSBWiqMVgMypeYLjgFb9oTaqNwz4KMsJoK8H8C9wBvrNrn7ZITJpIL4h6kKePw_kemVUrOGKCSQanmgT-VG-mOgbGQ2nVn_dso1QM9Y-1MfdZiZtTJa7AP60HngL5H2Rms133C6LiY"""
    },
)

print(a)
