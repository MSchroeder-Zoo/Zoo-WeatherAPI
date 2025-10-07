import duckdb
import pandas as pd

def query_weather():
    con = duckdb.connect('tomorrow_zoo_weather.duckdb')

    print("=" * 70)
    print("Latest Weather Data")
    print("=" * 70)

    df = con.execute("""
        SELECT
            time,
            location,
            values__temperature as temp_f,
            values__humidity as humidity,
            values__wind_speed as wind_speed,
            values__weather_code as weather_code
        FROM weather.weather_data
        ORDER BY time DESC
        LIMIT 10
    """).fetchdf()

    print(df.to_string())

    print("\n" + "=" * 70)
    print("Summary Stats")
    print("=" * 70)
'''
    summary = con.execute("""
        SELECT
            COUNT(*) as record_count,
            MIN(values__temperature) as min_temp,
            MAX(values__temperature) as max_temp,
            AVG(values__temperature) as avg_temp,
            min(time) as earliest_record,
            max(time) as latest_record
        FROM weather.weather_realtime
    """).fetchdf()

    print(summary.to_string())

    con.close()
'''
if __name__ == "__main__":
    query_weather()
    