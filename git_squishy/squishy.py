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


class NoCurrentBranchException(SquishyException):
    EXIT_CODE = 4


def run_cmd(cmd, exception_klazz=None, exception_msg=None):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (out, err) = p.communicate('stdout')
    out = out.decode('utf-8', 'replace')
    exit_code = p.returncode
    if exit_code != 0 and exception_klazz:
        raise exception_klazz(exception_msg)
    return (out.strip(), err, exit_code)


def get_current_branch():
    """Return the current branch's name."""
    cmd = ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
    (current_branch, _, _) = run_cmd(cmd, NoCurrentBranchException, "Could not get current branch")
    return current_branch.strip()


def assert_branch_exists(branch):
    """Check if a branch exists, raise an exception if not."""
    cmd = ['git', 'rev-parse', '--verify', branch]
    run_cmd(cmd, NoSuchBranchException, "Branch %s does not exist." % branch)


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


def get_diverged_commits(base_branch):
    """Get the number of commits diverged from `base_branch`."""

    # git log base_branch..current_branch --pretty=oneline | count
    cmd = ['git', 'log', str(base_branch) + '..', '--pretty=oneline']
    # TODO(rski) implement an exception for this?
    (out, _, _) = run_cmd(cmd)
    if out:
        commit_n = out.count("\n") + 1
    else:
        commit_n = 0

    return commit_n


def squash(current_branch, commit_n):
    """Squash $commit_n commits on current_branch."""
    pass


def _main():
    base_branch = get_base_branch()
    current_branch = get_current_branch()
    commit_number = get_diverged_commits(base_branch)
    squash(current_branch, commit_number)


def main():
    """Main"""
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
