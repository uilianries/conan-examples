from conans import ConanFile
from conans import CMake, RunEnvironment, tools
import os

class TestConanGTestExample(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "gtest/1.10.0"
    default_options = {"gtest:shared": True}

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def test(self):
        os.environ["CTEST_OUTPUT_ON_FAILURE"] = "1"
        env_build = RunEnvironment(self)
        with tools.environment_append(env_build.vars):
            cmake = self._configure_cmake()
            cmake.test(output_on_failure=True)
