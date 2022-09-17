function showActiveLink(menu) {
    try {
        let elem = document.getElementById(menu).querySelectorAll('a');
        let url = document.location.href;
        for (const link of elem) {
            if (url === link.href) {
                link.classList.add('active')
            }
        }
        // console.log (elem)

    } catch {

    }
}

showActiveLink('menu')