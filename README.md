# voteapp
Vote Intention App
    Webserver/DB/Flask App
        Docker container -  docker-compose up
        Loads init.sql file to start db
        Flask app accesses DB and returns via AJAX calls

        https://gabimelo.medium.com/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e



Vote prog
---------
PROJECT1: Steps
-----

    - Python to talk to database
    - Submit vote
    - Start up queue
    - Put vote in queue
    - Encrypt vote

    


    * Register domains
    * Decide minimal viable product
    * Put that in week timetable
    * Create DB model
    * Create simple register vote form

    * Add Ajax to populate
        * Add as view
        * Alter form
    * Drop down in form
    * Population of drop down
    * Change vote back from manytomany
    * Post form back
    * Activate submit button after postcode

    * Put code into git
    * Create DB
    * ActiveMQ docker image
    * Put into git

    * Dockerize things 
    * Put whole thing in docker-compose

    *   possibly nginx & gunicorn
    *   https://gunicorn.org/#quickstart

    * Put vote onto queue

    - Setup databse:
        Vote line

    - Put vote into database
    - Look up using democracy club
    - encrypt vote


    - Automatic test -init
    - Deploy on server

    - Connect to mapit initially
    - Ansible deployment

    - Validate inputs
        - Emails
        - Other things

    - Something to pull off queue and add to vote db

    - Simple diplay of list of votes

    - Add constituency winning limits in - just a file is fine - redeploy

    - Read about constituencies, party information
    - Create DB loader for constituencies
    - Add constituencies in
        https://www.doogal.co.uk/ElectoralConstituencies.php
    - Add party information in
    - Add constituency information in
    - Need to account for parties that have never stood (asking for a friend)

    - Update vote form (Just revote) Prepopulate from URL  
    - Vote deletion/unsubscribe form - email confirmation
    - Email confirmation 

    - Connect to stats about previous voting in the area

    - Link for people to email if there is an issue

    - Accessibility check
    - Add a map
    - Add email to ask to update
    - Add privacy policy
    - Add About section to front end
    - Add queue to allow scaling if required
    - encrypt push t queue
    - Use remote queue and do processing locally to secure
    - Encrpyt into queue so no security issues
    - Talk to MVM, Guardian, monbiot
    - Talk to LibDems, Green party, maybe labour, WEP
    - Anyway to unlink the email from the vote?
    - Vote form must say this isn't actually a vote - just a poll
    - Log all interactions
    - Add in recaptcha type thing
    - Do I need to split general and local elections
    - Performance test
    - Deploy
    - Scale up
    - Unit tests
    - Recatcha

    - Add party logo
    - What order for parties in form
    - Could put multiple parties - tell people what they need to win

    - Get manifesto-vote sites to link to me afterwards
    - Improve regex for postcode
    - Provide anonomized database for others



PROJECT1: Running this
------------
    start database
        app/database: docker-compose up -d

    start website, postcode db, activemq
        docker build . -t voteapp:v0
        app/webvote: docker-compose up -d

    start consumer
        app/voteconsumer (not docker yet)

    start processor
        

    http://localhost:8000/vote/
    http://localhost:8161/admin/queues.jsp
PROJECT1: MVP
---
    Submit a vote
    Re-vote
    Delete your vote
    Constituencies in
    Thresholds in
    Parties in
    Very simple display in

    Simple website
    Privacy statement
    Secure machine
    Backups
    Secure database


PROJECT1: Domains
-------
    myvote.org.uk - Got
    uk.vote - Not assigned - might be expensive

PROJECT1: Views we need
-------------
    Voters
        Vote/Change vote (goes to click on link email)
        Click on link response page
        Delete my votes

    Public
        Show all votes/Map of votes

    Admin
        Remind people control
        Set thresholds/winning limits

PROJECT1: Database items:

Voter
    ID
    Email Address
    Postcode
    
Constiuencies
    ID
    Name

Parties
    ID
    Party Name

Voter<->Party
    Voter ID
    Party ID
    Reason (optional)

Party<->Constiuency
    Party ID
    Constituency ID




PROJECT1: Inital steps
-------------
    Virtualenv
    virtualenv --python=python3 voteapp
    cd voteapp
    source bin/activate
    pip install django
    django-admin startproject voteapp
    django-admin startapp vote
    python3 manage.py runserver

PROJECT1: Redo db:
--------
    rm db.sqlite3
    rm vote/migrations/0001_initial.py
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

PROJECT1: Postgres
--------
    CREATE DATABASE postcodes;
    \c polls;
    CREATE USER postcodes WITH PASSWORD 'postcodes'
    ALTER ROLE postcodes SET client_encoding TO 'utf8';
    ALTER ROLE postcodes SET default_transaction_isolation TO 'read committed';
    ALTER ROLE postcodes SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE polls TO postcodes;

    Expose network here but should just be able to do within docker

    Loading the whole thing up.
    Put in init db script
    Migrating the db
    Export that DB
    Using that as init script

    Output initial DB to put back into init script
        docker exec -i postcodes pg_dump --username postcodes postcodes > testdbout

PROJECT1: Postcode loader
---------------
    Order:
    Postcode,In Use?,Latitude,Longitude,Easting,Northing,Grid Ref,Introduced,Terminated,Altitude,Population,Households,Nearest Station,Distance To Station (KM),Built Up Area,Built Up Area Sub-Division,Water
 Company,Sewage Company

    Management command:
        https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/


PROJECT1: Dockerizing
-----------
    https://www.digitalocean.com/community/tutorials/how-to-build-a-django-and-gunicorn-application-with-docker
    https://blog.logrocket.com/dockerizing-a-django-app/
    docker run -p 127.0.0.1:8000:8000 docker-django-v0.0

    docker build . -t docker-vote

    docker build . -t voteapp:v0
    docker-compose up
    docker exec -it --env-file env vote sh -c "python manage.py makemigrations && python manage.py migrate"
    docker exec -it --env-file env vote sh -c "echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('keith', 'admin@myproject.com', 'keith')\" | python manage.py shell"
    docker exec -i postcodes pg_dump --username postcodes postcodes > testdbout


PROJECT1: Running it for dev
------------------
    docker build . -t voteapp:v0
    docker-compose up
    docker exec -it --env-file env vote sh -c "python manage.py makemigrations && python manage.py migrate"
    docker exec -it --env-file env vote sh -c "echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('keith', 'admin@myproject.com', 'keith')\" | python manage.py shell"


PROJECT1: Adding in email
---------------
    https://www.twilio.com/blog/build-email-newsletter-django-twilio-sendgrid
    https://pythoncircle.com/post/657/adding-email-subscription-feature-in-django-application/
    https://www.freecodecamp.org/news/build-your-own-serverless-subscriber-list-with-go-and-aws/

Loading postcode/representative data

    Postcodes
        Small Area
        Big Area

    Small Area
        List of parties

    Big area
        List of parties

------------------------------------------------------------------------------


PROJECT1: File structure
--------------
    voteapp
        voteapp
            settings
        vote

        requirements.txt
        db.sqlite3
        Dockerfile
        docker-compose.yml
            

    voteapp
        appdev
        apprelease
        appgit
            deploy
            webvote

PROJECT1: ActiveMQ stuff
--------------
    https://ameyanekar.medium.com/create-an-activemq-client-using-python-c532b6f91074
    need the stomp library (add to requirements)
    https://github.com/apache/activemq/blob/main/assembly/src/release/examples/stomp/python/stomppy/publisher.py

PROJECT1: Connect to vote DB
-----------------
    pip install psycopg2
    admin, admin
    votes, votes


