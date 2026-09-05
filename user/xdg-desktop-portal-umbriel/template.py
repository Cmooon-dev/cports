pkgname = "xdg-desktop-portal-umbriel"
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
install_if = ["umbriel>=0.1.0-r1"]
pkgdesc = "Wayland compositor with scrolling, dwindle and master layouts"
license = "MIT"
url = "https://github.com/noctalia-dev/xdg-desktop-portal-umbriel"
source = "https://github.com/noctalia-dev/xdg-desktop-portal-umbriel/archive/refs/heads/main.zip"
sha256 = "6938e0d1a629881435289fb9079590eca236e7ebc01a604acf3af2ce6a20cb16"


def post_install(self):
    self.install_license("LICENSE")
