pop = 16218
import json
file = 'FEMA_east_midtown_buildings_with_address_zip_city_state.json'
f = open(file)
data = json.load(f)
pop_dict = {}
k = 0
for i in data['features']:
    #print (i["properties"]["PROP_ADDR"])
    if (i["properties"]["HEIGHT"] is not None and i["properties"]["SQMETERS"] is not None):
        pop_dict[i["properties"]["BUILD_ID"]] = float(i["properties"]["HEIGHT"]) / 3.0 * float(i["properties"]["SQMETERS"])
        k += float(i["properties"]["HEIGHT"]) / 3.0 * float(i["properties"]["SQMETERS"])

for (b,p) in pop_dict.items():
    pop_dict[b] = (pop/k) * p
f.close()
print(pop_dict)
