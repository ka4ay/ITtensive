'''Изучите данные по динамике изменения величины прожиточного минимума в городе Москве:
https://video.ittensive.com/math-stat/data-6048-2020-06-29.utf.csv

Проверьте, что значения AveragePerCapita не распределены нормально (через QQ-Plot или любым другим методом).

Проведите дисперсионный анализ для серий Seniors и Children и установите,
с каким p-уровнем значимости средние этих серий различаются.

Постройте регрессионную модель AveragePerCapita от Quarter, WorkingPopulation, Seniors и Children.
Выпишите коэффициенты линейной модели и сделайте предсказание на второй квартал 2020 года.'''


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

data = pd.read_csv("https://video.ittensive.com/math-stat/data-6048-2020-06-29.utf.csv", delimiter=';')
AveragePerCapita = data['AveragePerCapita']
Seniors = data['Seniors']
Children = data['Children']

st.probplot(AveragePerCapita, dist='norm', plot=plt)
plt.show()

stats = st.f_oneway(Seniors, Children) # дисперсионный анализ для серий Seniors и Children

print(stats, '\n Cредние серий Seniors и Children различаются с p-уровнем значимости ', round(stats[1], 5))

