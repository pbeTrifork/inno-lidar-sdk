cmake_minimum_required(VERSION 3.0...4.0)
project(TestInnoSDK CXX)

find_package(inno_client_sdk REQUIRED)

add_executable(example src/conan_test.cpp)
target_link_libraries(example PRIVATE inno_client_sdk::inno_client_sdk)