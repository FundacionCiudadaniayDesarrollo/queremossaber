#!/bin/bash

NAME="queremossaber"                                  # Name of the application
DJANGODIR=/home/queremos/app/queremossaber            # Django project directory
SOCKFILE=/home/queremos/app/queremossaber/run/$NAME.sock  # we will communicte using this unix socket
USER=queremos                                      # the user to run as
GROUP=queremos                                     # the group to run as
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=$NAME.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=$NAME.wsgi                     # WSGI module name
VIRTUAL=/home/queremos/virtualenv/app/2.7       # Virtualenv

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source $VIRTUAL/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $VIRTUAL/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
