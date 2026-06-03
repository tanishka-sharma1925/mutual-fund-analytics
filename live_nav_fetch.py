import requests
import pandas as pd

scheme_codes = [
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

for code in scheme_codes:

    print("=" * 60)

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        fund_name = data["meta"]["scheme_name"]

        print(f"Downloading: {fund_name}")

        nav_df = pd.DataFrame(data["data"])

        filename = f"data/raw/nav_{code}.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Saved: {filename}")
        print(f"Rows: {len(nav_df)}")

    else:
        print(f"Failed for scheme {code}")