#!/bin/bash
echo "Enter your Favourite Commit Message:"
read message
git add .
git commit -m "$message"
git push
