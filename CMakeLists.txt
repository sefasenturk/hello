PROJECT(MyHello)
cmake_minimum_required(VERSION 2.8)

# this will do quite a useful setup and checks for us
# Not necessary, but convenient
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# No need to specify STATIC, that is the default. Not specifying
# later allow to build SHARED
ADD_LIBRARY(hello hello.cpp)
#ADD_EXECUTABLE(greet main.cpp)
#TARGET_LINK_LIBRARIES(greet hello)
#IF (WIN32 AND "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
#	TARGET_LINK_LIBRARIES(greet stdc++)
#ENDIF()
