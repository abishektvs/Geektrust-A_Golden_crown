from utilities import count_letters,encrypt
from collections import namedtuple

emblem_of = {"LAND"  : "PANDA",
             "WATER" : "OCTOPUS",
             "ICE"   : "MAMMOTH",
             "AIR"   : "OWL",
             "FIRE"  : "DRAGON",
             "SPACE" : "GORILLA",
            }

SecretMessage = namedtuple("SecretMessage",['ally_kingdom', 'ally_message'])

class King():

    def __init__(self, kingdom, secret_message_list):
        self.secret_messages = []
        self.kingdom = kingdom
        for secret_message in secret_message_list:
            ally_kingdom, *ally_message = secret_message.split()
            self.secret_messages.append(SecretMessage(ally_kingdom = ally_kingdom,
                                        ally_message = "".join(ally_message)))

    def analyze_support(self):
        support = self.kingdom
        minimum_support = 3

        for secret_message in self.secret_messages:
            if self.support_recieved(secret_message):
                support += ' ' + secret_message.ally_kingdom

        if len(support) > minimum_support:
            return support
        else:
            return "NONE"   

    def support_recieved(self, secret_message):
        emblem = emblem_of[secret_message.ally_kingdom]
        encrypted_emblem = encrypt(emblem)
        count_of_letter_in_emblem = count_letters(encrypted_emblem)
        is_supporting = True

        for letter in count_of_letter_in_emblem:
            if secret_message.ally_message.count(letter) < count_of_letter_in_emblem[letter]:
                
                is_supporting = False
                break

        return is_supporting