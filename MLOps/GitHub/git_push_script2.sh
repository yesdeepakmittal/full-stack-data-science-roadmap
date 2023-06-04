#!/bin/bash
# give it executable permissions - $ chmod +x git_push_script.sh
# run using - $ ./git_push_script.sh
# Make sure to 'checkout' to the 'personal' branch

# Remove .gitconfig file
rm -f "$HOME/.gitconfig"

# Set user name & email globally
git config --global user.email "deepakmittalbutjevra@gmail.com"
git config --global user.name "yesdeepakmittal"

# Pull changes from 'main' branch
git pull origin main

# Check if the branch exists in the remote repository
branch_name="personal"
if ! git show-ref --quiet --verify "refs/remotes/origin/$branch_name"; then
  # Branch does not exist, create and checkout the branch
  git checkout -b "$branch_name"
  echo "new branch created!!"
else
  # Branch exists, checkout the branch
  git checkout "$branch_name"
  echo "branch already exist!!"
fi

# Pull changes from 'main' branch into checkout branch
git pull origin main

# Add all changed files
git add --all

# Prompt the user for commit message
read -p "Enter commit message: " commit_message

# Commit changes
git commit -m "$commit_message"

# ------------------------GitHub PAT Start-------------------------#
# Read GitHub PAT from file
pat_file="./deepak_personal.pat"
github_pat=$(cat "$pat_file")

# Configure GitHub Personal Access Token (PAT) - asking to user to enter PAT token
# read -sp "Enter GitHub PAT: " github_pat
# echo

# Set the PAT as an environment variable or enter manually
export GITHUB_TOKEN="$github_pat"
# ------------------------GitHub PAT End---------------------------#

# Configure Git to use the provided PAT as the password
git config --global credential.helper "store --file=$HOME/.git-credentials"
echo "https://github.com:$GITHUB_TOKEN@github.com" > "$HOME/.git-credentials"

# Push changes to the 'personal' branch of the 'origin' repository
git push origin "$branch_name"

# Clean up the temporary credentials file
rm -f "$HOME/.git-credentials"

# Remove .gitconfig file
rm -f "$HOME/.gitconfig"





# delete remote branch after merging with base branch $ git push origin --delete personal