# Gunicorn configuration file for TrainingProtec backend
# Server: /var/www/tranning/backend/

# Server socket
bind = "127.0.0.1:5050"

# Worker processes
workers = 3

# Worker class
worker_class = "sync"

# Timeout for worker processes (seconds)
timeout = 120

# Maximum number of requests a worker will handle before being restarted
max_requests = 1000
max_requests_jitter = 50

# Preload app for faster worker boot
preload_app = True

# Logging
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"

# Process naming
proc_name = "trainingprotec"

# PID file
pidfile = "/var/run/gunicorn/trainingprotec.pid"

# Daemon mode - OFF (systemd manages the process)
daemon = False

# User and group
user = "www-data"
group = "www-data"

# Working directory
chdir = "/var/www/tranning/backend"

# WSGI module
wsgi_app = "app:app"
