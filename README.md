# Sublime plugin: Open In SourceTree

Sublime Text 3 plugin for openning project in Atlasian SourceTree right from editor.


## Installation

    $ cd ~/Library/Application Support/Sublime Text 3/Packages
    $ git clone https://github.com/voidius/sublime-open-in-sourcetree.git OpenInSourceTree

NB! It is important to save this plugin in directory called "OpenInSourceTree"

### Optionally

If you wish you can install the command line tool for SourceTree. This can be done by clicking on the SourceTree menu and then on Install Command Line Tools - an executable named 'stree' will be created inside /usr/local/bin.

In case you don't have 'stree' in your $PATH, plugin will try to execute SourceTree.app inside /Applications.


## Usage

* through Command Palette: search for "Open In SourceTree" command
* through keyboard shortcut: super+k, super+s by default


## Configuration

See commentaries in Default settings file (Default.sublime-settings)
