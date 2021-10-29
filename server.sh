  GNU nano 4.8                       server.sh                        Modified  
#!/bin/bash
cd /var/www/myapp
. venv/bin/activate
cd src
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
