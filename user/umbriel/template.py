pkgname = "umbriel"
pkgver = "0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "git",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "lcms2-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
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
sha256 = "87a971826c11bd1fa0ea243ec9f15c0b06fa043b9ca547ff885c97176f6b7ef1"


def post_install(self):
    # self.install_bin("build/umbriel")
    # self.install_bin("build/start-umbriel")
    # self.install_file("examples/config.toml", "usr/share/umbriel")
    # self.install_file("data/umbriel.desktop", "usr/share/wayland-sessions")
    self.install_license("LICENSE")
