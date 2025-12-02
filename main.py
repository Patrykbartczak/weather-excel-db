from services.openweather_api import fetch_weather
from services.excel_files import save_to_excel, read_excel_file
from config import Config
# from services.dashboard import line_chart
from services.dashboard import create_plots
import time

while True:
    weather = fetch_weather()
    save_to_excel(weather)
    # weather_data = read_excel_file(Config.XLSX_PATH)
    weather_data = read_excel_file('./services/pogoda_rozszerzona.xlsx')
    create_plots(weather_data)
    # line_chart(weather_data)
    print('Pobrałem dane!')

    time.sleep(10000)
