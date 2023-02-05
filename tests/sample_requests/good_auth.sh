#!/bin/sh
curl -X POST localhost:5000/vk \
    --data '{"type": "confirmation", "group_id": 217991594, "secret": "BigSecret"}' \
    -H "Content-type: application/json"
