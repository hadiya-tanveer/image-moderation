from fastapi import FastAPI, File, UploadFile, Depends

from auth import get_token_auth
from moderation import analyze_image_mock
from models import create_token, get_all_tokens, delete_token
import secrets

app = FastAPI()

@app.post("/moderate")
async def moderate(file: UploadFile = File(...), token=Depends(get_token_auth())):
    contents = await file.read()
    result = analyze_image_mock(contents)
    return result

@app.post("/auth/tokens")
def create_new_token(isAdmin: bool = False, auth=Depends(get_token_auth(admin_only=True))):
    new_token = secrets.token_hex(16)
    create_token(new_token, is_admin=isAdmin)
    return {"token": new_token, "isAdmin": isAdmin}

@app.get("/auth/tokens")
def list_tokens(auth=Depends(get_token_auth(admin_only=True))):
    return get_all_tokens()

@app.delete("/auth/tokens/{token}")
def remove_token(token: str, auth=Depends(get_token_auth(admin_only=True))):
    delete_token(token)
    return {"message": "Token deleted"}
