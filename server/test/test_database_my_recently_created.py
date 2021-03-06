from conftest import create_user_in_db
from database.my_recently_created import get_my_recent_proposals, \
    get_proposal_entities, get_my_recently_created_units, \
    get_my_recently_created_sets
import rethinkdb as r


def create_some_proposals(posts_table, units_table, sets_table, db_conn):
    """
    Create some proposals to check the calls.
    """

    posts_table.insert([{
        'kind': 'proposal',
        'user_id': 'abcd1234',
        'entity_versions': [{
            'kind': 'set', 'id': 'A',
        }, {
            'kind': 'unit', 'id': 'D',
        }],
    }, {
        'kind': 'proposal',
        'user_id': '5678xywz',
        'entity_versions': [{
            'kind': 'set', 'id': 'B',
        }, {
            'kind': 'unit', 'id': 'E',
        }],
    }, {
        'kind': 'proposal',
        'user_id': 'abcd1234',
        'entity_versions': [{
            'kind': 'set', 'id': 'C',
        }, {
            'kind': 'unit', 'id': 'F',
        }],
    }]).run(db_conn)
    sets_table.insert([{
        'entity_id': 'A',
        'status': 'accepted',
        'created': r.now(),
    }, {
        'entity_id': 'B',
        'status': 'accepted',
        'created': r.now(),
    }, {
        'entity_id': 'C',
        'status': 'accepted',
        'created': r.now(),
    }]).run(db_conn)
    units_table.insert([{
        'entity_id': 'D',
        'status': 'accepted',
        'created': r.now(),
    }, {
        'entity_id': 'E',
        'status': 'accepted',
        'created': r.now(),
    }, {
        'entity_id': 'F',
        'status': 'accepted',
        'created': r.now(),
    }]).run(db_conn)


def test_get_my_recent_proposals(db_conn, posts_table, users_table,
                                 units_table, sets_table):
    """
    Get the user's most recent proposals.
    """

    create_user_in_db(users_table, db_conn)
    current_user = users_table.get('abcd1234').run(db_conn)
    create_some_proposals(posts_table, units_table, sets_table, db_conn)
    proposals = get_my_recent_proposals(current_user, db_conn)
    assert len(proposals) == 2


def test_get_proposal_entities():
    """
    Pull out the entity ids matching the kind.
    """

    proposals = [{
        'entity_versions': [{
            'kind': 'unit',
            'id': 'A',
        }, {
            'kind': 'set',
            'id': 'B',
        }, {
            'kind': 'unit',
            'id': 'C',
        }]
    }]
    kind = 'unit'
    entity_ids = get_proposal_entities(proposals, kind)
    assert len(entity_ids) == 2
    assert entity_ids[0] == 'A'
    assert entity_ids[1] == 'C'


def test_get_my_recently_created_units(db_conn, posts_table, sets_table,
                                       units_table, users_table):
    """
    Get the user's most recent units.
    """

    create_user_in_db(users_table, db_conn)
    current_user = users_table.get('abcd1234').run(db_conn)
    create_some_proposals(posts_table, units_table, sets_table, db_conn)
    units = get_my_recently_created_units(current_user, db_conn)
    assert len(units) == 2
    assert units[0]['entity_id'] == 'D'
    assert units[1]['entity_id'] == 'F'


def test_get_my_recently_created_sets(db_conn, posts_table, units_table,
                                      sets_table, users_table):
    """
    Get the user's most recent sets.
    """

    create_user_in_db(users_table, db_conn)
    current_user = users_table.get('abcd1234').run(db_conn)
    create_some_proposals(posts_table, units_table, sets_table, db_conn)
    sets = get_my_recently_created_sets(current_user, db_conn)
    assert len(sets) == 2
    assert sets[0]['entity_id'] == 'A'
    assert sets[1]['entity_id'] == 'C'
