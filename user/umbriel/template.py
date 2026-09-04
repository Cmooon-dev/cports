pkgname = "umbriel"
pkgver = "0.1.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "cmake",
    "git",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "lcms2-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
    "libei-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "nlohmann-json",
    "pango-devel",
    "pixman-devel",
    "tomlplusplus-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = ["xwayland-satellite"]
pkgdesc = "Wayland compositor with scrolling, dwindle and master layouts"
license = "MIT"
url = "https://github.com/noctalia-dev/umbriel"
source = "https://github.com/noctalia-dev/umbriel/archive/refs/heads/main.zip"
sha256 = "15a5078e8429d012c8b434e37ce748bd7b0c897e394073a89443f3a9c98917d9"


def post_install(self):
    self.install_license("LICENSE")
