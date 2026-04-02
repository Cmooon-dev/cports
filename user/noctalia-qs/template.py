pkgname = "noctalia-qs"
pkgver = "0.0.12"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON"]
hostmakedepends = [
    "cli11",
    "cmake",
    "curl",
    "git",
    "ninja",
    "qt6-qtshadertools",
    "spirv-tools",
    "vulkan-headers",
    "wayland-protocols",
]
makedepends = [
    "jemalloc-devel",
    "libdrm-devel",
    "libxcb-devel",
    "linux-pam-devel",
    "pipewire-devel",
    "pkgconf",
    "polkit-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtquick3d-devel",
    "qt6-qtshadertools-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
]
hardening = ["!int"]

pkgdesc = "Custom fork of Quickshell powering Noctalia Shell"
license = "LGPL-3.0-only"
url = "https://github.com/noctalia-dev/noctalia-qs"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2a56bd693945957cd112a7eadc38b719cc85f485b8f377565ba25f8708377088"
