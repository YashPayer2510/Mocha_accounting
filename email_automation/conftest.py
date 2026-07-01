"""
Root conftest for the email_automation package.
Ensures the project root is on sys.path so all existing imports
(pages.*, utilities.*, actions.*) resolve correctly.
"""
import os
import sys

# Project root = parent of email_automation/
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)
