from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    avatar_color: str
    image: Optional[str] = None

class PlayResponse(BaseModel):
    is_winner: bool
    prize_amount: Optional[str] = None
    message: str

# --- 评论数据 (完全对应设计图与文件名) ---
reviews_db = [
    {
        "id": 1, 
        "user_name": "Thanh", 
        "content": "This really helped me cover my rent and bills. I finally feel some relief.", 
        "likes": 120, 
        "time_ago": "1 week ago", 
        "avatar_color": "#FFC0CB", 
        "image": "image1@1x.png" # 对应第一张图
    },
    {
        "id": 2, 
        "user_name": "HybridOpticz", 
        "content": "Didn't get selected this time, but I appreciate the opportunity.", 
        "likes": 45, 
        "time_ago": "1 week ago", 
        "avatar_color": "#333333",
        "image": "image2@1x.png" # 虽然设计图里没图，但您的文件里有，我这里也加上了
    },
    {
        "id": 3, 
        "user_name": "Sayem Ahmed", 
        "content": "This helped me finally buy a computer I needed for work and study.", 
        "likes": 89, 
        "time_ago": "2 weeks ago", 
        "avatar_color": "#4682B4",
        "image": "image3@1x.png"
    },
    {
        "id": 4, 
        "user_name": "haf", 
        "content": "This support helped me buy a car I really needed for work and family.", 
        "likes": 234, 
        "time_ago": "2 weeks ago", 
        "avatar_color": "#9b59b6",
        "image": "image4@1x.png"
    },
    {
        "id": 5, 
        "user_name": "Kintaro", 
        "content": "I wasn't chosen, but it was still worth trying. Hoping for next time.", 
        "likes": 12, 
        "time_ago": "2 weeks ago", 
        "avatar_color": "#2ecc71",
        "image": "image5@1x.png"
    },
    {
        "id": 6, 
        "user_name": "Jonathan Staianov", 
        "content": "I never expected this, but it helped me get through a very difficult time.", 
        "likes": 567, 
        "time_ago": "3 weeks ago", 
        "avatar_color": "#f1c40f",
        "image": "image6@1x.png"
    }
]

@app.get("/")
def read_root():
    return {"message": "Backend is ready!"}

@app.get("/stats")
def get_stats():
    return {"participants": 134867 + random.randint(1, 100), "satisfaction": 98}

@app.get("/reviews", response_model=List[Review])
def get_reviews():
    return reviews_db

@app.post("/play", response_model=PlayResponse)
def play_game():
    if random.random() < 0.2: 
        return {"is_winner": True, "prize_amount": "$5,000", "message": "CONGRATULATIONS! You won financial support!"}
    else:
        return {"is_winner": False, "message": "Sorry, you were not selected this time."}
