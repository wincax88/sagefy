from modules.model import Model
from models.post import Post
from modules.validations import is_required, is_string, is_one_of


class Vote(Post):
    """A vote or response on a proposal."""

    # For votes, a body is not required but optional,
    # But a replies to id is required
    schema = dict(Post.schema.copy(), **{
        'body': {
            'validate': (is_string,)
        },
        'replies_to_id': {
            'validate': (is_required, is_string,)
        },

        # The only true unique field of a vote...
        # Where True is yes, None is discuss, False is no
        'response': {
            'validate': ((is_one_of, True, None, False),),
            'default': None
        }
    })

    def __init__(self, fields=None):
        """

        """
        Model.__init__(self, fields)
        self.kind = 'vote'

    # TODO You can only vote once per proposal.
    # TODO You can update the response on your vote.
    # TODO You cannot vote on your own proposal.
    # TODO A vote should not require a body.
