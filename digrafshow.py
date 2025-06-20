import pandas as pd
import numpy as np
import plotly.express as px
import string

# Dane wejściowe
keystrokes = [{'key': 'L', 'press_time': 1205.08, 'release_time': 1287.07}, {'key': 'shift', 'press_time': 983.24, 'release_time': 1331.06}, {'key': 'o', 'press_time': 1657.23, 'release_time': 1738.08}, {'key': 'r', 'press_time': 2097.1, 'release_time': 2179.06}, {'key': 'e', 'press_time': 2413.12, 'release_time': 2495.12}, {'key': 'm', 'press_time': 2790.22, 'release_time': 2871.06}, {'key': 'space', 'press_time': 2976.53, 'release_time': 3083.07}, {'key': 'i', 'press_time': 3529.11, 'release_time': 3585.1}, {'key': 'p', 'press_time': 3823.12, 'release_time': 3931.13}, {'key': 's', 'press_time': 4156.14, 'release_time': 4238.14}, {'key': 'u', 'press_time': 4507.13, 'release_time': 4614.14}, {'key': 'm', 'press_time': 4852.18, 'release_time': 4934.16}, {'key': 'space', 'press_time': 5038.13, 'release_time': 5120.17}, {'key': 'd', 'press_time': 5404.19, 'release_time': 5511.15}, {'key': 'o', 'press_time': 5677.16, 'release_time': 5759.2}, {'key': 'l', 'press_time': 5893.2, 'release_time': 5974.17}, {'key': 'o', 'press_time': 6107.19, 'release_time': 6189.17}, {'key': 'r', 'press_time': 6495.19, 'release_time': 6577.21}, {'key': 'space', 'press_time': 6713.2, 'release_time': 6794.21}, {'key': 's', 'press_time': 7051.21, 'release_time': 7133.22}, {'key': 'i', 'press_time': 7274.22, 'release_time': 7356.21}, {'key': 't', 'press_time': 7562.23, 'release_time': 7643.19}, {'key': 'space', 'press_time': 7778.45, 'release_time': 7885.24}, {'key': 'a', 'press_time': 8012.2, 'release_time': 8119.23}, {'key': 'm', 'press_time': 8313.29, 'release_time': 8421.21}, {'key': 'e', 'press_time': 8495.26, 'release_time': 8577.24}, {'key': 't', 'press_time': 9151.25, 'release_time': 9233.25}, {'key': ',', 'press_time': 10456.3, 'release_time': 10537.82}, {'key': 'space', 'press_time': 10769.29, 'release_time': 10851.28}, {'key': 'c', 'press_time': 11137.47, 'release_time': 11244.32}, {'key': 'o', 'press_time': 11410.44, 'release_time': 11491.34}, {'key': 'n', 'press_time': 11725.29, 'release_time': 11832.33}, {'key': 's', 'press_time': 11985.34, 'release_time': 12092.33}, {'key': 'e', 'press_time': 12226.43, 'release_time': 12308.35}, {'key': 'c', 'press_time': 12520.32, 'release_time': 12601.32}, {'key': 't', 'press_time': 12968.61, 'release_time': 13075.34}, {'key': 'e', 'press_time': 13283.36, 'release_time': 13390.48}, {'key': 't', 'press_time': 14146.39, 'release_time': 14279.36}, {'key': 'u', 'press_time': 14492.39, 'release_time': 14599.39}, {'key': 'r', 'press_time': 14909.4, 'release_time': 14965.44}, {'key': 'space', 'press_time': 15075.39, 'release_time': 15182.42}, {'key': 'a', 'press_time': 15463.5, 'release_time': 15570.44}, {'key': 'd', 'press_time': 15862.44, 'release_time': 15943.57}, {'key': 'i', 'press_time': 16547.44, 'release_time': 16706.45}, {'key': 'p', 'press_time': 17075.44, 'release_time': 17156.46}, {'key': 'i', 'press_time': 17725.46, 'release_time': 17858.64}, {'key': 's', 'press_time': 18241.51, 'release_time': 18349.5}, {'key': 'c', 'press_time': 18666.49, 'release_time': 18747.49}, {'key': 'i', 'press_time': 18963.51, 'release_time': 19045.49}, {'key': 'n', 'press_time': 19176.67, 'release_time': 19284.52}, {'key': 'g', 'press_time': 19543.67, 'release_time': 19651.98}, {'key': 'space', 'press_time': 19760.55, 'release_time': 19840.55}, {'key': 'e', 'press_time': 19970.51, 'release_time': 20077.67}, {'key': 'l', 'press_time': 20193.56, 'release_time': 20275.55}, {'key': 'i', 'press_time': 20715.58, 'release_time': 20849.61}, {'key': 't', 'press_time': 21004.54, 'release_time': 21111.56}, {'key': ',', 'press_time': 21301.73, 'release_time': 21408.56}, {'key': 'space', 'press_time': 21486.57, 'release_time': 21593.58}, {'key': 's', 'press_time': 21876.64, 'release_time': 21957.6}, {'key': 'e', 'press_time': 22092.6, 'release_time': 22147.67}, {'key': 'd', 'press_time': 22306.61, 'release_time': 22388.59}, {'key': 'space', 'press_time': 22499.72, 'release_time': 22607.62}, {'key': 'd', 'press_time': 22735.61, 'release_time': 22843.6}, {'key': 'o', 'press_time': 22881.58, 'release_time': 23014.7}, {'key': 'space', 'press_time': 23040.73, 'release_time': 23147.74}, {'key': 'e', 'press_time': 23638.63, 'release_time': 23771.66}, {'key': 'i', 'press_time': 24014.65, 'release_time': 24121.66}, {'key': 'v', 'press_time': 24458.06, 'release_time': 24590.65}, {'key': 's', 'press_time': 25520.7, 'release_time': 25627.67}, {'key': 'm', 'press_time': 25974.69, 'release_time': 26056.72}, {'key': 'o', 'press_time': 26190.68, 'release_time': 26272.69}, {'key': 'd', 'press_time': 26449.69, 'release_time': 26556.75}, {'key': 'space', 'press_time': 26800.05, 'release_time': 26903.72}, {'key': 't', 'press_time': 27061.84, 'release_time': 27168.68}, {'key': 'e', 'press_time': 27273.71, 'release_time': 27380.84}, {'key': 'm', 'press_time': 27494.78, 'release_time': 27576.76}, {'key': 'p', 'press_time': 27918.75, 'release_time': 28025.83}, {'key': 'o', 'press_time': 28157.77, 'release_time': 28290.76}, {'key': 'r', 'press_time': 28365.74, 'release_time': 28446.76}, {'key': 't', 'press_time': 28606.77, 'release_time': 28714.77}, {'key': 'i', 'press_time': 29444.82, 'release_time': 29552.79}, {'key': 'n', 'press_time': 29864.82, 'release_time': 29945.78}, {'key': 'c', 'press_time': 30306.8, 'release_time': 30414.8}, {'key': 'i', 'press_time': 30733.85, 'release_time': 30815.98}, {'key': 'd', 'press_time': 31096.89, 'release_time': 31229.96}, {'key': 'i', 'press_time': 31343.87, 'release_time': 31476.87}, {'key': 'd', 'press_time': 31964.84, 'release_time': 32097.85}, {'key': 'u', 'press_time': 32365.86, 'release_time': 32446.86}, {'key': 'n', 'press_time': 32656.86, 'release_time': 32738.89}, {'key': 't', 'press_time': 32920.85, 'release_time': 33028.87}, {'key': 'space', 'press_time': 33085.88, 'release_time': 33166.86}, {'key': 'u', 'press_time': 33379.18, 'release_time': 33485.87}, {'key': 't', 'press_time': 33590.87, 'release_time': 33697.88}, {'key': 'space', 'press_time': 33781.03, 'release_time': 33862.29}, {'key': 'l', 'press_time': 34050.93, 'release_time': 34157.87}, {'key': 'a', 'press_time': 34177.06, 'release_time': 34258.89}, {'key': 'b', 'press_time': 34449.9, 'release_time': 34531.91}, {'key': 'o', 'press_time': 34617.9, 'release_time': 34724.89}, {'key': 'r', 'press_time': 34876.93, 'release_time': 34984.93}, {'key': 'e', 'press_time': 35244.91, 'release_time': 35352.93}, {'key': 'space', 'press_time': 35515.94, 'release_time': 35596.95}, {'key': 'e', 'press_time': 35751.97, 'release_time': 35832.94}, {'key': 't', 'press_time': 35994.94, 'release_time': 36102.16}, {'key': 'space', 'press_time': 36210.95, 'release_time': 36291.95}, {'key': 'd', 'press_time': 36499.01, 'release_time': 36605.99}, {'key': 'o', 'press_time': 36618.05, 'release_time': 36700.05}, {'key': 'l', 'press_time': 36806.96, 'release_time': 36888.97}, {'key': 'o', 'press_time': 37022.07, 'release_time': 37102.96}, {'key': 'r', 'press_time': 37229.99, 'release_time': 37389.0}, {'key': 'e', 'press_time': 37519.97, 'release_time': 37602.17}, {'key': 'space', 'press_time': 37739.01, 'release_time': 37821.09}, {'key': 'm', 'press_time': 38033.99, 'release_time': 38141.18}, {'key': 'a', 'press_time': 38239.04, 'release_time': 38321.02}, {'key': 'g', 'press_time': 39027.04, 'release_time': 39109.01}, {'key': 'n', 'press_time': 39270.05, 'release_time': 39352.14}, {'key': 'a', 'press_time': 39451.03, 'release_time': 39558.06}, {'key': 'space', 'press_time': 39595.03, 'release_time': 39676.03}, {'key': 'a', 'press_time': 39828.05, 'release_time': 39910.06}, {'key': 'l', 'press_time': 40028.03, 'release_time': 40110.07}, {'key': 'i', 'press_time': 40319.03, 'release_time': 40426.33}, {'key': 'q', 'press_time': 40576.04, 'release_time': 40658.17}, {'key': 'u', 'press_time': 40851.05, 'release_time': 40932.06}, {'key': 'a', 'press_time': 41212.12, 'release_time': 41345.25}]


