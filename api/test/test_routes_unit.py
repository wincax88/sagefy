import rethinkdb as r
import json
import routes.unit


def test_get_unit(db_conn,
                  units_table, sets_table, topics_table):
    """
    Expect to get the unit information for displaying to a contributor.
    """

    units_table.insert([{
        'entity_id': 'zytx',
        'created': r.now(),
        'modified': r.now(),
        'accepted': True,
        'name': 'Wildwood',
        'requires': ['ntza'],
    }, {
        'entity_id': 'zytx',
        'created': r.time(1986, 11, 3, 'Z'),
        'modified': r.time(1986, 11, 3, 'Z'),
        'accepted': True,
        'name': 'Umberwood',
    }, {
        'entity_id': 'ntza',
        'created': r.time(1986, 11, 3, 'Z'),
        'modified': r.time(1986, 11, 3, 'Z'),
        'accepted': True,
        'name': 'Limberwood',
    }, {
        'entity_id': 'tyui',
        'created': r.now(),
        'modified': r.now(),
        'accepted': True,
        'name': 'Wildwood',
        'requires': ['zytx'],
    }]).run(db_conn)

    sets_table.insert({
        'entity_id': 'W',
        'name': 'Woods',
        'created': r.now(),
        'modified': r.now(),
        'accepted': True,
        'members': [{
            'kind': 'unit',
            'id': 'zytx',
        }]
    }).run(db_conn)

    topics_table.insert([{
        'created': r.now(),
        'modified': r.now(),
        'user_id': 'abcd1234',
        'name': 'A Modest Proposal',
        'entity': {
            'id': 'zytx',
            'kind': 'unit'
        }
    }, {
        'created': r.now(),
        'modified': r.now(),
        'user_id': 'abcd1234',
        'name': 'Another Proposal',
        'entity': {
            'id': 'zytx',
            'kind': 'unit'
        }
    }, {
        'created': r.now(),
        'modified': r.now(),
        'user_id': 'abcd1234',
        'name': 'A Third Proposal',
        'entity': {
            'id': 'abcd',
            'kind': 'card'
        }
    }]).run(db_conn)

    code, response = routes.unit.get_unit_route({}, 'zytx')
    assert code == 200
    # Model
    assert response['unit']['entity_id'] == 'zytx'
    assert response['unit']['name'] == 'Wildwood'
    # Topics
    assert len(response['topics']) == 2
    assert response['topics'][0]['entity']['kind'] == 'unit'
    # Versions
    assert len(response['versions']) == 2
    assert response['versions'][1]['name'] == 'Umberwood'
    # Requires
    assert len(response['requires']) == 1
    assert response['requires'][0]['entity_id'] == 'ntza'
    # Required By
    assert len(response['required_by']) == 1
    assert response['required_by'][0]['entity_id'] == 'tyui'
    # Sets
    assert len(response['sets']) == 1
    assert response['sets'][0]['entity_id'] == 'W'
    # TODO@ sequencer data: learners, quality, difficulty


def test_get_unit_404(db_conn):
    """
    Expect to fail to get an unknown unit (404).
    """

    code, response = routes.unit.get_unit_route({}, 'zytx')
    assert code == 404