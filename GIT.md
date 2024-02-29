# Git Basics and Centralized vs Distributed Version Control Systems 

## Centralized vs Distributed VCS

### Centralized VCS

In a centralized VCS, there is a single, central repository. Teams would clone the entire repository and push changes directly to this central server.
The cons of using a centralized VCS is that once someone is writing to the file, it remains in a locked state and cannot be worked on by other members, this is problematic as teams get bigger.
![img.png](img.png)

### Distributed VCS

In a distributed VCS, every member pulls from the main repo and has their own local repository with complete history and branches. Changes are shared between repositories through pushing, pulling, and merging. This allows teams to work on the same file at the same time.

Git is an example of a distributed version control system

![img_1.png](img_1.png)

## Common Workflow Commands

1. **Init**: Initialize a repository (creates and tracks with .git).

2. **Add**: Add file changes to the staging area.

3. **Commit**: Record changes to the repository.

4. **Push**: Upload local repository changes to a remote repository.

5. **Pull**: Fetch changes from a remote repository and merge them into the current branch.

6. **Status**: Show the status of working directory and staging area.

## Additional Commands
7. **Log**: Show commit logs.

8. **Diff**: Check the difference between commits.

9. **Checkout**: Change to another commit.

10. **Reset**: Revert to a previous commit (loses changes made after it, use with caution).

## Branching
Branching allows for parallel development without affecting the main branch. It's useful for isolating features, bug fixes, or experiments.

To create a new branch: <br>
git branch <branch_name>

To switch to a branch: <br>
git checkout <branch_name>
