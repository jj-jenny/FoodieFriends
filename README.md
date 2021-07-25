# FoodieFriends
[NUS] CP2106: Independent Software Development Project (Orbital)

Team Members: Jenny Jian Jie, Nicole Goh Wanyu

Achievement Level: Gemini

# Milestone 1 (Ideation)

// To include problem motivation, proposed core features / user stories, design and plan

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

// To include core features developed, problems encountered

## Updates

1. Hosting of Telegram Bot on Heroku
2. Addition of calculate bill function to our split bills command
3. Selection of food locations for the 5 different regions and embedding their Google Maps link

## Problems Encountered

## Testing of FoodieFriends bot:
Try our bot out @ FoodieFriendsBot on Telegram!

Current cloud hosted version has working commands for split bills and food recommendation by region. 

** The hosted version has a limited list of food places for now so there could be repetitions among the 3 recommendations given, we will be running the more extensive list of food places once we have tidied it up for the next milestone.


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

https://docs.google.com/document/d/1ddv3aLesPcRdzKxA5241zh_DvN9_7TZxUAXO9Un93j4/edit



