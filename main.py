from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 新增
from pydantic import BaseModel
from typing import List, Optional
import random

app = FastAPI()

# --- 新增：允许跨域请求 (给网页开门) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有网址访问
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 数据模型 ---
class Review(BaseModel):
    id: int
    user_name: str
    content: str
    likes: int
    time_ago: str
    avatar_color: str # 新增头像颜色

class PlayResponse(BaseModel):
    is_winner: bool
    prize_amount: Optional[str] = None
    message: str

# --- 模拟数据 ---
reviews_db = [
    {"id": 1, "user_name": "Thanh", "content": "This really helped me cover my rent!", "likes": 120, "time_ago": "1 week ago", "avatar_color": "#FFC0CB"},
    {"id": 2, "user_name": "HybridOpticz", "content": "Didn't win but nice opportunity.", "likes": 45, "time_ago": "1 week ago", "avatar_color": "#333333"},
    {"id": 3, "user_name": "Sayem", "content": "Finally bought a computer for work.", "likes": 89, "time_ago": "2 weeks ago", "avatar_color": "#4682B4"}
]

@app.get("/")
def read_root():
    return {"message": "Backend is ready!"}

@app.get("/stats")
def get_stats():
    # 每次刷新稍微变动一点人数，模拟实时感
    return {"participants": 134867 + random.randint(1, 100), "satisfaction": 98}

@app.get("/reviews", response_model=List[Review])
def get_reviews():
    return reviews_db

@app.post("/play", response_model=PlayResponse)
def play_game():
    if random.random() < 0.3: # 30%中奖率
        return {"is_winner": True, "prize_amount": "$5,000", "message": "CONGRATULATIONS! You won financial support!"}
    else:
        return {"is_winner": False, "message": "Sorry, you were not selected this time."}
