class CovidRecord:
    """
    A simple class to hold record data from NYT database
    """

    def __init__(self, _date='', _county='', _state='', _fips=0, _cases=0, _death=0):
        """
        Default constructor for transforming each line of the file into data point

        :param _date: Date covid case was recorded
        :param _county: County in which data was recorded
        :param _state: State in which data was recorded
        :param _fips: Federal Information Processing Standards code
        :param _cases: Number of total cases recorded
        :param _death: Number of total deaths recorded
        """
        self.date = _date
        self.county = _county
        self.state = _state

        if _fips == '':
            self.fips = 0
        else:
            self.fips = int(_fips)
        self.cases = int(_cases)

        if _death == '':
            self.death = 0
        else:
            self.death = int(_death)


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of points
    :param file_path: Path to data file
    :return: List of CovidRecord points
    """
    # data point list
    covid_data = list()

    # open the NYT file path
    fin = open(file_path)

    # get rid of the headers
    fin.readline()

    done = False

    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        elements = line.strip().split(",")

        new_point = CovidRecord((elements[0]), (elements[1]), (elements[2]),
                                (elements[3]), (elements[4]), (elements[5]))

        # to reduce file sizes, only grab Virginia points
        if new_point.state == 'Virginia':
            covid_data.append(new_point)

    return covid_data


if __name__ == "__main__":
    # load covid data as list of CovidRecord objects
    data = parse_nyt_data('us-counties.csv')

    # each element in list data is a CovidRecord object. Each of which contains
    # date, county, state, fips, cases, and deaths

    # for example, we can print out the data for the first point in the US counties file
    point = data[0]

    print("Date: ", point.date, " County: ", point.county, " State: ", point.state,
          " FIPS: ", point.fips, " Cases: ", point.cases, " Deaths: ", point.death)

    ## write code to address the following question:
    ## (1) When was the first positive COVID case in Rockingham County? (2) When was the first in Harrisonburg?
    # (1) Make lists of just Rockingham county and Harrisonburg data
    Rock_county = []
    harrisonburg_city = list()
    for element in data:
        if element.county == 'Harrisonburg city':
            harrisonburg_city.append(element)
        elif element.county == 'Rockingham':
            Rock_county.append(element)
    # Check Rockingham county and Harrisonburg lists for first date with a covid case
    for row in Rock_county:
        if row.cases != 0:
            print("First case in Rockingham county was", row.date)
            break
    for row in harrisonburg_city:
        if row.cases != 0:
            print("First case in Harrisonburg was", row.date)
            break
    print("    ")

    ## write code to address the following question:
    ## (3) What day was the greatest number of new daily cases recorded in Harrisonburg? When was the greatest day in Rockingham County?
    # (3) Have variable for cases at last date, and variable for max new cases. Iterate through Rock_county to update
    last_cases_rock = 0
    max_new_cases_rock = 0
    for stuff in Rock_county:
        if (stuff.cases - last_cases_rock) >= max_new_cases_rock:
            max_new_cases_rock = (stuff.cases - last_cases_rock)
        last_cases_rock = stuff.cases

    # (3) Compare changes in cases iterating through Rock_County Entries to find the date with most new cases
    last_cases_rock2 = 0
    for Entries in Rock_county:
        if (Entries.cases - last_cases_rock2) == max_new_cases_rock:
            print(Entries.date, "Was the day with the greatest number of new cases in Rockingham County")
        else:
            last_cases_rock2 = Entries.cases

    # (3) Day of Max for cases in Harrisonburg, same technique as for Rockingham county
    last_cases_har = 0
    max_new_cases_har = 0
    for stuf in harrisonburg_city:
        if (stuf.cases - last_cases_har) >= max_new_cases_har:
            max_new_cases_har = (stuf.cases - last_cases_har)
        last_cases_har = stuf.cases

    last_cases_har2 = 0
    for entries in harrisonburg_city:
        if (entries.cases - last_cases_har2) == max_new_cases_har:
            print(entries.date, "Was the day with the greatest number of new cases in Harrisonburg")
        else:
            last_cases_har2 = entries.cases
    print("    ")

    ##write code to address the following question:
    ##(5) What was the worst seven-day period in either the city and county for new COVID cases? This is the 7-day period where the number of new cases was maximal.
    # (5) Create a list of changes in cases for Rockingham county
    Rock_case_deltas = list()
    Rock_case_last = 0
    Rock_case_change = 0
    for A in Rock_county:
        rock_case_change = A.cases - Rock_case_last
        Rock_case_deltas.append(rock_case_change)
        Rock_case_last = A.cases

    # (5) Find the worst 7-day period and index of the start of this period using the list of case deltas
    Rock_max_sum = 0
    for i in range(len(Rock_case_deltas)-6):
        Rock_seven_sum = sum(Rock_case_deltas[i:i+7])
        if Rock_seven_sum > Rock_max_sum:
            Rock_max_sum = Rock_seven_sum
            Rock_max_start = i

    # Use the index for the start of the worst 7-day period to show this week in Rock_county and # of new cases
    last_cases_rock3 = Rock_county[Rock_max_start-1].cases
    print("Worst 7 day period for cases in Rockingham county")
    for a in Rock_county[Rock_max_start:Rock_max_start+7]:
        new_cases_rock = a.cases - last_cases_rock3
        print(a.date, ':', new_cases_rock, "New cases")
        last_cases_rock3 = a.cases
    print("    ")

    # Same code as for Rockingham county
    Har_case_deltas = list()
    Har_case_last = 0
    Har_case_change = 0
    for B in harrisonburg_city:
        Har_case_change = B.cases - Har_case_last
        Har_case_deltas.append(Har_case_change)
        Har_case_last = B.cases

    Har_max_sum = 0
    for i in range(len(Har_case_deltas) - 6):
        Har_seven_sum = sum(Har_case_deltas[i:i + 7])
        if Har_seven_sum > Har_max_sum:
            Har_max_sum = Har_seven_sum
            Har_max_start = i

    last_cases_Har3 = harrisonburg_city[Har_max_start - 1].cases
    print("Worst 7 day period for cases in the city of Harrisonburg")
    for b in harrisonburg_city[Har_max_start:Har_max_start + 7]:
        new_cases_Har = b.cases - last_cases_Har3
        print(b.date, ':', new_cases_Har, "New cases")
        last_cases_Har3 = b.cases
