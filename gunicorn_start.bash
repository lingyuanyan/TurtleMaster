#!/bin/bash

NAME="TurtleMaster"                                  # Name of the application
DJANGODIR=/home/wwwadmin/TurtleMaster             # Django project directory
SOCKFILE=/home/wwwadmin/TurtleMaster/TurtleMaster.sock  # we will communicte using this unix socket
USER=wwwadmin                                        # the user to run as
GROUP=wwwadmin                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=TurtleMaster.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=TurtleMaster.wsgi:application                     # WSGI module name
PYTHON_VENV=venv_t
echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source $PYTHON_VENV/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $PYTHON_VENVT/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
