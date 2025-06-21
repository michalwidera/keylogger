import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

# Dane wejściowe
digraf_operatora_e = [{'digraph': 'lo', 'interval': 219.13}, {'digraph': 'or', 'interval': 388.98}, {'digraph': 're', 'interval': 213.01}, {'digraph': 'em', 'interval': 298.95}, {'digraph': 'ip', 'interval': 450.0}, {'digraph': 'ps', 'interval': 642.83}, {'digraph': 'su', 'interval': 247.02}, {'digraph': 'um', 'interval': 1095.22}, {'digraph': 'do', 'interval': 326.15}, {'digraph': 'ol', 'interval': 705.93}, {'digraph': 'lo', 'interval': 189.0}, {'digraph': 'or', 'interval': 414.31}, {'digraph': 'si', 'interval': 765.03}, {'digraph': 'it', 'interval': 339.81}, {'digraph': 'am', 'interval': 353.05}, {'digraph': 'me', 'interval': 286.34}, {'digraph': 'et', 'interval': 242.61}, {'digraph': 'co', 'interval': 248.41}, {'digraph': 'on', 'interval': 443.59}, {'digraph': 'ns', 'interval': 440.09}, {'digraph': 'se', 'interval': 346.37}, {'digraph': 'ec', 'interval': 1815.79}, {'digraph': 'ct', 'interval': 370.86}, {'digraph': 'te', 'interval': 1321.97}, {'digraph': 'et', 'interval': 1070.07}, {'digraph': 'tu', 'interval': 347.37}, {'digraph': 'ur', 'interval': 674.96}, {'digraph': 'ad', 'interval': 295.02}, {'digraph': 'di', 'interval': 324.83}, {'digraph': 'ip', 'interval': 1327.21}, {'digraph': 'pi', 'interval': 1890.08}, {'digraph': 'is', 'interval': 490.6}, {'digraph': 'sc', 'interval': 1378.99}, {'digraph': 'ci', 'interval': 246.14}, {'digraph': 'in', 'interval': 1892.37}, {'digraph': 'ng', 'interval': 263.65}, {'digraph': 'el', 'interval': 352.3}, {'digraph': 'li', 'interval': 289.83}, {'digraph': 'it', 'interval': 263.3}, {'digraph': 'se', 'interval': 216.72}, {'digraph': 'ed', 'interval': 240.03}, {'digraph': 'do', 'interval': 197.4}, {'digraph': 'ei', 'interval': 351.28}, {'digraph': 'iu', 'interval': 1969.77}, {'digraph': 'us', 'interval': 1913.12}, {'digraph': 'sm', 'interval': 377.36}, {'digraph': 'mo', 'interval': 242.58}, {'digraph': 'od', 'interval': 361.03}, {'digraph': 'te', 'interval': 211.77}, {'digraph': 'em', 'interval': 299.16}, {'digraph': 'mo', 'interval': 267.73}, {'digraph': 'op', 'interval': 1334.06}, {'digraph': 'po', 'interval': 214.22}, {'digraph': 'or', 'interval': 259.14}, {'digraph': 'ci', 'interval': 400.97}, {'digraph': 'id', 'interval': 1706.32}, {'digraph': 'di', 'interval': 273.08}, {'digraph': 'id', 'interval': 1421.77}, {'digraph': 'du', 'interval': 425.93}, {'digraph': 'un', 'interval': 1558.08}, {'digraph': 'nt', 'interval': 366.88}, {'digraph': 'ut', 'interval': 522.06}, {'digraph': 'la', 'interval': 281.71}, {'digraph': 'ab', 'interval': 531.29}, {'digraph': 'bo', 'interval': 245.03}, {'digraph': 'or', 'interval': 1241.18}, {'digraph': 're', 'interval': 316.58}, {'digraph': 'et', 'interval': 166.54}, {'digraph': 'do', 'interval': 249.0}, {'digraph': 'ol', 'interval': 240.37}, {'digraph': 'lo', 'interval': 188.46}, {'digraph': 'or', 'interval': 440.33}, {'digraph': 're', 'interval': 212.55}, {'digraph': 'ma', 'interval': 206.01}, {'digraph': 'ag', 'interval': 349.35}, {'digraph': 'gn', 'interval': 448.74}, {'digraph': 'na', 'interval': 207.07}, {'digraph': 'al', 'interval': 226.38}, {'digraph': 'li', 'interval': 212.82}, {'digraph': 'iq', 'interval': 411.91}, {'digraph': 'qu', 'interval': 377.92}, {'digraph': 'ua', 'interval': 282.95}]
digraf_operatora_m = [{'digraph': 'lo', 'interval': 193.0}, {'digraph': 'or', 'interval': 285.0}, {'digraph': 're', 'interval': 265.97}, {'digraph': 'em', 'interval': 686.04}, {'digraph': 'ip', 'interval': 216.99}, {'digraph': 'ps', 'interval': 204.13}, {'digraph': 'su', 'interval': 220.82}, {'digraph': 'um', 'interval': 268.05}, {'digraph': 'do', 'interval': 171.01}, {'digraph': 'ol', 'interval': 214.97}, {'digraph': 'lo', 'interval': 163.32}, {'digraph': 'or', 'interval': 233.69}, {'digraph': 'si', 'interval': 146.12}, {'digraph': 'it', 'interval': 236.33}, {'digraph': 'am', 'interval': 250.83}, {'digraph': 'me', 'interval': 155.96}, {'digraph': 'et', 'interval': 398.55}, {'digraph': 'co', 'interval': 117.43}, {'digraph': 'on', 'interval': 264.65}, {'digraph': 'ns', 'interval': 232.3}, {'digraph': 'se', 'interval': 242.06}, {'digraph': 'ec', 'interval': 241.92}, {'digraph': 'ct', 'interval': 345.08}, {'digraph': 'te', 'interval': 547.98}, {'digraph': 'et', 'interval': 269.01}, {'digraph': 'tu', 'interval': 321.03}, {'digraph': 'ur', 'interval': 262.1}, {'digraph': 'ad', 'interval': 475.03}, {'digraph': 'di', 'interval': 325.01}, {'digraph': 'ip', 'interval': 399.0}, {'digraph': 'pi', 'interval': 315.1}, {'digraph': 'is', 'interval': 284.29}, {'digraph': 'sc', 'interval': 268.84}, {'digraph': 'ci', 'interval': 219.85}, {'digraph': 'in', 'interval': 239.29}, {'digraph': 'ng', 'interval': 340.95}, {'digraph': 'el', 'interval': 171.16}, {'digraph': 'li', 'interval': 264.89}, {'digraph': 'it', 'interval': 340.02}, {'digraph': 'se', 'interval': 190.02}, {'digraph': 'ed', 'interval': 241.02}, {'digraph': 'do', 'interval': 146.07}, {'digraph': 'ei', 'interval': 713.06}, {'digraph': 'iu', 'interval': 264.87}, {'digraph': 'us', 'interval': 260.15}, {'digraph': 'sm', 'interval': 350.98}, {'digraph': 'mo', 'interval': 165.0}, {'digraph': 'od', 'interval': 180.97}, {'digraph': 'te', 'interval': 212.1}, {'digraph': 'em', 'interval': 91.98}, {'digraph': 'mp', 'interval': 217.01}, {'digraph': 'po', 'interval': 188.02}, {'digraph': 'or', 'interval': 75.24}, {'digraph': 'rt', 'interval': 167.71}, {'digraph': 'in', 'interval': 315.99}, {'digraph': 'nc', 'interval': 289.0}, {'digraph': 'ci', 'interval': 194.0}, {'digraph': 'id', 'interval': 310.97}, {'digraph': 'dd', 'interval': 912.06}, {'digraph': 'du', 'interval': 143.01}, {'digraph': 'un', 'interval': 292.02}, {'digraph': 'nt', 'interval': 135.0}, {'digraph': 'ut', 'interval': 134.98}, {'digraph': 'la', 'interval': 125.96}, {'digraph': 'ab', 'interval': 247.0}, {'digraph': 'bo', 'interval': 60.07}, {'digraph': 'or', 'interval': 185.95}, {'digraph': 're', 'interval': 105.97}, {'digraph': 'at', 'interval': 606.91}, {'digraph': 'do', 'interval': 89.92}, {'digraph': 'ol', 'interval': 167.31}, {'digraph': 'lo', 'interval': 162.79}, {'digraph': 'or', 'interval': 49.02}, {'digraph': 're', 'interval': 135.95}, {'digraph': 'ma', 'interval': 282.69}, {'digraph': 'ag', 'interval': 322.96}, {'digraph': 'gn', 'interval': 115.37}, {'digraph': 'na', 'interval': 128.72}, {'digraph': 'al', 'interval': 148.97}, {'digraph': 'li', 'interval': 161.01}, {'digraph': 'iq', 'interval': 180.16}, {'digraph': 'qu', 'interval': 144.84}, {'digraph': 'ua', 'interval': 310.03}]
digraf_operatora_m2= [{'digraph': 'lo', 'interval': 425.22}, {'digraph': 'or', 'interval': 260.17}, {'digraph': 're', 'interval': 290.75}, {'digraph': 'em', 'interval': 402.31}, {'digraph': 'ip', 'interval': 217.99}, {'digraph': 'ps', 'interval': 228.81}, {'digraph': 'su', 'interval': 325.39}, {'digraph': 'um', 'interval': 319.65}, {'digraph': 'do', 'interval': 172.38}, {'digraph': 'ol', 'interval': 188.5}, {'digraph': 'lo', 'interval': 189.03}, {'digraph': 'or', 'interval': 207.28}, {'digraph': 'si', 'interval': 146.16}, {'digraph': 'it', 'interval': 390.85}, {'digraph': 'am', 'interval': 198.67}, {'digraph': 'me', 'interval': 181.95}, {'digraph': 'et', 'interval': 553.06}, {'digraph': 'co', 'interval': 194.51}, {'digraph': 'on', 'interval': 289.98}, {'digraph': 'ns', 'interval': 336.01}, {'digraph': 'se', 'interval': 320.0}, {'digraph': 'ec', 'interval': 319.03}, {'digraph': 'ct', 'interval': 449.15}, {'digraph': 'te', 'interval': 365.95}, {'digraph': 'et', 'interval': 373.4}, {'digraph': 'tu', 'interval': 294.52}, {'digraph': 'ur', 'interval': 184.03}, {'digraph': 'ad', 'interval': 500.93}, {'digraph': 'di', 'interval': 325.06}, {'digraph': 'ip', 'interval': 476.28}, {'digraph': 'pi', 'interval': 366.68}, {'digraph': 'is', 'interval': 283.94}, {'digraph': 'sc', 'interval': 294.99}, {'digraph': 'ci', 'interval': 168.42}, {'digraph': 'in', 'interval': 240.01}, {'digraph': 'ng', 'interval': 392.8}, {'digraph': 'el', 'interval': 172.03}, {'digraph': 'li', 'interval': 315.98}, {'digraph': 'it', 'interval': 494.98}, {'digraph': 'se', 'interval': 241.36}, {'digraph': 'ed', 'interval': 188.7}, {'digraph': 'do', 'interval': 196.85}, {'digraph': 'ei', 'interval': 1021.83}, {'digraph': 'iu', 'interval': 961.88}, {'digraph': 'us', 'interval': 285.05}, {'digraph': 'sm', 'interval': 352.0}, {'digraph': 'mo', 'interval': 345.29}, {'digraph': 'od', 'interval': 516.62}, {'digraph': 'te', 'interval': 159.96}, {'digraph': 'em', 'interval': 118.58}, {'digraph': 'mp', 'interval': 216.47}, {'digraph': 'po', 'interval': 106.05}, {'digraph': 'or', 'interval': 134.91}, {'digraph': 'rt', 'interval': 164.51}, {'digraph': 'in', 'interval': 239.7}, {'digraph': 'ni', 'interval': 577.45}, {'digraph': 'id', 'interval': 285.55}, {'digraph': 'di', 'interval': 299.06}, {'digraph': 'id', 'interval': 724.21}, {'digraph': 'dn', 'interval': 142.71}, {'digraph': 'nt', 'interval': 160.0}, {'digraph': 'ut', 'interval': 340.81}, {'digraph': 'la', 'interval': 384.06}, {'digraph': 'ab', 'interval': 272.87}, {'digraph': 'bo', 'interval': 141.81}, {'digraph': 'or', 'interval': 208.2}, {'digraph': 're', 'interval': 131.11}, {'digraph': 'et', 'interval': 269.21}, {'digraph': 'do', 'interval': 119.97}, {'digraph': 'ol', 'interval': 163.19}, {'digraph': 'lo', 'interval': 214.33}, {'digraph': 'or', 'interval': 130.52}, {'digraph': 're', 'interval': 131.07}, {'digraph': 'ma', 'interval': 178.94}, {'digraph': 'ag', 'interval': 478.45}, {'digraph': 'gn', 'interval': 114.71}, {'digraph': 'na', 'interval': 232.11}, {'digraph': 'al', 'interval': 122.15}, {'digraph': 'li', 'interval': 265.81}, {'digraph': 'iq', 'interval': 204.05}, {'digraph': 'qu', 'interval': 222.94}, {'digraph': 'ua', 'interval': 180.94}]

