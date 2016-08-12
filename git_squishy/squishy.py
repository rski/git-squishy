#!/usr/bin/env python
from __future__ import print_function

import sys


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
    return "test"


def check_branch_exists(branch):
    """Check if a branch exists, exit if not."""
    pass


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
        check_branch_exists(base_branch)

    return base_branch


def get_diverged_commits(base_branch):
    """Get the number of commits diverged from `base_branch`."""


def squash(current_branch, base_branch):
    pass


def main():
    base_branch = get_base_branch()
    current_branch = get_current_branch()
    get_diverged_commits(base_branch)
    squash(current_branch, base_branch)
