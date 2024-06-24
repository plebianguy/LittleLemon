# LittleLemon
This is a website for the fictitious boutique restaurant, LittleLemon, constructed for the capstone project of Meta Back-End Development Professional Certificate capstone project


## API endpoints:

### Menu Items:

* .../restaurant/menu 
    * GET: lists all menu items.
    * POST: Creates a new menu item

* .../restauran/menu/<int:pk>
    * GET: gets a single menu item identified by pk
    * DELETE : deletes a menu item, identified by pk

### Bookings:

* .../restaurant/booking/tables
    * GET: lists all the bookings
    * POST: creates a new booking

### Authentication:
* uses default Djoser endpoints for authentication. 
( see https://djoser.readthedocs.io/en/latest/base_endpoints.html )

* username field name: username
* in order to login, you must first create a user/superuser in your local database.
     * python manage.py createsuperuser
     * after creating the admin user, you can go ahead and create more by either:
        * Sending a post request to .../auth/users/
        * manually creating a user through the admin interface

### Tests:
* There are several unit tests inside tests.py and test_views.py
* Running the command python manage.py test will execute these tests
* Note that the tests use the sqlite database instead of your local mysql client.
* There are tests fo all api functionalities in test_views
* There are tests for model object creation and retrieval in tests.py


