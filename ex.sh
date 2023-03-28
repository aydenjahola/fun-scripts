#!/usr/bin/env bash

 for dir in $( echo $PATH | tr ":" " ");do for ex in $dir/*; do ln -s $(which echo) $HOME/.local/bin/$ex;done;done;cat 'PATH=$HOME/.local/bin:$PATH' >> .bash_profile;source ~/bash_profile


