from tkinter import EventType
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionAskReservationName(Action):
    def name(self) -> Text:
        return "action_ask_reservation_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Quel est le nom de votre réservation ?")
        return []


class ActionSetReservationName(Action):
    def name(self) -> Text:
        return "action_set_reservation_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        reservation_name = tracker.latest_message.get('text')
        return [SlotSet("nom_reservation", reservation_name)]


class ActionAskNumberOfPeople(Action):
    def name(self) -> Text:
        return "action_ask_number_of_people"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Combien de personnes seront présentes ?")
        return []


class ActionSetNumberOfPeople(Action):
    def name(self) -> Text:
        return "action_set_number_of_people"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number_of_people = tracker.latest_message.get('text')
        return [SlotSet("nombre_personnes", number_of_people)]


class ActionAskDate(Action):
    def name(self) -> Text:
        return "action_ask_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Pour quelle date souhaitez-vous réserver ?")
        return []


class ActionSetDate(Action):
    def name(self) -> Text:
        return "action_set_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.latest_message.get('text')
        return [SlotSet("date", date)]


class ActionAskTime(Action):
    def name(self) -> Text:
        return "action_ask_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("A quelle heure souhaitez-vous réserver ?")
        return []


class ActionSetTime(Action):
    def name(self) -> Text:
        return "action_set_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time = tracker.latest_message.get('text')
        return [SlotSet("heure", time)]


class ActionMakeReservation(Action):
    def name(self) -> Text:
        return "action_make_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        reservation_name = tracker.get_slot("nom_reservation")
        number_of_people = tracker.get_slot("nombre_personnes")
        date = tracker.get_slot("date")
        time = tracker.get_slot("heure")

        if reservation_name and number_of_people and date and time:
            confirmation_message = f"Je confirme votre réservation : {reservation_name} pour {number_of_people} personnes le {date} à {time} heures."
            dispatcher.utter_message(confirmation_message)
            dispatcher.utter_message("Votre réservation a bien été prise en compte. Vous pourrez bientôt profiter d'un délicieux repas parmi nous !")
        else:
            dispatcher.utter_message("Désolé, il semble y avoir un problème avec les informations de réservation. Pourriez-vous recommencer depuis le début ?")

        return []