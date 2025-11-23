# day5_capstone/runner_setup.py

import os

from google.adk import runners
from google.adk.agents.config import load_agent_from_config

# Optional: if you use a .env file locally
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # dotenv is optional; safe to ignore if not installed
    pass

# ─────────────────────────────────────────
# 1. API key – GitHub Actions will pass this via env var
# ─────────────────────────────────────────
# For Gemini via Google AI Studio:
#   GOOGLE_API_KEY or GEMINI_API_KEY
# For Vertex: you'll use GOOGLE_CLOUD_PROJECT etc.
#
# Just make sure this matches whatever your ADK setup expects.
API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not API_KEY:
    # Don't crash, but warn loudly – helps in CI logs
    print("⚠️ WARNING: No GOOGLE_API_KEY or GEMINI_API_KEY found in environment.")

# ─────────────────────────────────────────
# 2. Load your CPD root agent config
# ─────────────────────────────────────────
# ⬇️ IMPORTANT: change this to your real config path.
# Example if you have: day5_capstone/config/cpd_root_agent.yaml
#   config_path = "day5_capstone/config/cpd_root_agent.yaml"
# or just "config/cpd_root_agent.yaml" if you run from repo root.
config_path = "day5_capstone/config/cpd_root_agent.yaml"  # TODO: adjust if needed

root_agent = load_agent_from_config(config_path)

# ─────────────────────────────────────────
# 3. Create a Runner instance used everywhere
# ─────────────────────────────────────────
runner = runners.Runner(agent=root_agent)
