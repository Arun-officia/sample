# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from starlette.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import mysql.connector
#
# app = FastAPI()
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )
#
# security = HTTPBasic()
#
# VALID_USERNAME = "vebbox"
# VALID_PASSWORD = "12345"
#
#
# def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
#     if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password",
#             headers={"WWW-Authenticate": "Basic"},
#         )
#     return credentials.username
#
# class Item(BaseModel):
#     username: str
#     age: str
#     phonNo:str
#     email:str
#     cource:str
#
#
# @app.post("/get")
# def read_root1(obj: Item):
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="firstdb",
#         port="3310"
#     )
#
#     mypost = mydb.cursor()
#     mypost.execute("INSERT INTO student_details (student_name,age,student_phno,student_email,cource)"
#                    " VALUES ('" + obj.username + "','" + obj.age + "', '" + obj.phno + "','" + obj.email + "','" + obj.cource+ "')")
#     mypost.fetchall()
#     mydb.commit()
#
# @app.post("/view")
# def read_root1():
#         mydb = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",
#             database="firstdb",
#             port="3310"
#         )
#
#         mypost = mydb.cursor()
#         mypost.execute("SELECT * FROM student_details")
#         r = mypost.fetchall()
#         mydb.commit()
#         return r

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

security = HTTPBasic()

VALID_USERNAME = "vebbox"
VALID_PASSWORD = "12345"

def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

class Item(BaseModel):
    username: str
    age: str
    phoneNo: str
    email: str
    cource: str

@app.post("/get")
def insert_student(obj: Item, username: str = Depends(basic_auth)):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="firstdb",
        port="3310"
    )
    mycursor = mydb.cursor()
    insert_query = """
        INSERT INTO student_details 
        (student_name, age, student_phno, student_email, cource)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (obj.username, obj.age, obj.phoneNo, obj.email, obj.cource)
    mycursor.execute(insert_query, values)
    mydb.commit()
    return {"message": "Student data inserted successfully."}

@app.get("/view")
def view_students(username: str = Depends(basic_auth)):
    mydb = mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12780023",
        password="glV8hmDLtw",
        database="sql12780023",
        port="3306"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM onepiece")
    results = mycursor.fetchall()
    return results
