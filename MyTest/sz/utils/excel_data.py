import math
from sz.internal.model.account_model import city_id


def return_address(address):
    value = {"name": address, "search_key": f"{address},"}
    value = str(value).replace("'", '"')
    return value


def return_city(province, city, district, index_city):
    city1 = city_id.get(province[index_city], {}).get("id", {})
    city2 = city_id.get(province[index_city], {}).get("city", {}).get(city[index_city], {}).get("id", {})
    city3 = city_id.get(province[index_city], {}).get("city", {}).get(city[index_city], {}).get("city", {}).get(
        district[index_city], {})
    ids = [x for x in [city1, city2, city3] if x]
    names_list = [province[index_city], city[index_city], district[index_city]]
    names = []
    for x in names_list:
        if judge_nan(x):
            continue
        names.append(x)
    if not ids:
        return None
    res = {
        "ids": ids,
        "code": ids[-1],
        "names": names,
        "search_key": "".join(names),
    }
    return str(res).replace("'", '"')

def return_province(province, index_city):
    p = province[index_city]
    if isinstance(p, str):
        for key in city_id.keys():
            if p in key:
                id = city_id.get(key, {}).get("id", {})
                res = {
                    "ids": [id],
                    "code": id,
                    "names": [key],
                    "search_key": key,
                }
                return str(res).replace("'", '"')
    return None

def judge_nan(value):
    try:
        if math.isnan(value):
            return True
    except:
        ...
    return False


def judge_data_list(value):
    if "[" in str(value) and "]" in str(value):
        value = str(value).replace("[", "").replace("]", "").replace("'", "").replace('"', "").split(",")
        if value and value[0]:
            return value
        else:
            return []
    else:
        return value
