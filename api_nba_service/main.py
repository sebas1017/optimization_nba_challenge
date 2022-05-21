from fastapi import FastAPI

from nba_players_data_app  import routes
from starlette.responses import JSONResponse
import os
import uvicorn



app = FastAPI(title="NBA API PLAYERS",version="1.0.0")
app.include_router(routes.router)

@app.exception_handler(404)
async def custom_404_handler(_, __):
	return JSONResponse({"message": "el recurso solicitado no existe"}, status_code=404)
	




if __name__=="__main__":
	PORT = int(os.environ.get('PORT', 8000))
	uvicorn.run("main:app",host='0.0.0.0',port=PORT ,reload=True)