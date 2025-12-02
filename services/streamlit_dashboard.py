import pandas as pd
import matplotlib.pyplot as plt
import random
import plotly.express as px

df = pd.read_excel('pogoda_rozszerzona.xlsx')
df['timestamp_dt'] = pd.to_datetime(df['timestamp'],
    format="%H:%M:%S %d-%m-%Y"
)

            # sorotwanie po time stamp
df = df.sort_values('timestamp_dt')
# print(df)

                    # PLOTLY

        # WYKRES KOŁOWY

# fig = px.pie(
#     df, #określenie z jakiego zasobu bedzie korzystac
#     names = 'description',
#     title = '% usage of weather'
#
# )
# fig.show()

        # WYKRES SŁUPKOWY

# fig = px.bar(
#     df,
#     'place',
#     title='% usage of weather'
# )
# fig.update_layout(xaxis_title='City',
#                   yaxis_title= 'Ammount of record'
#
# )
# fig.show()
# # podstawowy wykres
# fig = px.bar(
#     data_frame=df,
#     x="place",
#     title="Liczba obserwacji w miastach",
#     color="place",  # różne kolory dla miast
#     color_discrete_sequence=["#FF6B6B", "#4ECDC4", "#1A535C", "#FFBE0B", "#8338EC"]
# )
#
# # styl słupków
# fig.update_traces(
#     marker=dict(
#         line=dict(width=2, color="black"),  # obramowanie
#         opacity=0.9
#     ),
#     texttemplate='%{y}',        # wyświetlanie wartości nad słupkami
#     textposition='outside'
# )
#
# # styl layoutu
# fig.update_layout(
#     xaxis_title="Miasto",
#     yaxis_title="Liczba rekordów",
#     template="simple_white",     # jasny elegancki motyw
#     font=dict(
#         family="Arial",
#         size=14,
#         color="black"
#     ),
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     margin=dict(l=40, r=40, t=60, b=40)
# )
#
# # styl osi
# fig.update_xaxes(
#     tickangle=45,
#     showgrid=True,
#     gridcolor="#E0E0E0"
# )
#
# fig.update_yaxes(
#     showgrid=True,
#     gridcolor="#E0E0E0",
#     rangemode="tozero"
# )
#
# fig.show()

        #Wykres punktowy scatter

# fig = px.scatter(
#     df,
#     x= 'temp',
#     y= 'humidity',
#     title= 'Temp. vs humidity',
#     labels={'temp':'Temp. C', 'humidity': 'Humidity %'}
# )
# fig.show()

        # WYkres liniowy
city = 'Toronto'
sub = df[ df['place'] == city].sort_values('timestamp_dt')
fig = px.line(
    sub,
    x='timestamp_dt',
    y='temp',

)

fig.show()












                    # MATPLOT LIB
            # wykres punktowy temp vs temp

# plt.figure()
# plt.scatter(df['temp'],df['humidity'])
# plt.title('Temp. vs humidity')
# plt.xlabel('Temp in C.')
# plt.ylabel('humidity in %.')
# plt.xlim(-30,50)
# plt.ylim(0,100)
# plt.grid()
# plt.show()

            #Histogram rozkładu temperatur
# plt.figure()
# # wyciąganie wartości y, x i informacji o słupkach
# y_values, x_values, patches = plt.hist(df['temp'])
# plt.xlabel("Temperatura")
# plt.ylabel("Liczba obserwacji")
# plt.title("Rozkład temperatur")
# plt.ylim(0, 20)
#
# print(y_values, x_values, patches)
# for p in patches:
#     p.set_facecolor((random.random(), random.random(), random.random()))
# plt.show()

            #Wykres pudełkowy - temperatury wg. miasta
top_cities = df['place'].value_counts().head().index
#wybrór wierszy, któ®e maja jedno z 5 miast w wartosciach place
subset = df[df['place'].isin(top_cities)]
#wypis wszystkich wierszy (:) i tylko kolumny placew
# print(subset.loc[:,['place']])

data_for_box = [subset[subset['place'] == city]['temp'] for city in top_cities]

# plt.figure()
# plt.boxplot(data_for_box,labels=top_cities)
# plt.show()

            #Temperatura i temp. odczuwalna w czasie dla jednego miasta
city = 'Oslo'
city_df = df[df['place'] == city]

# plt.figure()
# plt.plot(city_df['timestamp_dt'],city_df['temp'], label= 'Temperatura')
# plt.plot(city_df['timestamp_dt'], city_df['temp_feels_like'], label='Feels like')
# plt.legend()
# plt.title(f'Temperatura w czasie - {city}')
# plt.show()


            #Średnia temperatura w miastach - wykres słupkowy
# mean_temp = df.groupby('place')['temp'].mean().sort_values()
# plt.figure()
# plt.bar(mean_temp.index, mean_temp.values)
# plt.ylim(-5,30)
# plt.show()

#utwórz wykres slupkowy gdzie pokazes srednia wilgoptnosc w miastach
# mean_humidity = df.groupby('place')['humidity'].mean().sort_values(ascending=False)
# plt.figure()
# plt.bar(mean_humidity.index, mean_humidity.values)
# plt.ylabel('value in %')
# plt.show()

    #utwórz wykres liniowy, gdzie pokazuejsz predkosc wiatru w miescie na przestrzeni czasu
# plt.figure()
# plt.plot(city_df['timestamp_dt'], city_df['wind'])
# plt.title('Wind speed in Oslo')
# plt.ylabel('Speed in m/s')
# plt.xlabel('Data')
# plt.grid()
# plt.show()


    #Zadanie 1
    # Narysuj wykres kołowy, który pokazuje udział procentowy typów pogody. Dodaj etykiety z wartościami procentowymi.
desc_weather = df.value_counts('description')

# print(desc_weather)
# plt.pie(desc_weather, autopct='%1.1f%%')
# plt.title('% type of weather')
# plt.legend(desc_weather.index, title='Weather type', bbox_to_anchor=(1.05, 0.5), loc='center left')
# plt.show()
    #Zadanie 2
    # Wykres słupkowy: liczba obserwacji dla każdego miasta Policz, ile rekordów pochodzi z każdego miasta (place).
# Narysuj wykres słupkowy, który pokazuje liczbę obserwacji dla poszczególnych miast. Dodaj etykiety nad słupkami (opcjonalnie).
#
# city_count = df.value_counts('place')
# plt.bar(city_count, height='dzem')
# plt.title('Count by city')


