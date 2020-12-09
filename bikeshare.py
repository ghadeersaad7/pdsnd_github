import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
   
    while True:
         city= input('Input one city from the list(chicago, new york city, washington) \n').lower()
         
         try:
            #if isinstance(city, str) and city in ['chicago','new york city','washington']:
            if  isinstance(city, str) and city in ['chicago','new york city','washington']:
                break
            else:
                print('Please inter correct value')
         except ValueError:
            print('Input not valid')
            

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = input('Input a month Ex: january, february, ..., june or all \n').lower()
        try:
            if isinstance(month, str) and month in ['january','february','march','april','may','june','all'] :
                break
            else:
                print('Please inter correct month')
        except ValueError:
            print('Input not valid')
    #return month 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input('Input a day Ex: monday, tuesday, ... or all \n').lower()
        try:
            if isinstance(day, str) and day in ['saturday ','sunday','monday','tuesday','wednesday','thursday','friday','all'] :
                break
            else:
                print('Please inter correct day')
        except ValueError:
            print('Input not valid')
    

    print('-'*40)
    print('\n The city you choose is: '+city+'\n The month you choose is: '+month+'\n The day you choose is: '+day+'\n')
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
    df['hour'] = df['Start Time'].dt.hour
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
    index = (df['month'].mode()[0])-1
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('\nThe most common month is: '+months[index])
    # TO DO: display the most common day of week
    print('\nThe most common day of week is: '+ (df['day_of_week'].mode()[0]))
    # TO DO: display the most common start hour
    print('\nThe most common start hour is: ')
    print(df['hour'].mode()[0])
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most common start station is: ')
    print(df['Start Station'].mode()[0])
    
    # TO DO: display most commonly used end station
    print('\nThe most common end station is: ')
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of start station and end station trip is: ')
    groupStartEndStation = df.groupby(['Start Station','End Station'])
    print(groupStartEndStation.size().sort_values(ascending=False).head(1))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('\nTotal travel time is :')
    print(total)
    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('\nMean travel time is :')
    print(mean)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    typesCounts = df['User Type'].value_counts()
    print('\nCounts of User Types :')
    print(typesCounts)
    
    if city != 'washington':
        # TO DO: Display counts of gender
        genderCounts = df['Gender'].value_counts()
        print('\nCounts of Gender :')
        print(genderCounts)
        
        # TO DO: Display earliest, most recent, and most common year of birth
        earliestBY = df['Birth Year'].mode()[0]
        recentBY = df['Birth Year'].max()
        commonBY = df['Birth Year'].min()
        print('\nEarliest Year of Birth :')
        print(earliestBY)
        print('\nMost Recent Year of Birth :')
        print(recentBY)
        print('\nMost Common Year of Birth :')
        print(commonBY)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no \n')
        if view_data.lower() != 'yes':
            break

        else :
            start_loc = 0
            end_loc = 5
            count = 1
            while (count):
                print(df.iloc[start_loc : end_loc ])
                start_loc += 5
                end_loc += 5
                view_display = input('do you wish to continue? Enter yes or no\n').lower()
                if  view_display == 'yes':
                    count = 1
                else:
                    count = 0
            
       
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
