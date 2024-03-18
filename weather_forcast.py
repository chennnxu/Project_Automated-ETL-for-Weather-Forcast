from datetime import datetime

def log_process(message):
    """This function logs the message a give stage of the code execution to a log file. 
    Function returns nothing.
    """
    # Year-MonthName-Day-Hour:Minitue:Second
    timestamp_format = '%Y-%h-%d %H:%M:%S'
    # Get current timestamp
    now = datetime.now()
    # Format the timestamp
    timestamp =  now.strftime(timestamp_format)

    # Write the log message to a file
    with open("code_log.txt", "a") as f:
        f.write(f"{timestamp}: {message}"+"\n")

if __name__ == "__main__":
    log_process("test test")