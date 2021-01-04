class ClientError(Exception):
    response = None
    code = None
    message = ""

    def __init__(self, *args, **kwargs):
        args = list(args)
        if len(args) > 0:
            self.message = str(args.pop(0))
        for key in list(kwargs.keys()):
            setattr(self, key, kwargs.pop(key))
        super().__init__(self.message, *args, **kwargs)
        if self.response:
            self.code = self.response.status_code


class GenericRequestError(ClientError):
    """Sorry, there was a problem with your request"""


class ClientGraphqlError(ClientError):
    """Raised due to graphql issues"""


class ClientJSONDecodeError(ClientError):
    """Raised due to json decoding issues"""


class ClientConnectionError(ClientError):
    """Raised due to network connectivity-related issues"""


class ClientBadRequestError(ClientError):
    """Raised due to a HTTP 400 response"""


class ClientForbiddenError(ClientError):
    """Raised due to a HTTP 403 response"""


class ClientNotFoundError(ClientError):
    """Raised due to a HTTP 404 response"""


class ClientThrottledError(ClientError):
    """Raised due to a HTTP 429 response"""


class ClientRequestTimeout(ClientError):
    """Raised due to a HTTP 408 response"""


class ClientIncompleteReadError(ClientError):
    """Raised due to incomplete read HTTP response"""


class ClientLoginRequired(ClientError):
    """Instagram redirect to https://www.instagram.com/accounts/login/"""


class ReloginAttemptExceeded(ClientError):
    pass


class PrivateError(ClientError):
    """For Private API and last_json logic"""


class FeedbackRequired(PrivateError):
    pass


class ChallengeError(PrivateError):
    pass


class ChallengeRedirection(ChallengeError):
    pass


class ChallengeRequired(ChallengeError):
    pass


class SelectContactPointRecoveryForm(ChallengeError):
    pass


class RecaptchaChallengeForm(ChallengeError):
    pass


class SubmitPhoneNumberForm(ChallengeError):
    pass


class LoginRequired(PrivateError):
    """Instagram request relogin
    Example:
    {'message': 'login_required',
    'response': <Response [403]>,
    'error_title': "You've Been Logged Out",
    'error_body': 'Please log back in.',
    'logout_reason': 8,
    'status': 'fail'}
    """


class SentryBlock(PrivateError):
    pass


class RateLimitError(PrivateError):
    pass


class BadPassword(PrivateError):
    pass


class PleaseWaitFewMinutes(PrivateError):
    pass


class UnknownError(PrivateError):
    pass


class MediaError(PrivateError):
    pass


class MediaNotFound(MediaError):
    pass


class UserError(PrivateError):
    pass


class UserNotFound(UserError):
    pass


class CollectionError(PrivateError):
    pass


class CollectionNotFound(CollectionError):
    def __init__(self, *args, **kwargs):
        super().__init__(
            f"Collection \"{kwargs.get('name')}\" not found",
            *args, **kwargs
        )


class DirectError(PrivateError):
    pass


class DirectThreadNotFound(DirectError):
    pass


class DirectMessageNotFound(DirectError):
    pass


class VideoTooLongException(PrivateError):
    pass


class VideoNotDownload(PrivateError):
    pass


class VideoNotUpload(PrivateError):
    pass


class VideoConfigureError(VideoNotUpload):
    pass


class VideoConfigureStoryError(VideoConfigureError):
    pass


class PhotoNotUpload(PrivateError):
    pass


class PhotoConfigureError(PhotoNotUpload):
    pass


class PhotoConfigureStoryError(PhotoConfigureError):
    pass


class IGTVNotUpload(PrivateError):
    pass


class IGTVConfigureError(IGTVNotUpload):
    pass


class AlbumNotDownload(PrivateError):
    pass


class AlbumUnknownFormat(PrivateError):
    pass


class AlbumConfigureError(PrivateError):
    pass


class StoryNotFound(MediaNotFound):
    pass


class HashtagError(PrivateError):
    pass


class HashtagNotFound(HashtagError):
    def __init__(self, *args, **kwargs):
        super().__init__(
            f"Hashtag \"{kwargs.get('name')}\" not found",
            *args, **kwargs
        )


class LocationError(PrivateError):
    pass


class LocationNotFound(LocationError):
    def __init__(self, *args, **kwargs):
        super().__init__(
            f"Location \"{kwargs.get('location_pk')}\" not found",
            *args, **kwargs
        )
