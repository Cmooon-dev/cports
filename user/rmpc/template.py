pkgname = "rmpc"
pkgver = "0.11.0"
pkgrel = 0
build_style = "cargo"
makedepends = ["cargo-auditable"]
pkgdesc = "Modern, configurable, terminal based MPD Client with album art"
license = "BSD-3-Clause"
url = "https://github.com/mierak/rmpc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "930019066228d18e9530a8c0d77f10e231ab5efbbbca73b331efcd6fbb47557d"


def post_install(self):
    self.install_license("LICENSE")
