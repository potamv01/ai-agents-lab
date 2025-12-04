# day5_capstone/test_cpd_agent.py

"""Integration-style checks for the CPD agent runner.

This module is written to be run manually, but pytest will collect it by
default. We skip the tests entirely when the Google ADK dependency is not
available so CI environments without that package do not fail during
collection.
"""

import asyncio
import importlib.util
from pprint import pprint

import pytest


# The official Google ADK package is not available in the execution
# environment used for automated testing. Skip the module early to avoid import
# errors during pytest collection.
try:  # pragma: no cover - import guard
    has_google_adk = importlib.util.find_spec("google.adk") is not None
except ModuleNotFoundError:
    has_google_adk = False

if not has_google_adk:
    pytest.skip(
        "google-adk is not installed; skip CPD agent integration checks.",
        allow_module_level=True,
    )


from runner_setup import runner  # uses the file we just created


async def ask_cpd_agent(
    message: str,
    user_id: str = "demo_user",
    session_id: str = "cpd_demo",
):
    print(f"\nUser > {message}")
    response = await runner.run_debug(
        [message],
        user_id=user_id,
        session_id=session_id,
        verbose=True,
    )
    return response


async def main():
    # You can change these test queries to whatever you want
    queries = [
        "What is the overall training completion rate?",
        "Which staff are underperforming below 70% completion?",
        "Please generate a reminder email for staff_id: 101",
    ]

    for q in queries:
        resp = await ask_cpd_agent(q)
        print("\nAssistant response:")
        pprint(resp)
        print("\n" + "=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
