#!/bin/sh
curl -X POST localhost:5000/vk \
    --data-binary "@tests/sample_requests/wall_post_new_data.json" \
    -H "Content-type: application/json"
