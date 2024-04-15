# Bitbucket Pipelines Pipe: Cloudflare Cache Purge

[![Git Hub](https://img.shields.io/badge/git-hub-green.svg)](https://github.com/originix/cloudflare-purge-cache)
[![Docker Hub](https://img.shields.io/badge/Docker-Hub-blue.svg)](https://hub.docker.com/r/originix/cloudflare-purge-cache)


This Bitbucket Pipelines pipe allows you to request a cache purge of your Cloudflare.

## YAML Definition

Add the following snippet to the script section of your `bitbucket-pipelines.yml` file:

```yaml
- pipe: docker://originix/cloudflare-purge-cache:0.1.0
  variables:
    CF_API_KEY: '<string>' # required
    CF_ZONE_ID: '<string>' # required
    PURGE_EVERYTHING: '<bool>' # optional
    FILES: '<string>' # optional
    TAGS: '<string>' # optional
    HOSTS: '<string>' # optional
    PREFIXES: '<string>' # optional
    DEBUG: '<string>' # optional
```

## Variables

| Variable         | Usage                                                |
|------------------|------------------------------------------------------|
| CF_API_KEY (\*)  | Cloudflare API key                                   |
| CF_ZONE_ID (\*)  | Cloudflare Zone ID                                   |
| PURGE_EVERYTHING | purge everything                                     |
| FILES            | List of white space separated file to purge cache.   |
| TAGS             | List of white space separated tag to purge cache.    |
| HOSTS            | List of white space separated host to purge cache.   |
| PREFIXES         | List of white space separated prefix to purge cache. |
| DEBUG            | Turn on extra debug information. Default: `false`.   |

_(\*) = required variable. This variable needs to be specified always when using the pipe._

## Examples

### Purge all cache example:

Purge cache for everything:

```yaml
script:
  - pipe: docker://originix/cloudflare-purge-cache:0.1.0
    variables:
      CF_API_KEY: $CF_API_KEY
      CF_ZONE_ID: $CF_ZONE_ID
      PURGE_EVERYTHING: 'true'
```

### Purge files example:

Purge cache for a list of files:

```yaml
script:
  - pipe: docker://originix/cloudflare-purge-cache:0.1.0
    variables:
      CF_API_KEY: $CF_API_KEY
      CF_ZONE_ID: $CF_ZONE_ID
      FILES: 'www.example.com/img/cat.png www.example.com/img/dog.png'
```

### Purge tags example:

Purge cache for a list of tags:

```yaml
script:
  - pipe: docker://originix/cloudflare-purge-cache:0.1.0
    variables:
      CF_API_KEY: $CF_API_KEY
      CF_ZONE_ID: $CF_ZONE_ID
      TAGS: 'tag-foo tag-bar'
```

### Purge hosts example:

Purge cache for a list of hosts:

```yaml
script:
  - pipe: docker://originix/cloudflare-purge-cache:0.1.0
    variables:
      CF_API_KEY: $CF_API_KEY
      CF_ZONE_ID: $CF_ZONE_ID
      HOSTS: 'example.com api.example.com'
```

### Purge prefix example:

Purge cache for a list of prefix:

```yaml
script:
  - pipe: docker://originix/cloudflare-purge-cache:0.1.0
    variables:
      CF_API_KEY: $CF_API_KEY
      CF_ZONE_ID: $CF_ZONE_ID
      PREFIXES: 'example.com/media/* api.example.com/users/*'
```


## Support

If you’d like help with this pipe, or you have an issue or feature request.

If you’re reporting an issue, please include:

- the version of the pipe
- relevant logs and error messages
- steps to reproduce

## License

Copyright (c) 2024 originix.
MIT License, see [LICENSE](LICENSE) file.
