from members.model import MemberModel
class MemberController:
    def __init__(self):
        self.model = MemberModel()

    def create_table(self):
        self.model.create()
        self.model.insert_many()
        self.model.fetch_all()



