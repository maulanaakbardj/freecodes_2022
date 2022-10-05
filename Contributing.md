## Git Commands for a Simple Workflow

The following steps are enough for creating a pull request.

- Create a Fork of this repository.
- Simply click on the “fork” button of the repository page on GitHub.
- Clone your Fork
    The standard clone command creates a local git repository from your remote fork on GitHub.
    ```
    git clone https://github.com/USERNAME/REPOSITORY.git
    ```
- Modify the Code
    Add the changed files to the staging area with the command 
    ```
    git add -A
    ```
    Once you are satisfied with the added files, you can then commit them to your local repository with the commit command as follows:
    ```
    git commit -m "INSERT YOUR COMMIT MESSAGE HERE"
    ```

- Push your Changes
    In your workspace, use the git push command to upload your changes to your remote fork on GitHub.
    ```
    git push remote origin
    ```

- Create a Pull Request

    On the GitHub webpage of your remote fork, click the “pull request” button and make a pull request from your repo's branch to this repository's base branch. Wait for the owner to merge or comment your changes and be proud when it is merged :)
