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

## Updates, Features and Problems encountered

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
Milestone 3 updates:

To do:
- Increase number of food places per region to 50 each -- DONE
- Sort by cuisine type (Chinese, Indian, Malay, Western) -- DONE
- Sort by postal code (read first 2 digits then filter from txt file) -- DONE
- Add new commands -- DONE
- BotFather /help commands or easy access -- DONE
- User Testing
- Include price range indication for food places -- DONE
- Include cuisine indication into region -- DONE
- Improve code for filtering by cuisine type -- DONE
- Debug side cases for split bill function (names with spaces, $ for amounts) -- DONE


## Testing of FoodieFriends bot:
Try our bot out @ FoodieFriendsBot on Telegram!

Current cloud hosted version has working commands for split bills and food recommendation by region. 

README GDOC: https://docs.google.com/document/d/1FB3Lspx5IpIAiJI42V_CIAmzAZ1mfNGYC-9NvBehqL0/edit?usp=sharing



