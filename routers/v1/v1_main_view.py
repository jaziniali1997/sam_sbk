from . import v1


@v1.get("")
def v1_main_view():
    return {"message": "hello from v1_main_view"}
