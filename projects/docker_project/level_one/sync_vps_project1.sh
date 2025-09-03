#!/usr/bin/env bash

SOURCE_DIR="/home/anant/codes/bootcamp/projects/docker_project/level_one"
DEST="naruto@taklu.chickenkiller.com:/home/naruto/docker_project"
RSYNC_OPTS="-avz --delete"

while inotifywait -r -e modify,create,delete,move $SOURCE_DIR; do
	echo "Change detected, syncing.."
	rsync $RSYNC_OPTS --exclude-from='/home/anant/codes/bootcamp/projects/docker_project/level_one/rsync_ignore.txt' $SOURCE_DIR $DEST
	echo "Sync complete."
done
