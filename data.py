import main
import datetime
import requests
import matplotlib.pyplot as plt


LINK = "https://api.covid19india.org/v3/data-all.json"
r = requests.get(LINK)
data = r.json()

# import json
# with open("case_data.json", "r") as file:
#     text = file.read()
# data = json.loads(text)

dates = list(data.keys())
data = [data[key]["TT"]["total"] for key in data.keys()]


confirmed = []
recovered = []
deceased = []

for d in data:
    confirmed.append(d.get("confirmed", 0))
    recovered.append(d.get("recovered", 0))
    deceased.append(d.get("deceased", 0))


c_p = [round(((r + d) / c * 100), 2)
       for r, d, c in zip(recovered, deceased, confirmed)]
a_p = [round(100 - c, 2) for c in c_p]


message = f"On: {dates[-1]}\nClosed%: {c_p[-1]}\nActive%: {a_p[-1]}"
print(message)


FILENAME = 'image.png'

dates = [d[5:] for d in dates]
plt.figure(figsize=(10, 6))
plt.plot(dates[-15:], c_p[-15:], "g-")
plt.plot(dates[-15:], a_p[-15:], "r-")
plt.grid()
plt.xlabel('Dates')
plt.ylabel('%age of total cases')
plt.title('Closed vs Active case %ages')
plt.savefig(FILENAME, bbox_inches='tight')


main.tweet(message, FILENAME)
