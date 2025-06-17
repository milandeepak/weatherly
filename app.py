import requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Add session middleware for storing cities in session
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("SECRET_KEY", "fallback-secret"))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    cities = request.session.get("cities", [])
    cities_per_row = [cities[i:i + 5] for i in range(0, len(cities), 5)]
    return templates.TemplateResponse("index.html", {"request": request, "cities_per_row": cities_per_row})

@app.post("/", response_class=HTMLResponse)
async def add_city(request: Request, city: str = Form(...)):
    cities = request.session.get("cities", [])
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f8b794366a2605ac9b420df813e61e25'
    try:
        r = requests.get(url.format(city)).json()
        if r.get('cod') == 200:
            weather_data = {
                'city': city,
                'temperature': round(r['main']['temp']),
                'description': r['weather'][0]['description'].capitalize(),
                'icon': r['weather'][0]['icon'],
                'humidity': r['main']['humidity'],
                'wind_speed': round(r['wind']['speed']),
            }
            # Check if city already exists
            if not any(c['city'].lower() == city.lower() for c in cities):
                cities.append(weather_data)
            else:
                for c in cities:
                    if c['city'].lower() == city.lower():
                        c.update(weather_data)
                        break
            request.session["cities"] = cities
    except Exception as e:
        print(f"Error fetching weather data: {e}")
    return RedirectResponse(url="/", status_code=303)

@app.get("/remove/{index}")
async def remove_city(request: Request, index: int):
    cities = request.session.get("cities", [])
    if 0 <= index < len(cities):
        cities.pop(index)
        request.session["cities"] = cities
    return RedirectResponse(url="/", status_code=303)

