#!/usr/bin/env bash

export $(grep -v '^#' $PWD/.env | xargs | tr -d '\r')
