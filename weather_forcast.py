from datetime import datetime
import requests
import json

WEATHER_API_URL = "https://wttr.in/{}"

def log_process(message):
    """This function logs the message a give stage of the code execution to a log file. 
    Function returns nothing.
    """
    # Year-MonthName-Day-Hour:Minitue:Second
    timestamp_format = '%Y-%h-%d %H:%M:%S'
    # Get current timestamp
    now = datetime.now()
    # Format the timestamp
    timestamp = now.strftime(timestamp_format)

    # Write the log message to a file
    with open("code_log.txt", "a") as f:
        f.write(f"{timestamp}: {message}"+"\n")

# Extract
def get_weather_report(city):
    """This purpose of the function is to extract the weather report from the website and save it as a dataframe
    The function returns the dataframe for further processing."""
    url = WEATHER_API_URL.format(city)
    try: 
        data = requests.get(url)
    except:
        return f'The weather forcast for {city} is not availabel.'
    return data.text

# Transform
def transform(weather_report):
    """This function access the data and add ... and ..."""
    # data = json.dumps(weather_report)
    data = weather_report
    return data

# Load
def load_to_text(data, output_path):
    """This function saves the final data as a '' file in the provided path.
    Function returns nothing"""
    with open(f"{output_path}/weather_report.txt","w") as f:
        f.write(data)
    return None


if __name__ == "__main__":
    log_process("Extract")
    weather_report = get_weather_report("berlin")
    log_process("Transform")
    transformed_weather_report = transform(weather_report)
    log_process("Load")
    load_to_text(transformed_weather_report,".")


# Shell Scripting Version see file weather_report.sh
