from faker import Faker
from src.participant.constants import NOUN_INDEX_RANGE, ADJECTIVE_INDEX_RANGE
from random import randint
from src.participant.schema import ParticipantSchema


def generate_new_participant(room_id: str) -> object:
    """Generates random user data

    Args:
        room_id (str): If a room_id is provided
                       add it into the participants document

    Returns:
        object: A participantschema type object
    """
    if room_id:
        pass
    else:
        username: str = generate_username()
        participant_data: dict = {"username": username,
                                  "user_rooms": list(),
                                  "is_active": True}
        participant = ParticipantSchema(**participant_data)
        return participant


def generate_username() -> str:
    """A utility function to generate a username
       using adjective + noun approach

    Returns:
        string: A string value divided by an '_'
    """
    adjective: str = get_word(word_type="adjective")
    noun: str = get_word(word_type="noun")
    username = adjective+"_"+noun
    return username


def get_word(word_type: str) -> str:
    """A utility function which is used to generate a random
       Noun or Adjective using the faker package
    Args:
        word_type (str): The word type, a noun or adjective

    Returns:
        str: A randomly generated word
    """
    fake: object = Faker()
    if word_type == "noun":
        index = randint(NOUN_INDEX_RANGE[0], NOUN_INDEX_RANGE[1])
    if word_type == "adjective":
        index = randint(ADJECTIVE_INDEX_RANGE[0], ADJECTIVE_INDEX_RANGE[1])

    return fake.get_words_list(part_of_speech=word_type)[index]
