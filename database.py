# Удаляет пользователя из черного списка
def delete_user_from_blacklist(id):
    current_user = session.query(BlackList).filter_by(vk_id=id).first()
    session.delete(current_user)
    session.commit()


# Удаляет пользователя из избранного
def delete_user_from_fav(id):
    current_user = session.query(Fav_User).filter_by(vk_id=id).first()
    session.delete(current_user)
    session.commit()


#Создает пользователя в бд
def db_candidate(cand_lst):
    with db:
        db.create_tables([VkUsers])
        data_db = VkUsers.select()
        id_list = [i.id for i in data_db]


# Проверяет, зарегистрирован ли пользователь бота в БД
def check_db_master(id):
    current_user_id = session.query(User).filter_by(vk_id=id).first()
    return current_user_id


# Проверяет, есть ли пользователь в БД
def check_db_user(id):
    dating_user = session.query(Fav_User).filter_by(vk_id=id).first()
    blocked_user = session.query(BlackList).filter_by(vk_id=id).first()
    return dating_user, blocked_user


# Проверяет, есть ли пользователь в черном списке
def check_db_black(id):
    current_users_id = session.query(User).filter_by(vk_id=id).first()
    # Находим все анкеты из избранного, которые добавил данный пользователь
    all_users = session.query(BlackList).filter_by(user_id=current_users_id.id).all()
    return all_users


# Проверяет, есть ли пользователь в избранном
def check_db_fav(id):
    current_users_id = session.query(User).filter_by(vk_id=id).first()
    # Находим все анкеты из избранного, которые добавил данный пользователь
    all_users = session.query(Fav_User).filter_by(user_id=current_users_id.id).all()
    return all_users


# Пишет сообщение пользователю
def write_msg(user_id, message, attachment=None):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'random_id': vk_api.utils.get_random_id(),
               'attachment': attachment})


# Регистрация пользователя
def reg_user(vk_id):
    try:
        new_user = User(vk_id=vk_id)
        session.add(new_user)
        session.commit()
        return True
    except (IntegrityError, InvalidRequestError):
        return False


def reg_new_user(id_num):
    write_msg(id_num, 'Вы прошли регистрацию.')
    register_user(id_num)


# Сохранение выбранного пользователя в БД
def add_user_to_fav(event_id, vk_id, name, surname, city, link, id_user):
    try:
        new_user = DatingUser(
            vk_id=vk_id,
            first_name=first_name,
            second_name=second_name,
            city=city,
            link=link,
            id_user=id_user
        )
        session.add(new_user)
        session.commit()
        write_msg(event_id,
                  'Пользователь успешно добавлен в избранное')
        return True
    except (IntegrityError, InvalidRequestError):
        write_msg(event_id,
                  'Пользователь уже в избранном.')
        return False

# Сохранение в БД фото добавленного пользователя
def add_user_photos(event_id, link_photo, count_likes, id_dating_user):
    try:
        new_user = Photos(
            link_photo=link_photo,
            count_likes=count_likes,
            id_dating_user=id_dating_user
        )
        session.add(new_user)
        session.commit()
        write_msg(event_id,
                  'Фото пользователя сохранено в избранном')
        return True
    except (IntegrityError, InvalidRequestError):
        write_msg(event_id,
                  'Невозможно добавить фото этого пользователя(Уже сохранено)')
        return False
