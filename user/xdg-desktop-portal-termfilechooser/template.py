pkgname = "xdg-desktop-portal-termfilechooser"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cmake",
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = ["inih-devel", "elogind-devel"]
depends = [
    "xdg-desktop-portal",
]
pkgdesc = "Backend for choosing files with your favorite file chooser"
license = "MIT"
url = "https://github.com/boydaihungst/xdg-desktop-portal-termfilechooser"
source = f"{url}/archive/refs/heads/main.zip"
sha256 = "5d430f8c586cd2895315a31e37bf1730093211b4a86815c601a8b61c5328ccac"


def post_install(self):
    self.install_file(
        "contrib/config.sample",
        "usr/share/examples/xdg-desktop-portal-termfilechooser",
    )
    self.uninstall("usr/share/xdg-desktop-portal-termfilechooser/systemd")
    self.install_license("LICENSE")
