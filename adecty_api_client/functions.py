#
# (c) 2022, Yegor Yakubovich
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from requests import get

from adecty_api_client.adecty_api_client_error import AdectyApiClientError

DOMAIN = 'http://api.adecty.com/'


def request_create(endpoint: str, data: dict):
    url = '{domain}{endpoint}'.format(
        domain=DOMAIN,
        endpoint=endpoint,
    )
    json = data
    response = get(url=url, json=json)
    if response.status_code == 200:
        response = response.json()
        if response['status'] == 'error':
            raise AdectyApiClientError(response['message'])
        return response
