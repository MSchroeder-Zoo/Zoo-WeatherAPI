SELECT
            time,
            location,
            values__temperature as temp_f,
            values__humidity as humidity,
            values__wind_speed as wind_speed,
            values__weather_code as weather_code
        FROM weather.weather_data
        ORDER BY time DESC
        LIMIT 10;
