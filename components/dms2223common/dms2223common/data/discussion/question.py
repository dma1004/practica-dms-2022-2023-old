from dms2223common.data.discussion.comment import Comment
from dms2223common.data.discussion.discussion_component import DiscussionComponent
from dms2223common.data.discussion.discussion_composite import DiscussionComposite


class Question(DiscussionComposite):

    def __init__(self, autor, title, texto):
        super().__init__(autor, texto)
        self.title = title

    def addChild(self, child: DiscussionComponent):
        if not isinstance(child, Question) and not isinstance(child, Comment):
            self.childs.append(child)
