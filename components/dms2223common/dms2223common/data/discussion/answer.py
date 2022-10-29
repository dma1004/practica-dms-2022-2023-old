from dms2223common.data.discussion.discussion_component import DiscussionComponent
from dms2223common.data.discussion.discussion_composite import DiscussionComposite


class Answer(DiscussionComposite):

    def __init__(self, autor, texto):
        super().__init__(autor, texto)
        self.votes = 0

    def voteUp(self):
        self.votes += 1

    def voteDown(self):
        self.votes -= 1

    def addChild(self, child: DiscussionComponent):
        self.childs.append(child)
