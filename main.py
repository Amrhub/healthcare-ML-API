from fastapi import FastAPI

from pydantic import BaseModel

from pymongo import MongoClient

app = FastAPI()

client = MongoClient(
    "mongodb+srv://healthcaregp:healthcaregp@cluster0.qq548.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.healthcaredb

deviceDataCollection = db["deviceData"]


class DeviceData(BaseModel):
    id: float
    heartRate: float
    spo2: float
    temp: float
    ECG: list
    GPS: list


@app.get("/")
def read_root():
    return {"Hello": "HealthCare 2.0"}


@app.post('/data')
def post_data(data: DeviceData):
    deviceDataCollection.insert_one(data.dict())
    return data


@app.get('/data')
def get_data():
    return list(deviceDataCollection.find({}, {"_id": 0}))


@app.delete('/data')
def delete_data():
    deviceDataCollection.delete_many({})
    return {"message": "All data deleted"}
