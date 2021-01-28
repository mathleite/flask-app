from datetime import timezone, datetime, timedelta


class Date:
    @staticmethod
    def get_current_datetime():
        brazil_utc_timezone = -3
        time_zone_diff = timedelta(hours=brazil_utc_timezone)
        correct_timezone = timezone(time_zone_diff)

        return datetime.now().astimezone(correct_timezone).strftime('%Y-%m-%d %H:%M:%S')
