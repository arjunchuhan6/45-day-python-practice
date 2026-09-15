# Git and GitHub command reference

# Configure your name for Git commits.
# git config --global user.name "Your Name"

# Configure your email for Git commits.
# git config --global user.email "you@example.com"

# Display the installed Git version.
# git --version

# Create a new Git repository in the current folder.
# git init

# Show the current branch and changed files.
# git status

# Add one file to the staging area.
# git add filename.py

# Add all changed and untracked files to the staging area.
# git add .

# Remove a file from the staging area without deleting it.
# git restore --staged filename.py

# Save staged changes in the local repository.
# git commit -m "Describe the changes"

# Display the commit history.
# git log

# Display the commit history in a compact format.
# git log --oneline

# Show unstaged changes in tracked files.
# git diff

# Show staged changes waiting for the next commit.
# git diff --cached

# Rename the current branch to main.
# git branch -M main

# List all local branches.
# git branch

# Create and switch to a new branch.
# git switch -c feature-name

# Switch to an existing branch.
# git switch branch-name

# Merge another branch into the current branch.
# git merge branch-name

# Add a GitHub repository as a remote named origin.
# git remote add origin https://github.com/username/repository.git

# Display configured remote repositories.
# git remote -v

# Upload the main branch to GitHub and remember the remote branch.
# git push -u origin main

# Upload later commits to GitHub.
# git push

# Download remote commits and update the current branch.
# git pull

# Download remote information without changing local files.
# git fetch

# Copy an existing GitHub repository to your computer.
# git clone https://github.com/username/repository.git

# Create a file listing files Git should ignore.
# New-Item .gitignore

# Remove a file from Git tracking but keep it on the computer.
# git rm --cached filename.py

# Remove a tracked file from Git and from the computer.
# git rm filename.py

