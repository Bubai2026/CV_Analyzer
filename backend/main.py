from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router as analysis_router

app = FastAPI(title="GenAI Resume Analyzer API")

# 1. Enable CORS (Cross-Origin Resource Sharing)
# This ensures that your frontend and backend can talk to each other without being blocked
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],
)

# 2. Include the Router
# This "registers" the /analyze route so it is no longer 404
app.include_router(analysis_router)

# 3. Root Endpoint for Health Check
@app.get("/")
async def root():
    return {
        "message": "Backend is running successfully",
        "docs": "Visit /docs for the API documentation"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)