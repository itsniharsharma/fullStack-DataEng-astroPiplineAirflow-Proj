import requests

TRANSIT_API = "http://localhost:5000/api/astronihar/d1"  # your local API
CHART_PATH = "data/transit_chart.svg"

def fetch_transit_chart():
    response = requests.get(TRANSIT_API)
    if response.status_code != 200:
        raise Exception("API failed")
    
    data = response.json()
    svg_content = data.get("svg", "")
    if not svg_content:
        raise Exception("SVG not found in response")

    with open(CHART_PATH, "w", encoding="utf-8") as f:
        f.write(svg_content)
