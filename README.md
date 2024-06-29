<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Dotfiles](#dotfiles)
    - [Install](#install)
    - [Repository Setup](#repository-setup)
    - [External Links](#external-links)

<!-- markdown-toc end -->

# Dotfiles
My own set of dotfiles

## Install
First and foremost, install Chezmoi. My method of doing so was with [Linux Homebrew](https://brew.sh). Taken from its website, the easiest way to install brew is with this:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After Homebrew is installed, use it to install Chezmoi:

```sh
brew install chezmoi
```

If everything goes well, you can now initialize the repository.

## Repository Setup

```sh
chezmoi init JohnDevlopment
```

This command will clone this repository into `~/.local/share/chezmoi`. When you first initialize the repository, you will be prompted for some information, so make sure you have those things on hand. They are:

1. Zoxide command (defaults to `cd`)
2. Your Github email address
3. Your Github username
4. Your Wandb username
5. Your Twitter username

After you provide all that information, a config file is generated: `~/.config/chezmoi/chezmoi.toml`. From there, you can start installing the dot files.

Firstly, I would recommend installing `~/.bashrc`. This file will not produce any errors when you source it. However, some of its components only get loaded when their respective files/directories exist. In order, they are:

1. `~/.bash_aliases`
2. `~/.bash_functions`
3. `~/.bash_completions`
4. `~/.bash_env`
5. `~/.cargo/env` - Rust environment

These files are *conditionally loaded*, that is, loaded if they exist.

After those are loaded, there is a section for loading zoxide. The recommended way to install zoxide is this:

```sh
curl -sSfL https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | sh
```

Alternatively, you can use a package manager (instructions can be found [here][Zoxide install]).

Once you are ready, type:

```sh
chezmoi apply ~/.bashrc
```

You can preview the changes before applying them. Type:

```sh
chezmoi diff ~/.bashrc
```

## External Links

1. [Chezmoi website](https://www.chezmoi.io)
   - [Install](https://www.chezmoi.io/install)
2. [Linux Homebrew](https://brew.sh)
3. [How to install zoxide][Zoxide install]

[Zoxide install]: https://github.com/ajeetdsouza/zoxide#installation
