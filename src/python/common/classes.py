import typing as t


class Task:
    def __init__(self,
                 ind: int,
                 title: t.Optional[str] = None, 
                 question: t.Optional[str] = None,
                 question_images: t.Optional[t.List[t.Any]] = None,
                 tip: t.Optional[str] = None,
                 tip_images: t.Optional[t.List[t.Any]] = None,
                 answer: t.Optional[str] = None,
                 answer_images: t.Optional[t.List[t.Any]] = None,
                 comment: t.Optional[str] = None,
                 comment_images: t.Optional[t.List[t.Any]] = None
                 ):
        self.ind = ind
        self.title = title
        self.question = question
        self.question_images = question_images
        self.tip = tip
        self.tip_images = tip_images
        self.answer = answer
        self.answer_images = answer_images
        self.comment = comment
        self.comment_images = comment_images
        


class Work:
    def __init__(self, ind: int, title: str):
        self.ind = ind
        self.title = title