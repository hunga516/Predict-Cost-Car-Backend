class NewsController {
    index(req, res) {
        res.render('news')
    }

    show(req, res) {
        const slug = req.params.slug
        res.send(`${slug}`)
    }
}

module.exports = new NewsController()