from models.cards.choice_card import ChoiceCard
import pytest

xfail = pytest.mark.xfail


def test_choice_body(cards_table, db_conn):
    """
    Expect a choice card to require a body (question).
    """

    card, errors = ChoiceCard.insert(db_conn, {
        'unit_id': 'RUF531',
        'name': 'What is?',
        'options': [{
            'value': 'abadaba',
            'correct': True,
            'feedback': 'Bazaaa...'
        }],
    })
    assert len(errors) == 1
    card['body'] = 'Testing 1234'
    errors = card.validate(db_conn)
    assert len(errors) == 0


def test_choice_options(db_conn, cards_table):
    """
    Expect a choice card to require a options (answers).
    (value, correct, feedback)
    """

    card, errors = ChoiceCard.insert(db_conn, {
        'unit_id': 'RUF531',
        'name': 'What is?',
        'body': 'Testing 1234',
    })
    assert len(errors) == 1
    card['options'] = [{
        'value': 'abadaba',
        'correct': True,
        'feedback': 'Bazaaa...'
    }]
    errors = card.validate(db_conn)
    assert len(errors) == 0


def test_choice_order(db_conn, cards_table):
    """
    Expect a choice card to allow set order.
    """

    card, errors = ChoiceCard.insert(db_conn, {
        'unit_id': 'RUF531',
        'name': 'What is?',
        'body': 'Testing 1234',
        'options': [{
            'value': 'abadaba',
            'correct': True,
            'feedback': 'Bazaaa...'
        }],
    })
    assert len(errors) == 0
    card['order'] = 'set'
    errors = card.validate(db_conn, )
    assert len(errors) == 0


def test_choice_max_opts(db_conn, cards_table):
    """
    Expect a choice card to allow max options (question).
    """

    card, errors = ChoiceCard.insert(db_conn, {
        'unit_id': 'RUF531',
        'name': 'What is?',
        'body': 'Testing 1234',
        'options': [{
            'value': 'abadaba',
            'correct': True,
            'feedback': 'Bazaaa...'
        }],
    })
    assert len(errors) == 0
    card['max_options'] = 2
    errors = card.validate(db_conn)
    assert len(errors) == 0


@xfail
def test_validate_response(db_conn, cards_table):
    """
    Expect to check if a given response is valid for the card kind.
    """

    assert False


@xfail
def test_score_response(db_conn, cards_table):
    """
    Expect to score if a given response is correct for the card kind.
    """

    assert False
