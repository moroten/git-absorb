# Moroten's Development Tools

This repository contains a collection of small useful developer tools.

## git-absorb

Patch the git history with fixup commits of you unstaged changes.

Runs `git commit --fixup` on unstaged changes by analysing `git diff` and `git blame`.
Any paths given on the command line will be passed on to `git diff`.
The `git blame` command runs on the revs `$(git merge-base HEAD <upstream>)..HEAD`.

### Usage

* `git absorb origin/main`
* `git absorb -r origin/main` - The same as above but also call `git rebase --interactive origin/main`.
