from enum import Enum


class GitCommand(str, Enum):
    GIT = "git"
    PUSH = "push"
    ADD = "add"
    STASH = "stash"
    APPLY = "apply"
    RM = "rm"
    COMMIT = "commit"
    CACHED = "--cached"
    MESSAGE_FLAG = "-m"


def check_git_stash_commands(command_parts: list) -> str:
    match command_parts:
        case [GitCommand.GIT, GitCommand.STASH]:
            return f"Temporarily shelves changes in your working directory so you can work on a different task."
        case [GitCommand.GIT, GitCommand.STASH, GitCommand.PUSH, "-m", stash_message]:
            return f"Stashes changes with a custom message {stash_message} for easy identification."
        case [GitCommand.GIT, GitCommand.STASH, GitCommand.APPLY]:
            return f"Applies the most recently stashed changes."
        case [GitCommand.GIT, GitCommand.STASH, GitCommand.APPLY, stash_name]:
            return f"Applies the stashed changes with the specified name {stash_name}."
        case _:
            raise ValueError("Invalid Git Command")


def check_git_add_commands(command_parts: list) -> str:
    match command_parts:
        case [GitCommand.GIT, GitCommand.ADD, "."]:
            return "Stage all changes for the next commit."
        case [GitCommand.GIT, GitCommand.ADD, filename]:
            return f"Stage a specific file {filename} for the next commit."
        case _:
            return check_git_stash_commands(command_parts=command_parts)


def extract_and_check_command(command_string: str) -> str:
    command_parts = command_string.split()
    if command_parts[0] != GitCommand.GIT:
        raise ValueError("Invalid Git Command")
    match command_parts:
        case [GitCommand.GIT, GitCommand.RM, GitCommand.CACHED, filename]:
            return f"Unstage file {filename} while retaining the changes in the working directory."
        case [
            GitCommand.GIT,
            GitCommand.COMMIT,
            GitCommand.MESSAGE_FLAG,
            commit_message,
        ]:
            return f"Commit changes to the repository with a descriptive message {commit_message}."
        case [GitCommand.GIT, GitCommand.PUSH]:
            return f"Upload your commits to the remote repository."
        case _:
            return check_git_add_commands(command_parts=command_parts)


def git_commands_simulator() -> None:
    while True:
        command_expression = input("Please enter a git command: ")
        if command_expression == "exit":
            break
        try:
            print(extract_and_check_command(command_string=command_expression))
        except ValueError as err:
            print(err)


if __name__ == "__main__":
    git_commands_simulator()