# Konwersja do DataFrame
df_e = pd.DataFrame(digraf_operatora_e).groupby("digraph").mean().rename(columns={"interval": "interval_e"})
df_m = pd.DataFrame(digraf_operatora_m2).groupby("digraph").mean().rename(columns={"interval": "interval_m"})
# df_m2= pd.DataFrame(digraf_operatora_m2).groupby("digraph").mean().rename(columns={"interval": "interval_m2"})

# Połączenie danych po digrafach
df_merged = df_e.join(df_m, how='inner')

# Obliczenie korelacji
correlation, p_value = pearsonr(df_merged["interval_e"], df_merged["interval_m"])

# Wizualizacja
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_merged, x="interval_e", y="interval_m")
plt.title(f'Porównanie czasów digrafów (korelacja = {correlation:.2f}, wartość p testu istotności = {p_value:.2f})')
plt.xlabel('Operator A - Średni czas digrafu (ms)')
plt.ylabel('Operator B - Średni czas digrafu (ms)')
plt.grid(True)
plt.tight_layout()

# df_merged_sorted = df_merged.sort_values(by="interval_e")

plt.savefig("test-di.svg", format='svg')

print(correlation)
if -0.1 <= correlation < 0.1:
    print('nieprawdopodobne aby te same osoby wprowadzały tekst')
