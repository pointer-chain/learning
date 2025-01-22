lead_pool = {}

if __name__ == '__main__':
    for lead in lead_pool.get("result").get("data"):
        print(f"'{lead.get('name')}':'{lead.get('id')}',")
