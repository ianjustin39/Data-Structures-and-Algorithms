class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if len(group.get_users()) != 0 and user in group.get_users():
        return True

    if len(group.get_groups()) != 0:
        group_list = group.get_groups()
        for per_group in group_list:
            return is_user_in_group(user, per_group)

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print("Test case 1: ", bool(is_user_in_group(sub_child_user, parent)))
print("Test case 2: ", bool(is_user_in_group('Lisa', parent)))


new_parent = Group("parent")
print("Test case 3: ", bool(is_user_in_group(sub_child_user, new_parent)))
print("Test case 4: ", bool(is_user_in_group('Tom', new_parent)))