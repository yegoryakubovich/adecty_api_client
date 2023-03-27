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


class WalletOffer:
    account_session_token: str

    def __init__(self, account_session_token: str = None):
        self.account_session_token = account_session_token

    def create(
            self,
            type: str,
            system_name,
            system_data: dict,
            value_from: int,
            value_to: int,
            rate: int,
            account_session_token: str = None,
    ):
        endpoint = 'pay/wallet/offer/create'
        data = {
            'offer_type': type,
            'system_name': system_name,
            'system_data': system_data,
            'value_from': value_from,
            'value_to': value_to,
            'rate': rate,
            'account_session_token': account_session_token if account_session_token else self.account_session_token,
        }
        return request_create(
            endpoint=endpoint,
            data=data,
        )

    def get(
            self,
            id: int,
            account_session_token: str = None,
    ):
        endpoint = 'pay/wallet/offer/get'
        data = {
            'offer_id': id,
            'account_session_token': account_session_token if account_session_token else self.account_session_token,
        }
        return request_create(
            endpoint=endpoint,
            data=data,
        )

    def update(
            self,
            id: int,
            system_data: dict = None,
            rate: int = None,
            active: bool = None,
            account_session_token: str = None,
    ):
        endpoint = 'pay/wallet/offer/update'
        data = {
            'offer_id': id,
            'account_session_token': account_session_token if account_session_token else self.account_session_token,
        }

        if system_data:
            data['system_data'] = system_data
        if rate:
            data['rate'] = rate
        if active:
            data['active'] = active

        return request_create(
            endpoint=endpoint,
            data=data,
        )

    def delete(
            self,
            id: int,
            account_session_token: str = None,
    ):
        endpoint = 'pay/wallet/offer/delete'
        data = {
            'offer_id': id,
            'account_session_token': account_session_token if account_session_token else self.account_session_token,
        }

        return request_create(
            endpoint=endpoint,
            data=data,
        )


class Wallet:
    account_session_token: str
    offer: WalletOffer

    def __init__(self, account_session_token: str = None):
        self.account_session_token = account_session_token
        self.offer = WalletOffer(account_session_token=self.account_session_token)

    def create(self, account_session_token: str = None):
        endpoint = 'pay/wallet/create'
        data = {
            'account_session_token': account_session_token if account_session_token else self.account_session_token,
        }
        return request_create(
            endpoint=endpoint,
            data=data,
        )

    def get(self, account_session_token: str = None):
        endpoint = 'pay/wallet/get'
        data = {
            'account_session_token': account_session_token if account_session_token else self.account_session_token,
        }
        return request_create(
            endpoint=endpoint,
            data=data,
        )

    def actions_get(self, page=1, account_session_token: str = None):
        endpoint = 'pay/wallet/actions/get'
        data = {
            'account_session_token': account_session_token if account_session_token else self.account_session_token,
            'page': page,
        }
        return request_create(
            endpoint=endpoint,
            data=data,
        )

    def offers_get(self, page=1, account_session_token: str = None):
        endpoint = 'pay/wallet/offers/get'
        data = {
            'account_session_token': account_session_token if account_session_token else self.account_session_token,
            'page': page,
        }
        return request_create(
            endpoint=endpoint,
            data=data,
        )


class Pay:
    account_session_token: str
    wallet = Wallet

    def __init__(self, account_session_token: str = None):
        self.account_session_token = account_session_token
        self.wallet = Wallet(account_session_token=self.account_session_token)
