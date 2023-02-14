#!/bin/sh
# test requests wall_post_new
curl -X POST localhost:5000/vk \
    --data-binary "@tests/sample_requests/wall_post_new_data/wall_post_new_data.json" \
    -H "Content-type: application/json"
curl -X POST localhost:5000/vk \
    --data-binary "@tests/sample_requests/wall_post_new_data/long_text_with_image.json" \
    -H "Content-type: application/json"
curl -X POST localhost:5000/vk \
    --data-binary "@tests/sample_requests/wall_post_new_data/long_text_without_images.json" \
    -H "Content-type: application/json"
curl -X POST localhost:5000/vk \
    --data-binary "@tests/sample_requests/wall_post_new_data/many_images_without_text.json" \
    -H "Content-type: application/json"
curl -X POST localhost:5000/vk \
    --data-binary "@tests/sample_requests/wall_post_new_data/one_image_without_text.json" \
    -H "Content-type: application/json"
curl -X POST localhost:5000/vk \
    --data-binary "@tests/sample_requests/wall_post_new_data/text_with_one_image.json" \
    -H "Content-type: application/json"
curl -X POST localhost:5000/vk \
    --data-binary "@tests/sample_requests/wall_post_new_data/repost.json" \
    -H "Content-type: application/json"
