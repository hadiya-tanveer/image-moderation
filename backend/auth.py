from fastapi import Request, HTTPException, status, Depends
from models import is_valid_token, log_usage

def get_token_auth(admin_only=False):
    async def verify_token(request: Request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

        token = auth_header.split()[1]
        token_data = is_valid_token(token)

        if not token_data:
            raise HTTPException(status_code=401, detail="Invalid token")

        if admin_only and not token_data.get("isAdmin"):
            raise HTTPException(status_code=403, detail="Admin token required")

        # Log usage
        log_usage(token, str(request.url.path))

        return token_data  # can be used in endpoint if needed
    return verify_token
