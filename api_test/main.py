from fastapi import FastAPI

app = FastAPI()

# Dummy database
users = {
    "misbah": {"pin": 1234, "bank_balance": 50000},
    "aiesha": {"pin": 1111, "bank_balance": 10000}
}

@app.post("/authenticate")
async def authenticate(name: str, pin_number: int):
    if name not in users:
        return {"message": "User not found"}

    if users[name]["pin"] != pin_number:
        return {"message": "Invalid pin"}

    return {
        "message": "Authenticated",
        "bank_balance": users[name]["bank_balance"]
    }


@app.post("/bank-transfer")
async def bank_transfer(sender_name: str, recipient_name: str, amount: int):

    if sender_name not in users or recipient_name not in users:
        return {"message": "User not found"}

    sender = users[sender_name]
    recipient = users[recipient_name]

    if sender["bank_balance"] < amount:
        return {"message": "Insufficient balance"}

    sender["bank_balance"] -= amount
    recipient["bank_balance"] += amount

    return {
        "message": "Transfer successful",
        "sender_balance": sender["bank_balance"],
        "recipient_balance": recipient["bank_balance"]
    }
