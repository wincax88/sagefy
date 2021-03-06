from schemas.card_parameters import schema as card_parameters_schema
from modules.sequencer.pmf import init_pmf, \
    get_guess_pmf_value, \
    get_slip_pmf_value
from database.util import insert_document, update_document, get_document
from modules.sequencer.params import init_guess, init_slip, precision, \
    init_transit


def get_card_parameters(params, db_conn):
    """
    """

    tablename = card_parameters_schema['tablename']
    return get_document(tablename, params, db_conn)


def insert_card_parameters(data, db_conn):
    """
    """

    schema = card_parameters_schema
    return insert_document(schema, data, db_conn)


def update_card_parameters(prev_data, data, db_conn):
    """
    """

    schema = card_parameters_schema
    return update_document(schema, prev_data, data, db_conn)


def get_distribution(card_parameters, kind):
    """
    Parse own distribution hypotheses,
    changing the keys back into numbers.
    """

    key = '{kind}_distribution'.format(kind=kind)
    if key in card_parameters:
        distribution = card_parameters[key]
        distribution = deliver_distribution(distribution)
    else:
        init = init_guess if kind == 'guess' else init_slip
        distribution = {
            h: 1 - (init - h) ** 2
            for h in [h / precision for h in range(1, precision)]
        }
        card_parameters[key] = distribution
    if kind == 'guess':
        return init_pmf(distribution)
    if kind == 'slip':
        return init_pmf(distribution)


def deliver_distribution(hypotheses):
    """
    Prepare the distribution for code use / JSON output.
    """
    return {float(k): v for k, v in hypotheses.items()}


def bundle_distribution(hypotheses):
    """
    Prepare for saving the distribution to the database.
    """

    return {str(k): v for k, v in hypotheses.items()}


def get_guess(card_parameters):
    """
    Gets the guess value for the card.
    """

    guess_distribution = get_distribution(card_parameters, 'guess')
    return get_guess_pmf_value(guess_distribution)


def get_slip(card_parameters):
    """
    Gets the slip value for the card.
    """

    slip_distribution = get_distribution(card_parameters, 'slip')
    return get_slip_pmf_value(slip_distribution)


def get_transit():
    """
    Gets the transit value for the card.
    TODO-2 use a formulation for transit.
    """

    return init_transit


def get_num_learners():
    """
    Gets the number of learners who interact with the card.
    TODO-3 calculate based on the responses table.
    """

    return 0


def get_card_parameters_values(card_parameters):
    """
    Get the value outputs for the card parameters.
    """

    return {
        'guess': get_guess(card_parameters),
        'slip': get_slip(card_parameters),
        'transit': get_transit(),
        'num_learners': get_num_learners(),
    }
