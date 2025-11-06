import os
import sys

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.files import copy, load
def get_version():
	try:
		with open("SDK_VERSION", "r") as content:
			return content.readline().strip()
	except Exception as e:
		print(f"Could not read version: {e}", file=sys.stderr)

class innoClientSDK(ConanFile):

	name = "inno_client_sdk"
	license = "BSD-2-Clause"
	author = "Paul M. B. Bendixen <pbe@trifork.com>"
	url = "https://github.com/pbeTrifork/inno-lidar-sdk"
	description = "SDK for Seyond Inc. LiDARs"
	topics = ("LiDAR", "SDK", "Falcon")

	settings = "os", "compiler", "build_type", "arch"
	options = {"shared": [True, False]}
	default_options = {"shared": False}

	def set_version(self):
		content = load(self, "SDK_VERSION")
		self.version = self.version or content.strip()

	def generate(self):
		toolchain = CMakeToolchain(self)
		toolchain.generate()

	def layout(self):
		cmake_layout(self)

	def build(self):
		cmake = CMake(self)
		cmake.configure(variables={"MAKE_SHARED":"ON"})
		cmake.build()

	def package(self):
		copy(self, "*.h", os.path.join(self.source_folder, "src"), os.path.join(self.package_folder, "include"))
		copy(self, "*.so", self.build_folder, os.path.join(self.package_folder, "lib"), keep_path=False)
		copy(self, "*.a", self.build_folder, os.path.join(self.package_folder, "lib"), keep_path=False)

	def package_info(self):
		self.cpp_info.libs = ["inno_client_sdk"]