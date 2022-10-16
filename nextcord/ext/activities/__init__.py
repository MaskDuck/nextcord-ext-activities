from typing import Optional, Union

from nextcord import InviteTarget, Invite, VoiceChannel

from .enums import Activity, ActivityDevelopment

__version__ = "2022.06.11"
__author__ = "MaskDuck"
__license__ = "MIT License"


async def create_activity_invite(
    self,
    activity: Union[Activity, ActivityDevelopment],
    /,
    *,
    activity_id: Optional[int] = None,
    reason: Optional[str] = None,
    max_age: int = 0,
    max_uses: int = 0,
    temporary: bool = False,
    unique: bool = True,
) -> Invite:
    """
    .. note::

        This should be called using ``nextcord.VoiceChannel.create_activity_invite()``.

    Creates an instant invite for the specified activity.

    You must have the :attr:`~nextcord.Permissions.create_instant_invite` permission to
    do this.

    :param activity: The activity to create an invite link for. ``activity_id`` must be specified if this is :attr:`Activity.custom`.
    :type activity: Union[Activity, ActivityDevelopment]
    :param activity_id: The ID of the activity to create an invite link for. This can not be ``None`` if ``activity`` is of type ``Activity.custom``.
    :type activity_id: Optional[int]
    :param max_age: How long the invite should last in seconds. If it's 0 then the invite doesn't expire. Defaults to ``0``.
    :type max_age: int
    :param max_uses: How many times the invite can be used. If it's 0 then there are unlimited uses. Defaults to ``0``.
    :type max_uses: int
    :param temporary: Denotes that the invite grants temporary membership (i.e. they get kicked after they disconnect). Defaults to ``False``..
    :type temporary: bool
    :param unique: Indicates if a unique invite URL should be created. Defaults to True. If this is set to ``False`` then it will return a previously created invite.
    :type unique: bool
    :param reason: The reason the invite is being created. Shows up on the audit log.
    :type reason: Optional[str]
    :returns: The created invite.
    :rtype: :class:`~nextcord.Invite`
    :raise: :exc:`~nextcord.HTTPException` Invite creation failed.
    """
    if activity is Activity.custom:
        if activity_id is None:
            raise ValueError("activity_id is required for Activity.custom")

        activity_id = int(activity_id)
    else:
        activity_id = int(activity)

    res = await self.create_invite(
        reason=reason,
        max_age=max_age,
        max_uses=max_uses,
        temporary=temporary,
        unique=unique,
        target_type=InviteTarget.embedded_application,
        target_application_id=activity_id,
    )

    return res


VoiceChannel.create_activity_invite = create_activity_invite  # type: ignore
