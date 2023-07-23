<h1 align="center">SMART CCTV</h1>

<a href="https://smartcctv.herokuapp.com/" target="_blank" rel="noopener" alt="Smart CCTV, click here to open the website"><img src="media/amIrespon.png" alt="Smart CCTV" max-height="650px" max-width="1300px"></a>
<hr>
View GitHub repository
<a href="https://github.com/Zaurtime/smart_cctv" target="_blank" rel="noopener">here</a>

The live site can viewed here
<a href="https://smartcctv.herokuapp.com/" target="_blank" rel="noopener">here</a>

# SMART CCTV - README INTRODUCTION
 
## PURPOSE OF THIS SITE:
Smart CCTV is an online e-commerce cameras store. The site specifically sells cameras, recently released in various different categories.

## IMPORTANT INSTRUCTIONS:
If you wish to register or receive a confirmation email, you need to enter a real email address or generate a test email through an email generator site when registering or purchasing items.
 
<br>

**Stripe test cards for checkout** 

- The card payment succeeds and doesn’t require authentication.
  * Fill out the credit card form using the credit card number 4242 4242 4242 4242 with any expiration, CVC, and postal code.
- The card payment requires authentication.	
  * Fill out the credit card form using the credit card number 4000 0025 0000 3155 with any expiration, CVC, and postal code.
  
  You can read more about <a href="https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements#web-test-the-integration" target="_blank" rel="noopener">here</a>
  
 ## SUPERUSER SITE ADMIN FUNCTION:
This site uses Django's Admin functionality for content moderation control. The site has a Superuser with their own login credentials.
 
The Admin panel can be accessed simply from the home page. You can navigate to it by clicking in the URL bar, hit / (forward slash) on keyboard and type admin. Like so: **/admin** and hit **enter**

**NOTE:**
- During the development of this project, I posted test testimonials posts and added user records. This was done to test the functionality of the **Add testimonials**, **Edit testimonials** and **Delete testimonials** functions. And to test that testimonials were successfully added, edited and deleted.
- You will also find some comments visible in the testimonials detail, this was also done to test functionality.
- **(All of the testimonials content is simply just placeholder text used to test the functionality of content display for site)**
- The User after the purchase can leave a review.
- Site Admin can do all of the above from the admin panel.
 
<br>

# SEO (Search Engine Optimisation) and Marketing
## SEO
Keywords and phrases entered as metadata in the head of the HTML document and throughout the main content of the site help search engines find relevant, searchable content.

