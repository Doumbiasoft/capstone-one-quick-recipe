# Capstone one: Quick-Recipe

![img](/app/static/images/quick-recipe-logo.png)
## Unit 29 Capstone One

>To create a recipe recommendation system that utilizes free food APIs to suggest recipes to users based on their dietary restrictions, preferences, and available ingredients.
>**Host:** **[Render.com](https://render.com)**
>**The application is online at:**
>**https://quick-recipe.onrender.com**

![img](/app/static/images/quick-recipe-github-illustration.jpg)

**API**: **[Tasty (RAPID API)](https://rapidapi.com/apidojo/api/tasty)**

**DATABASE SCHEMA**:
![Img-Light](/documentations/database-schema-quick_recipe-white-bg.png#gh-light-mode-only)![Img-Dark](/documentations/database-schema-quick_recipe.png#gh-dark-mode-only)

## Application components:
This application has been created using the following components:
- **Python3** (version 3.11.1)
- **Flask** as a framework
- **Posgtres sql** as a Database

>**NB:**
>For this project I use Blueprint to organize the application.
That was a bit challenging because by using Blueprint everything wont work properly without additional configuration.

The rest of the components are available in the **requirements.txt**

## Summary:

The main goal of this application is to create a recipe recommendation system that utilizes free food APIs to suggest recipes to users based on their dietary restrictions, preferences, and available ingredients.
But with the limitations of the features of API [Tasty (RAPID API)](https://rapidapi.com/apidojo/api/tasty) I could not achieved those features like the recommendation based on the dietary or ingredient. Instead I implemented the recommendations based on the user's preferences recipe save in the favorite recipes.

**Find below all the features implemented by this application:**

- **User's account:**

The application allows users to create an account to get access to certain features like **``print``**, **``add favorites``**, **``sharing``**.

For an account activation this application use email notification and send an activation link.
we have two types of authentication.
    - First one is to authenticate with your **email address** and **password**.
    - Second one is to authenticate with **Google**

All user can do all basic action in user's profile like edit password, edit personal information, delete accounts.
Users authenticated with the Google authentication can just delete their account.

- **Allow users to search for recipe:**

The API has a limit number of requests. So to solve this problem, I use caching and saving some data in Database.
Users can save their favorite recipes if they are authenticated.

- **Recipe recommendation**

The user will be able to see similar recipe in the favorites section
This favorite section is only available for authenticated users.
