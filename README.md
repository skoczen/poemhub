This is the repository for poemhub.org.

Keep an eye on it. :)


# Setup:
heroku addons:add memcachier --app poemhub
heroku addons:add redistogo:nano --app poemhub
heroku addons:add heroku-postgresql --app poemhub
heroku addons:add pgbackups:auto-month --app poemhub
heroku addons:add pointdns --app poemhub