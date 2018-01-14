# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'ih791894.vds.myihor.ru'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
MONGO_USERNAME = 'miadmin'
MONGO_PASSWORD = 'mi!superPass'

MONGO_DBNAME = 'mipdd'

# По умолчанию Eve запускает API в режиме "read-only" (т.е. поддерживаются только GET запросы),
# мы включаем поддержку методов POST, PUT, PATCH, DELETE.
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    # Описываем ресурс `/users`
    'users': {
        # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
        # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
        # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
        'schema': {
            'username': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 32,
                'required': True,
                # уникальное поле (индекс не создаётся, просто значение должно быть уникальным)
                'unique': True,
            },
            'firstname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 10,
                'required': True,
            },
            'lastname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
                'required': True,
            },
            'role': {

                'type': 'list',  # тип: список
                'allowed': ["author", "contributor"],  # разрешаем использовать значения: "author", "contributor"
            },
            'location': {
                'type': 'dict',  # тип: словарь
                # описываем "схему" словаря
                'schema': {
                    'address': {'type': 'string'},
                    'city': {'type': 'string'}
                },
            },
            'born': {
                'type': 'datetime',
            },
            'active': {
                'type': 'boolean',
                'default': True
            }
        }
    },

    # Описываем ресурс `/groups`
    'groups': {
        # Описываем модель данных (см. выше).
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 32,
                'required': True,
                'unique': True
            },
            'users': {
                'type': 'list',  # тип: список
                'default': [],  # по умолчанию: пустой список
                # описываем "схему" списка
                'schema': {
                    'type': 'objectid',  # тип данных: objectid
                    # ссылаемся на запись в другой коллекции
                    'data_relation': {
                        'resource': 'users',  # на ресурс `users` (который мы описали выше)
                        'field': '_id',  # на поле `_id`
                        'embeddable': True
                    }
                }
            }
        }
    },
# Описываем ресурс `/traffic_laws`
    'traffic_laws': {
        # Описываем модель данных (см. выше).
        'schema': {
            'number': {
                'type': 'float',
                'required': True,
                'min': 1

            },
            'title': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 255,
                'required': True,
                'unique': True
            },
            'text': {
                'type': 'string',
                'required': True
            },
            'mivar': {
                'type': 'string'
            }

        }
    },

    #знаки
    'signs': {
        # Описываем модель данных (см. выше).
        'schema': {
            'number': {
                'type': 'float',
                'required': True,
                'min': 1
            },
            'title': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 255,
                'required': True,
                'unique': True
            },
            'text': {
                'type': 'string',
                'required': True
            },
            'mivar': {
                'type': 'string'
            },
            'aruco': {
                'type': 'integer',
                'min': 10,
                'required': True,
                'unique': True
            },
            'img':{
                'type': 'string',
                'required': True
            }
        }
    },
# Описываем ресурс `/cars`
    'cars': {
        # Описываем модель данных (см. выше).
        'schema': {
            'number': {
                'type': 'float',
                'required': True,
                'min': 1

            },
            'title': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 255,
                'required': True,
                'unique': True
            },
            'text': {
                'type': 'string',
                'required': True
            },
            'aruco': {
                'type': 'integer',
                'min': 10,
                'required': True,
                'unique': True
            },
            'img':{
                'type': 'string',
                'required': True
            },
            'ip': {
                'type': 'string',
                'required': True
            },
            'other':{
                'type': 'string'
            }
        }
    },
}