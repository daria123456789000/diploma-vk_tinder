if event.obj.message["text"].lower() == "избранное":
                        request_fav_list = db.request_fav_list(self_id)
                        for fav_user in request_fav_list:
                            data = vk.vk_user.users.get(user_id=fav_user.watched_vk_id, fields="name, surname")
                            name = data[0]['name']
                            surname = data[0]['surname']
                            user_photo_list = vk.vk_user.photos.get(owner_id=fav_user.watched_vk_id, album_id="profile",
                                                                    extended=1)
                            user_photos = vk.prev_photos(user_photo_list)
                            vk.send_message(vk.vk_group_session, self_id, f'{name} {surname}\n'
                                                                          f'https://vk.com/id{favorite_user.watched_vk_id}\n',
                                            f'photo{favorite_user.watched_vk_id}_{user_photos[0][0]},'
                                            f'photo{favorite_user.watched_vk_id}_{user_photos[1][0]},'
                                            f'photo{favorite_user.watched_vk_id}_{user_photos[2][0]}',
                                            keyboard=back_keyboard.get_keyboard())
                        continue

                    elif event.obj.message["text"] == "выход":
                        vk.send_message(vk.vk_group_session, event.obj.message["from_id"], text="выход из чат-бота")
                        user_dict[event.obj.message["from_id"]] = 1
                        break
