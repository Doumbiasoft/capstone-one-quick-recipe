#Capstone One

### App Name: (Quick Recipe)
![img](/static/images/quick-recipe-logo.png)

**1. What goal will your website be designed to achieve?**

>To create a recipe recommendation system that utilizes free food APIs to suggest recipes to users based on their dietary restrictions, preferences, and available ingredients.


**2. What kind of users will visit your site? In other words, what is the demographic of your users?**

 >   The system will take inputs from the user such as their dietary restrictions (vegetarian, gluten-free, etc.), preferred cuisine types (Italian, Indian, Mexican, etc.), and available ingredients

**3. What data do you plan on using? You may have not picked your actual API yet,which is fine, just outline what kind of data you would like it to contain.**

>I am going to use the data from the **[Spoonacular API (RAPID API)](https://rapidapi.com/spoonacular/api/recipe-food-nutrition)**.


**4. In brief, outline your approach to creating your project (knowing that you may not know everything in advance and that these details might change later). Answer questions like the ones below, but feel free to add more information:**


**a. What does your database schema look like?**
![img](/documentations/database-schema-quick_recipe-white-bg.png)


**b. What kinds of issues might you run into with your API?**

>Limit of requests in free subscription

**c. Is there any sensitive information you need to secure?**

>Yes, the User's information like:
>
>Last Name, FirstName, Birth Date, gender, weight


**d. What functionality will your app include?**

**User authentication and profile creation:** 
>Users will be required to create a profile and provide information about their dietary restrictions and preferences.

**Recipe search and recommendation:** 
>The system will use free food APIs to search for recipes based on the user's preferences and suggest them to the user.

**Ingredient matching:** 
>The system will suggest recipes based on the ingredients available to the user.

**Recipe details:** 
>The system will provide details about the suggested recipes, such as ingredients, preparation time, and nutritional information.

**Recipe saving:** 
>The user can save recipes they like for future reference.

**Recipe sharing:** 
>Users can share recipes they like with their friends or on social media.

**e. What will the user flow look like?**

-	Registration And Authentication
-	Favorite Recipes
-	Share Recipes
-	Rating Recipes


**f. What features make your site more than CRUD?**
      
-	Mailing system 
-	Registration with Google, Facebook, and Apple Authentication



**Do you have any stretch goals?**
