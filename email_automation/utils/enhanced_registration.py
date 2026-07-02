"""
EnhancedRegistration – subclass of the existing Registration page object.

Purpose: capture the exact first_name, last_name, and email generated
during registration (all sharing one timestamp) so the email validator
can resolve {first_name} / {email} placeholders in subject lines.

Constraint: the parent class (pages/registration.py) is NOT modified.
"""
import datetime
import logging
import time

from pages.registration import Registration


class EnhancedRegistration(Registration):
    """
    Drop-in replacement for Registration that uses a single shared
    timestamp across all generated values and exposes them for
    downstream use by RegistrationTracker.
    """

    def __init__(self, driver) -> None:
        super().__init__(driver)
        # Single timestamp shared by first_name, last_name, and email
        self._run_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.captured_first_name: str = ""
        self.captured_last_name: str = ""
        self.captured_email: str = ""

    # ── Overrides that capture generated values ───────────────────────────────

    def registration_signup_first_name(self, registration_test_data: dict) -> None:
        """Mirror parent logic with shared timestamp; capture the value."""
        self.actions.wait_for_element(self.registration_first_name)
        unique_first_name = (
            f"{registration_test_data['registration_first_name']}"
            f"_FN_{self._run_timestamp}"
        )
        self.captured_first_name = unique_first_name
        self.actions.send_keys(self.registration_first_name, unique_first_name)
        logging.info("Entered First Name: %s", unique_first_name)
        time.sleep(2)

    def registration_signup_last_name(self, registration_test_data: dict) -> None:
        """Mirror parent logic with shared timestamp; capture the value."""
        self.actions.wait_for_element(self.registration_last_name)
        unique_last_name = (
            f"{registration_test_data['registration_last_name']}"
            f"_LN_{self._run_timestamp}"
        )
        self.captured_last_name = unique_last_name
        self.actions.send_keys(self.registration_last_name, unique_last_name)
        logging.info("Entered Last Name: %s", unique_last_name)
        time.sleep(2)

    def registration_signup_email(self, registration_test_data: dict) -> str:
        """Mirror parent logic with shared timestamp; capture the value."""
        self.actions.wait_for_element(self.registration_email_id)
        self.unique_email_id = (
            f"{registration_test_data['registration_email_id']}"
            f"+{self._run_timestamp}@gmail.com"
        )
        self.captured_email = self.unique_email_id
        self.actions.send_keys(self.registration_email_id, self.unique_email_id)
        time.sleep(2)
        return self.unique_email_id

    # ── Convenience ───────────────────────────────────────────────────────────

    @property
    def registration_summary(self) -> dict:
        """Return a dict suitable for RegistrationTracker.add_registration()."""
        return {
            "email": self.captured_email,
            "first_name": self.captured_first_name,
            "last_name": self.captured_last_name,
        }
