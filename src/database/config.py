import os
import streamlit as st

from supabase import Client, create_client


def _get_secret(key: str) -> str:
    try:
        return st.secrets[key]
    except Exception:
        value = os.getenv(key)
        if value:
            return value
        raise RuntimeError(
            f"Missing '{key}' secret. Set it in .streamlit/secrets.toml or as an environment variable."
        )


supabase: Client = create_client(
    _get_secret("supabase_Url"),
    _get_secret("supabase_Key"),
)