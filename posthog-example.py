import posthog
from secret import posthost_api_key
from time import sleep

# Substitutes posthog.api_key which still exists but has been deprecated
posthog.project_api_key = posthost_api_key

posthog.debug = True



#posthog.capture('distinct id', 'event name', dictionary_of_properties)


user_id='5555' 
properties={'movie_id': '123', 'movie_name': 'The Matrix', 'category': 'Action'}


posthog.capture(user_id, 'movie selected', properties)
sleep(1)
posthog.capture(user_id, 'movie played', properties)
sleep(1)
posthog.capture(user_id, 'movie paused', properties)