"""
You can declare the HTTP status code used for the response with the parameter status_code in any of the
path operations:
 - @app.get()
 - @app.post()
 - @app.put()
 - @app.delete()
 - etc.

Notice that status_code is a parameter of the "decorator" method (get, post, etc).
Not of your path operation function, like all the parameters and body.
"""

from fastapi import FastAPI, status


app = FastAPI()

@app.post("/user/",status_code= status.HTTP_201_CREATED)
async def create_user(name: str):
    return {"name": name}

