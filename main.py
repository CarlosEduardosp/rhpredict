from src.desenvolvimento.app import app
import uvicorn


# para produção
"""if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)"""


# para desenvolvimento
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)