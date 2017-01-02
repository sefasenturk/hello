from conans import ConanFile, CMake

class HelloConan(ConanFile):
    name = "Hello"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    exports = "*"
    generators = "cmake" # Not required, but useful

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["hello"]
