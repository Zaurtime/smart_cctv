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
  * Most of the site was construted using this language
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
  * Used for creating forms in the site.

<br>

# Deployment

## Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

* Navigate to heroku and create an account
* Click the new button in the top right corner
* Select create new app
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
* Scroll down to Manual deploy and choose the main branch
* Click deploy


## AWS
* Create an aws account
* Navigate to S3 in services and create a bucket
* Set up IAM
* Create a static file and a media file within the bucket using the information required during the bucket creation (i.e. access key and secret key)
* Configure in settings.py
* Add access key and secret key to env.py
* Add keys to config vars in Heroku
* Disable collectstatic in config vars
* Add new directory path for static files in settings.py

## Stripe
* Create a developer account
* Add stripe keys (public and private) to env.py and heroku config vars
* Set up Stripe according to Stripe's documentation
* Add site url to Stripe's webhooks section
* Add the webhook secret key to env.py and Heroku config vars

## Credits
* I used the Boutique Ado walkthrough project as guidance for my project
* Spent a lot of time looking up Bootstrap documentation
* Also spent time reading Django documentation
* I used some posts from Stack Overflow for various little snippets of code, which can be found commented within the code blocks
it has been used in
* My mentor sessions with [Gareth McGirr](https://github.com/Gareth-McGirr/) who was very helpful in guiding me with my planning for the project
* All camera images were taken from online store [eBay](https://www.ebay.ie)

