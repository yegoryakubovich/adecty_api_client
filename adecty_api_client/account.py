#
# (c) 2023, Yegor Yakubovich
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


from adecty_api_client.functions import request_create


class Account:
    account_session_token: str

    def __init__(self, account_session_token: str = None):
        self.account_session_token = account_session_token

    def create(self, username: str, password: str):
        endpoint = 'account/create'
        data = {
            'username': username,
            'password': password,
        }
        return request_create(
            endpoint=endpoint,
            data=data,
        )

    def get(self, account_session_token: str = None):
        endpoint = 'account/get'
        data = {
            'account_session_token': account_session_token if account_session_token else self.account_session_token,
        }
        return request_create(
            endpoint=endpoint,
            data=data,
        )

    def session_create(self, username: str, password: str):
        endpoint = 'account/session/create'
        data = {
            'username': username,
            'password': password,
        }
        return request_create(
            endpoint=endpoint,
            data=data,
        )
