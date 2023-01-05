#!/bin/bash

# took it from https://github.com/pardahlman/docker-rabbitmq-cluster

set -e

# Start RMQ from entry point.
# This will ensure that environment variables passed
# will be honored
/usr/local/bin/docker-entrypoint.sh rabbitmq-server -detached

sleep 5s
# rabbitmq-server -detached

# Do the cluster dance
rabbitmqctl stop_app
rabbitmqctl join_cluster sunny-rabbit@rabbit-host

# Stop the entire RMQ server. This is done so that we
# can attach to it again, but without the -detached flag
# making it run in the forground
rabbitmqctl stop

# # Wait a while for the app to really stop
sleep 2s

# # Start it
rabbitmq-server

