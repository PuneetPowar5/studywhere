#!/bin/bash

# Define the command to be executed by the cron job
COMMAND="curl http://127.0.0.1:5000/api/notifyUsers?eventId=1 >/dev/null 2>&1"

# Define the cron schedule
SCHEDULE="*/1 * * * *"

# Define the crontab file name
CRONTAB_FILE="my_cronjob"

# Create a new crontab file with the new cron job
echo "$SCHEDULE $COMMAND" > $CRONTAB_FILE

# Add the crontab file to the system crontab
crontab $CRONTAB_FILE

# Print the current list of cron jobs for verification
crontab -l
