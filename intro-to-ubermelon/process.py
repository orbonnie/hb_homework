log_file = open("um-server-01.txt")


def generate_sales_reports(log_file):
    """Print sales info for Monday."""

    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


generate_sales_reports(log_file)