# Filtrowanie klawiszy nieistotnych do analizy digrafów
filtered_keystrokes = [k for k in keystrokes if k['key'] not in ['.','shift','alt', '@' , '#', ',' , '(', ')' , '&' , '%', 'alt gr', 'backspace' , 'enter', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' , '$', '^', '-', ';', '!' , '/', '−' , 'caps lock']]

# Tworzenie digrafów i obliczanie czasu między naciśnięciami
digraphs = []
x_dig = []
y_dig = []
interval = []
hold_a = []
hold_b = []
for i in range(len(filtered_keystrokes) - 1):
    first = filtered_keystrokes[i]
    second = filtered_keystrokes[i + 1]
    if first['key'] == 'space' or second['key'] == 'space':
        continue

    first['key'] = first['key'].lower()
    second['key'] = second['key'].lower()

    digraph = f"{first['key']}{second['key']}"

    press_interval = round( second['press_time'] - first['press_time'] , 2)
    hold_first = round(first['release_time'] - first['press_time'],2)
    hold_second =  round(second['release_time'] - second['press_time'],2)

    digraphs.append({'digraph': digraph, 'interval': press_interval, 'hold_a': hold_first, 'hold_b': hold_second})

    x_dig.append(first['key'])
    y_dig.append(second['key'])
    interval.append(press_interval)
    hold_a.append(hold_first)
    hold_b.append(hold_first)

for k in digraphs:
    print(k)




# Przygotowanie danych
letters = list(string.ascii_lowercase[:26])  # 'a' do 'j'

df = pd.DataFrame({'X': x_dig, 'Y': y_dig, 'interval': interval, 'hold_a': hold_a, 'hold_b': hold_b})
print(df)

# odcięcie 4-go kwantyla
iqr_mask = df["interval"].between(0, df["interval"].quantile(4/5))
subset = df[iqr_mask]
print(subset)

# Tworzenie wykresu
# fig = px.scatter(df, x='X', y='Y', size = 'interval', title='Scatterplot z uporządkowanymi literami')
# https://www.reddit.com/r/learnpython/comments/rbbtqs/help_with_removing_outliers_from_variables_on/?tl=pl
fig = px.scatter(subset, x='X', y='Y', size = 'interval', title='Digraf rejestracji danych z keyloggera')

# Ustawienie porządku kategorii (rosnąco)
fig.update_layout(
    xaxis=dict(
        title='Pierwsza litera digrafu',
        type='category',
        categoryorder='array',
        categoryarray=letters  # określa kolejność liter
    ),
    yaxis=dict(
        title='Druga litera digrafu',
        type='category',
        categoryorder='array',
        categoryarray=letters
    )
)

# fig.write_image("C:/Users/michal.GM7ZG7P/Desktop/fig1.svg")
fig.show()
