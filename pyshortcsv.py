import pandas as pd
import requests
import pyshorteners

df = pd.read_csv("/Users/anushree/PycharmProjects/Algorithms/Implementing-Restoring-Division-Algorithm-for-Computer-Architecture-Project/url_links.csv")
data = []
tiny = pyshorteners.Shortener()
for index, row in df.iterrows():
    url = row['Website']

    s_url = tiny.tinyurl.short(url)
    row['shorten_url'] = s_url
    data.append(row)


df1 = pd.DataFrame(data)
df1.to_csv("/Users/anushree/PycharmProjects/Algorithms/Implementing-Restoring-Division-Algorithm-for-Computer-Architecture-Project/url_links_processed.csv")