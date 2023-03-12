# Смотреть логи в /var/lib/docker/containers/<container-id>/<container-id>-json.log
docker run -d \
    -p <HOST>:<CONTAINER> \
    --env-file .env \
    --log-driver=json-file \
    --name fakelbot \
    fakel/fakelbot:latest