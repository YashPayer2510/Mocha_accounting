"""
Email Chain Definition for Mocha Accounting Onboarding Journey.

Subjects, schedules, and body keywords are sourced directly from
'Email chain.docx' provided by the Mocha team.

Placeholder convention used in subject_template:
    {first_name}  – the first name submitted during registration
    {otp}         – 6-digit OTP (regex-matched, not literal)
"""
from dataclasses import dataclass, field
from typing import List, Optional

SENDER = "noreply@mochaaccounting.com"


@dataclass
class EmailDefinition:
    """Represents one email in the Mocha Accounting onboarding sequence."""
    email_id: str
    name: str
    day_offset: int
    trigger: str
    subject_template: str
    sender: str
    # Phrases that MUST exist in the normalised body text
    required_keywords: List[str]
    # Distinctive subject fragment used for Gmail API search queries
    subject_search_fragment: str
    cta_text: Optional[str] = None
    # True for emails that arrive within minutes of the triggering action
    is_immediate: bool = False
    description: str = ""


EMAIL_CHAIN: List[EmailDefinition] = [
    # ── Email 1 ────────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_1",
        name="Welcome & Email Verification (OTP)",
        day_offset=0,
        trigger="Immediately after sign-up form submission",
        subject_template="Hi {first_name}, your signup code is {otp}",
        sender=SENDER,
        subject_search_fragment="your signup code is",
        required_keywords=[
            "thank you for choosing mocha accounting",
            "streamlining your accounting",
            "if you didn't create an account",
            "support@mochatechnologies.com",
            "mocha support team",
        ],
        cta_text=None,
        is_immediate=True,
        description="OTP verification email sent immediately after the sign-up form is submitted.",
    ),
    # ── Email 2 ────────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_2",
        name="Account Active – Welcome",
        day_offset=0,
        trigger="Immediately after email address is verified",
        subject_template="Hi {first_name}, Welcome to Mocha! Here are your account details",
        sender=SENDER,
        subject_search_fragment="Welcome to Mocha! Here are your account details",
        required_keywords=[
            "congratulations",
            "fully verified and ready to go",
            "invoicing made simple",
            "inventory management",
            "purchase order tracking",
            "quick start guide",
            "support@mochatechnologies.com",
        ],
        cta_text="Learn More",
        is_immediate=True,
        description="Welcome / account-active email sent right after OTP verification.",
    ),
    # ── Email 3 ────────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_3",
        name="Invite to Demo",
        day_offset=2,
        trigger="2 days after Email 2",
        subject_template="Start strong with a personalized Mocha walkthrough!",
        sender=SENDER,
        subject_search_fragment="Start strong with a personalized Mocha walkthrough",
        required_keywords=[
            "personalized walkthrough",
            "transform your business financial management",
            "reduce accounting errors by up to 75%",
            "zero cost, no obligation demo",
            "save 80+ hours",
            "schedule your free 1:1 session",
            "support@mochatechnologies.com",
        ],
        cta_text="Schedule Your Free 1:1 Session",
        description="Demo invitation sent 2 days after Email 2.",
    ),
    # ── Email 3.1 ──────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_3_1",
        name="Demo Reminder / Follow-up (1)",
        day_offset=4,
        trigger="2 days after Email 3 – if demo not yet booked",
        subject_template="Still Curious About Mocha Accounting? Let's Connect!",
        sender=SENDER,
        subject_search_fragment="Still Curious About Mocha Accounting",
        required_keywords=[
            "financial management easier",
            "no commitment required",
            "completely free 30-minute session",
            "understand the invoicing module",
        ],
        cta_text="Schedule Your Free 1:1 Session",
        description="First demo reminder, sent 2 days after Email 3 if demo was not booked.",
    ),
    # ── Email 4 ────────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_4",
        name="Feature Highlight – Accounting",
        day_offset=6,
        trigger="2 days after Email 3.1",
        subject_template="Simplify Your Finances with Mocha Accounting",
        sender=SENDER,
        subject_search_fragment="Simplify Your Finances with Mocha Accounting",
        required_keywords=[
            "receivables management",
            "payables tracking",
            "robust dashboard",
            "data security",
            "schedule your free 1:1 session",
        ],
        cta_text="Schedule Your Free 1:1 Session",
        description="Accounting feature spotlight email, sent 2 days after Email 3.1.",
    ),
    # ── Email 4.1 ──────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_4_1",
        name="Demo Reminder / Follow-up (2)",
        day_offset=8,
        trigger="2 days after Email 4 – if demo not yet booked",
        subject_template="Don't Miss Out: Your Accounting Game-Changer Awaits",
        sender=SENDER,
        subject_search_fragment="Don't Miss Out: Your Accounting Game-Changer Awaits",
        required_keywords=[
            "other businesses are optimizing their finances",
            "demo is filling up fast",
            "invoicing techniques",
            "inventory management tricks",
            "schedule your free 1:1 session",
        ],
        cta_text="Schedule Your Free 1:1 Session",
        description="Second demo reminder, sent 2 days after Email 4 if demo was not booked.",
    ),
    # ── Email 5 ────────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_5",
        name="Feature Highlight – Invoicing",
        day_offset=10,
        trigger="2 days after Email 4.1",
        subject_template="Master Your Invoicing with Mocha Accounting",
        sender=SENDER,
        subject_search_fragment="Master Your Invoicing with Mocha Accounting",
        required_keywords=[
            "invoicing that works as hard as you do",
            "gst compliance made easy",
            "steady cash flow management",
            "seamless returns",
            "get paid faster",
            "reduce payment delays by up to 70%",
            "schedule your free 1:1 session",
        ],
        cta_text="Schedule Your Free 1:1 Session",
        description="Invoicing feature spotlight email, sent 2 days after Email 4.1.",
    ),
    # ── Email 5.1 ──────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_5_1",
        name="Demo Reminder / Follow-up (3)",
        day_offset=12,
        trigger="2 days after Email 5 – if demo not yet booked",
        subject_template="We're Here to Help - Free Demo Invitation Still Open",
        sender=SENDER,
        subject_search_fragment="Free Demo Invitation Still Open",
        required_keywords=[
            "haven't yet booked your free mocha accounting demo",
            "30-minute live online session",
            "no pressure. no commitment",
            "schedule your free 1:1 session",
        ],
        cta_text="Schedule Your Free 1:1 Session",
        description="Third demo reminder, sent 2 days after Email 5 if demo was not booked.",
    ),
    # ── Email 6 ────────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_6",
        name="Feature Highlight – Inventory",
        day_offset=14,
        trigger="2 days after Email 5.1",
        subject_template="Take Control of Your Inventory with Mocha Accounting",
        sender=SENDER,
        subject_search_fragment="Take Control of Your Inventory with Mocha Accounting",
        required_keywords=[
            "automate restocking",
            "real-time stock tracking",
            "comprehensive stock management",
            "mocha accounting mobile app",
            "schedule your free 1:1 session",
        ],
        cta_text="Schedule Your Free 1:1 Session",
        description="Inventory feature spotlight email, sent 2 days after Email 5.1.",
    ),
    # ── Email 7 ────────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_7",
        name="Case Study",
        day_offset=16,
        trigger="2 days after Email 6",
        subject_template="How a Hotel Business Saved 80 Hours Monthly with Mocha Accounting",
        sender=SENDER,
        subject_search_fragment="How a Hotel Business Saved 80 Hours Monthly",
        required_keywords=[
            "80 hours monthly time saved",
            "99.8% inventory accuracy",
            "90% faster invoicing",
            "anisha hindocha",
            "reduce accounting errors by 75%",
            "schedule your free 1:1 session",
        ],
        cta_text="Schedule Your Free 1:1 Session",
        description="Customer success / case study email, sent 2 days after Email 6.",
    ),
    # ── Email 7.1 ──────────────────────────────────────────────────────────────
    EmailDefinition(
        email_id="email_7_1",
        name="Final Demo CTA",
        day_offset=18,
        trigger="2 days after Email 7 – if demo not yet booked",
        subject_template="Last Chance - Your Free Mocha Accounting Demo Ends Soon",
        sender=SENDER,
        subject_search_fragment="Last Chance - Your Free Mocha Accounting Demo Ends Soon",
        required_keywords=[
            "final opportunity",
            "zero commitment required",
            "save you 50+ hours monthly",
            "this invitation expires in 72 hours",
            "schedule your free 1:1 session",
        ],
        cta_text="Schedule Your Free 1:1 Session",
        description="Final demo CTA, sent 2 days after Email 7 if demo was not booked.",
    ),
]

# Fast lookup by email_id
EMAIL_CHAIN_MAP: dict[str, EmailDefinition] = {e.email_id: e for e in EMAIL_CHAIN}
