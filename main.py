from fastmcp import FastMCP
import time
import requests

mcp = FastMCP("mcp_config")

@mcp.tool()
async def hello(name: str) -> str:
    """
    Say hello to someone
    """
    return f"Hello {name}"

@mcp.tool()
async def add(a: int, b: int) -> int:
    """
    Add two numbers
    """
    return a + b

@mcp.tool()
async def get_time() -> str:
    """
    Get the current time
    """
    return time.strftime("%H:%M:%S")

@mcp.tool()
async def get_developer() -> str:
    """
    Get the developer of the tool
    """
    return "@Cc啊程开发的工具"

@mcp.tool()
async def get_realtime_weather(city_name: str) -> dict:
    """
    获取实时天气数据
    :param city_name: 城市名，例如 "北京"、"上海"、"广州"
    """
    url = f"https://wttr.in/{city_name}?format=j1"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        weather = data["current_condition"][0]
        temp = weather["temp_C"]  # 气温(摄氏度)
        desc = weather["weatherDesc"][0]["value"]  # 天气描述
        wind = weather["windspeedKmph"]  # 风速(公里/小时)
        humidity = weather["humidity"]  # 湿度
        
        return {"result" : [f"📍 城市：{city_name}", f"🌡  实时温度：{temp} ℃", f"☁ 天气状况：{desc}", f"💨 风速：{wind} km/h", f"💧 湿度：{humidity} %"]}
        
    except Exception as e:
        print(f"获取天气失败：{e}")




if __name__ == "__main__":
    mcp.run( transport="sse", host="0.0.0.0", port=8000)