const {div, h1, p, a, ul, li} = require('../../modules/tags')
// const c = require('../../modules/content').get
// const spinner = require('../components/spinner.tmpl')
const icon = require('../components/icon.tmpl')
const previewSetHead = require('../components/preview_set_head.tmpl')
const previewUnitHead = require('../components/preview_unit_head.tmpl')
const previewCardHead = require('../components/preview_card_head.tmpl')

module.exports = (data) => {
    // TODO-2 update this to look for some status field
    // if(!data.follows) { return spinner() }

    return div(
        {id: 'follows', className: 'page'},
        h1('Follows'),
        a(
            {href: '/notices'},
            icon('back'),
            ' Back to notices.'
        ),
        follows(data.follows)
    )
}

const follows = (data) => {
    if(data.length) { return ul(data.map(f => follow(f))) }
    return p(
        'No follows. ',
        a(
            {href: '/search'},
            icon('search'),
            ' Search'
        )
    )
}

const follow = (data) => {
    const {kind, name, body} = data.entity
    return li(
        {className: 'follow'},
        a(
            {
                id: data.id,
                href: '#',
                className: 'follows__unfollow-button',
            },
            icon('remove'),
            ' Unfollow'
        ),
        kind === 'unit' ?
            previewUnitHead({ name, body, labelKind: true, }) :
        kind === 'set' ?
            previewSetHead({ name, body, labelKind: true, }) :
        ['video', 'choice'].indexOf(kind) > -1 ?
            previewCardHead({ name, kind, labelKind: true, }) :
            null
    )
}
