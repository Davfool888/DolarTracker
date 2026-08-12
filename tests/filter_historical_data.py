import json
from datetime import datetime


INPUT_FILE = "data/raw/xbtusd_1m.json"
OUTPUT_FILE = "data/raw/xbtusd_1m_from_2014.json"

START_DATE = datetime(2014, 1, 1)


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp / 1000)


def filter_from_2014():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    print(f"Registros originales: {len(data):,}")

    filtered_data = []

    start_timestamp = int(
        START_DATE.timestamp() * 1000
    )

    for row in data:

        timestamp = row[0]

        if timestamp >= start_timestamp:
            filtered_data.append(row)

    print(
        f"Registros desde 2014: "
        f"{len(filtered_data):,}"
    )

    print(
        f"Primer registro: "
        f"{timestamp_to_datetime(filtered_data[0][0])}"
    )

    print(
        f"Último registro: "
        f"{timestamp_to_datetime(filtered_data[-1][0])}"
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            filtered_data,
            file,
            separators=(",", ":")
        )

    print()
    print(
        f"Archivo creado: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    filter_from_2014()