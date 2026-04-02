pkgname = "cli11"
pkgver = "2.6.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "meson",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "catch2-devel",
]
depends = [
    "boost",
    "catch2",
]
pkgdesc = "Command line parser for C++11"
license = "BSD-3-Clause"
url = "https://github.com/CLIUtils/CLI11"
source = f"{url}/archive/refs/tags/v2.6.2.tar.gz"
sha256 = "c6ea6b2e5608b3ea8617999bd5f47420c71b2ebdb8dc4767c1034d1da5785711"


def post_install(self):
    self.install_license("./LICENSE")
