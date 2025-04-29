FROM kestra/kestra@sha256:3446591c72295dd04761a318c4eaf45bc4d328ff8cef462182652e6f2102a796

WORKDIR /app

RUN mkdir -p confs/

CMD ["server", "standalone", "--config", "/app/config/kestra_config.yml"]
