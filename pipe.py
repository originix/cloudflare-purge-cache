import datetime
import json
import requests

from bitbucket_pipes_toolkit import Pipe, get_logger, enable_debug

logger = get_logger()
enable_debug()


# defines the schema for pipe variables
variables = {
    'CF_API_KEY': {'type': 'string', 'required': True},
    'CF_ZONE_ID': {'type': 'string', 'required': True},
    'PURGE_EVERYTHING': {'type': 'boolean', 'required': False, 'default': False},
    'FILES': {'type': 'string', 'required': False, 'nullable': True},
    'TAGS': {'type': 'string', 'required': False, 'nullable': True},
    'HOSTS': {'type': 'string', 'required': False, 'nullable': True},
    'PREFIXES': {'type': 'string', 'required': False, 'nullable': True},
    'DEBUG': {'type': 'boolean', 'required': False, 'default': False}
}

# initialize the Pipe object. At this stage the validation of variables takes place
pipe = Pipe(schema=variables, check_for_newer_version=True)

CF_API_KEY = pipe.get_variable('CF_API_KEY')
CF_ZONE_ID = pipe.get_variable('CF_ZONE_ID')
PURGE_EVERYTHING = pipe.get_variable('PURGE_EVERYTHING')
FILES = pipe.get_variable('FILES')
TAGS = pipe.get_variable('TAGS')
HOSTS = pipe.get_variable('HOSTS')
PREFIXES = pipe.get_variable('PREFIXES')

# create a unique caller id from BITBUCKET_REPO_FULL_NAME and BITBUCKET_BUILD_NUMBER
# see https://confluence.atlassian.com/bitbucket/variables-in-pipelines-794502608.html
# to get the list of all available environment variables in pipelines

caller = datetime.datetime.utcnow().isoformat()

pipe.log_info(f"Sending request a Cloudflare purge cache for the zone id: {CF_ZONE_ID}")

try:
    headers = {
        'Authorization': f'Bearer {CF_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {}

    if PURGE_EVERYTHING:
        data['purge_everything'] = True

    if FILES is not None:
        data['files'] = FILES.split()

    if TAGS is not None:
        data['tags'] = TAGS.split()

    if HOSTS is not None:
        data['hosts'] = HOSTS.split()

    if PREFIXES is not None:
        data['prefixes'] = PREFIXES.split()

    pipe.log_debug(f"Sending a data: {data}")

    purge_cache = requests.post(
        f"https://api.cloudflare.com/client/v4/zones/{CF_ZONE_ID}/purge_cache",
        data=json.dumps(data),
        headers=headers
    )
    purge_cache_json = purge_cache.json()

    if not purge_cache_json.get('success', False):
        raise Exception(purge_cache_json)

    # print a colorized success message (in green)
    purge_cache_id = purge_cache_json['result']['id']
    pipe.success(f'Successfully requested a Cloudflare purge cache: {purge_cache_id}')

except Exception as error:
    # log the ERROR message (in red)
    pipe.log_error('Error requesting a Cloudflare purge cache')

    # print a colorized error message and call system exit
    pipe.fail(f"Failed to request a Cloudflare purge cache: {error}")
