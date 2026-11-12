# Uganda Wildlife Authority website

The Django project is in `UWA/`. The Render web service is publicly available at
https://uwa-01-7.onrender.com.

## Database

Local development uses SQLite by default. To use persistent shared data on
Render, create a Render PostgreSQL database and set `DATABASE_URL` in the web
service environment to its **Internal Database URL**. Keep the URL private.
The deployment build runs Django migrations.

The current site has no user-registration feature; adding a PostgreSQL database
does not create registration or login pages.