## Dog Walker Booking System ( PP3 )

The aim of this project is to build a booking system where people can book a dog walker for their pet and leave a review after the walk.

## Table of Content

* [Planning](#planning)
     * [User Stories](#user-stories)
     * [UI](#ui)
* [Deployment](#deployment)
     * [Git Hub](#github)
     * [Heroku](#heroku)
* [Resources](#resources)
* [Credits](#credits)


## Planning

### User Stories

  * Booking a Walk.
     - As a Pet Owner - I want to be able to book a dog walker for a specific day and time.

  * Available Walks.
     - As a Pet Owner - I want to be able to see abvailable walks that can be book e.g. Morning / Afternoon.
   
  * Leaving a Review.
     - As a Pet Owner - I would like to be able to rate and review the walk.
   
  * Viewing Upcoming Bookings

     - As a dog walker - I want to see all my upcoming walks and which pet owners have booked them so I can plan my schedule.

  * Receiving Feedback

     - As a dog walker - I want to receive reviews from pet owners after walks so I can build my reputation and improve my service.
   
## UI

### Home Page
![Home Page](https://github.com/user-attachments/assets/40a5f44f-4c6a-4c3e-aa01-3f514c805234)
 
### Home Page when logged in
![Home Page when logged in](https://github.com/user-attachments/assets/1268d2cb-2039-4cf3-b10b-b2892d32bf7c)


## Deployment

### GitHub

Repository
I made a public local repository on my Github account, I then linked my repository to my VSCode account and started building. When writing my code I ensured that I committed my changes to the repository using clear and direct messages for any changes,this is done by doing the following in the terminal;

git add .
git commit -m “Enter message here”
git push
I would send a commit after each change then I would push the file once i made 3 or 4 changes.

Hosting
This is how I hosted my website: On Github I Selected my Dog-Walker-Booking-PP3 Repository, then go to;

Settings
Pages
Once on the pages site I would ensure the following settings were applied; Source would need to be set to ‘Deploy from branch’ Branch will need to be set to main and then root. Save.

<img width="1655" alt="Screenshot 2025-06-23 at 12 47 47" src="https://github.com/user-attachments/assets/ad2d1c37-9b12-488f-bc26-0aafd5f9c694" />


<img width="1661" alt="Screenshot 2025-06-23 at 12 48 32" src="https://github.com/user-attachments/assets/dbc7de5f-f846-48cb-bff2-fd9848219e65" />


### Heroku

Deploying my project on Heroku I first created a new app by clicking the "New" button in the top right to get a dropdown menu with the following choice
* Create new app
* Create new pipline

I clicked "Create new app"

<img width="1658" alt="Screenshot 2025-06-23 at 13 04 18" src="https://github.com/user-attachments/assets/77f25958-d873-4f05-800d-9229f3f63ffe" />

Once ive clicked "Create new app" i would then need to name my app "dog-walker-booking-pp3" all in lowercase or an error will occur, once this is done i then selected my location

<img width="1658" alt="Screenshot 2025-06-23 at 13 04 45" src="https://github.com/user-attachments/assets/cebfe6ea-f457-47cc-b686-fecb792daf62" />

I then navigated to the "deploy" section to connect my GitHub repository to Heroku i would do this by;
* Selecting github as my deployment method.
* Then once conected i would search for my project by typing in "dog".
* Once ive search my github i would select the project i would like to link to Heroku.

<img width="1657" alt="Screenshot 2025-06-23 at 13 05 36" src="https://github.com/user-attachments/assets/0d28dbd8-dc25-4609-8966-7353dc473ff5" />

Once all the above have been completed i would then process a Manual deployment and i would need to repeat this process after i made any changed within my source code  
<img width="1798" alt="Screenshot 2025-06-23 at 13 07 05" src="https://github.com/user-attachments/assets/e211c7da-eb4c-486e-b735-4cb6f1f363ed" />

To complete the deployment of my app i updated the ALLOWED_HOSTS in the settings.py file by adding
ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']

<img width="371" alt="Screenshot 2025-06-23 at 13 08 24" src="https://github.com/user-attachments/assets/b7a6b0ed-c26d-4d79-a855-3c562d955a08" />

This tells Django to accept any requests made by Heroku. The 127.0.0.1 allows the app to run without any errors as without this Django will block any requests and throw up a "400 Bad Request error".



## Resources

* Django 5 By Example Fifth Edition - By Antonio Mele < packt >
* Code Institute
   - Love Sandwiches
   - I Think Therefore I Blog
* Django Project Site
  
## Credits
 * Bootstrap for navbar layout


