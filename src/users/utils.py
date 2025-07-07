def user_directory_path(instance, filename):
    """
    Returns the file path for user profile images.
    The path is structured as 'user_<user_id>/<filename>'.
    """
    return 'user_{0}/{1}'.format(instance.user.id, filename)