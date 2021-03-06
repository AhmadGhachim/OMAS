def duration(start_time, end_time):
    """
    Calculates duration in minutes, between start and end time
    :param start_time: string (ex. 16:29:21)
    :param end_time: string (ex. 16:29:21)
    :return: integer
    """
    h = int(end_time[:2]) - int(start_time[:2])
    m = int(end_time[3:5]) - int(start_time[3:5])
    s = 0
    if int(end_time[6:]) - int(start_time[6:]) > 30:
        s = 1
    return h * 60 + m + s


def timestamp_from_duration(start_time, dur):
    """
    Calculates the timestamp after a given time duration from the given timestamp
    :param start_time: string (ex. 16:29:21)
    :param dur: integer (minutes)
    :return: string (ex. 16:29:21)
    """
    h = str(int(start_time[0:2]) + dur // 60)
    return ("0" + h + ":" + str(int(start_time[3:5]) + dur % 60) + start_time[5:])[-8:]


def total_duration(list_of_timestamps):
    """
    Calculates the total duration using multiple timestamps
    :param list_of_timestamps: list of strings
    :return: integer (minutes)
    """
    time_duration = 0
    for x in range(0, len(list_of_timestamps), 2):
        time_duration += duration(list_of_timestamps[x], list_of_timestamps[x + 1])
    return time_duration

def am_pm_to_24_hours(timestamp):
    """
    Convert a timestamp from 12-hour format to 24-hour format.
    :param timestamp: a string representing a timestamp (containing AM or PM) (Ex. 02:30:45 PM)
    :return: a string representing 24-hour timestamp (Ex. 14:30:45)
    """
    timestamp = timestamp.split(' ')
    if timestamp[1] == 'AM':
        return timestamp[0]
    timestamp = timestamp[0].split(":")
    if timestamp[0] == "12":
        timestamp[0] = "00"
    else:
        timestamp[0] = str(int(timestamp[0])+12)
    return ":".join(timestamp)

if __name__ == '__main__':
    print(am_pm_to_24_hours("12:30:45 PM"))
    print(am_pm_to_24_hours("10:12:21 AM"))
    print(am_pm_to_24_hours("08:34:56 PM"))