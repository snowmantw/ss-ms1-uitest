#!/bin/bash
openssl enc -aes-256-cbc -d -in $2 -pass pass:$1

