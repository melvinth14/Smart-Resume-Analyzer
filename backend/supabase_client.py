import os
from typing import Any, Optional

import requests

try:
    from supabase import create_client  # type: ignore
except Exception:
    create_client = None


class _RestTable:
    def __init__(self, base_url: str, key: str, table: str):
        self.base_url = base_url.rstrip("/")
        self.key = key
        self.table = table
        self._method = "POST"
        self._payload: Any = None
        self._filters: list[tuple[str, str]] = []

    def insert(self, payload: Any):
        self._method = "POST"
        self._payload = payload
        return self

    def update(self, payload: Any):
        self._method = "PATCH"
        self._payload = payload
        return self

    def eq(self, column: str, value: str):
        self._filters.append((column, f"eq.{value}"))
        return self

    def execute(self) -> dict:
        url = f"{self.base_url}/rest/v1/{self.table}"
        if self._filters:
            params = "&".join(f"{col}={val}" for col, val in self._filters)
            url = f"{url}?{params}"
        headers = {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation",
        }
        response = requests.request(
            self._method, url, headers=headers, json=self._payload, timeout=30
        )
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return {}


class _RestClient:
    def __init__(self, base_url: str, key: str):
        self.base_url = base_url
        self.key = key

    def table(self, name: str) -> _RestTable:
        return _RestTable(self.base_url, self.key, name)


def get_supabase_client() -> Optional[object]:
    url = os.getenv("SUPABASE_URL", "").strip()
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip()
    if not url or not key:
        return None

    if create_client is not None:
        return create_client(url, key)

    return _RestClient(url, key)
