#!/bin/bash
tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 omAPI.views.app:app'
echo "API server started..."
tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 profpage:app'
echo "Profile server started..."
tmux new-session -d 'python3 -m classes.scheduler'
echo "Post scheduler started..."
echo "Finished"
