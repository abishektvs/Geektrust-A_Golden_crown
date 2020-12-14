from utilities import encrypt_emblem, count_letters
from constants import kingdom_Emblem_map

class King():

    def __init__(self, kingdom, secret_message_list):
        self.messages = {}
        self.kingdom = kingdom

        for secret_message in secret_message_list:
            ally_kingdom, *ally_message = secret_message.split()
            self.messages[ally_kingdom] = "".join(ally_message)

    def analyze_support(self):
        support = [self.kingdom]
        for ally_kingdom, ally_message in self.messages.items():
            if self.support_recieved(ally_kingdom, ally_message):
                support.append(ally_kingdom)

        if len(support) > 3:
            a = " ".join(support)
            print(a)
        else:
            print("NONE")   

    def support_recieved(self, kingdom, secret_msg):
        emblem = kingdom_Emblem_map[kingdom]
        encrypted_emblem = encrypt_emblem(emblem)
        emblem_letter_count = count_letters(encrypted_emblem)
        is_supporting = True

        for letter in emblem_letter_count:
            if secret_msg.count(letter) < emblem_letter_count[letter]:
                is_supporting = False
                break

        return is_supporting