const {li, div, img, a, span, h3} = require('../../modules/tags')
const {timeAgo} = require('../../modules/auxiliaries')
const icon = require('./icon.tmpl')

const renderProposal = (data) => {
    if (!data.kind === 'proposal') { return }
    // const evKind = data.entity_version.kind
    // const ev = data.ev || {}
    return div(
        {className: 'post__proposal'}
        // TODO-2 TP@ show preview components
    )
}

const voteResponse = (response) => {
    if(!response) { return }
    return [
        span(
            {
                className: `post__vote--${response ? 'good' : 'bad'}`
            },
            icon(response ? 'good' : 'bad'),
            response ? ' Yes' : ' No'
        ),
        ' '
    ]
}

module.exports = (data, currentUserID) => {
    const topicId = data.topic_id
    return li(
        {
            id: data.id,
            className: 'post',
        },
        div(
            {className: 'post__avatar'},
            a(
                {href: `/users/${data.user_id}`},
                img({
                    src: data.user_avatar || '',
                    width: 48,
                    height: 48
                })
            )
        ),
        div(
            {className: 'post__content'},
            div({className: 'post__when'}, timeAgo(data.created)),
            a(
                {
                    className: 'post__name',
                    href: `/users/${data.user_id}`,
                },
                data.user_name || '???'
            ),
            div(
                data.replies_to_id ? a(
                    {
                        className: 'post__in-reply',
                        href: `/topics/${data.topic_id}#${data.replies_to_id}`
                    },
                    icon('reply'),
                    ' In Reply'
                ) : null,
                data.replies_to_id ? ' ' : null,
                data.kind === 'proposal' ? h3('Proposal: ' + data.name) : null,
                voteResponse(data.response),
                data.body
            ),
            data.kind === 'proposal' ? renderProposal(data) : null,
            div(
                {className: 'post__footer'},
                currentUserID === data.user_id ? a(
                    {href: `/topics/${topicId}/posts/${data.id}/update`},
                    icon('update'),
                    ' Edit'
                ) : a(
                    {href: `/topics/${topicId}/posts/create?` +
                           `replies_to_id=${data.id}`},
                    icon('reply'),
                    ' Reply'
                ),
                data.kind === 'proposal' ? a(
                    {href: `/topics/${topicId}/posts/create?` +
                           `replies_to_id=${data.id}&kind=vote`},
                    icon('vote'),
                    ' Vote'
                ) : null,
                a(
                    {href: `/topics/${data.topicID}#${data.id}`},
                    icon('post'),
                    ' Share'
                )
                // TODO-3 a(
                //     {href: '#'}
                //     icon('remove')
                //     ' Flag'
                // ) if currentUserID isnt data.user_id
            )
        )
    )
}
