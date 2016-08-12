#!/usr/bin/env python
from __future__ import print_function

import sys
import subprocess


class SquishyException(Exception):
    pass


class TooManyArgumentsException(SquishyException):
    """Only specify the base branch as an argument."""
    EXIT_CODE = 1


class NoBaseBranchException(SquishyException):
    """No base branch specified."""
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
    (_, _) = p.communicate()
    if p.returncode != 0:
        raise NoSuchBranchException("Branch %s does not exist." % branch)


def get_base_branch():
    """Get the base branch name if specified in arguments."""
    if len(sys.argv) > 2:
        raise TooManyArgumentsException("More than one arguments specified. The only argument should be the base branch.")
    elif len(sys.argv) < 2:
        raise NoBaseBranchException("Base branch name not specified.")
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


def _main():
    base_branch = get_base_branch()
    current_branch = get_current_branch()
    commit_number = get_diverged_commits(current_branch, base_branch)
    squash(current_branch, commit_number)


def main():
    try:
        _main()
    except SquishyException as e:
        try:
            u = unicode(e)
        except NameError:
            print(e)
        else:
            print(u.encode('utf-8'))

        sys.exit(e.EXIT_CODE)
