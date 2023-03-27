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


from adecty_api_client.account import Account
from adecty_api_client.pay import Pay


class AdectyApiClient:
    account_session_token: str
    account: Account
    pay: Pay

    def __init__(self, account_session_token: str = None):
        self.account_session_token = account_session_token
        self.account = Account(account_session_token=account_session_token)
        self.pay = Pay(account_session_token=account_session_token)
