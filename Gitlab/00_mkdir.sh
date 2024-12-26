mkdir -p ./gitlab_config ./gitlab_data ./gitlab_logs ./gitlab-runner 

cat <<EOL > ./gitlab-runner/config.toml
concurrent = 1
check_interval = 0

[[runners]]
  name = "docker-runner"
  url = "http://172.28.164.85/"
  token = "YOUR_RUNNER_TOKEN"
  executor = "docker"
  [runners.custom_build_dir]
  [runners.custom_build_dir.volume]
  [runners.docker]
    tls_verify = false
    image = "alpine:latest"
    privileged = true
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache"]
    shm_size = 0
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]
EOL
