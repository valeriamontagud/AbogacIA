"""
Roles y autorización.
"""

from fastapi import Depends, HTTPException

from app.modules.auth.dependencies import (
    get_current_user
)

from app.modules.users.models import User


def require_role(role: str):

    def role_checker(
        current_user: User = Depends(get_current_user)
    ):

        if current_user.role != role:

            raise HTTPException(
                status_code=403,
                detail="Not enough permissions"
            )

        return current_user

    return role_checker