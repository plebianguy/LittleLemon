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
* in order to login and obtaine a token you must make a POST request to '.../auth/token/login/
* admin credentials:
    * username: admin
    * password: lemon@123!


