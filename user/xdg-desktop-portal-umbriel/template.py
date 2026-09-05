pkgname = "xdg-desktop-portal-umbriel"
pkgver = "0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cmake",
    "git",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gtk4-devel",
    "libdrm-devel",
    "mesa-gbm-devel",
    "nlohmann-json",
    "pipewire-devel",
    "sdbus-cpp",
    "tomlplusplus-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = [
    "xdg-desktop-portal",
]
install_if = ["umbriel=0-r0"]
pkgdesc = "Wayland compositor with scrolling, dwindle and master layouts"
license = "MIT"
url = "https://github.com/noctalia-dev/xdg-desktop-portal-umbriel"
source = "https://github.com/noctalia-dev/xdg-desktop-portal-umbriel/archive/refs/heads/main.zip"
sha256 = "5ab221d5d50928a9946b99c416d8b2300ff2c6ba74db5fc73ae240d2624663ed"


def post_install(self):
    self.install_license("LICENSE")
