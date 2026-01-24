#!/bin/bash

echo "Starting rollback for DeploySentry..."

kubectl rollout undo deployment deploysentry-app

echo "Rollback completed."
