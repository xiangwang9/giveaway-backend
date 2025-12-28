from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import random

app = FastAPI()

# --- 这里是数据模型 ---
class Review(BaseModel):
    id: int
    user_name: str
    content: str
    likes: int
    time_ago: str

class PlayResponse(BaseModel):
    is_winner: bool
    prize_amount: Optional[str] = None
    message: str

# --- 这里是模拟数据 ---
reviews_db = [
    {"id": 1, "user_name": "Thanh", "content": "This really helped me!", "likes": 120, "time_ago": "1 week ago"},
    {"id": 2, "user_name": "Steve", "content": "Grateful for this opportunity.", "likes": 45, "time_ago": "1 week ago"}
]

# --- 这里是接口 ---
@app.get("/")
def read_root():
    return {"message": "Server is running successfully!"}

@app.get("/stats")
def get_stats():
    return {"participants": 134867, "satisfaction": 98}

@app.get("/reviews", response_model=List[Review])
def get_reviews():
    return reviews_db

@app.post("/play", response_model=PlayResponse)
def play_game():
    # 模拟抽奖逻辑
    if random.random() < 0.2:
        return {"is_winner": True, "prize_amount": "$5,000", "message": "You Won!"}
    else:
        return {"is_winner": False, "message": "Try again!"}
