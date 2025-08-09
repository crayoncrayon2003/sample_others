# ref
* https://docs.airbyte.com/
* https://docs.airbyte.com/platform/using-airbyte/getting-started/oss-quickstart
* https://github.com/airbytehq/airbyte.git

# Install abctl
Airbyte has discontinued docker-compose.
Instead, it uses abctl. For example, for installation and control.

```
curl -LsfS https://get.airbyte.com | bash -s
```

# start airbyte
## run
```
abctl local install
```

## setting
```
abctl local credentials --email airbyte@example.com --password password
```

## access
```
http://localhost:8000
```

# stop airbyte
```
abctl local uninstall --persisted
```
