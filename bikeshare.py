import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    #ref: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
    while True: 
        city = input('\nDo you like to see the data for Chicago, New york, or Washington?\n')
        city = city.lower()
        if city not in ('chicago','new york','washington'):
           print('please enter valid city name')
        else:
            break
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    # TO DO: get user input for month (all, january, february, ... , june)
    try:
           filter = input('\nwould like to filter the data by month, day ? type "none" for no item filter\n')
           if filter.lower() == 'month':
                s_month = input('\nWhich month? please type January, February, March, April, May or June ?\n')
                month = s_month.lower()
                s_day = input('\nWhich day? please type the day ex. Friday or "none" for no item filter \n')
                s_day= s_day.lower()
                if s_day != 'none':
                    day = s_day
                else:
                    day = 'all'
                        
           elif filter.lower() == 'day':
                s_day = input('\nWhich day? please type the day ex. Friday \n')
                day = s_day.lower()
                month = 'all'
           else:
                month,day = 'all','all'
            
    except ValueError:
            print('\nPlease enter valid input!\n')


   


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
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
    common_month = df['month'].mode()[0]
    print('Most common  Month:', common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common  day:', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('Most common Start Hour:', common_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most common  Start:', common_start)


    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most common  End:', common_end)


    # TO DO: display most frequent combination of start station and end station trip
    #ref: https://stackoverflow.com/questions/53037698/how-can-i-find-the-most-frequent-two-column-combination-in-a-dataframe-in-python
    common_start_end = df.groupby(['Start Station','End Station']).size().idxmax()

    print('Most common  Start and End station:', common_start_end)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_travel = df['Trip Duration'].sum()
    print('total sum of travel time:', sum_travel)
    

    # TO DO: display mean travel time
    sum_mean = df['Trip Duration'].mean()
    print('the mean of travel time:', sum_mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user types counts:', user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('Gender counts:', gender_types)
    # TO DO: Display earliest, most recent, and most common year of birth
        most_common = df['Birth Year'].mode()[0]
        print('the most common birth year:', most_common)
    
        recent = df['Birth Year'].max()
        print('the most recent:', recent)
    
        earl = df['Birth Year'].min()
        print('the most earliest:', earl)
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
     print('\nShow data...\n')
     start_time = time.time()
    
     count = 0
     inner_counter = 0
     while True:
        count+=1    
        if count < 5:
          print(df.iloc[inner_counter]) 
          inner_counter+=1
        elif count == 5:
            ans =input('do you want to continue ...')
            if ans == 'yes':
               count=0
            else: 
                break
            
        
     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print (df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
