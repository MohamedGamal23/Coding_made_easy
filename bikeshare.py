import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all','sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city={}
    while True: 
        try:
           city=input("Enter your chosen city:chicago, new york city or washington :").lower()
           if city in CITIES:
             break
        except ValueError:
            print("this is not a valid input")
                  
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
           month=input("Enter your chosen month :january, february,march...etc./n or type 'all'  :").lower()
           if month in MONTHS:
             break
        except ValueError:
            print("this is not a valid input")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        try:
           day=input("Enter your chosen day : type 'all' or choose your day :sunday , monday ...etc.  :").lower()
           if day in DAYS:
             break
        except ValueError:
            print("this is not a valid input")


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0] 
    print('most popular month',popular_month)             

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0] 
    print('most popular day', popular_day) 

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print(user_counts)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
       gender_counts = df['Gender'].value_counts()
       print(gender_counts)
    else :
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
       birth_year = df['Birth Year']
       earliest_year = birth_year.min()
       print("The most earliest birth year:", earliest_year)
       most_recent = birth_year.max()
       print("The most recent birth year:", most_recent)
       most_common_year = birth_year.value_counts().idxmax()
       print("The most common birth year:", most_common_year)
    else :
       print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def View_data(df):
    valid_response=['yes','no']
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()

    start_loc = 0
    while (view_data not in valid_response):
          view_data=input( 'please type only yes or no :').lower()
    while (view_data  in valid_response and view_data=='yes'):
          print(df.iloc[start_loc:start_loc+5])
          start_loc += 5
          view_data = input("Do you wish to continue?: ").lower()
          while (view_data  not in valid_response):
                 view_data=input( 'please type only yes or no:').lower()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        View_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
