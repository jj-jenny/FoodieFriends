# FoodieFriends
[NUS] CP2106: Independent Software Development Project (Orbital)

Team Members: Jenny Jian Jie, Nicole Goh Wanyu

Achievement Level: Gemini

# Milestone 1 (Ideation)

// Includes problem motivation, proposed core features / user stories, design and plan

## Motivation 

Have you ever had trouble deciding on what to eat? Or simply just want to try new food but don’t know where? Or face difficulty splitting bills paid by multiple people? 

Many people have experienced spending hours deciding on where to eat, walking around the whole place just to end up deciding on a random restaurant. Even after the meal, it may be difficult to split the shared bill, especially if multiple people paid for food at different places.

## Aim 

We aim to make it easy for users to find suitable places to have their meals, especially with friends or in a large group via applications that they already use daily (eg Telegram). We also have a split bill function for shared meals to make it easy for groups to sort their expenses.

## User Stories

1. As someone who first visits a mall/location, I want to be able to easily access a list of food options available in the area that suits my taste and preferences.

2. As someone who is looking to try new food, I want to be able to receive suggestions on what to eat in the area.

3. As someone who meets in a group, I want to be able to easily split multiple shared bills and know how much I should pay/receive. 

## Core Features

- Generate food recommendations based on location and food preferences.
- Split bills among groups.

![Programme Flow](https://user-images.githubusercontent.com/78203310/126294720-50170cdb-f890-4557-95a0-0f2500ea27f5.jpg)

### How are we different from similar platforms?
Yelp (Food recommendations App)
- Unlike using Yelp where users have to download a new application, we make use of Telegram, which is already being used by our target groups, to make getting food recommendations much more convenient for them.


GooglePay/ DBS PayLah!’s split bill function
- GooglePay/ DBS PayLah! Would require users to have accounts which then requires secure logins since they are binded to bank accounts. By making use of Telegram, users can easily split bills without having to login or create accounts since they already have a Telegram account.


# Milestone 2 (Prototype)

// Includes core features developed, problems encountered

## Updates, Features and Problems Encountered

1. Hosting of Telegram Bot on Heroku 

    1.1 In order to host our telegram bot on Heroku’s servers, we had to reconstruct quite a lot of our code since we had to convert our code to use webhooks.
    - We originally used the pyTelegrambotAPI package but it was not very suitable when converting to webhooks so we had to change to using the python-telegram-bot package, resulting in major edits to modules used from the  different Telegram API packages.
    
    1.2 As we are only using free hosting servers, we have very limited options with several restrictions.
    -  Telegram bots hosted on Heroku have an inactivity time limit of 30 minutes. Afterwards, our telegram bot will be asleep and will take time to restart when activated. This results in a slight delay in response from the bot upon the ‘/start’ command from the Telegram user if the bot has not been utilized 

2. Addition of calculate bill function to our split bills command

    2.1 Originally we did not use ‘import decimal’ when doing our calculations and this resulted in our output being very long when there are decimal places.
    - By using ‘import decimal’, we were able to improve our calculations and limit it to 2d.p (as per usual money calculations).

3. Selection of food locations for the 5 different regions and embedding their Google Maps link

    3.1 During our selection of locations, we realized that Singapore does not have a South region and has Northeast as the fifth region instead.
    - Modified our South command into Northeast and its relevant food places.

    3.2 The database of food locations will have many different recommendations and it will be very messy if we display them all every time.
    - We modified our bot to display a list of 3 different random food recommendations everytime. To get more recommendations, users can simply press the specific region button again for a different set of recommendations.
    - This prevents the message from being too long while also ensuring that users can see many different food recommendations.


# Milestone 3 (Extension)

// To include bugs squashed, edge features developed, problems encountered, and user testing

## Updates

1) Increased amount of locations per region to 50 each
Since the bot returns 3 places randomly each time, we wanted to increase the size of the database from 20 to 50 such that it is less likely to return the same places again with each call.

2) Filter by type of cuisine
We added another function to allow users to choose a specific type of cuisine they would like to choose from. This outputs a list of 3 food places which corresponds to the cuisine they have opted for. We have selected to group the locations into Chinese, Malay, Indian, Western, Thai and Others. Similar to the filter by location function, the output is random and changes when called again.

3) Added the filter by postal code function
To filter our food locations by a specific postal code, we added a function to our bot such that it displays food locations containing the postal code that match the first 2 digits of the user’s input postal code. We increased the number from the first 3 digits to the first 2 digits to ensure that the output displayed is not too limited.

4) Addition of new command shortcuts for easy access // BotFather /help commands
In order to make all our functions more accessible, we added new command shortcuts via BotFather for our users to have easier access.


## Testing and Improvements
We conducted user testing by getting our friends and family to try out the bot functions when they are splitting bills or looking for food recommendations and collated the feedback we received.

### Improvements made based on feedback received:

1) Included price range indication for recommended food places
Many of our testers mentioned that having the price indication would allow them to make a more informed decision on whether the particular recommendation is suitable for them. 
    - For example, if they want to save money they can decide on recommendations in the $ range.

2) Included cuisine type as part of the description displayed when filtering by region
For some food places, it is unclear by their name what type of cuisine they serve, which may confuse some users. Thus, we decided to indicate the cuisine type as part of the description as well. This also led to us modifying our code for the filtering by cuisine function to make use of the description while filtering.

3) Error messages and input format of split bill function
When our testers tried the split bill function, there were times where the input format was not clear and resulted in the function failing to display the calculated output.
    - catching InvalidOperation error

## Testing of FoodieFriends bot:
Try our bot out @ FoodieFriendsBot on Telegram!


README GDOC: https://docs.google.com/document/d/1FB3Lspx5IpIAiJI42V_CIAmzAZ1mfNGYC-9NvBehqL0/edit?usp=sharing



