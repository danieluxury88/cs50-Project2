## CS50 - Project 2 Commerce

Design an eBay-like e-commerce site that allows post auction listing, place bids, comment, and add listings to a watchlist.

This project belongs to SQL, Models and Migrations chapter.

## Knowledge
- See [Django's Model field reference.](https://docs.djangoproject.com/en/4.0/ref/models/fields/)
- See [Django's forms.](https://docs.djangoproject.com/en/4.0/topics/forms/)
- Django decorators
  - Add @login_required decorator on any view to grant access to logged in users.

## Tasks
- [x] Create superuser **python manage.py createsuperuser**
- [x] Create models: user, auction listing, bids, comments and watchlist.
- [x] Create listings: allow user to enter title, description, starting bid, image URL, category.
- [x] Active listings page: default page with active listings.
- [ ] Listings page: Clicking on a listing should take to listing details.
  - [x] Add/Remove from watchlist.
  - [x] Place valid bid.
  - [x] If owner, ability to close bid.
  - [ ] Notify if auction has been won.
  - [x] Allow comments.
- [ ] Watchlist page.
- [ ] Categories page.
- [ ] Admin interface to view, add, edit, delete listings, comments and bids.