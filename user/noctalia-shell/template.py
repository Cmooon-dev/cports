pkgname = "noctalia-shell"
pkgver = "4.7.4"
pkgrel = 0
depends = [
    "brightnessctl",
    "ffmpeg",
    "imagemagick",
    "noctalia-qs",
    "python",
    "qt6-qtmultimedia",
]
pkgdesc = "Sleek and minimal desktop shell"
license = "MIT"
url = "https://github.com/noctalia-dev/noctalia-shell"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b3546878e02597c71df243a99ea92c1c0861d62defe2b27693a6f59021a3ae1c"
# options = ["empty"]

# There are optional dependencies for noctalia one could install
# cliphist: clipboard history support
# cava: audio visualizer component
# wlsunset: NightLight support
# power-profiles-daemon: power profile management
# ddcutil: external display brightness control


def install(self):
    self.install_files(
        "Assets",
        "usr/share/etc/quickshell/noctalia-shell/",
    )
    self.install_files(
        "Commons",
        "usr/share/etc/quickshell/noctalia-shell/",
    )
    self.install_files(
        "Helpers",
        "usr/share/etc/quickshell/noctalia-shell/",
    )
    self.install_files(
        "Modules",
        "usr/share/etc/quickshell/noctalia-shell/",
    )
    self.install_files(
        "Scripts",
        "usr/share/etc/quickshell/noctalia-shell/",
    )
    self.install_files(
        "Services",
        "usr/share/etc/quickshell/noctalia-shell/",
    )
    self.install_files(
        "Shaders",
        "usr/share/etc/quickshell/noctalia-shell/",
    )
    self.install_files(
        "Widgets",
        "usr/share/etc/quickshell/noctalia-shell/",
    )
    self.install_file("shell.qml", "usr/share/etc/quickshell/noctalia-shell/")
    self.install_license("LICENSE")
