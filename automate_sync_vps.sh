#!/usr/bin/env bash

SOURCE_DIR="/home/anant/codes/bootcamp"
DEST="naruto@taklu.chickenkiller.com:/home/naruto/"
RSYNC_OPTS="-avz --delete"

while inotifywait -r -e modify,create,delete,move $SOURCE_DIR; do
	echo "Change detected, syncing.."
	rsync $RSYNC_OPTS --dry-run --exclude-from='/home/anant/codes/bootcamp/rsync_exclude.txt' $SOURCE_DIR $DEST
	echo "Sync complete."
done
