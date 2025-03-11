from mm_starknet.domain import address_to_domain


def test_address_to_domain_exist():
    res = address_to_domain("0x0060b56b67e1b4dd1909376496b0e867f165f31c5eac7902d9ff48112f16ef9b")
    assert res.is_ok()
    assert res.ok == "abc.stark"


def test_address_to_domain_not_exist():
    res = address_to_domain("0x0060b56b67e1b4dd1909376496b0e867f165f31c5eac7902d9ff48112f16ef9a")  # not existed
    assert res.is_ok()
    assert res.ok is None