Here is the link  [Facebook B2C](https://www.facebook.com/profile.php?id=100095301210655)

Screenshots of my Facebook Business Page - as shown below 

![Facebook Screenshot](/media/facebookB2C.png)

![Facebook ContactPost](/media/faceBookContactPost.png)


A Site Map was created by for this site by using [xml-sitemaps.com](www.xml-sitemaps.com). This enables search engines to find searchable content easily on the site. To ensure the site is GDPR compliant, I created a robots.txt file to restrict access for search engines to parts of the site that contain user information.

### Marketing
In the footer of Contact page, site visitors can find a link to sign up to the Smart CCTV newsletter.

![newsletter](https://github.com/Zaurtime/smart_cctv/assets/119350794/cbfaaae1-8375-4192-ba19-6ea4da7ed5f8)


Site Users can submit their email addresses on the form provided on the newsletter page.


# Testing

## CSS
All css pages were run through the [w3 CSS Validator](https://jigsaw.w3.org/css-validator/). No errors were found.
![cssValid](https://github.com/Zaurtime/smart_cctv/assets/119350794/d215d382-8a6b-4167-b418-ce25e8b182bb)

 
<br>

## Lighthouse Testing
Results of lighthouse testing on the site overall Performance 98 score ![lighthouse](https://github.com/Zaurtime/smart_cctv/assets/119350794/a2841614-29a7-4db4-bfa8-9ef981591097)



# Technologies Used

* [GitPod](https://gitpod.io/)
  * The environment used to create the site
* [Github](https://github.com/)
  * Used for version control and repository for the project
* [Django framework](https://www.djangoproject.com/)
  * The framework used to construct the site
* [ElephantSQL](https://api.elephantsql.com/console/cac17a18-94fd-4be5-99fe-f319179d4a64/details)
  * Holds the database for this site
* [Python](https://www.python.org/)
  * Most of the site was constructed using this language
* [HTML](https://html.com/semantic-markup/)
* [Bootstrap](https://getbootstrap.com/)
  * Much of the site uses Bootstrap
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
  * Used to style the small portion of the site Bootstrap couldn't handle.
* [JavaScript](https://www.javascript.com/)
  * Used to handle small events such as popups
* [AWS S3](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23storage&trk=9845b571-f118-41f9-ae80-53f3364524c4&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Storage|S3|GB|EN|Text&s_kwcid=AL!4422!3!489216385180!e!!g!!aws%20s3&ef_id=CjwKCAjwkMeUBhBuEiwA4hpqEJmK52Rp_outs9Ama8hbA1IhA0MOr-OkiPis4BSWVAuobKN7yEmQsRoCSNMQAvD_BwE:G:s&s_kwcid=AL!4422!3!489216385180!e!!g!!aws%20s3&awsf.Free%20Tier%20Types=*all)
  * Used to store site images
* [Stripe](https://stripe.com/gb)
  * Used to handle customer payments
* [Heroku](https://id.heroku.com/login)
  * The hosting site for Tripp's Treasures
* [Dango Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  * Used for creating forms on the site.

<br>

# Deployment

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

* Navigate to heroku and create an account
* Click the new button in the top right corner
* Select create a new app
* Enter app name
* Select region and click create app
* Click the resources tab and search for Heroku Postgres
* Select hobby dev and continue
* Go to the settings tab and then click reveal config vars
* Add the following config vars:
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
  - DATABASE_URL
  - EMAIL_HOST_USER
  - SECRET_KEY
  - SECRET_WH_SECRET
  - STRIPE_PUBLIC_KEY
  - STRIPE_SECRET_KEY
  - USE_AWS
* Click the deploy tab
* Scroll down to Connect to GitHub and sign in / authorize when prompted
* In the search box, find the repository you want to deploy and click connect
* Scroll down to Manual Deploy and choose the main branch
* Click Deploy

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create an app, give it a name and select a region
3. Go to app settings and set DATABASE_URL to config vars
4. Install the plugins dj-database-url and psycopg2-binary in terminal.
5. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
6. Create a Procfile with the text: web: gunicorn your_app_name.wsgi
7. Ensure debug is set to false in the settings.py file, add localhost, smartcctv.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
8. In the settings.py ensure the connection is to the Heroku postgres database, no indentation if you are not using a separate test database. 
9.  Run "python3 manage.py showmigrations" to check the status of the migrations

10. Run "python3 manage.py migrate" to migrate the database

11. Run "python3 manage.py createsuperuser" to create a super/admin user

12. Run "python3 manage.py loaddata genres.json" on the categories file in products/fixtures to create the genres

13. Run "python3 manage.py loaddata albums.json" on the products file in products/fixtures to create the albums

14. Run "python3 manage.py loaddata tracks.json" on the products file in products/fixtures to create the tracks

15. Install gunicorn (pip install gunicorn) and add it to the requirements.txt file using the command pip3 freeze > requirements.txt

16. Disable collectstatic in Heroku before any code is pushed using the heroku settings config vars: set DISABLE_COLLECTSTATIC: 1

17.  Ensure the following environment variables are set in Heroku

18.  Connect the app to GitHub, and enable automatic deploys from the main if you wish

19.  Click deploy to deploy your application to Heroku for the first time

20.  Click on the link provided to access the application

21.  If you encounter any issues accessing the build logs is a good way to troubleshoot the issue


### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in the upper right-hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.

### Stripe
* Create a developer account
* Add stripe keys (public and private) to env.py and heroku config vars
* Set up Stripe according to Stripe's documentation
* Add site url to Stripe's webhooks section
* Add the webhook secret key to env.py and Heroku config vars

### AWS
* Create an aws account
* Navigate to S3 in services and create a bucket
* Set up IAM
* Create a static file and a media file within the bucket using the information required during the bucket creation (i.e. access key and secret key)
* Configure in settings.py
* Add access key and secret key to env.py
* Add keys to config vars in Heroku
* Disable collect static in config vars
* Add new directory path for static files in settings.py

### Credits
* I used the Boutique Ado walkthrough project as guidance for my project
* Spent a lot of time looking up Bootstrap documentation
* Also spent time reading Django documentation
* I used some posts from Stack Overflow for various little snippets of code, which can be found commented within the code blocks it has been used in
* All camera images were taken from the online store [eBay](https://www.ebay.ie)

## Acknowledgements

### Special thanks to the following:
* My mentor sessions with [Gareth McGirr](https://github.com/Gareth-McGirr/) who was very helpful in guiding me with my planning for the project and completing
* Code Institute Tutor Support Network
* My team vs colleagues with whom I study on the course
