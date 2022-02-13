from rest_framework.exceptions import NotFound, ParseError


class RepositoryNotFound(NotFound):
    """Exception to render a 404 with the code 'NAME_UNKNOWN'"""

    def __init__(self, name):
        """Initialize the exception with the repository name."""
        super().__init__(
            detail={
                "errors": [
                    {
                        "code": "NAME_UNKNOWN",
                        "message": "Repository not found.",
                        "detail": {"name": name},
                    }
                ]
            }
        )


class RepositoryInvalid(ParseError):
    """Exception to render a 400 with the code 'NAME_INVALID'"""

    def __init__(self, name, message=None):
        """Initialize the exception with the repository name."""
        message = message or "Invalid repository name."
        super().__init__(
            detail={
                "errors": [{"code": "NAME_INVALID", "message": message, "detail": {"name": name}}]
            }
        )


class BlobNotFound(NotFound):
    """Exception to render a 404 with the code 'BLOB_UNKNOWN'"""

    def __init__(self, digest):
        """Initialize the exception with the blob digest."""
        super().__init__(
            detail={
                "errors": [
                    {
                        "code": "BLOB_UNKNOWN",
                        "message": "Blob not found.",
                        "detail": {"digest": digest},
                    }
                ]
            }
        )


class BlobInvalid(ParseError):
    """Exception to render a 400 with the code 'BLOB_UNKNOWN'"""

    def __init__(self, digest):
        """Initialize the exception with the blob digest."""
        super().__init__(
            detail={
                "errors": [
                    {
                        "code": "BLOB_UNKNOWN",
                        "message": "blob unknown to registry",
                        "detail": {"digest": digest},
                    }
                ]
            }
        )


class ManifestNotFound(NotFound):
    """Exception to render a 404 with the code 'MANIFEST_UNKNOWN'"""

    def __init__(self, reference):
        """Initialize the exception with the manifest reference."""
        super().__init__(
            detail={
                "errors": [
                    {
                        "code": "MANIFEST_UNKNOWN",
                        "message": "Manifest not found.",
                        "detail": {"reference": reference},
                    }
                ]
            }
        )


class ManifestInvalid(ParseError):
    """Exception to render a 400 with the code 'MANIFEST_INVALID'"""

    def __init__(self, digest):
        """Initialize the exception with the manifest digest."""
        super().__init__(
            detail={
                "errors": [
                    {
                        "code": "MANIFEST_INVALID",
                        "message": "manifest invalid",
                        "detail": {"digest": digest},
                    }
                ]
            }
        )