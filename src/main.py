"""A very minimal API to showcase GitLab CI/CD pipelines.

"""
from fastapi import FastAPI, HTTPException
app = FastAPI()


@app.get("/")
async def read_main():
    """The root endpoint, simply says hi to the user :)
    """
    return {"msg": "Hello, World!"}


@app.get("/one-to-ten/{number}")
async def read_number(number):
    """This endpoint returns the given number (1-10 only) in hexadecimal, binary
    and octal formats.

    """
    try:
        number = int(number)
    except ValueError as err:
        raise HTTPException(status_code=400, detail="Invalid input!") from err
    if number < 1 or number > 10:
        raise HTTPException(
            status_code=422, detail="Only numbers 1-10 are accepted!")
    return {"number": {"binary": bin(number), "hexadecimal": hex(number), "octal": oct(number)}}
