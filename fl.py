from pyflightdata import FlightData
import pandas as pd

api=FlightData()
# print(api.get_countries()[:5])

lst = api.get_history_by_flight_number('I52380')[-5:]
# print(api.get_history_by_flight_number('AI101')[-5:])

str1 = str(lst)
print(str1)
df = pd.DataFrame(eval(str1))
print(len(df.index))

# count = sum(len(v) for v in lst.itervalues())
# df = pd.DataFrame(str1)
# df.words.str.count("identification").sum()
# df = pd.DataFrame(lst, columns=['words'])
# print(df.words.str.count("identification").sum())