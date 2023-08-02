if __name__ == '__main__':
        if msg_text == "vkinder":
            menu_bot(user_id)
            msg_text, user_id = loop_bot()

                
            if msg_text.lower() == 'да':
                reg_new_user(user_id)
            elif len(msg_text) > 1:
                 sex = 0
                if msg_text[0:7].lower() == 'девушка':
                   sex = 1
                elif msg_text[0:7].lower() == 'мужчина':
                     sex = 2
            age_at = msg_text[8:10]
                if int(age_at) < 18:
                    write_msg(user_id, 'Показан минимальный возраст - 18 лет')
                    age_at = 18
            age_to = msg_text[11:14]
                if int(age_to) >= 100:
                    write_msg(user_id, 'Показано максимальное значение 99 лет')
                    age_to = 99
            city = msg_text[14:len(msg_text)].lower()
            result = search_users(sex, int(age_at), int(age_to), city)
            create_result(result)
            current_user_id = check_db_master(user_id)
            for i in range(len(result)):
                dating_user, blocked_user = check_db_user(result[i][3])
                user_photo = get_profile_photos(result[i][3])
                   if user_photo == 'нет доступа к фото' or dating_user is not None or blocked_user is not None:
                      continue
                   sorted_user_photo = sort_photos_by_likes(user_photos)
                   write_msg(user_id, f'\n{result[i][0]}  {result[i][1]}  {result[i][2]}', )
                   try:
                       write_msg(user_id, f'фото:',
                                 attachment=','.join
                                ([sorted_user_photo[-1][1], sorted_user_photo[-2][1],
                                  sorted_user_photo[-3][1]]))
                    except IndexError:
                           for photo in range(len(sorted_user_photo)):
                               write_msg(user_id, f'фото:',
                                         attachment=sorted_user_photo[photo][1])

                    
for event in vk.longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
       if self_id == event.obj.message["from_id"]:
          if event.obj.message["text"].lower() == "дальше":
          break
                                    
                                
def user_blacklist(id):
    all_users = check_db_black(id)
    write_msg(id, f'Анкеты в черном списке:')
    for num, user in enumerate(all_users):
        write_msg(id, f'{user.name}, {user.surname}, {user.link}')
        write_msg(id, '1 - Удалить из черного списка, 0 - Далее \nq - Выход')
            def go_to_blacklist(id):
    all_users = check_db_black(id)
        # Удаляем запись из бд - черный список
        if msg_texts == '1':
            print(user.id)
            delete_user_from_blacklist(user.vk_id)
            write_msg(user_ids, f'Анкета успешно удалена')
            if num >= len(all_users) - 1:
                write_msg(user_ids, f'Это была последняя анкета.\n'
                                    f'Vkinder - вернуться в меню\n')
        elif msg_texts.lower() == 'q':
            write_msg(ids, 'Vkinder - для активации бота.')
            break


def add_user_to_blacklist(event_id, vk_id, first_name, second_name, city, link, link_photo, count_likes, id_user):
    try:
        new_user = BlackList(
            vk_id=vk_id,
            first_name=first_name,
            second_name=second_name,
            city=city,
            link=link,
            link_photo=link_photo,
            count_likes=count_likes,
            id_user=id_user
        )
        session.add(new_user)
        session.commit()
        write_msg(event_id,
                  'Пользователь заблокирован')
        return True
    except (IntegrityError, InvalidRequestError):
       write_msg(event_id,
                  'Пользователь уже есть в черном списке')
        return False
        msg_texts, user_id = loop_bot()
        if msg_texts == '0':
            if num >= len(all_users) - 1:
                write_msg(user_id, f'Это последняя анкета.\n'
                                    f'Vkinder - вернуться в меню\n')
        elif msg_texts == '1':
            print(user.id)
            delete_user_from_blacklist(user.vk_id)
            write_msg(user_id, f'Анкета успешно удалена')
            if num >= len(all_users) - 1:
                write_msg(user_id, f'Это последняя анкета\n'
                                    f'Vkinder - вернуться в меню\n')
        elif msg_texts.lower() == 'q':
            write_msg(ids, 'Vkinder - для активации бота.')
            break
                
  if not user_list:
        vk.send_message(vk.vk_group_session, self_id, "Вам пары не нашлось, проверьте свои "
                                                      "данные.\Возможно, неверно указан город в личном профиле?",
                        keyboard=welcome_keyboard.get_keyboard())
        user_dict[self_id] = 1
        return
       elif msg_texts.lower() == 'q':
            write_msg(id, 'Vkinder для активации бота')
            break


if __name__ == "__main__":
    main()
