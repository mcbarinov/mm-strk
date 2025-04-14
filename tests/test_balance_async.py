import pytest

from mm_starknet import balance_async
from mm_starknet.balance import ETH_ADDRESS_MAINNET, STRK_ADDRESS_MAINNET

pytestmark = pytest.mark.anyio


async def test_get_balance(mainnet_rpc_url):
    address = "0x076601136372fcdbbd914eea797082f7504f828e122288ad45748b0c8b0c9696"  # Bybit: Hot Wallet
    assert (await balance_async.get_balance(mainnet_rpc_url, address, ETH_ADDRESS_MAINNET)).unwrap() > 1
    assert (await balance_async.get_balance(mainnet_rpc_url, address, STRK_ADDRESS_MAINNET)).unwrap() > 1
