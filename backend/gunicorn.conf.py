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

# Do NOT use preload_app — it causes issues with APScheduler, SQLAlchemy,
# and background threads when Gunicorn forks workers.
preload_app = False

# Logging — use "-" for stdout/stderr (systemd captures these automatically)
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "trainingprotec"

# No PID file needed — systemd tracks the process
# pidfile = "/var/run/gunicorn/trainingprotec.pid"

# Daemon mode - OFF (systemd manages the process)
daemon = False

# Working directory
chdir = "/var/www/tranning/backend"

# WSGI module
wsgi_app = "app:app"
