from fastapi import APIRouter, Body, HTTPException, WebSocket
from app.internal.models import model
from ..schemas.parking import Parking
from app.apps.mock.consumer import consumer
import json

router = APIRouter()

async def get_all():
    res = model.session.query(model.Parking).all()
    return res

async def get_by_id(id: int):
    res = model.session.query(model.Parking).all()
    for park_slot in res:
        if park_slot.id == id:
            return park_slot
    raise HTTPException(status_code=404, detail="No parking slot")

async def reserve_parking(parking: Parking):

    # cur = model.cursor
    # cur.execute(f"SELECT * FROM parking WHERE id={parking.id}")
    # res = cur.fetchone()

    # if res is not None:
    #     try:
    #         cur.execute(f"UPDATE parking SET occupied={False} WHERE id={parking.id} RETURNING id")
    #         res1 = cur.fetchone()
    #         print(res1)
    #         model.conn.commit()

    #     except Exception as e:
    #         print(e)
    #         model.conn.rollback()

    res = model.session.query(model.Parking).all()
    for park_slot in res:
        print(park_slot)
        if park_slot.id == parking.id:
            try:
                park_slot.occupied = parking.occupied
                model.session.commit()
                print("OK")
                return {'status': 'ok'}
            except Exception as e:
                print(e)
                model.session.rollback()
    raise HTTPException(status_code=404, detail="No parking slot")

async def socket_test(websocket: WebSocket):
    await websocket.accept()
    while True:
        # data = await websocket.receive_text()
        for message in consumer:
            await websocket.send_text(f"Message text was: {json.dumps(message.value)}")


def create_routes():
    router.add_api_route("/api/v1/parking", 
                         get_all, 
                         response_model=list[Parking],
                         tags=["Parking"])

    router.add_api_route("/api/v1/parking/{id}",
                         get_by_id,
                         response_model=Parking,
                         tags=["Parking"])

    router.add_api_route("/api/v1/parking",
                         reserve_parking,
                         methods=["PUT"],
                         tags=["Parking"])

    router.add_websocket_route("/api/v1/websocket",
                               socket_test)
