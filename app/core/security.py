from jose import jwt
from datetime import datetime, timedelta
from .config import Settings

SECRET_KEY = Settings.JWT_SECRET
ALGORITHM = Settings.JWT_ALGORITHM


def create_access_token(data: dict):
# Add custom payload
    payload = {
    "user_id": data.get("user_id", ""),                      # custom field
    "exp": datetime.utcnow() + timedelta(minutes=1)  # expiration
}

# Encode JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token
    print(token)
