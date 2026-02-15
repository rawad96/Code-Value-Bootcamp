from solution.git_simulator import extract_and_check_command
import pytest


def test_git_simulator_stash_commands() -> None:
    assert (
        extract_and_check_command("git stash")
        == "Temporarily shelves changes in your working directory so you can work on a different task."
    )
    assert (
        extract_and_check_command("git stash push -m stash_message")
        == "Stashes changes with a custom message stash_message for easy identification."
    )
    assert (
        extract_and_check_command("git stash apply")
        == "Applies the most recently stashed changes."
    )
    assert (
        extract_and_check_command("git stash apply stash")
        == "Applies the stashed changes with the specified name stash."
    )


def test_git_simulator_add_commands() -> None:
    assert (
        extract_and_check_command("git add .")
        == "Stage all changes for the next commit."
    )
    assert (
        extract_and_check_command("git add file.txt")
        == "Stage a specific file file.txt for the next commit."
    )


def test_git_simulator_commit_and_push_commands() -> None:
    assert (
        extract_and_check_command("git commit -m Initial_commit")
        == "Commit changes to the repository with a descriptive message Initial_commit."
    )
    assert (
        extract_and_check_command("git push")
        == "Upload your commits to the remote repository."
    )


def test_git_simulator_with_invalid_command() -> None:
    with pytest.raises(ValueError, match="Invalid Git Command"):
        extract_and_check_command("git invalid_command")
