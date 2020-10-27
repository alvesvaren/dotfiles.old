# My dotfiles

## Install files to file system:

> **IMPORTANT WARNING!** This will overwrite all your local dotfiles
```bash
./script.py install
```

Make sure all packages is installed from the file pkglist (these are the names for the Arch Linux and AUR packages)

## Update repo with local files:

```bash
./script.py copy
```

## Merge other branches with changes to *base*

Merge all other branches with base:

```bash
./merge.sh
```

Merge all other branches with base and push to origin:

```bash
SHOULD_PUSH=true ./merge.sh
```

## Structure

### Branches

The project uses git branches to manage different devices.
For example: the *laptop* branch has some commits specific to my laptop and the *pc* branch has some for my pc.

This allows me to use the *base* branch as a base for new devices, and values specific to each device (like outputs etc.)

To use my files with your computer, use the *base* branch and check out the differences between that and whatever branch is closest to your device.

> **Tip:** to change branch, type `git checkout branchname`
> To create a new branch, type `git checkout -b branchname`

> To view the difference between branches checkout a base branch, then type `git diff otherbranch`

### File structure

The file *filelist* contains one two values per line, separated by a space.


The first value is the location of the file relative to your `$HOME` variable.

The second value is the location of the file relative to the `files` directory in this repository.


For example, the row:
```
.config/i3/config i3/config
```
means that there's should be a file called config in the `$HOME/.config/i3/config`, and that this file is the same as the file in `./files/i3/config`

### Packages

The file *pkglist* contains all packages that should be installed for everything to work correctly.

The package names are Arch and AUR package names that should exist in either all Arch official repositories (core, extra, community or multilib) or in the AUR.

> If the AUR helper/pacman wrapper [Yay](https://github.com/Jguer/yay) is installed, an option to install these packages will appear when running `./script.py install`

