#!/bin/bash
tmux send-keys -t scheduler "C-c"
echo "Scheduler stopped..."
tmux send-keys -t profileserv "C-c"
echo "Profile server stopped..."
tmux send-keys -t apiserv "C-c"
echo "API server stopped..."
echo "Finished"
