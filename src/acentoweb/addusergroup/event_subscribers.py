# -*- coding: utf-8 -*-
from plone import api
from acentoweb.addusergroup.interfaces import IUserGroupSettings 


def add_user_to_group(event):
    """Event subscriber to add a user to specific groups after the first login."""

    # Get the user object from the event
    import pdb; pdb.set_trace()
    user = event.object
    
    # Get the user id
    #user_id = user.getId()
    user_id =  plone.api.user.get_current()

    groups =  api.portal.get_registry_record('usergroup', interface=IUserGroupSettings)

    # Add the user to the groups
    if groups:
        for group in groups:
            plone.api.group.add_user(groupname=group, user=user_id)