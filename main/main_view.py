from . import app


@app.get('/')
def main_view():
    return {"message": "hello from main_view"}
