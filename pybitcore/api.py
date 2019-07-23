import json
import requests


class BitCoreAPI:
    def __init__(self, host="127.0.0.1", port=3000):
        self.url_base = f"http://{host}:{port}"
        
    def get_transaction_by_block_height(self, block_height: int):
        _url = self.url_base + f"/api/BTC/mainnet/tx?blockHeight={block_height}"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_transaction_by_block_hash(self, block_hash: str):
        _url = self.url_base + f"/api/BTC/mainnet/tx?blockHash={block_hash}"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_coins(self, txid: str):
        _url = self.url_base + f"/api/BTC/mainnet/tx/{txid}/coins"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_address_transactions(self, address: str):
        _url = self.url_base + f"/api/BTC/mainnet/address/{address}/txs"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_transaction_outputs_by_address(self, address: str):
        _url = self.url_base + f"/api/BTC/mainnet/address/{address}/?unspent=true"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_balance_for_an_address(self, address: str):
        _url = self.url_base + f"/api/BTC/mainnet/address/{address}/balance"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_block(self, block_id: str):
        _url = self.url_base + f"/api/BTC/mainnet/block/{block_id}"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_current_height(self):
        _url = self.url_base + f"/api/BTC/mainnet/block/tip"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_wallet(self, pub_key: str):
        _url = self.url_base + f"/api/BTC/mainnet/wallet/{pub_key}"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_wallet_address(self, pub_key: str):
        _url = self.url_base + f"/api/BTC/mainnet/wallet/{pub_key}/addresses"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_wallet_transactions(self, pub_key: str):
        _url = self.url_base + f"/api/BTC/mainnet/wallet/{pub_key}/transactions"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_balance(self, pub_key: str):
        _url = self.url_base + f"/api/BTC/mainnet/wallet/{pub_key}/balance"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_wallet_utxos(self, pub_key: str):
        _url = self.url_base + f"/api/BTC/mainnet/wallet/{pub_key}/balance"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_wallet_utxos(self, pub_key: str):
        _url = self.url_base + f"/api/BTC/mainnet/wallet/{pub_key}/utxos"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_fee_estimate_for_within_n_blocks(self, target: int):
        _url = self.url_base + f"/api/BTC/mainnet/fee/{target}"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_daily_transactions(self):
        _url = self.url_base + f"/api/BTC/mainnet/stats/daily-transactions"
        _str = requests.get(_url).text
        return json.loads(_str)
    
    def get_enabled_chains(self):
        _url = self.url_base + f"/api/status/enabled-chains"
        _str = requests.get(_url).text
        return json.loads(_str)