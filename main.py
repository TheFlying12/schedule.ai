import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    # Run the FastAPI app with uvicorn
    uvicorn.run("src.api.app:app", host="0.0.0.0", port=8000, reload=True)
