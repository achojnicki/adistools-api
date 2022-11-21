class users:
    def get_user_by_user_email(self, user_email):
        query={'user_email':user_email}

        user=self._users.find_one(query)
        return user