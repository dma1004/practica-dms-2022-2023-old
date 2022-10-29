from typing import List

from dms2223common.data.discussion.discussion_component import DiscussionComponent


class DiscussionComposite(DiscussionComponent):

    def __init__(self, autor, texto):
        super().__init__(autor, texto)
        self.childs = []

    def addChild(self, child: DiscussionComponent):
        pass

    def getChilds(self) -> List[DiscussionComponent]:
        return self.childs
