"""Battlefy team object."""

import dateutil.parser

from .player import Player, Captain


class Team:
    """ Function and utilities for managing teams from the battlefy api.

    :param dict battlefy: The raw battlefy data
    :param str discord_field_id: The battlefy field id of the discord field
    :param str fc_field_id: The battlefy field id of the friend-code field
    """

    def __init__(self, battlefy, discord_field_id, fc_field_id):
        self.raw = battlefy
        self.name = self.raw["name"]
        self.logo = self.raw["persistentTeam"].get("logoUrl", None)
        self.created_at = dateutil.parser.isoparse(self.raw["createdAt"])

        self.captain = Captain(
            battlefy=self.raw.get("captain", None),
            discord_field=self.__get_custom_field_by_id(discord_field_id),
            fc_field=self.__get_custom_field_by_id(fc_field_id))
        self.players = [Player(battlefy=raw) for raw in battlefy["players"]]

    def __get_custom_field_by_id(self, _id: str, default=None):
        """ Return a custom field

        :param _id: The id of the custom field.
        :return:
            The value of the custom field, or default/None if the custom field doesn't exist.
        """
        # Field is a weird word if you look at it for too long
        for field in self.raw.get("customFields", {}):
            if field["_id"] == _id:
                return field["value"]
        return default
