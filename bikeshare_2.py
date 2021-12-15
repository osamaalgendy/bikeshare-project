import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
months = ["jan", "feb", "mar", "apr", "may", "jun", "all"]
days = ["sunday", "saturday", "monday", "Tuesday",
        "wednesday", "thursday", "friday", "all"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input(
            "Would you like to see data for : Chicago, New York City, or Washington? \n")).lower()
        if city in CITY_DATA:
            print("You select %s city" % city)
            break
        else:
            print("sorry, Please type in correct city...")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("what is the name of the month to filter by,or \"all\" to apply no month filter \n\
        example: Jan, Feb, Mar, Apr, May, Jun or all for no filter\n")).lower()
        if month in months:
            print("You select %s month" % month)
            break
        else:
            print("Please type in correct Month...")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = str(input(
            "Which day? please type the name of the day (for example : sunday)  or all for no filter:\n")).lower()
        if day in days:
            print("You select %s day" % day)
            break
        else:
            print("Please enter a valid day...")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.day_name().str.lower()

    if month != 'all':
        month = months.index(month) + 1
        df = df[df["month"] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.lower()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("the most common month is : %d" % df["month"].mode()[0])

    # display the most common day of week

    print("the most common day of week is : %s" % df["day"].mode()[0])

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print("the most common start hour is : %d" % df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("the most common start station is : %s" %
          (df["Start Station"].mode()[0]))

    # display most commonly used end station
    print("the most common end station is : %s" % df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    most_combination = (df["Start Station"] + " to " +
                        df["End Station"]).mode()[0]
    print("display most frequent combination is %s" % most_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("the total travel time is : %.2f " %
          (df["Trip Duration"].sum()/60), "minute")

    # display mean travel time
    print("the mean travel time is : %.2f " %
          (df["Trip Duration"].mean()/60), "minute")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("the counts of user types is : \n %s" %
          df["User Type"].value_counts())

    # Display counts of gender
    if city != "washington":
        print("the counts of gender is : \n %s" % df["Gender"].value_counts())

    # Display earliest, most recent, and most common year of birth
    if city != "washington":
        print("the earliest year of birth is : %d" % df["Birth Year"].min())
        print("the most recent year of birth is : %d" % df["Birth Year"].max())
        print("the most common of birth is  : %d" % df["Birth Year"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

# show row data by 5 then by user request
        df.head()
        data_counter_start = 0

        while True:
            data_counter_end = data_counter_start + 5
            show_data = input(
                "would you like to show row data? press Enter if you want , no for exit.\n")
            if show_data.lower() == "":
                print(df.iloc[data_counter_start:data_counter_end])
                data_counter_start += 5

            elif show_data.lower() == "no":
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
