from mm_starknet import balance
from mm_starknet.balance import (
    ETH_ADDRESS_MAINNET,
    STRK_ADDRESS_MAINNET,
)


def test_get_balance(mainnet_rpc_url):
    address = "0x076601136372fcdbbd914eea797082f7504f828e122288ad45748b0c8b0c9696"  # Bybit: Hot Wallet
    assert balance.get_balance(mainnet_rpc_url, address, ETH_ADDRESS_MAINNET).unwrap() > 1
    assert balance.get_balance(mainnet_rpc_url, address, STRK_ADDRESS_MAINNET).unwrap() > 1
