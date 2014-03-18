
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "bb4df6f7-1f2f-4a79-90a7-cb1381470118f3fd9956-3d7d-4aae-85dc-ff3840b8aeb04bd52cb9-f7a5-4fdf-bea9-b373c2f93331"
NEVERCACHE_KEY = "471313b5-0fe2-4798-b52e-297ea2e250b13bdee414-7a38-4eeb-8814-cafa8695f4dc5cdacf2d-eb10-4a69-a629-232af502988f"

FABRIC = {
     "SSH_USER": "vagrant", # SSH username
     "SSH_PASS":  "vagrant", # SSH password (consider key-based authentication)
     "SSH_KEY_PATH":  "", # Local path to SSH key file, for key-based auth
     "HOSTS": ["192.168.124.12"], # List of hosts to deploy to
     "VIRTUALENV_HOME":  "/home/vagrant", # Absolute remote path for virtualenvs
     "PROJECT_NAME": "test_deploy", # Unique identifier for project
     "REQUIREMENTS_PATH": "requirements/project.txt", # Path to pip requirements, relative to project
     "GUNICORN_PORT": 8000, # Port gunicorn will listen on
     "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
     "LIVE_HOSTNAME": "192.168.124.12", # Host for public site.
     "REPO_URL": "git://github.com/cchuang6/test_deploy.git", # Git or Mercurial remote repo URL for the project
     "DB_PASS": "password", # Live database password
     "ADMIN_PASS": "default", # Live admin user password
     "SECRET_KEY": SECRET_KEY,
     "NEVERCACHE_KEY": NEVERCACHE_KEY,
}


DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
