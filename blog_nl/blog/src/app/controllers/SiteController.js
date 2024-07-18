class SiteController {
    // [GET] /search
    search(req, res) {
        console.log("hit");
        res.render('search')
    }

    // [GET] /
    index(req, res) {
        res.render('home')
    }
}

module.exports = new SiteController()
