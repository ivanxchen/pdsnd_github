import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}

WEEK_LIST = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        city = input('Would you like to see data for Chicago | CH, New York City | NYC, or Washington | WA?\n').lower()
        print()
        if city=='chicago' or city=='ch':
            city='chicago'
        if city=='new york city' or city=='nyc':
            city='new york city'
        if city=='washington' or city=='wa':
            city='washington'
        if city not in CITY_DATA:
            print("\nI'm sorry, I'm not sure which city you're referring to. Let's try again.")
            continue
        city = CITY_DATA[city]
        break

    # TO DO: get user input for month (january, february, ... , june)
    while 1:
        select = input('Would you like to filter the data by month and/or day? Enter yes or no. Type "no" for no time filter.\n').lower()
        print()
        if select=='yes' or select=='y':
            select=True
        elif select=='no' or select=='n':
            select=False
        else:
            print("\nI'm sorry, you did not enter a valid selection. Let's try again.")
            continue
        break

    # TO DO: get user input for day of week (monday, tuesday, ... sunday)
    while 1:
        if select:
            filter=input('Would you like to filter the data by month, day, or both\n').lower()
            print()
            if filter=='month':
                month = input('Which month? January, February, March, April, May, or June?\n').lower()
                print()
                if month not in MONTH_LIST:
                    print("\nI'm sorry, I'm not sure which month you're trying to filter by. Let's try again.")
                    continue
                month = MONTH_LIST[month]
                day='all'
            elif filter=='day':
                day = input('Which day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
                print()
                if day not in WEEK_LIST:
                    print("\nI'm sorry, I'm not sure which day of the week you're trying to filter by. Let's try again.")
                    continue
                day = WEEK_LIST[day]
                month='all'
            elif filter=='both':
                month = input('Which month? January, February, March, April, May, or June?\n').lower()
                print()
                if month not in MONTH_LIST:
                    print("\nI'm sorry, I'm not sure which month you're trying to filter by. Let's try again.")
                    continue
                month = MONTH_LIST[month]
                day = input('And which day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday\n').lower()
                print()
                if day not in WEEK_LIST:
                    print("\nI'm sorry, I'm not sure which day of the week you're trying to filter by. Let's try again.")
                    continue
                day = WEEK_LIST[day]
            else:
                print("\nI'm sorry, I'm not sure which time period you're trying to filter by. Let's try again.")
                continue
            break
        else:
            day='all'
            month='all'
            break


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
    df = pd.read_csv(city)
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most popular times of travel."""

    print('\nCalculating The Most Popular Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    popular_month = df['month'].mode()[0]
    for num in MONTH_LIST:
        if MONTH_LIST[num]==popular_month:
            popular_month = num.title()
    print('Most popular month for travel:', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    popular_day = df['day_of_week'].mode()[0]
    for num in WEEK_LIST:
        if WEEK_LIST[num]==popular_day:
            popular_day = num.title()
    print('Most popular day of week for travel:', popular_day)

    # TO DO: display the most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour of day for travel:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost popular start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('\nMost popular end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost popular trip from start to end: {}'.format(df['Start Station'].mode()[0] + ' to ' + df['End Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_sum = df['Trip Duration'].sum()
    minutes, seconds = divmod(trip_sum, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)
    print('\nPassengers travelled a total of: %d years %02d days %02d hrs %02d mins %02d secs' % (years, days, hours, minutes, seconds))

    # TO DO: display mean travel time
    trip_mean = df['Trip Duration'].mean()
    minutes, seconds = divmod(trip_mean, 60)
    hours, minutes = divmod(minutes, 60)
    print('\nPassengers travelled an average of: %d hrs %02d mins %02d secs' % (hours, minutes, seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nUser Type:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print("\nI'm sorry, there is no gender data for this city.")
    else:
        print('\nGender Type:')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('\nData related to birth year of users is not available for this city.')
    else:
        birth = df.groupby('Birth Year', as_index=False).count()
        print('\nEarliest year of birth was {}.'.format(int(birth['Birth Year'].min())))
        print('Most recent year of birth was {}.'.format(int(birth['Birth Year'].max())))
        print('Most common year of birth year was {}.'.format(int(birth.iloc[birth['Start Time'].idxmax()]['Birth Year'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    '''Displays five lines of data. Ask user if they would like to see five more. Continues until user initiates stop.'''

    start_loc = 0
    end_loc = 5

    display = input('Would you like to view individual trip data? Enter yes or no\n').lower()
    print()
    if display=='yes' or display=='y':
        display=True
    elif display=='no' or display=='n':
        display=False
    else:
        print("\nI'm sorry, I'm not sure if you wanted to see individual trip data or not. Let's try again.")
        display_data(df)
        return

    if display:
        while 1:
            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5
            end_display = input('\nWould you like to view more individual trip data? Enter yes or no.\n').lower()
            print()
            if end_display=='yes' or end_display=='y':
                continue
            elif end_display=='no' or end_display=='n':
                break
            else:
                print("\nI'm sorry, you didn't enter a valid response!")
                return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes' and restart != 'y':
            break

if __name__ == "__main__":
	main()
