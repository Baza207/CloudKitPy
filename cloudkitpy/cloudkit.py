#
# cloudkit.py
# CloudKitPy
#
# Created by James Barrow on 27/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python


class CloudKit:

    # Enviroments - Constants to use when configuring the
    # environment of containers.
    DEVELOPMENT_ENVIRONMENT = 'DEVELOPMENT_ENVIRONMENT'
    """The container environment is not accessible by apps available
     on the store."""
    PRODUCTION_ENVIRONMENT = 'PRODUCTION_ENVIRONMENT'
    """The container environment is accessible by both development
     apps and apps available on the store."""

    # Comparator Values - The following values are allowed for
    # the comparator key in a filter dictionary.
    EQUALS = 'EQUALS'
    """The left-hand value is equal to the right-hand value."""
    NOT_EQUALS = 'NOT_EQUALS'
    """The left-hand value is not equal to the right-hand value."""
    LESS_THAN = 'LESS_THAN'
    """The left-hand value is less than the right-hand value."""
    LESS_THAN_OR_EQUALS = 'LESS_THAN_OR_EQUALS'
    """The left-hand value is less than or equal to the right-hand value."""
    GREATER_THAN = 'GREATER_THAN'
    """The left-hand value is greater than the right-hand value."""
    GREATER_THAN_OR_EQUALS = 'GREATER_THAN_OR_EQUALS'
    """The left-hand value is greater than or equal to the right-hand value."""
    NEAR = 'NEAR'
    """The left-hand location is within the specified distance
     of the right-hand location."""
    CONTAINS_ALL_TOKENS = 'CONTAINS_ALL_TOKENS'
    """The records have text fields that contain all specified tokens."""
    IN = 'IN'
    """The left-hand value is in the right-hand list."""
    NOT_IN = 'NOT_IN'
    """The left-hand value is not in the right-hand list."""
    CONTAINS_ANY_TOKENS = 'CONTAINS_ANY_TOKENS'
    """The records with text fields contain any of the specified tokens."""
    LIST_CONTAINS = 'LIST_CONTAINS'
    """The records contain values in a list field."""
    NOT_LIST_CONTAINS = 'NOT_LIST_CONTAINS'
    """The records don't contain the specified values in a list field."""
    NOT_LIST_CONTAINS_ANY = 'NOT_LIST_CONTAINS_ANY'
    """The records don't contain any of the specified values in
     a list field."""
    BEGINS_WITH = 'BEGINS_WITH'
    """The records with a field that begins with a specified value."""
    NOT_BEGINS_WITH = 'NOT_BEGINS_WITH'
    """The records with a field that doesn't begin with a specified value."""
    LIST_MEMBER_BEGINS_WITH = 'LIST_MEMBER_BEGINS_WITH'
    """The records contain a specified value as the first item in
     a list field."""
    NOT_LIST_MEMBER_BEGINS_WITH = 'NOT_LIST_MEMBER_BEGINS_WITH'
    """The records don't contain a specified value as the first item
     in a list field."""
    LIST_CONTAINS_ALL = 'LIST_CONTAINS_ALL'
    """The records contain all values in a list field."""
    NOT_LIST_CONTAINS_ALL = 'NOT_LIST_CONTAINS_ALL'
    """The records don't contain all specified values in a list field."""

    # Actions for a Reference Dictionary
    # The delete action for the reference object.
    NONE = 'NONE'
    """No action when a referenced record is deleted."""
    DELETE_SELF = 'DELETE_SELF'
    """Deletes a source record when the target record is deleted."""
    VALIDATE = 'VALIDATE'
    """Deletes a target record only after all source records are deleted.
     Verifies that the target record exists before creating this type of
     reference. If it doesn't exist, creating the reference fails."""

    def __init__(self, config):
        """Configure CloudKitPy."""
        pass

    def get_default_container(self):
        return None

    def get_container(self, container_id):
        return None

    def get_all_containers(self):
        return []
