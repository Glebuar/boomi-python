class BoomiError(Exception):
    """Base for all SDK‑specific issues."""

class AuthenticationError(BoomiError):
    """Supplied credentials are invalid or expired."""

class RateLimitError(BoomiError):
    """The Boomi API returned HTTP 429."""

class ApiError(BoomiError):
    """Any other non‑retryable API error (HTTP >= 400)."""