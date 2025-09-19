import random
import datetime
import pandas as pd

def generate_esg_metrics(days=30):
    data = []
    base_energy = 120  # kWh/ton
    base_co2 = 0.85    # kg/ton
    base_faults = 3    # faults/day

    for i in range(days):
        date = datetime.date.today() - datetime.timedelta(days=i)
        energy = round(base_energy - random.uniform(0, 10), 2)
        co2 = round(base_co2 - random.uniform(0, 0.1), 3)
        faults = max(0, int(base_faults + random.choice([-1, 0, 1])))

        data.append({
            "date": date,
            "energy_kwh_per_ton": energy,
            "co2_kg_per_ton": co2,
            "faults": faults
        })

    df = pd.DataFrame(data)
    df.sort_values("date", inplace=True)
    return df

if __name__ == "__main__":
    df = generate_esg_metrics()
    print(df.tail())
    df.to_csv("synthetic_esg_metrics.csv", index=False)