elif 0.1 <= correlation < 0.4:
    print('mało prawdopodobne aby te same osoby wprowadzały tekst')
elif 0.4 <= correlation < 0.7:
    print('istnieje pewne prawdopodobieństwo że te same osoby wprowadzały tekst')
elif 0.7 <= correlation < 0.9:
    print('prawdopodobnie te same osoby wprowadzały tekst')
elif 0.9 <= correlation < 1:
    print('bardzo prawdopodobnie te same osoby wprowadzały tekst')
elif correlation == 1:
    print('to te same osoby')
else:
    print(correlation, " <- sprawdź.")

print(p_value)
if p_value < 0.05:
    print('korelacja istotna, mało prawdopodobne aby to był przypadek.')
else:
    print('korelacja może być przypadkowa.')

plt.show()



# correlation, p_value, df_merged_sorted.head(10)

#

'''
1. correlation (współczynnik korelacji Pearsona)
To wartość od -1 do 1, która mówi o sile i kierunku liniowej zależności między dwiema zmiennymi:

Wartość	Interpretacja
+1	idealna dodatnia korelacja liniowa
0	brak korelacji liniowej
-1	idealna ujemna korelacja liniowa
0.7 do 0.9	silna dodatnia korelacja
0.4 do 0.7	umiarkowana dodatnia korelacja
0.1 do 0.4	słaba dodatnia korelacja
blisko 0	bardzo słaba lub brak korelacji liniowej

2. p_value (wartość p dla testu istotności korelacji)
To wartość statystyczna, która mówi, czy zaobserwowana korelacja jest istotna statystycznie, czyli:

Mała wartość p (np. < 0.05) → korelacja jest istotna (mało prawdopodobne, że to przypadek).

Duża wartość p (np. > 0.05) → korelacja może być przypadkowa.

'''

