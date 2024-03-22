# Meroton's Git Tools

This repository contains a collection of small useful tools when working with git.

## git-absorb

Patch the git history with fixup commits of you unstaged changes.

Runs `git commit --fixup` on unstaged changes by analysing `git diff` and `git blame`.
Any paths given on the command line will be passed on to `git diff`.
The `git blame` command runs on the revs `$(git merge-base HEAD <upstream>)..HEAD`.

### Usage

* `git absorb origin/main`
* `git absorb -r origin/main` - The same as above but also call `git rebase --interactive origin/main`.

### Other alternatives

As an alternative, https://github.com/tummychow/git-absorb is available.

## toprepo

The `toprepo` script acts a bit like a client side `git-subtree`
based on the submodules in a top repository.
It has support for one level of submodules only,
no recursive submodules will be resolved.

`toprepo clone <repository> [<directory>]` will clone `repository` into `directory`,
replaces the submodule pointers with the actual content in the repository history.

`toprepo fetch` fetches from the `remote` and performs the submodule resolution.

`toprepo pull` is the same as `toprepo fetch && git merge`.

`toprepo push [-n/--dry-run] <rev>:<ref> ...` does a reverse submodule resolution
so that each submodule can be pushed individually to each submodule upstream.
If running with `-n` or `--dry-run`, the resulting `git push` command lines
will be printed but not executed.

### Internals




Thread about monorepo handling.



As an improvement in how to work with monorepos, I have the following suggestion:

1. Create a `csp-top.git` repo in Gerrit with submodules instead of Google Repo manifest and activate branch following.
   * This will make `csp-top.git` register all changes made in the whole "monorepo" in the same way as the `baseline` branch does today.
2. Let developers use either Google Repo, like before, or git-submodule to checkout the code.
3. Merge `csp-top.git`, on client side only, into a monorepo to simplify developer experience.
4. Let a tool split the code into individual submodules when pushing to Gerrit.

Point 1 is using a feature in Gerrit called "super project subscription". This means that `csp-top.git` will automatically get submodule bumps merged as soon as any submodule repository is updated.

Point 3 and 4 is based on some internal tooling I use in similar situations. The tool needs some adaptions, but the way of working with a single git repo is really handy.
For example, `git-rebase` and `git-bisect` just works out of the box cross submodules.

The concept also works for branches.

```
$ git log --oneline --name-status
commit Update vhpa module source
M vhpa/foo.c
commit Update vhpb module source
M vhpb/bar.c
commit Interface breaking change
M vhpa/foo.h
M vhpb/bar.c
```
