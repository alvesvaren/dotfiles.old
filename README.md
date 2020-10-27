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

## Structure

The project uses git branches to manage different devices.
For example: the *laptop* branch has some commits specific to my laptop and the *pc* branch has some for my pc.

This allows me to use the *main* branch as a base for new devices, and values specific to each device (like outputs etc.)

To use my files with your computer, use the *main* branch and check out the differences between that and whatever branch is closest to your device

> Tip: to change branch, type `git checkout branchname`

