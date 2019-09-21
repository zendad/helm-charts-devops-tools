DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'awx.main.db.profiled_pg',
        'NAME': "{{ pg_database }}",
        'USER': "{{ pg_username }}",
        'PASSWORD': "{{ pg_password }}",
        'HOST': "{{ pg_hostname|default('postgresql') }}",
        'PORT': "{{ pg_port }}",
    }
}
BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(
    "{{ rabbitmq_user }}",
    "{{ rabbitmq_password }}",
    "localhost",
    "5672",
    "awx")
CHANNEL_LAYERS = {
    'default': {'BACKEND': 'asgi_amqp.AMQPChannelLayer',
                'ROUTING': 'awx.main.routing.channel_routing',
                'CONFIG': {'url': BROKER_URL}}
}
