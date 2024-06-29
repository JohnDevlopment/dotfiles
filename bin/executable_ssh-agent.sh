#!/bin/bash

if dir /tmp/tmp.ssh-agent* &>/dev/null; then
    cat /tmp/tmp.ssh-agent*
    exit $?
fi

tmpfile=$(mktemp --tmpdir tmp.ssh-agent.XXXXX)
ssh-agent > $tmpfile
cat $tmpfile
