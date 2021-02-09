import persistent

class Message(persistent.Persistent):
    def __init__(self, content):
        self.content = content

    def edit(self, new_content):
        self.content = new_content
