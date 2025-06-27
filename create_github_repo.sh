#!/bin/bash

# This script creates a new GitHub repository using GitHub CLI and sets it as the remote origin

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null
then
    echo "GitHub CLI (gh) could not be found. Please install it first."
    exit 1
fi

# Prompt for repository name
read -p "Enter the new GitHub repository name: " repo_name

# Create the repository on GitHub (private by default)
gh repo create "$repo_name" --private --confirm

# Set the new repository as the remote origin
git remote set-url origin git@github.com:$(gh api user --jq '.login')/"$repo_name".git

echo "New repository created and remote origin set to git@github.com:$(gh api user --jq '.login')/$repo_name.git"
echo "You can now push your code using: git push -u origin main"
