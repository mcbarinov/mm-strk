"""Starknet domain resolution via starknet.id API."""

from mm_http import http_request
from mm_result import Result
from mm_std import str_contains_any


async def address_to_domain(address: str, timeout: float = 5.0, proxy: str | None = None) -> Result[str | None]:
    """Resolve a Starknet address to its .stark domain name."""
    url = "https://api.starknet.id/addr_to_domain"
    res = await http_request(url, params={"addr": address}, proxy=proxy, timeout=timeout)
    if (
        res.status_code == 400
        and res.body is not None
        and str_contains_any(res.body.lower(), ["no data found", "no domain found"])
    ):
        return res.to_result_ok(None)
    if res.is_err():
        return res.to_result_err()
    domain_res = res.json_body("domain")
    if domain_res.is_ok():
        return res.to_result_ok(domain_res.unwrap())
    return res.to_result_err("unknown_response")
