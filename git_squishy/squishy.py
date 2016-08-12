#!/usr/bin/env python
from __future__ import print_function

import sys
import subprocess


class SquishyException(Exception):
    pass


class TooManyArgumentsException(SquishyException):
    EXIT_CODE = 1


class NoBaseBranchException(SquishyException):
    EXIT_CODE = 2


class NoSuchBranchException(SquishyException):
    EXIT_CODE = 3


def get_current_branch():
    """Return the current branch's name."""
    # current_branch = git rev-parse --abbrev-ref HEAD
    # assert_branch_exists(branch)
    # return current_branch
    return "test"


def assert_branch_exists(branch):
    """Check if a branch exists, exit if not."""
    cmd = ['git', 'rev-parse', '--verify', branch]
    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT
                         )
    (out, _) = p.communicate()
    if (p.returncode != 0):
        sys.exit(NoSuchBranchException.EXIT_CODE)


def get_base_branch():
    """Get the base branch name if specified in arguments."""
    if len(sys.argv) > 2:
        print("Only specify the base branch as an argument.")
        sys.exit(TooManyArgumentsException.EXIT_CODE)
    elif len(sys.argv) < 2:
        print("No base branch specified.")
        sys.exit(NoBaseBranchException.EXIT_CODE)
    else:
        base_branch = sys.argv[1]
        assert_branch_exists(base_branch)

    return base_branch


def get_diverged_commits(current_branch, base_branch):
    """Get the number of commits diverged from `base_branch`."""
    # git log base_branch..current_branch --pretty=oneline | count
    return 0


def squash(current_branch, commit_n):
    """Squash $commit_n commits on current_branch."""
    pass


def main():
    base_branch = get_base_branch()
    current_branch = get_current_branch()
    commit_number = get_diverged_commits(current_branch, base_branch)
    squash(current_branch, commit_number)
