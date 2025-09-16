# from models.user import UserCreate, UserOut
#
# # Giả lập database bằng list
# _fake_users = []
# _id_counter = 1
#
# def get_all_users() -> list[UserOut]:
#     return _fake_users
#
# def create_user(user: UserCreate) -> UserOut:
#     global _id_counter
#     new_user = UserOut(id=_id_counter, name=user.name)
#     _id_counter += 1
#     _fake_users.append(new_user)
#     return new_user
