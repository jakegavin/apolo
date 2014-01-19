# Ashland Water Polo

An informational website built for the Ashland High School Water Polo team.

This project uses the Python Imaging Library (PIL). 

Templates use bootstrap. 

The photo app is loosely based on the Portfolio app in [Djago by Example]
    (https://github.com/akulakov/django/tree/master/dbe) by akulakov


### To Do
*   General Items
    *   Write tests
    *   Clean up templates
        *   Move conditional constructs into views.py
    *   Add validators to models
    *   Create about link in footer (lightbox popup)
    *   Clean up CSS
    *   Install South for database migrations
*   Create resources app
    *   Password protect page
*   Create homepage
    *   Links to social media
*   Schedule App
    *   Fix sorting of schedules
    *   Add error message using {% empty %} if a tournament doens't have games added
    *   Turn opponent teams into objects
        *   Season stats page
*   Roster App
    *   Fix trailing comma on coaches roster list
        *   (', ').join(coach)
    *   Clean up coaches template page formatting. 
        *   Use divs instead of tables
*   Photos App
    *   Clean up photo app code fragments
    *   Fix lightbox 'X' off page
*   History Section
    *   Create Alumni App
*   Admin 
    *   Clean up admin panel 
        *   Sort categories
        *   Search
        *   Image thumbnails