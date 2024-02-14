import asyncio
from typing import Union
from fastapi import FastAPI
from fastapi import File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the specific origin you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    await asyncio.sleep(5)

    data = [
        {   "id":1,
            "name": "nkm",
            "time_range": [0, 2.2],
            "text": "Hindi. India is full of different castes, creeds, religions, and cultures, but they live together. That's the reasons India is famous for the common saying of unity in diversity. India is the seventh largest country in the world. Jai Hind."
        },
        {"id":2,
            "name": "glen",
            "time_range": [2.2, 3.7],
            "text": "Geography and culture. India has the second largest population in the world. India is also known as Bharat, Hindustan, and"
        },
        {"id":3,
            "name": "nkm",
            "time_range": [3.7, 6],
            "text": "Hindi. India is full of different castes, creeds, religions, and cultures, but they live together. That's the reasons India is famous for the common saying of unity in diversity. India is the seventh largest country in the world. Jai Hind.",
        },
        {"id":4,
            "name": "glen",
            "time_range": [31.2, 54.7],
            "text": "Geography and culture. India has the second largest population in the world. India is also known as Bharat, Hindustan, and",
        },
        {"id":5,
            "name": "nkm",
            "time_range": [11.4, 29.2],
            "text": "Hindi. India is full of different castes, creeds, religions, and cultures, but they live together. That's the reasons India is famous for the common saying of unity in diversity. India is the seventh largest country in the world. Jai Hind.",
        },
        {"id":6,
            "name": "glen",
            "time_range": [31.2, 54.7],
            "text": "Geography and culture. India has the second largest population in the world. India is also known as Bharat, Hindustan, and",
        },
        {"id":7,
            "name": "nkm",
            "time_range": [11.4, 29.2],
            "text": "Hindi. India is full of different castes, creeds, religions, and cultures, but they live together. That's the reasons India is famous for the common saying of unity in diversity. India is the seventh largest country in the world. Jai Hind.",
        },
        {"id":8,
            "name": "glen",
            "time_range": [31.2, 54.7],
            "text": "Geography and culture. India has the second largest population in the world. India is also known as Bharat, Hindustan, and",
        },
        {"id":9,
            "name": "nkm",
            "time_range": [11.4, 29.2],
            "text": "Hindi. India is full of different castes, creeds, religions, and cultures, but they live together. That's the reasons India is famous for the common saying of unity in diversity. India is the seventh largest country in the world. Jai Hind.",
        },
        {"id":10,
            "name": "glen",
            "time_range": [31.2, 54.7],
            "text": "Geography and culture. India has the second largest population in the world. India is also known as Bharat, Hindustan, and",
        },
        {"id":11,
            "name": "nkm",
            "time_range": [11.4, 29.2],
            "text": "Hindi. India is full of different castes, creeds, religions, and cultures, but they live together. That's the reasons India is famous for the common saying of unity in diversity. India is the seventh largest country in the world. Jai Hind.",
        },
        # Add more items as needed
    ]

    return data
    # return {"message": f"Successfully uploaded {file.filename}"}
