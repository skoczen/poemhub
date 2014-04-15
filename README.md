This is the repository for poetr.com.

Keep an eye on it. :)


# Setup:
heroku addons:add memcachier --app poetr
heroku addons:add redistogo:nano --app poetr
heroku addons:add heroku-postgresql --app poetr
heroku addons:add pgbackups:auto-month --app poetr
heroku addons:add pointdns --app poetr