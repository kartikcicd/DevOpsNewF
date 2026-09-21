# A Version control system (VCS) is a tool used in software development and collaborative projects to track and manage changes to source code.
# Features of a VCS include:
# 1. Version Tracking: VCS allows developers to keep track of changes made to the source code over time. 
#    Each change is recorded as a new version, enabling developers to view the history of modifications and revert to 
#    previous versions if needed.
# 2. Collaboration: VCS enables multiple developers to work on the same codebase simultaneously.
# 3. Branching and Merging: VCS allows developers to create branches, which are separate lines of development.

# Three Types of Version Control Systems:
# 1. Local Version Control Systems: In a local VCS, all the version history is stored on the local machine. 
#    Developers can track changes and revert to previous versions, but collaboration is limited.
# 2. Centralized Version Control Systems (CVCS): In a CVCS, there is a central server that stores the version history, 
#    and developers commit their changes to this central server. This allows for better collaboration but creates a single 
#    point of failure.
# 3. Distributed Version Control Systems (DVCS): In a DVCS, each developer has a complete copy of the entire version history 
#    on their local machine. 
# Local repo -> central repo -> other developers' local repos.

# Git is a distribted VCS that is used to track changes in source code during software development. 
# It is designed for coordinating work among programmers, but it can be used to track changes in any set of files. 
# Its goals include speed, data integrity, and support for distributed, non-linear workflows.

# -> Multiple developers can work on the same project without interfering with each other.
# -> Revert to previous versions of a project or file.
# -> Develop features in isolation from the main codebase.
# -> Each developer has a full local copy of the entire project history, which allows for easy branching and merging.
# -> Stores snapshots of the entire project, rather than just differences between files, 
#    which allows for more efficient storage and retrieval of data.

# Repository
# 1. Local Repo: A copy of the project that is present on your local machine
# 2. Remote Repo: A version of the project that is hosted on a remote server, such as GitHub, GitLab, or Bitbucket.

# Commits
# A commit is a snapshot of the project at a specific point in time. 
# Each commit has a unique identifier (hash) and contains information about the changes made, the author, and the timestamp.

# Branches
# A branch is a separate line of development in a Git repository.
# It allows developers to work on new features, bug fixes, or experiments without affecting the main codebase.
# The default branch in a Git repository is usually called "main" or "master".
# Main (or Master) Branch: The primary branch where the stable version of the project is maintained (Production ready code). (prod)
# Feature Branch: Used for developing new features and bug fixes (dev, qa, staging, etc.). (development code, testing, bug fixes, etc.)
# bugFix Branch -> main branch

# Merging
# Merging is the process of integrating changes from one branch into another.
# It combines the changes made in different branches and creates a new commit that represents the merged state

# Cloning
# Cloning is the process of creating a local copy of a remote repository.

# Pull and Push
# Pull: The process of fetching and integrating changes from a remote repository into your local repository.
# Push: The process of sending your local commits to a remote (Centralized) repository.

# Three States of Git
# Working Dir -> Staging Area (Commit)-> Local Repository -> (Push) Remote Repository
# 1. Working Directory: The files and directories that you are currently working on.
# 2. Staging Area: A temporary area where you can prepare changes before committing them.
# 3. Local Repository: A local copy of the entire project history, including all commits and branches.
# 4. Remote Repository: A version of the project that is hosted on a remote server, such as GitHub, GitLab, or Bitbucket.


# 1. git init - Initializes a new Git repository in the current directory. 
# It creates a .git directory that contains all the necessary files and metadata for version control.

# 2. git add <filename> - Adds changes in the specified file(s) to the staging area, preparing them for the next commit.