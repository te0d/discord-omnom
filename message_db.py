import discord
import transaction
import BTrees.OOBTree
import ZODB

from message import Message

class MessageDatabase:
    def __init__(self):
        # in memory since discord doesn't send updates about messages sent before the bot connects
        # it could be worked around by occasional polling, but not necessary for a POC
        self._zodb = ZODB.DB(None)

        connection = self._zodb.open()
        if (not hasattr(connection.root, "messages")):
            connection.root.messages = BTrees.OOBTree.BTree()
            transaction.commit()

        connection.close()

    def add_message(self, message):
        connection = self._zodb.open()
        messages = connection.root.messages
        messages[message.id] = Message(message.content)
        transaction.commit()
        connection.close()

    def get_message(self, id):
        connection = self._zodb.open()
        messages = connection.root.messages
        message = messages[id]
        connection.close()
        return message

    def get_count(self):
        connection = self._zodb.open()
        messages = connection.root.messages
        count = len(messages)
        connection.close()
        return count

    def edit_message(self, message):
        connection = self._zodb.open()
        messages = connection.root.messages
        messages[message.id].edit(message.content)
        transaction.commit()
        connection.close()

    def delete_message(self, message):
        connection = self._zodb.open()
        messages = connection.root.messages
        messages.pop(message.id, None)
        transaction.commit()
        connection.close()

    def clear(self):
        connection = self._zodb.open()
        messages = connection.root.messages
        messages.clear()
        transaction.commit()
        connection.close()
